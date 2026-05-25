# CLAUDE.md

Project memory for the **competitor backlink enrichment pipeline**. Read this before editing anything.

---

## What this project is

A single Python module, `backlink_enrich.py`, that takes competitor backlink exports (from Ahrefs/Semrush) plus ranking-keyword exports, and adds derived analysis columns. It is the **data-prep stage** of a larger link-building operation:

1. **(this code)** Ingest competitor backlink + keyword files → add classifier columns + keyword metrics → one combined CSV.
2. (separate SOP) Extract/score linkable prospects, paid-vs-free, pricing, outreach.
3. (separate SOP) Vet individual prospects before outreach.

This repo is **only stage 1**. Don't build stages 2–3 here unless asked.

The script is **config-driven**: all tunables (brand terms, generic-anchor list, thresholds, column aliases) live in a `CONFIG` dict and module-level lists at the top of the file. **Edit config, not function bodies.**

---

## Repo / data layout

Input is a folder tree. The script walks it; filenames vary and are auto-detected by header, NOT by name.

```
competitor_backlinks/
├── CompetitorA/
│   ├── <anything>.csv        # backlinks file  (auto-detected)
│   └── <anything>.csv        # keywords file   (auto-detected)
├── CompetitorB/
│   ├── ...
└── ...
```

Each competitor folder has **two CSVs**: one backlink export, one ranking-keyword export. They may come from different tools (one competitor Ahrefs, another Semrush) — the code adapts per file.

Outputs:
- `<competitor>_enriched.csv` written inside each competitor folder (if `per_competitor_files=True`).
- `all_competitors_enriched.csv` at the root — all competitors stacked, with a `competitor` column.

---

## Single dependency

`pandas`. Install: `pip install pandas --break-system-packages` (or in a venv). Optional: `tldextract` for perfect eTLD+1 (the code has a built-in fallback table and does not require it).

---

## How to run

Edit `CONFIG` (at minimum `root_domain` and `brand_terms`), then:

```bash
python3 backlink_enrich.py
```

The `__main__` block calls `process_all_competitors("competitor_backlinks")`. Or call programmatically:

```python
import backlink_enrich as be
be.CONFIG["root_domain"] = "mybrand.com"
be.CONFIG["brand_terms"] = ["mybrand", "my brand"]
combined = be.process_all_competitors(
    root="competitor_backlinks",
    output_path="all_competitors_enriched.csv",
    per_competitor_files=True,
    join_both_sides=False,   # True → adds source_* AND target_* kw metric columns
)
```

---

## Input contract: backlink file

Canonical 22-column schema (merged Ahrefs+Semrush). Header names the classifiers depend on:

`Source url`, `Target url`, `Anchor`, `Type of anchor`, `Sponsored`, `Ugc`, `Image`, `Sitewide`, `Nofollow` (plus `Page ascore`, `External links`, `Internal links`, `Text`, `Frame`, `Form`, `First seen`, `Last seen`, `New link`, `Lost link`, `Source title`, `Backlink Domain`, `Classification of backlink page`).

Classifiers read via `r.get("Source url", "")` etc., so missing optional columns degrade gracefully. **`Source url`, `Target url`, `Anchor` are required.** Bool columns accept `true/TRUE/1/yes/y/t`.

## Input contract: keyword file

Per-URL ranking export. Column names are **auto-resolved** via `KW_ALIASES` (case-insensitive). Required fields: `url`, `keyword`, `volume`, `position`. Optional: `traffic`, `serp_features`.
- Ahrefs headers like `Current URL`, `Volume`, `Position`, `Organic traffic`, `SERP features` → resolved.
- Semrush headers like `URL`, `Keyword`, `Search Volume`, `Position`, `Traffic`, `SERP Features` → resolved.
- If a header isn't recognized, `aggregate_keyword_file` raises `KeyError` naming the missing field and listing seen headers. **Fix = add the header string to the right list in `KW_ALIASES`**, don't patch the function.

---

## Output columns produced

**Four classifier columns** (always):
| Column | From | Values |
|---|---|---|
| `domain` | Source url | host, lowercased, www-stripped |
| `classification_backlink_page` | Target url | Home / Blog-Resource / Product / Collection / Service / Contact-About / Question-Guide / Image / Other |
| `type_of_anchor` | Anchor | Naked / Branded / Keyword / Other (+ `Keyword:Exact`/`:Partial`/`:Topical` if `anchor_sub_bucket=True`) |
| `type_of_backlink_website` | Source url + bool flags | Sponsored / Image / Sitewide / UGC-Forum / .edu-.gov / Profile / Podcast / Resource-Listicle / Directory / Digital PR-News / Guest Post-Niche Edit / Other |

**Eight keyword metrics** (when a keyword file is present, joined per URL):
`total_ranking_kws`, `total_traffic`, `total_volume`, `best_kw` (+ `best_kw_position`), `highest_position`, `rich_snippet_participation`, `avg_position_top5`, `top_3_keywords`.

Plus a `competitor` column (folder name).

---

## Function map

- `extract_domain(url, strip_www=True, registrable=False)` — host parser; `registrable=True` → eTLD+1.
- `classify_page(url, root_domain)` — page-type; detects Home via root_domain.
- `classify_anchor(anchor, root_domain, sub_bucket)` — anchor bucket; word-boundary regex matching.
- `classify_backlink_website(source_url, sponsored, ugc, image, sitewide, nofollow, type_of_anchor)` — link/site type; flags beat path patterns.
- `aggregate_keyword_file(df_kw, colmap=None)` — collapse kw export → one row/URL + 8 metrics. Auto-resolves columns.
- `merge_keyword_metrics(df_backlinks, df_kw_agg, backlink_col, prefix)` — left-join by normalized URL.
- `detect_file_type(path)` / `identify_competitor_files(folder)` — header-signature auto-detection.
- `add_classifier_columns(df)` — adds the 4 classifiers.
- `process_competitor(folder, competitor, join_both_sides)` — one folder.
- `process_all_competitors(root, output_path, per_competitor_files, join_both_sides)` — top-level entry point.
- `enrich(backlinks_path, keywords_path, output_path, join_both_sides)` — single-pair convenience (non-folder).

---

## Conventions & gotchas (LEARNED — respect these)

1. **Config over code.** Brand terms, generic anchors (`GENERIC_ANCHORS`), URL tokens (`_URL_TOKENS`), page patterns (`_PAGE_PATTERNS`), link-type patterns (`_LINKTYPE_PATTERNS`), and kw aliases (`KW_ALIASES`) are all editable data at the top. New requirement = extend a list, not rewrite logic.

2. **Anchor matching is word-boundary regex** (`_word_hit` via `\b...\b`). This is deliberate: it stops `more` matching `moreover` and `little` matching unrelated words — the main cause of the old ~80%-accuracy formula's false positives. Don't switch back to plain substring `in`.

3. **Brand terms must be distinctive.** Avoid bare generic tokens (`little`, `sleep`) that collide with English words; prefer joined/long forms (`littlesleepies`, `little sleepies`). A brand anchor with word-count > `anchor_word_count_threshold` (default 3) is reclassified as `Keyword`, not `Branded`.

4. **Keyword join is by EXACT normalized URL** (lowercased + trimmed). Source/Target URL in the backlink file must match the URL in the keyword file. If exports differ on trailing slash or http-vs-https, the join silently misses (metrics come out NaN). If you see widespread NaN kw metrics, that's the cause — add URL canonicalization to `merge_keyword_metrics` (strip trailing slash, normalize scheme) rather than assuming the data is wrong.

5. **`best_kw` = highest volume** (tie → best position). **`top_3_keywords` = ranked by `kw_top_rank_by`** (default `traffic`, switchable to `volume`). `highest_position` = numerically smallest position (closest to #1). `avg_position_top5` = mean position over the best-N ranked kws (`kw_top_n_for_avg`).

6. **Numbers get cleaned** through `_to_num` (strips commas, `$`, `%`, whitespace). SERP/text columns are `.fillna("")`-ed before string ops — NaN floats previously broke the rich-snippet check; keep that coercion.

7. **Subdomains are preserved by default** (`blog.x.com` ≠ `x.com`) because subdomains often have separate editorial control. Use `registrable=True` only when intentional rollup is wanted.

8. **File detection is by header, never filename.** `Source url`+`Target url` ⇒ backlinks; `keyword` without `target url` ⇒ keywords. Two-CSV-folder fallback assigns the leftover by elimination. If a real export uses headers that fool this, extend `_BACKLINK_SIGNATURE` / `_KEYWORD_SIGNATURE`.

---

## Testing

No formal test suite yet. Validated manually against the user's three sample backlink rows and mixed Ahrefs/Semrush keyword mocks. When changing classifier logic, build a tiny mock folder tree (two competitors, mismatched vendor headers) and run `process_all_competitors` end-to-end before committing. If you add a test suite, prefer `pytest` with small inline DataFrames over fixture files.

---

## Do / Don't

- **Do** keep the module single-file and dependency-light.
- **Do** make every new classification rule data-driven and add a one-line comment citing the signal it uses.
- **Don't** hardcode any brand or domain inside a function (the original formulas hardcoded `bloggeroutreach.io` / `stellarseo.com` — that was the thing we generalized away).
- **Don't** add network calls, scraping, or API keys here — this stage is pure local CSV transformation. Enrichment that needs the web belongs in stage 2.
- **Don't** silently drop rows; annotate instead, so the user can audit.