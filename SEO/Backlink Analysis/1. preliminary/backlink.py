"""
backlink_enrich.py
==================================================================
Adds derived columns to a competitor-backlink export and (optionally)
joins ranking-keyword metrics onto it.

DERIVED COLUMNS (classifiers)
  1. domain                       -> from Source url (dedupe/merge key)
  2. classification_backlink_page -> page-type of the Target url (the linked page)
  3. type_of_anchor               -> Naked / Branded / Keyword / Other (+ optional sub-bucket)
  4. type_of_backlink_website     -> link/site type taxonomy (guest post, directory, PR, ...)

KEYWORD-FILE METRICS (joined per URL)
  total_ranking_kws, total_traffic, total_volume,
  best_kw_position, highest_position, rich_snippet_participation,
  avg_position_top5, top_3_keywords   (+ best_kw text)

Only dependency: pandas.  (Optional: tldextract for perfect eTLD+1.)

Author note: every list/threshold lives in CONFIG at the top.
Edit CONFIG, not the functions.
==================================================================
"""

from __future__ import annotations

import re
import os
import glob
import pandas as pd
from typing import Iterable


# ==================================================================
# CONFIG  ----  EDIT THIS BLOCK PER PROJECT
# ==================================================================

CONFIG = {
    # ---- identity (from the project identity document) ----
    "root_domain": "littlesleepies.com",          # your brand domain, lowercase, no www/protocol

    # Brand terms: distinctive variants ONLY. Avoid bare generic tokens
    # like "little" or "sleep" that collide with English words — prefer the
    # full/joined forms. Matching is word-boundary aware (see _word_hit).
    "brand_terms": [
        "littlesleepies", "little sleepies", "little-sleepies",
        "sleepies", "lil sleepies",
    ],

    # Primary money keywords (from identity doc). Used only to split the
    # Keyword bucket into Exact / Partial / Topical when sub_bucket=True.
    "primary_keywords": [
        "bamboo pajamas", "kids pajamas", "toddler pajamas",
        "baby sleepwear", "matching family pajamas",
    ],

    # ---- anchor classifier tunables ----
    "anchor_word_count_threshold": 3,   # brand anchor with >N words is treated as Keyword(+brand)
    "anchor_short_len": 6,              # anchors shorter than this fall to "Other"
    "anchor_sub_bucket": True,          # split Keyword -> Exact/Partial/Topical

    # ---- keyword-file join ----
    # Which backlink column to attach ranking metrics to.
    #   "Source url" -> strength of the page that would HOST your link (prospect value)
    #   "Target url" -> strength of the competitor page EARNING links (content intel)
    # You can run the merge twice (see enrich()) to get both with prefixes.
    "kw_join_backlink_column": "Source url",
    "kw_top_n_for_avg": 5,              # avg position over the best-N ranked keywords
    "kw_top_keywords_n": 3,             # how many "top" keywords to list
    "kw_top_rank_by": "traffic",        # "traffic" or "volume" -> basis for "top" keywords

    # ---- column maps: rename to match YOUR kw export headers ----
    # Ahrefs "Organic keywords" and Semrush "Organic Positions" differ; map them here.
    "kw_colmap": {
        "url":          "URL",          # Ahrefs: "Current URL" | Semrush: "URL"
        "keyword":      "Keyword",
        "volume":       "Volume",       # Ahrefs: "Volume" | Semrush: "Search Volume"
        "position":     "Position",     # Ahrefs/Semrush: "Position" (Ahrefs may be "Current position")
        "traffic":      "Traffic",      # Ahrefs: "Traffic" / "Organic traffic" | Semrush: "Traffic"
        "serp_features":"SERP features" # Ahrefs: "SERP features" | Semrush: "SERP Features" (optional)
    },

    # SERP-feature tokens that count as a "rich" result the URL may participate in.
    "rich_snippet_tokens": [
        "featured snippet", "faq", "review", "rating", "recipe", "video",
        "sitelinks", "image pack", "images", "knowledge", "people also ask",
        "top stories", "thumbnail", "rich snippet", "rich result", "carousel",
        "how-to", "qa", "q&a", "snippet",
    ],
}

# Common multi-part public suffixes for eTLD+1 (extend as needed, or use tldextract).
_MULTI_TLDS = {
    "co.uk", "org.uk", "ac.uk", "gov.uk", "co.nz", "com.au", "co.jp",
    "co.in", "com.br", "co.za", "com.sg", "co.kr", "com.mx",
}

# URL tokens that mark an anchor as a naked URL.
_URL_TOKENS = (
    "http://", "https://", "www.",
    ".com", ".net", ".org", ".io", ".co", ".ai", ".app", ".dev",
    ".gov", ".edu", ".info", ".biz",
)

# Generic / navigational anchors -> "Other". Word-boundary matched.
GENERIC_ANCHORS = [
    "buy", "shop", "here", "click", "click here", "visit", "order", "this",
    "register", "recent", "report", "download", "now", "linkedin", "twitter",
    "facebook", "see", "more", "find", "go", "learn", "learn more", "discover",
    "explore", "check", "check out", "know", "get", "read", "read more",
    "source", "sources", "policy", "anonymous", "affiliate", "link", "links",
    "website", "web site", "view", "view here", "see more", "see here", "info",
    "more info", "full article", "original article", "official", "official site",
    "official website", "press release", "continue reading", "full story",
    "full post", "details", "details here", "find out more", "find out",
    "related", "related article", "related post", "recommended", "see this",
    "look here", "take a look", "try", "sign up", "subscribe", "free",
    "free trial", "demo", "request demo", "contact", "contact us", "email",
    "email us", "call", "call now", "hire", "watch", "listen", "page",
    "the page", "blog", "article", "post", "the site", "the website",
    "our site", "our website", "the article", "the post", "the company",
    "see also", "full guide", "full report", "citation", "reference", "ref",
    "continue", "return", "back", "this link", "this article", "this post",
    "this page", "this site", "this guide",
]


# ==================================================================
# 1. DOMAIN EXTRACTION
# ==================================================================

_PROTO_RE = re.compile(r"^[a-z]+://", re.I)

def extract_domain(url: str, strip_www: bool = True, registrable: bool = False) -> str:
    """Return the host of a URL, lowercased.

    strip_www   : drop a leading 'www.'
    registrable : roll up to eTLD+1 (collapses subdomains; e.g. blog.x.com -> x.com).
                  Uses a small multi-part-TLD table; install tldextract for full
                  accuracy on exotic suffixes.
    """
    if not isinstance(url, str) or not url.strip():
        return ""
    u = url.strip().lower()
    if not _PROTO_RE.match(u):
        u = "http://" + u                       # tolerate protocol-less inputs
    # strip protocol
    u = u.split("://", 1)[1]
    # host = everything before first '/'
    host = u.split("/", 1)[0]
    # drop credentials and port
    host = host.split("@")[-1].split(":")[0]
    if strip_www and host.startswith("www."):
        host = host[4:]
    if not registrable:
        return host
    parts = host.split(".")
    if len(parts) <= 2:
        return host
    last2 = ".".join(parts[-2:])
    last3 = ".".join(parts[-3:])
    if last2 in _MULTI_TLDS:
        return ".".join(parts[-3:]) if len(parts) >= 3 else host
    return last2 if last3 not in _MULTI_TLDS else last3


# ==================================================================
# 2. CLASSIFICATION OF BACKLINK PAGE  (page-type of a URL)
# ==================================================================

_IMG_EXT = (".jpg", ".jpeg", ".png", ".webp", ".svg", ".gif", ".avif")

_PAGE_PATTERNS = [
    ("Blog/Resource", ("/blog/", "/blog?", "/news/", "/article", "/post/",
                        "/insights", "/guides", "/guide/", "/resources",
                        "/resource/", "/learn", "/stories", "/journal")),
    ("Product",       ("/product", "/shop/", "/p/", "/item/", "/store/", "/buy/")),
    ("Collection",    ("/category", "/collection", "/collections", "/brand",
                        "/vendor", "/tag/", "/c/")),
    ("Service",       ("/service", "/services", "/solutions", "/pricing",
                        "/plans", "/features")),
    ("Contact-About", ("/about", "/contact", "/team", "/careers", "/company")),
    ("Question/Guide",("/how-", "/what-", "/why-", "/when-", "/where-", "/who-",
                       "/which-", "/tutorial", "/course", "/courses", "/tools",
                       "/faq", "/help")),
]

def classify_page(url: str, root_domain: str | None = None) -> str:
    """Page type of a URL. Pass the brand root_domain to detect its Home page.
    Apply to Target url for 'classification of backlink page'."""
    if not isinstance(url, str) or not url.strip():
        return "Unknown"
    u = url.strip().lower()
    rd = (root_domain or CONFIG["root_domain"]).lower().lstrip("www.")
    # home page (with/without protocol, www, trailing slash)
    bare = re.sub(r"^[a-z]+://(www\.)?", "", u).rstrip("/")
    if rd and bare == rd:
        return "Home"
    if u.rsplit("?", 1)[0].endswith(_IMG_EXT):
        return "Image"
    for label, patterns in _PAGE_PATTERNS:
        if any(p in u for p in patterns):
            return label
    return "Other"


# ==================================================================
# 3. TYPE OF ANCHOR TEXT  (Naked / Branded / Keyword / Other)
# ==================================================================

def _compile_word_res(terms: Iterable[str]) -> list[re.Pattern]:
    """Word-boundary regexes; precise so 'more' won't match 'moreover'."""
    return [re.compile(r"\b" + re.escape(t.lower().strip()) + r"\b") for t in terms if t.strip()]

_BRAND_RES   = _compile_word_res(CONFIG["brand_terms"])
_GENERIC_RES = _compile_word_res(GENERIC_ANCHORS)
_PKW_RES     = _compile_word_res(CONFIG["primary_keywords"])
_PKW_SET     = {k.lower().strip() for k in CONFIG["primary_keywords"]}

def _word_hit(text: str, compiled: list[re.Pattern]) -> bool:
    return any(rx.search(text) for rx in compiled)

def classify_anchor(anchor: str,
                    root_domain: str | None = None,
                    sub_bucket: bool | None = None) -> str:
    """Bucket an anchor. If sub_bucket, Keyword splits into
    Keyword:Exact / Keyword:Partial / Keyword:Topical."""
    rd = (root_domain or CONFIG["root_domain"]).lower()
    sub = CONFIG["anchor_sub_bucket"] if sub_bucket is None else sub_bucket

    a = (anchor or "").strip().lower()
    if a == "":
        return "Naked"
    # naked URL: brand domain OR any url token
    if rd in a or any(tok in a for tok in _URL_TOKENS):
        return "Naked"

    word_count = len(a.split())
    brand = _word_hit(a, _BRAND_RES)

    if brand and word_count > CONFIG["anchor_word_count_threshold"]:
        bucket = "Keyword"           # branded + descriptive -> keyword anchor
    elif brand:
        return "Branded"
    elif len(a) < CONFIG["anchor_short_len"]:
        return "Other"
    elif _word_hit(a, _GENERIC_RES):
        return "Other"
    else:
        bucket = "Keyword"

    if bucket == "Keyword" and sub:
        if a in _PKW_SET:
            return "Keyword:Exact"
        if _word_hit(a, _PKW_RES):
            return "Keyword:Partial"
        return "Keyword:Topical"
    return bucket


# ==================================================================
# 4. TYPE OF BACKLINK WEBSITE  (link / site-type taxonomy)
# ==================================================================

_LINKTYPE_PATTERNS = [
    ("Profile",            ("/user/", "/profile/", "/member/", "/members/",
                            "/u/", "/author/", "/@")),
    ("UGC/Forum",          ("/forum", "/thread", "/community", "/discussion",
                            "reddit.com/r/", "/comments", "discourse", "discuss.")),
    ("Podcast",            ("/podcast", "/episode", "/show/", "/interview")),
    ("Resource/Listicle",  ("/resources", "/resource/", "/links", "/tools",
                            "/best-", "/top-", "/recommended")),
    ("Directory",          ("/directory", "/listing", "/listings", "/businesses",
                            "/companies", "/wiki", "/profiles")),
    ("Digital PR / News",  ("/news", "/press", "/newsroom", "/in-the-news",
                            "/press-release")),
    ("Sponsored",          ("/sponsored", "/advertorial", "/promoted",
                            "/partner-content", "/paid-post")),
    ("Guest Post / Niche Edit", ("/blog/", "/post/", "/article", "/insights",
                                 "/guides", "/2019/", "/2020/", "/2021/",
                                 "/2022/", "/2023/", "/2024/", "/2025/", "/2026/")),
]

def _as_bool(v) -> bool:
    return str(v).strip().lower() in ("true", "1", "yes", "y", "t")

def classify_backlink_website(source_url: str,
                              sponsored=False, ugc=False, image=False,
                              sitewide=False, nofollow=False,
                              type_of_anchor: str = "") -> str:
    """Primary link/site type. Boolean flags dominate; then URL path patterns.
    Priority mirrors the SOP tie-break order."""
    src = (source_url or "").strip().lower()
    sponsored, ugc, image, sitewide = map(_as_bool, (sponsored, ugc, image, sitewide))
    is_image_url = src.rsplit("?", 1)[0].endswith(_IMG_EXT)

    # flag-driven (highest confidence)
    if sponsored:
        return "Sponsored"
    if image or is_image_url or "image" in str(type_of_anchor).lower():
        return "Image"
    if sitewide:
        return "Sitewide"
    if ugc:
        return "UGC/Forum"
    # institutional
    if re.search(r"\.(edu|gov)([/.]|$)", src) or ".ac." in src or ".gov." in src:
        return ".edu/.gov"
    # path-driven
    for label, patterns in _LINKTYPE_PATTERNS:
        if any(p in src for p in patterns):
            return label
    return "Other"


# ==================================================================
# KEYWORD-FILE METRICS
# ==================================================================

# Per-field aliases across Ahrefs / Semrush / others. First header present wins.
# Extend freely. Matching is case-insensitive and exact on the stripped header.
KW_ALIASES = {
    "url":      ["url", "current url", "page url", "page", "target url", "landing page"],
    "keyword":  ["keyword", "keywords", "query", "search term"],
    "volume":   ["volume", "search volume", "vol", "monthly searches",
                 "monthly search volume", "avg. monthly searches"],
    "position": ["position", "current position", "pos", "rank", "current rank",
                 "best position"],
    "traffic":  ["traffic", "organic traffic", "traffic (desc)", "est. traffic",
                 "estimated traffic", "traffic %", "organic traffic %"],
    "serp_features": ["serp features", "serp feature", "serp_features",
                      "features", "serp"],
}

def _resolve_kw_columns(df: pd.DataFrame, override: dict | None = None) -> dict:
    """Map canonical field -> actual column name present in df, using KW_ALIASES.
    An explicit `override` (e.g. CONFIG['kw_colmap']) takes precedence when its
    target column actually exists in df."""
    lower = {str(c).strip().lower(): c for c in df.columns}
    resolved = {}
    for field, aliases in KW_ALIASES.items():
        # explicit override first, if that column truly exists
        if override and field in override and override[field] in df.columns:
            resolved[field] = override[field]
            continue
        hit = next((lower[a] for a in aliases if a in lower), None)
        resolved[field] = hit            # may be None for optional fields
    return resolved

def _to_num(s: pd.Series) -> pd.Series:
    return pd.to_numeric(
        s.astype(str).str.replace(r"[,\s$%]", "", regex=True),
        errors="coerce",
    )

def aggregate_keyword_file(df_kw: pd.DataFrame, colmap: dict | None = None) -> pd.DataFrame:
    """Collapse a ranking-keyword export to one row per URL with the 8 metrics.
    Auto-resolves Ahrefs/Semrush/other column names via KW_ALIASES; `colmap`
    (e.g. CONFIG['kw_colmap']) is treated as an optional override.
    Returns a DataFrame keyed by 'url'."""
    cm = _resolve_kw_columns(df_kw, override=colmap or CONFIG.get("kw_colmap"))
    missing = [f for f in ("url", "keyword", "volume", "position") if not cm.get(f)]
    if missing:
        raise KeyError(
            f"Keyword file missing required field(s) {missing}. "
            f"Headers seen: {list(df_kw.columns)}. "
            f"Add the header to KW_ALIASES."
        )

    top_n_avg   = CONFIG["kw_top_n_for_avg"]
    top_kw_n    = CONFIG["kw_top_keywords_n"]
    rank_by     = CONFIG["kw_top_rank_by"]
    rich_tokens = [t.lower() for t in CONFIG["rich_snippet_tokens"]]

    d = df_kw.copy()
    d["_url"]  = d[cm["url"]].astype(str).str.strip().str.lower()
    d["_kw"]   = d[cm["keyword"]].astype(str).str.strip()
    d["_vol"]  = _to_num(d[cm["volume"]]).fillna(0)
    d["_pos"]  = _to_num(d[cm["position"]])
    d["_traf"] = _to_num(d[cm["traffic"]]).fillna(0) if cm.get("traffic") else 0.0
    has_serp   = bool(cm.get("serp_features"))
    if has_serp:
        d["_serp"] = d[cm["serp_features"]].fillna("").astype(str).str.lower()

    rows = []
    for url, g in d.groupby("_url"):
        g = g[g["_kw"].ne("")]
        if g.empty:
            continue
        g_pos = g.dropna(subset=["_pos"])

        # best keyword = highest volume (tie -> best position)
        gv = g.sort_values(["_vol", "_pos"], ascending=[False, True])
        best_row = gv.iloc[0]

        # top-N keywords by chosen basis
        basis = "_traf" if rank_by == "traffic" else "_vol"
        top_kw = (g.sort_values(basis, ascending=False)["_kw"]
                    .head(top_kw_n).tolist())

        # avg position over best-N ranked kws
        avg_top = (g_pos.nsmallest(top_n_avg, "_pos")["_pos"].mean()
                   if not g_pos.empty else None)

        rich = (bool(g["_serp"].apply(lambda s: any(t in s for t in rich_tokens)).any())
                if has_serp else None)

        rows.append({
            "url":                        url,
            "total_ranking_kws":          int(len(g)),
            "total_traffic":              round(float(g["_traf"].sum()), 1),
            "total_volume":               int(g["_vol"].sum()),
            "best_kw":                    best_row["_kw"],
            "best_kw_position":           (None if pd.isna(best_row["_pos"]) else round(float(best_row["_pos"]), 1)),
            "highest_position":           (None if g_pos.empty else round(float(g_pos["_pos"].min()), 1)),
            "rich_snippet_participation": rich,
            "avg_position_top5":          (None if avg_top is None else round(float(avg_top), 1)),
            "top_3_keywords":             " | ".join(top_kw),
        })

    return pd.DataFrame(rows)


def merge_keyword_metrics(df_backlinks: pd.DataFrame,
                          df_kw_agg: pd.DataFrame,
                          backlink_col: str | None = None,
                          prefix: str = "") -> pd.DataFrame:
    """Left-join aggregated kw metrics onto the backlink df by normalized URL.
    Use prefix='source_' / 'target_' to attach both sides without collision."""
    bcol = backlink_col or CONFIG["kw_join_backlink_column"]
    out = df_backlinks.copy()
    out["_join"] = out[bcol].astype(str).str.strip().str.lower()
    agg = df_kw_agg.copy()
    if prefix:
        agg = agg.rename(columns={c: f"{prefix}{c}" for c in agg.columns if c != "url"})
    merged = out.merge(agg, left_on="_join", right_on="url", how="left")
    return merged.drop(columns=["_join", "url"], errors="ignore")


# ==================================================================
# PIPELINE
# ==================================================================

def add_classifier_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Add the 4 derived classifier columns. Column names assume the user's
    22-col schema; adjust the .get() keys if your headers differ."""
    out = df.copy()

    out["domain"] = out["Source url"].apply(extract_domain)

    out["classification_backlink_page"] = out["Target url"].apply(
        lambda u: classify_page(u, CONFIG["root_domain"]))

    out["type_of_anchor"] = out["Anchor"].apply(classify_anchor)

    out["type_of_backlink_website"] = out.apply(
        lambda r: classify_backlink_website(
            r.get("Source url", ""),
            sponsored=r.get("Sponsored", False),
            ugc=r.get("Ugc", False),
            image=r.get("Image", False),
            sitewide=r.get("Sitewide", False),
            nofollow=r.get("Nofollow", False),
            type_of_anchor=r.get("Type of anchor", ""),
        ),
        axis=1,
    )
    return out


def enrich(backlinks_path: str,
           keywords_path: str | None = None,
           output_path: str = "backlinks_enriched.csv",
           join_both_sides: bool = False) -> pd.DataFrame:
    """End-to-end: read backlinks (+ optional kw file), add all columns, write CSV.

    join_both_sides=True attaches kw metrics for BOTH Source url (source_*) and
    Target url (target_*). Otherwise uses CONFIG['kw_join_backlink_column'].
    """
    df = pd.read_csv(backlinks_path)
    df = add_classifier_columns(df)

    if keywords_path:
        kw_agg = aggregate_keyword_file(pd.read_csv(keywords_path))
        if join_both_sides:
            df = merge_keyword_metrics(df, kw_agg, "Source url", prefix="source_")
            df = merge_keyword_metrics(df, kw_agg, "Target url", prefix="target_")
        else:
            df = merge_keyword_metrics(df, kw_agg)

    df.to_csv(output_path, index=False)
    print(f"Wrote {len(df):,} rows -> {output_path}")
    return df


# ==================================================================
# FILE-TYPE AUTO-DETECTION  (kw file vs backlink file, names vary)
# ==================================================================

# Header tokens that signal each file type. Matching is case-insensitive
# and substring-based, so "Search Volume", "Volume", "Current URL", etc. all hit.
_BACKLINK_SIGNATURE = [
    "source url", "target url", "anchor", "nofollow", "sponsored", "ugc",
    "sitewide", "external links", "internal links", "backlink", "referring",
    "first seen", "last seen", "lost link", "page ascore", "domain rating",
]
_KEYWORD_SIGNATURE = [
    "keyword", "volume", "search volume", "position", "current position",
    "traffic", "cpc", "kd", "keyword difficulty", "serp features",
]

def _header_tokens(path: str) -> list[str]:
    """Read just the header row, return lowercased column names."""
    head = pd.read_csv(path, nrows=0)
    return [str(c).strip().lower() for c in head.columns]

def _score(tokens: list[str], signature: list[str]) -> int:
    joined = " | ".join(tokens)
    return sum(1 for sig in signature if sig in joined)

def detect_file_type(path: str) -> str:
    """Return 'backlinks', 'keywords', or 'unknown' by header signature."""
    try:
        tokens = _header_tokens(path)
    except Exception:
        return "unknown"
    b, k = _score(tokens, _BACKLINK_SIGNATURE), _score(tokens, _KEYWORD_SIGNATURE)
    # Source/Target url pair is a near-certain backlink tell.
    if "source url" in tokens and "target url" in tokens:
        return "backlinks"
    # A keyword column without a target url is a near-certain kw tell.
    if "keyword" in tokens and "target url" not in tokens and b < 3:
        return "keywords"
    if b == k:
        return "unknown"
    return "backlinks" if b > k else "keywords"

def identify_competitor_files(folder: str) -> dict:
    """Given one competitor folder, find + classify its CSVs.
    Returns {'backlinks': path|None, 'keywords': path|None, 'unknown': [paths]}."""
    csvs = sorted(
        glob.glob(os.path.join(folder, "*.csv"))
        + glob.glob(os.path.join(folder, "*.CSV"))
    )
    found = {"backlinks": None, "keywords": None, "unknown": []}
    for p in csvs:
        t = detect_file_type(p)
        if t in ("backlinks", "keywords") and found[t] is None:
            found[t] = p
        elif t in ("backlinks", "keywords"):
            # second file of same detected type — keep the larger one, flag the other
            found["unknown"].append(p)
        else:
            found["unknown"].append(p)
    # Fallback: exactly two CSVs, one already typed, the other "unknown" -> assign it
    if len(csvs) == 2:
        if found["backlinks"] and not found["keywords"] and found["unknown"]:
            found["keywords"] = found["unknown"].pop(0)
        elif found["keywords"] and not found["backlinks"] and found["unknown"]:
            found["backlinks"] = found["unknown"].pop(0)
    return found


# ==================================================================
# FOLDER PIPELINE  (competitor_backlinks/<name>/{kw.csv, backlinks.csv})
# ==================================================================

def process_competitor(folder: str, competitor: str,
                        join_both_sides: bool = False) -> pd.DataFrame | None:
    """Enrich one competitor folder. Returns the enriched df (with a
    'competitor' column) or None if no backlink file was found."""
    files = identify_competitor_files(folder)
    if not files["backlinks"]:
        print(f"  [skip] {competitor}: no backlink CSV identified "
              f"(unknown: {[os.path.basename(u) for u in files['unknown']]})")
        return None

    print(f"  [ok]   {competitor}: "
          f"backlinks={os.path.basename(files['backlinks'])}, "
          f"keywords={os.path.basename(files['keywords']) if files['keywords'] else 'NONE'}")

    df = pd.read_csv(files["backlinks"])
    df = add_classifier_columns(df)

    if files["keywords"]:
        kw_agg = aggregate_keyword_file(pd.read_csv(files["keywords"]))
        if join_both_sides:
            df = merge_keyword_metrics(df, kw_agg, "Source url", prefix="source_")
            df = merge_keyword_metrics(df, kw_agg, "Target url", prefix="target_")
        else:
            df = merge_keyword_metrics(df, kw_agg)

    df.insert(0, "competitor", competitor)
    return df

def process_all_competitors(root: str = "competitor_backlinks",
                            output_path: str = "all_competitors_enriched.csv",
                            per_competitor_files: bool = True,
                            join_both_sides: bool = False) -> pd.DataFrame:
    """Walk competitor_backlinks/<competitor>/ folders, enrich each, and
    write one combined CSV (plus optional per-competitor CSVs).

    Folder layout expected:
        competitor_backlinks/
            CompetitorA/  -> two CSVs (kw + backlinks, any names)
            CompetitorB/  -> two CSVs
            ...
    """
    if not os.path.isdir(root):
        raise FileNotFoundError(f"Root folder not found: {root}")

    subfolders = sorted(
        d for d in glob.glob(os.path.join(root, "*")) if os.path.isdir(d)
    )
    if not subfolders:
        raise FileNotFoundError(f"No competitor subfolders inside {root}")

    print(f"Found {len(subfolders)} competitor folder(s) in '{root}':")
    frames = []
    for folder in subfolders:
        competitor = os.path.basename(folder.rstrip("/"))
        df = process_competitor(folder, competitor, join_both_sides=join_both_sides)
        if df is None:
            continue
        frames.append(df)
        if per_competitor_files:
            out = os.path.join(folder, f"{competitor}_enriched.csv")
            df.to_csv(out, index=False)

    if not frames:
        raise RuntimeError("No competitor produced an enriched table.")

    combined = pd.concat(frames, ignore_index=True, sort=False)
    combined.to_csv(output_path, index=False)
    print(f"\nCombined: {len(combined):,} rows from {len(frames)} competitor(s) "
          f"-> {output_path}")
    return combined


if __name__ == "__main__":
    # Walk competitor_backlinks/<competitor>/ and enrich everything.
    # Edit CONFIG (root_domain, brand_terms, kw_colmap) first.
    process_all_competitors(
        root="competitor_backlinks",
        output_path="all_competitors_enriched.csv",
        per_competitor_files=True,    # also writes <competitor>_enriched.csv in each folder
        join_both_sides=False,        # True -> source_* and target_* kw metrics
    )