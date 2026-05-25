# Authoritative Reference URLs — Link Spam & Quality Policies

> Claude should consult these (web_fetch) when a vetting judgment depends on
> what Google actually says, not what SEO blogs claim. Official Google docs
> are primary; third-party sources are interpretation only.

## TIER 1 — Google Official: Spam & Link Policies (PRIMARY SOURCES)

- Spam policies for Google Web Search (the master page — link spam, cloaking, hacked, scaled content, site reputation abuse, expired-domain abuse, sneaky redirects)
  https://developers.google.com/search/docs/essentials/spam-policies

- Google Search Spam Updates (how SpamBrain & link spam updates work, why recovery lags)
  https://developers.google.com/search/docs/appearance/spam-updates

- Google Search Essentials (the overarching "what Google expects" doc — replaces old Webmaster Guidelines)
  https://developers.google.com/search/docs/essentials

- Qualify outbound links to Google (rel="nofollow", "sponsored", "ugc" — the correct attributes for paid/UGC links)
  https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links

## TIER 2 — Google Official: Quality, E-E-A-T & Ranking Systems

- Creating helpful, reliable, people-first content (the "helpful content" guidance + self-assessment questions, E-E-A-T)
  https://developers.google.com/search/docs/fundamentals/creating-helpful-content

- Google Search ranking systems guide (lists the systems, incl. link analysis & the helpful content signal)
  https://developers.google.com/search/docs/appearance/ranking-systems-guide

- Search Quality Rater Guidelines (the full PDF raters use — E-E-A-T, Lowest-quality criteria, YMYL)
  https://services.google.com/fh/files/misc/hsw-sqrg.pdf

- How Google Search works (crawling, indexing, ranking overview)
  https://developers.google.com/search/docs/fundamentals/how-search-works

## TIER 3 — Google Official: Enforcement, Hacked Content & Reporting

- Manual Actions report (incl. "Unnatural links TO your site" and "Unnatural links FROM your site")
  https://support.google.com/webmasters/answer/9044175

- Disavow backlinks (when/how — use sparingly)
  https://support.google.com/webmasters/answer/2648487

- Fixing hacked sites overview (security foundation checks)
  https://developers.google.com/search/docs/monitor-debug/security/hacked-site

- Fix the Japanese keyword hack (the official guide that recommends the site: operator for detection)
  https://web.dev/articles/fix-the-japanese-keyword-hack

- Report spam, paid links, or malware to Google (Search Quality User Report)
  https://developers.google.com/search/help/report-quality-issues

## TIER 4 — Google Official: Updates History & Search Operators

- Google Search status dashboard / ranking updates list (authoritative update dates for penalty-fingerprinting)
  https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history

- Google Search Central Blog (where new spam/core updates are announced first)
  https://developers.google.com/search/blog

- Refine web searches (official list of supported search operators incl. before:/after:)
  https://support.google.com/websearch/answer/2466433

## TIER 5 — Reputable Third-Party (INTERPRETATION ONLY — never override Tier 1)

- Search Engine Land — Google algorithm update history (clean dated timeline)
  https://searchengineland.com/library/platforms/google/google-algorithm-updates

- Search Engine Journal — Google algorithm change history
  https://www.searchenginejournal.com/google-algorithm-history/

- Search Engine Roundtable (fastest reporting on live update chatter)
  https://www.seroundtable.com/

- Ahrefs glossary — Link Spam
  https://ahrefs.com/seo/glossary/link-spam

- Ahrefs — Google advanced search operators (the full operator list)
  https://ahrefs.com/blog/google-advanced-search-operators/

## USAGE RULES FOR CLAUDE
- When citing a policy, fetch and quote the Tier 1/2/3 Google page — not a blog's paraphrase.
- If a third-party source conflicts with a Google page, the Google page wins.
- Update dates for penalty-fingerprinting: prefer the Google status dashboard / blog; use SE Land/SEJ only to cross-check.
- Treat any "internal API leak" claims (e.g., "BadBackLinks signal") as unconfirmed unless tied to an official source.