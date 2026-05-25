# project.md — Backlink Prospect Vetting Criteria (Claude-Assisted SOP)

## TL;DR
- A defensible 2025-2026 vetting stack is built on three orthogonal axes: (1) is the site **real** (brand, traffic, history, third-party footprint), (2) is the site **healthy** (no penalty, no hacked footprint, no link-farm behavior, indexing-fresh), and (3) is the link **going to pass value to YOU** (topical fit, editorial placement, outbound recipient quality, anchor health).
- DR/DA floors are still useful but only as a *first filter*; every authority claim must be corroborated by organic traffic, branded search, and third-party presence — DR can be inflated in ~30 days via redirect chains and PBN tiers (services such as BoostMyDR's drisbullshit.com experiment openly market "DR 0 → DR 50+ in 30 days" for ~$99), so a high-DR / low-traffic / low-branded-search domain is a strong red flag, not a green light.
- The single most predictive 2026 signal is the prospect's **outbound link behavior** over the prior 3-6 months: who they link to, whether those recipients have been hit by HCU (Sept 14, 2023), the March 2024 spam/core updates, or the August 26 → September 22, 2025 spam update, and whether the link mix screams "guest-post farm" (sponsored crypto + casino + SaaS roundups in a single month).

## Key Findings (the validated heuristic stack)

The user's existing thresholds are **directionally correct but require sharpening, corroboration logic, and explicit relaxation rules** to avoid both false-positive rejections (rejecting legit niche/local sites) and false-negative acceptances (buying inflated PBN-style domains). The new checks below extend the user's list with criteria most modern expert link auditors consider load-bearing: anchor-text distribution audit of the prospect, link placement type (editorial vs. sidebar/footer/author-box), author E-E-A-T verifiability, AI-content saturation, redirect/cloaking checks, TLD trust class, domain-age-vs-authority mismatch, and link velocity anomalies.

---

## Details — Criterion-by-Criterion Validation & Sharpening

### 1. AUTHORITY METRIC (DR/DA-style score)

**User thresholds:** min 7-10, medium 20, ideal 35+. **Verdict: keep as a floor; enforce mandatory cross-check.**

Current consensus (2025-2026):
- DR and DA are **not** Google ranking factors — confirmed by John Mueller publicly multiple times. They are vendor estimates.
- DR can be manipulated in 10-30 days via **redirect chain inflation** — buying expired domains and 301-ing them to inflate referring-domain count. BoostMyDR's openly-documented drisbullshit.com experiment took a domain to DR 53 in 12 days for $99.
- Ahrefs' own published research finds DR-to-ranking-position correlation is roughly r ≈ 0.09 — statistically significant at scale, practically small for an individual page.
- The single best detector for inflated DR: **DR ÷ organic traffic ratio**, and **DA-vs-DR gap**. Per Rhino Rank's published heuristic: a DR 60+ with DA under 25 (gap >35) is "likely manipulated through redirect chains, PBN links, or other artificial methods." Conversely, DA significantly higher than DR is usually under-valued, not over-valued.
- Majestic's **Trust Flow ÷ Citation Flow ratio** is more manipulation-resistant. TF/CF ≥ 0.8 = healthy. TF/CF ≤ 0.3 = link-farm fingerprint.

**Sharpened rule:**
- Hard floor: **DR ≥ 20 OR DA ≥ 20 OR TF ≥ 15**, AND at least one corroborating signal (organic traffic, branded search, third-party presence).
- Auto-flag any prospect where: DR − DA > 25, OR TF/CF < 0.4, OR DR > 50 with monthly organic traffic < 500.
- DR alone is never sufficient justification — **traffic verification is mandatory.**

### 2. BRAND VISIBILITY / BRANDED SEARCH VOLUME

**User thresholds:** non-zero minimum, ~100 normal, ~1,000 ideal. **Verdict: keep, with explicit variant-enumeration protocol.**

Modern consensus treats branded search as one of the strongest signals of real-world authority and a leading indicator of AI Overview citation. Ahrefs' May 26, 2025 study by Louise Linehan & Xibeijia Guan, *"An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied)"*, found the top-3 Spearman correlations with AI Overview appearance were: **Branded Web Mentions (0.664), Branded Anchors (0.527), Branded Search Volume (0.392)** — confirming branded demand as a primary authority signal in modern Google/AI ranking systems. SparkToro research shows branded/navigational queries convert to site visits at much higher rates than informational queries even as overall click-through rates decline. Moz analysis shows sites with stronger branded search demand experience greater ranking stability during core updates.

**Operational protocol Claude should run:**
1. Enumerate brand-name variants: `brand`, `brand.com` (with TLD), `BrAnD` (cased), `b r a n d` (spaced), abbreviations/initialisms (e.g., HBR for Harvard Business Review), and common alt-spellings.
2. Look up each variant's monthly search volume.
3. Sum across variants — if total branded volume is zero across all variants AND the domain claims >10k monthly traffic, that is a *hollow-brand* red flag (likely fake-traffic or scraped-content site).
4. Verify the **#1 ranking site for the primary brand query is actually this domain** (defends against typosquatting — see Check #3).

**Sharpened thresholds:**
- 0 branded searches across all variants + claimed traffic >5k = AUTO-FAIL (hollow brand).
- 1-100 = conditional (acceptable only if niche/local).
- 100-1,000 = normal pass.
- 1,000+ = ideal.

### 3. BRAND TYPOSQUATTING / TRAFFIC-THEFT DETECTION

**Verdict: validated and important; formalize the operator workflow.**

Detection method:
1. Take the prospect domain's brand name. Run `"brand name"` and check the #1 organic result.
2. If the #1 result is a different domain (e.g., bestbuy.com when you are vetting bestbuy.co.ai), the prospect is a typosquatter trading on stolen brand search volume.
3. Cross-check the prospect's WHOIS / domain age — typosquatters are usually <2 years old vs. the real brand which is typically 10+ years.
4. Use a domain history checker (Apify Trovevault, ThreatFox, URLHaus, RDAP/WHOIS) to verify the domain was not previously parked, malware-infected, or held by a different operator.
5. Run `site:prospect-domain.com` and see whether the indexed content matches the brand identity it claims, or whether it is generic scraped/AI content riding the brand name.

A prospect that fails the "real #1 for its own brand query" test is **auto-fail.**

### 4. SECURITY / FOUNDATION — HACKED PAGES

**Verdict: validated; sharpen with specific footprint patterns.**

Google's official guide ("Fix the Japanese keyword hack" on web.dev) explicitly recommends the `site:yourdomain.com` operator as the front-line detection technique. The hacker pattern: auto-generated pages with Japanese (or Chinese, or Cyrillic) text in titles, with affiliate links to counterfeit-brand stores, monetized by cloaking (page returns clean HTML to humans but spam HTML to Googlebot).

**Operator playbook (Claude runs all of these):**
- `site:prospect.com` — flip through 5-10 result pages. Look for non-native-language titles, gibberish URL slugs (e.g., `/ltjmnjp/341.html`), pharma/counterfeit anchor text.
- `site:prospect.com japan` (or `china`, `viagra`, `cialis`, `replica`, `gucci`, `nike`, etc.) — surfaces Japanese-keyword/pharma injections.
- `site:prospect.com -inurl:prospect.com` — quick check for outbound cloaked redirects.
- Compare total `site:` result count vs. plausible page count from a crawler. A WordPress blog claiming ~500 posts that returns ~200,000 indexed URLs is hacked.
- Visit a sample of suspicious URLs both as a human and via a Googlebot user-agent emulator — divergent content = cloaking confirmed.

Any positive result here is **auto-fail.** A site with active hacked pages will pass tainted equity at best and a manual action infection at worst.

### 5. ADULT / CBD / CASINO / GAMBLING FOOTPRINT SCAN

**Verdict: validated; standardize term list and reasoning.**

Same `site:` operator method, with a broader injected-content term list. Recommended quoted queries (run each):

```
site:prospect.com "casino"
site:prospect.com "viagra" OR "cialis"
site:prospect.com "porn" OR "sex" OR "xxx"
site:prospect.com "cbd"
site:prospect.com "escort"
site:prospect.com "loan" OR "payday"
site:prospect.com "replica" OR "fake"
site:prospect.com "essay writing"
site:prospect.com "betting" OR "poker"
site:prospect.com "weed" OR "kratom"
```

Reasoning: these are the categories most often associated with parasite-SEO / site reputation abuse injections and with low-budget paid placements. A finance or parenting site that returns hits for "casino" or "viagra" indexed pages is either hacked or actively monetizing third-party junk — both disqualify it under Google's site reputation abuse policy (updated November 2024 and again January 21, 2025, with the language: *"Site reputation abuse is the practice of publishing third-party pages on a site in an attempt to abuse search rankings by taking advantage of the host site's ranking signals"*). A few sponsored disclosures or one off-topic affiliate page is not disqualifying — repeated multi-category hits are.

### 6. INDEXING FRESHNESS / CRAWL ACTIVITY

**Verdict: validated; clarify operator reliability.**

Google's `daterange:` operator using the Julian format has been **officially deprecated** and returns unreliable results — do not rely on it. Two reliable methods remain:

1. **Tools → Any time → Custom range** in Google's UI: filter `site:prospect.com` results to "Past month," "Past year," etc. This uses Google's indexed-date metadata accurately.
2. **`before:` and `after:` operators in YYYY-MM-DD format** (these still work per Google's own search-help docs: *"To find documents last updated before a particular date: Enter `before:` in front of a year or specific date"*). Example: `site:prospect.com after:2025-11-01 before:2026-05-01` shows pages indexed/updated in that window. Caveat: results reflect last *modified/indexed* date, not first publication date.
3. **`cache:` operator** is partially deprecated; use the URL Inspection tool in GSC for owned sites, or third-party Chrome extensions ("Crawl Date Checker for Google") for prospect sites the user does not control.

**Sharpened thresholds:**
- Zero new indexed URLs in last 6 months on a site claiming to publish regularly = AUTO-FAIL (likely deindexed or abandoned).
- <5 indexed URLs in last 3 months = conditional (suspicious; needs Wayback confirmation).
- Active monthly crawl/index of fresh URLs = pass.
- A site that has been silent for 6+ months and suddenly published a guest-post slot offer is **high-risk** — Google's crawl budget for that domain may be near-zero, meaning your link won't be discovered or weighted.

### 7. PUBLISHING ACTIVITY / SITE LIVENESS / EXPIRED-DOMAIN DETECTION

**Verdict: validated; explicit Wayback workflow.**

Google's official spam policy lists "expired domain abuse" as a distinct violation since March 2024: *"an expired domain name is purchased and repurposed primarily to manipulate Search rankings by hosting content that provides little to no value to users."* Detection workflow:

1. Pull domain registration history (RDAP/WHOIS). Sudden registrar change + sudden topic pivot = red flag.
2. Wayback Machine (archive.org): check 5-10 snapshots across the full domain history. Look for:
   - Sudden niche pivots (cooking blog → finance authority site).
   - Gaps of 6-24 months between snapshots (parked / abandoned period).
   - Periods showing pharma/casino/foreign-language content even years ago — Google remembers.
   - Snapshot density: a domain with one snapshot per year for one year only is usually a temporary/throwaway domain.
3. Compare claimed niche today with archived niche — a mismatch is the textbook expired-domain-abuse fingerprint.

Pass condition: same or topically adjacent niche across the full archive, consistent publishing density (≥1 snapshot/quarter for the past 2 years), and at least one fresh post within the last 30-60 days.

### 8. THIRD-PARTY VALIDATION / PR / BUSINESS DIRECTORIES

**Verdict: validated; expand the corroboration checklist.**

A site claiming ~100k monthly organic visits should have a multi-channel digital footprint. Claude should attempt to corroborate at least 3 of these:

- Trustpilot / Reviews.io / G2 / Capterra (B2B) / BBB / Glassdoor (employer signal).
- Business directory listings (Crunchbase, LinkedIn Company Page, AngelList, Yelp for local).
- Press / earned media (Google News, mentioned on Medium, Forbes contributor pieces, podcast appearances).
- Reverse-lookup of contact phone/email — does the same NAP (Name, Address, Phone) appear consistently across listings?
- A YouTube channel, podcast, or social presence that matches the brand.

Absence of corroboration on a site claiming >50k traffic = high suspicion of fabricated metrics. This is one of the cleanest signals because legitimate businesses leak signal everywhere.

### 9. NON-MANIPULATIVE / IDENTITY CONSISTENCY CHECK

**Verdict: validated; tie to NAP consistency.**

NAP (Name, Address, Phone number) consistency is a documented local SEO ranking factor and a general E-E-A-T signal. Inconsistent identity across the site itself ("Contact" says a US business, "About" says India outsourcing shop, footer copyright belongs to a third party) is the textbook fingerprint of a flipped / repurposed / "made-for-link-selling" domain.

Claude should run:
- Read About, Contact, Privacy Policy, Terms — extract entity name(s), address(es), phone(s), email(s).
- Cross-check those entities against WHOIS registrant (where unredacted) and the LinkedIn company page.
- Flag if: multiple inconsistent business names, an address that geocodes to a residence or virtual office in a different country than the claimed market, or a Privacy Policy boilerplate referencing a different company.

### 10. TOTAL PAGES vs TRAFFIC SANITY CHECK

**Verdict: validated; calibrate ratio expectations.**

Indexed-page count via `site:` is a rough Google estimate, not a precise figure (Google itself has stated `site:` totals are approximations). Cross-check with a crawler (Screaming Frog for ≤500 URLs free / unlimited paid, Sitebulb, JetOctopus) for sites under ~100k pages. Heuristics:

- A 200k-page site with <1k monthly organic traffic is almost certainly: (a) deindexed at scale, (b) auto-generated scaled content abuse hit by August 2025 spam update, or (c) a parked/expired property.
- Healthy benchmark (industry-dependent): publishers should see roughly **1-10+ monthly organic visits per indexed URL** as a baseline. Below ~0.05 visits/URL is fishy.
- Specifically watch for the "QualityCopiaFireflySiteSignal"-style fingerprint Google reportedly uses (per Breakline Agency's analysis of leaked Google modules): *"This module analyses the ratio of URLs generated during specific periods against the number of actual articles produced. A massive increase in page URLs without corresponding increases in substantive articles indicates poor quality to content ratios."*

### 11. KEYWORD-COUNT vs TRAFFIC SANITY CHECK (anti-fraud)

**Verdict: validated; this is one of the strongest fraud detectors.**

Healthy ranges (cross-niche; broaden for B2B/local):
- **Traffic ≥ keywords**: very common for high-CPC competitive niches (a site with 50k traffic on 100k keywords means ~0.5 visits per keyword, which is fine if there are a few hero pages doing the work).
- **Traffic ÷ ranking-keywords ratio** roughly 0.3-3 is normal.
- **10,000+ keywords with ~100 traffic** = ratio of 0.01 — almost always either deeply suppressed (algorithmic demotion), fake/scraped tool data, or rankings sit on page 5+ where they generate no real clicks.
- **100 traffic on <25 keywords** = also suspicious (either fake traffic or single-page fluke). A genuine 100-visit site should normally rank for 25-60+ keywords because of long-tail distribution.

Operationally: pull keywords from any backlink-analysis tool's "Organic keywords" report. Compute Traffic/Keywords ratio. Flag both extremes (<0.05 and >10).

### 12. NICHE RELEVANCE / KEYWORD OVERLAP

**Verdict: validated; quantify topical dedication.**

Modern consensus: a niche-relevant link from a mid-DR site outperforms a high-DR generic link. Google's entity-based understanding and AI Overview citation patterns strongly favor topical authority. The user's logic — that a dedicated niche site with modest traffic beats a giant generic site — is correct and aligned with current expert practice.

**Quantitative niche-fit checks:**
1. Pull the prospect's top 100 organic keywords. Compute: % that overlap with the user's target keyword universe.
2. **Topical dedication ratio** = ranking keywords in user's niche ÷ total ranking keywords. >30% = strong fit; 10-30% = adjacent/acceptable; <10% = generic site, link will pass diluted topical signal.
3. Check if **any of the user's existing target pages already rank in the prospect's top 100** — confirms organic topical relationship.
4. Use Majestic's **Topical Trust Flow** category breakdown to verify the prospect's earned trust is from the right niches (e.g., TF 25 from finance is more valuable for a finance site than TF 30 from random categories).

### 13. OUTBOUND LINK (OBL) PROFILE & GUEST-POST-FARM DETECTION

**Verdict: validated; operationalize with specific tools/reports.**

Tool-specific extraction (criterion 16 covers the forensic dimension; this is the structural check):

- **Ahrefs**: Site Explorer → **Outgoing Links** → **Linked domains** report. Per Ahrefs Help Center: *"Linked Domains has its own report in Site Explorer, under the Outgoing Links section… the report shows the unique domains that [the site] is linking out to."* Sort by "First seen" to surface recent outbound additions. Cross-check **Outgoing anchors** report for spammy/foreign-language anchor patterns.
- **Semrush**: Backlinks tool → **Outbound Domains** report (semrush.com/kb/1212-outbound-domains): *"Outbound Domains… you can quickly check out to which unique domains the analyzed website (or URL) points."* Default sort: number of outgoing links; alternate sort by Authority Score reveals if the prospect links mostly to low-AS junk.
- **Majestic**: Site Explorer outbound link columns (Total OutLinks, External Domains per URL, added 2017) and Topical Trust Flow on outbound recipients.
- **Screaming Frog / Sitebulb**: for sites under ~100k pages, crawl and aggregate external link counts per page; flag pages with >5 dofollow external commercial links.
- **Manual fallback**: open the 10 most recent posts; count dofollow external links per post.

**Heuristics:**
- Healthy editorial post: 1-3 dofollow external links per post, going to topically relevant authority sources (.edu, .gov, industry leaders).
- Guest-post-farm post: 4+ dofollow external links per post, going to a random mix of SaaS / crypto / casino / SEO services / unrelated niches.
- **Inbound:Outbound ratio anomaly** — a prospect with ~100 referring domains inbound but giving out 5,000-10,000 dofollow outbound links is a textbook link seller. Healthy editorial sites usually receive more dofollow links than they emit, or are roughly balanced.
- **Szymon Słowik's published filter (szymonslowik.com)**: *"If a domain is linking out to hundreds of unrelated sites across dozens of niches, it's a link farm dressed up as a blog. I don't care if the DR is 60. If the site's business model is selling links to everyone, the signal is diluted."*

### 14. TRAFFIC TREND / GROWTH DIRECTION

**Verdict: keep existing logic; add decline-cause diagnostic.**

When traffic is declining, diagnose *why* before rejecting:

- Match the drop date against known Google update dates: **Sept 14 2023 HCU**; **March 5 → April 19 2024 core**; **March 5-20 2024 spam**; **Aug 15 → Sept 3 2024 core**; **Nov 11 → Dec 5 2024 core**; **Dec 12-18 2024 core**; **Dec 19-26 2024 spam**; **March 13-27 2025 core**; **June 2025 core**; **Aug 26 → Sept 22 2025 spam**. A drop aligned within 1-3 days of any of these = algorithmic demotion. (Drop on a "random Tuesday" with no update = more likely technical/manual.)
- Sudden drop + recovery pattern within one update = volatility, not penalty.
- 6+ months of sustained decline through multiple updates = treat as penalty-active; AUTO-FAIL unless brand is truly elite.

### 15. PENALTY HISTORY & PENALTY-RISK FORECASTING

**Verdict: this is the most under-documented criterion; build out fully.**

You cannot see GSC for someone else's site, but algorithmic suppression leaves observable external fingerprints:

**A. "Crawled-currently-not-indexed" inference**: For a prospect site, run `site:prospect.com "{exact title of recent post}"`. If their recent posts (last 30-60 days) are not surfacing in `site:` results at all, Google is crawling but refusing to index — classic scaled-content-abuse or HCU suppression signal.

**B. Continuous-effort, zero-result fingerprint (user's Heuristic A)**: Validated — this maps onto the leaked **"QualityCopiaFireflySiteSignal"** pattern. Operationally: if the prospect has shipped >5k posts in the last 6-12 months but their traffic is flat or declining, they are algorithmically suppressed.

**C. Competitive-contagion (user's Heuristic B)**: Validated. Identify 5-10 direct competitors via SERP overlap and topical similarity. Check each competitor's traffic trend. If 3+ competitors have been demoted on the same Google update dates and the prospect is also near a marginal traffic level (~10k), the prospect is in a category Google is actively suppressing — your link will likely lose value within 1-2 quarters.

**D. SERP-disappearance test**: Check whether the prospect ranks for its own brand. A site demoted by HCU/spam updates often loses even brand-name rankings to scrapers and aggregators. Lost-own-brand-SERP = high suppression signal.

**E. Manual-action proxies**: A prospect site that is `noindex`ed at the homepage, returns 503/429 on first crawl, or has its sitemap empty despite many indexed URLs is a strong manual-action proxy.

**F. AI-content-saturation fingerprint** (new 2025 risk): For prospects, look for templated H2 patterns ("In conclusion," "Moreover," every-paragraph identical sentence-opener structure), zero unique imagery, no author identity, and listicle posts published >50/day. These trigger the August 2025 spam update's scaled-content-abuse classifier. Forecast: such sites will likely be demoted in the next 1-2 spam updates.

### 16. BACKLINK-BEHAVIOR FORENSICS (Outbound Recipient Health Audit)

**Verdict: high-signal advanced check; build out as standalone repeatable method.**

This is the criterion most under-served by surface tools. Step-by-step methodology:

**Step 1 — Extract.** From the prospect, pull the last 90-180 days of new outbound linked domains (Ahrefs Site Explorer → Outgoing Links → Linked domains, sort by "First seen"; or Semrush Backlinks → Outbound Domains; or Majestic site explorer outbound columns). Target: 50-200 recipient domains.

**Step 2 — Bulk health-check the recipients.** Paste recipients into Ahrefs **Batch Analysis** (handles up to 200 URLs/batch on standard+ plans, returns DR/UR/organic traffic/keywords/Top Country per URL). Alternative: Semrush Bulk Backlink Analysis (with **Backlinks Network Graph** which flags red-dot clusters that *"share an IP network and therefore could be a sign of a link scheme or manipulation. Backlinks from these domains might negatively impact search rankings"* per Semrush KB 1283) or Majestic bulk checker.

**Step 3 — Penalty-fingerprint each recipient.** For each recipient, look at the 12-24 month traffic graph and check for sharp drops aligned with: **Sept 14 2023 HCU, March 5 2024 spam/core, Aug 26 2025 spam update.** Any recipient that lost ≥50% on one of those dates and hasn't recovered is "penalized."

**Step 4 — Compute "bad neighborhood" share.** If >25% of the prospect's recent outbound dofollow links go to recipients that are clearly penalized, Google has likely already devalued the prospect's outbound link equity even if its own traffic looks intact. Per Google's stated position (ALM Corp summary of 2025 Google statements): *"if its systems determine a site is linking out in ways that are not helpful or do not align with policy, Google may simply ignore all links from that site."* A devalued linker is effectively worthless for you.

**Step 5 — Quality-of-company check.** If the prospect's recent outbound dofollow links go *to ranking, traffic-positive, topically relevant* sites in your niche, they're "good in the business" — strong pass signal. Mixed-bag (crypto + casino + random SaaS + your niche) = guest-post farm.

**Step 6 — Historical lag check.** Look 3-6 months back: for sites the prospect linked to in that window, did those recipients subsequently get penalized? A pattern of "linker links to X → X is penalized in next update" indicates the prospect actively services exactly the kind of clients Google is currently demoting. Avoid.

**Documented evidence base:**
- Google's official **2016 unnatural-outbound-links manual action** language (per Search Engine Land, Barry Schwartz): *"Google has detected a pattern of unnatural artificial, deceptive, or manipulative outbound links. Buying links or participating in link schemes in order to manipulate PageRank is a violation of Google's Webmaster Guidelines. As a result, Google has applied a manual spam action to the affected portions of your site."* Still active 2025-2026.
- **Surfer SEO study by Kasra Dash, published November 20, 2025** (surferseo.com/blog/helpful-content-update-study/), analyzing *"over 12,000 websites offering links and 500 websites hit by HCU"* using RankWatch data: *"Websites with a higher percentage of backlinks from link farms were consistently hit the hardest."* The article concluded that *"Google didn't just assess page quality—it assessed site-wide content structure and link profile health."* (Caveat: correlation, not proven causation.)
- **Case study — HouseFresh**: Per Managing Editor Gisele Navarro's own post *"HouseFresh has virtually disappeared from Google Search results. Now what?"*, the September 2023 HCU dropped daily visitors from ~4,000 to ~200 (~95% loss); the subsequent March 2024 core update brought cumulative traffic loss to **~91%** per Search Engine Land's coverage (searchengineland.com/review-site-google-traffic-affiliate-seo-content-440143).
- **Case study — GGRecon**: Per Esports Insider (October 2024), GGRecon announced closure on **October 18, 2024**; editor-in-chief Lloyd Coombes stated on X that GGRecon *"lost 95% of its traffic after being deemed 'unhelpful' by Google's algorithm"* and wrote on Medium: *"Google had basically stopped showing GGRecon anywhere near the top few pages… we lost investor confidence."*
- **Case study — 671 travel publishers**: James Brockbank (Managing Director, Digitaloft) published a 671-publisher analysis at digitaloft.co.uk/the-impact-of-googles-helpful-content-update-on-travel-publishers/. Brockbank wrote: *"I've analysed how 671 sites have performed since the update first rolled out in August 2022"* and found **175 sites (31%) lost more than 90% of their top-3 rankings**; **32% (213 sites) lost >90% of organic traffic**.
- **Case study — Laura Jawad (laurajawad.com)**: ~95% organic traffic loss by Aug 2024; site owner publicly hypothesized her demotion was caused by *outbound link devaluation cascade* — sites linking to her were HCU-hit, so her backlinks lost weight.

### 17. SPAM SCORE

**Verdict: keep as a *secondary* signal, not a primary disqualifier.**

Spam Score (Moz's 0-100% metric across 27 machine-learned signals comparing the domain to penalty/banned-site patterns) is **correlation-based, not causal.** Moz itself explicitly states that a high spam score does not mean a site is definitively spammy. Google does not use Moz Spam Score in ranking.

Thresholds (industry consensus per iMark InfoTech and Moz documentation):
- **<5%** = very clean.
- **<30%** = low risk / acceptable.
- **31-60%** = medium risk; investigate the underlying signals.
- **>60%** = treat as a strong negative signal; manually verify the underlying causes (link-farm referring profile, missing standard pages like Privacy/Terms, exact-match anchor dominance).

Caveats: ignore Spam Score on domains under 1 year old or with very few backlinks — insufficient data. Always pair Spam Score with the structural checks above; a 70% Spam Score with strong real traffic, branded search, and clean outbound profile may be a false positive driven by toxic inbound links the site doesn't control. Some advisors recommend a hard "≤10% to accept" rule when buying links specifically; that is overly conservative for editorial outreach but reasonable for paid placement vetting.

### 18. SOCIAL MEDIA PRESENCE

**Verdict: validated as a legitimacy signal; the "~10% of backlinks should be social" heuristic is loose, not strict.**

Modern consensus from John Mueller and Gary Illyes: social signals are not direct ranking factors. But absence of social presence on a site claiming substantial traffic is a hollow-brand signal. Practical checklist:

- Branded profiles on at least 2-3 of: LinkedIn (company page), X/Twitter, Facebook, Instagram, YouTube, Reddit.
- Profile is active (≥1 post per quarter), not abandoned.
- Linked from site footer/header.
- Branded handle matches domain name (consistency).

The "10% of backlinks should be social" rule of thumb is reasonable as a sanity-check (a real brand naturally accumulates nofollow profile links and post-share links from social platforms), but isn't a hard threshold. A site with 0% social-source backlinks is unusual; >30% social-source backlinks usually means the site has very few editorial links overall and is leaning on shareable social-platform profiles to inflate referring-domain counts.

### 19. TRAFFIC GEOGRAPHY / COUNTRY ALIGNMENT

**Verdict: validated; operationalize as a hard mismatch filter.**

Pull the prospect's top-5 countries by organic traffic. Compare with your target market.

- **>60% traffic from your target country/region** = ideal.
- **30-60% from your target market** = pass for English-language global brands; conditional for local businesses.
- **<10% from your target market** = the link will pass less geo-relevance; only accept if the topical fit is exceptional or if you're a global brand.
- **Strong mismatch fingerprint of bot/fake traffic**: a local US plumber site that shows 80% of its "organic traffic" from Indonesia, India, or Vietnam is almost certainly using bot/CTR-manipulation traffic services. Auto-fail.

Cross-check with traffic source breakdown — if a backlink-analysis tool reports a country split skewed entirely toward a single low-cost-bot region, treat as fake traffic.

---

## Additional Criteria (Industry-Standard Checks the User Should Add)

### A. ANCHOR-TEXT DISTRIBUTION HEALTH OF THE PROSPECT

A prospect's *inbound* anchor distribution is a strong indicator of whether they have been building manipulative links. Healthy distribution (consensus across multiple 2025-2026 anchor-text studies, including RankWithLinks and Linkscope calculators):

- Branded anchors: **30-50%**
- Naked URL anchors: **10-20%**
- Generic ("click here," "read more"): **10-20%**
- Partial-match keyword: **10-15%**
- Exact-match keyword: **≤5% (≤10% in some niches)**

If exact-match anchors exceed 15% or any single anchor phrase appears on >20-30% of referring domains, the prospect is at high Penguin/SpamBrain risk. Heavy "pharma," "essay writing," "casino" anchor categories in the inbound profile (visible in Ahrefs Anchors report) = avoid even if other metrics look fine.

### B. LINK PLACEMENT CONTEXT (where on the page your link will sit)

Editorial / in-content links carry materially more weight than sidebar, footer, or author-box links. John Mueller (Google) has stated in a Hangout: *"Sitewide header and footer links are not a very great weight in general."* Mueller has also confirmed: *"This is the area of the page where you have your primary content, the content that this page is actually about, not the menu, the sidebar, the footer, the header... Then that is something that we do take into account and we do try to use those links."* Practical preference order:

1. **In-content editorial link** in a topically relevant article (best).
2. **Author-bio link** in a guest post (acceptable; lower weight).
3. **Resource page / curated list link** (acceptable if curated, not auto-generated).
4. **Sidebar/footer/site-wide link** (low value; sometimes Google treats sitewide as one logical link).
5. **Comment-section link** (typically nofollow / UGC; near-zero SEO value).

Insist on in-content editorial placement; flag any prospect that offers only sidebar/footer placements as paying for low-value placement.

### C. NOFOLLOW / SPONSORED / UGC ATTRIBUTION PATTERNS

Confirm placement attribute before paying. A paid placement marked `rel="sponsored"` is honest, compliant with Google's link spam policy, but transfers no PageRank — set expectations accordingly. A paid placement marked `dofollow` violates Google's policy and exposes both sites to link-scheme risk. The prospect's **inbound** dofollow/nofollow ratio is also diagnostic: 100% dofollow inbound = unnatural; a healthy site has ~10-30% nofollow inbound (forums, social, news).

### D. AUTHOR E-E-A-T VERIFIABILITY

Per Google's **September 11, 2025 Search Quality Rater Guidelines** update (182-page document), raters look for: named, credentialed authors with verifiable profiles; author bio pages on the site; off-site corroboration (LinkedIn, professional bylines elsewhere). The September 2025 revision expanded YMYL to explicitly include **elections, civic institutions, and government trust** alongside health, finance, legal, and safety. For YMYL niches, verifiable author identity is near-mandatory. Flag prospects with "guest writer," "admin," "Team [Name]" bylines and no author page. A site that publishes guest posts under anonymous bylines is a link-farm tell.

### E. CONTENT ORIGINALITY / AI-CONTENT SATURATION

Per 2025 SQRG reporting, raters are instructed to assign the **Lowest** rating when main content is *"copied/paraphrased/auto or AI-generated with little to no effort, originality, or added value."* Flagged AI fingerprints (per Editorialge and other 2025 analyses):

- Templated repetitive sentence openers ("In conclusion," "Moreover," "Furthermore" every paragraph).
- Zero unique imagery, only stock photos.
- No first-party data, screenshots, or "before/after" examples.
- Publishing velocity inconsistent with possible human production (50+ posts/day on a small team).
- Hallucinated facts in product or YMYL content.

Per Google's Elizabeth Tucker (Director of Product, Search, 2024 statement): the goal is to *"reduce low-quality, unoriginal content by 40%"* (later revised to ~45% post-March 2024 core). Run a representative spot-check: read 3-5 recent posts. If they read like unedited LLM output, the prospect is at high risk of scaled-content-abuse demotion.

### F. REDIRECT / CLOAKING CHECKS

Test the prospect's URLs both via a normal browser and via a tool simulating Googlebot user-agent (e.g., curl with `-A "Googlebot"`, or a header-spoofing extension). Divergent content = active cloaking. Also check the homepage and a few internal URLs for unexpected 301 chains — a prospect that 301-redirects its homepage to a different domain when accessed from certain referrers/IPs is a sneaky-redirect violation under Google's spam policies.

### G. HTTPS / TECHNICAL HEALTH / CORE WEB VITALS

Baseline expectations: valid HTTPS, modern TLS, no mixed-content warnings, no 5xx errors on key pages, mobile-usable, Core Web Vitals at least "Needs Improvement" or better. A prospect that fails baseline technical hygiene is unlikely to retain rankings and is unlikely to pass equity. Use Google PageSpeed Insights as a quick check.

### H. MOBILE USABILITY

Google has been mobile-first indexing since 2019. A non-mobile-responsive prospect site is being ranked entirely on its mobile rendering — if the mobile rendering is broken/empty, your link is on a page Google considers thin. Manual check via Chrome DevTools device emulation.

### I. LINK VELOCITY ANOMALIES (prospect's inbound profile)

Pull the prospect's referring-domains-over-time chart. Look for:

- Sustained organic growth = healthy.
- Sudden spike of 500+ referring domains in one week with no corresponding PR/viral event = paid burst, likely PBN.
- High churn (gains many, loses many month-over-month) = rented links / PBN that's getting deindexed.
- Healthy pace: new sites should add roughly 3-5 referring domains/week; established sites 10-50/week. >100 referring domains added per day with no obvious cause = manipulated.

### J. PRESENCE IN KNOWN LINK MARKETPLACES / DATABASES

Check whether the domain appears in known guest-post marketplaces (Collaborator, Adsy, WhitePress, PRPosting, Linkhouse, Fiverr "DR 50+ guest post" gigs). Listed = explicit link seller. Not automatically a fail (some publishers legitimately list to monetize), but it raises the bar — for marketplace-listed sites, all other criteria must be unusually strong.

### K. TLD TRUST SIGNALS

Google treats most gTLDs equally for ranking (`.com`, `.net`, `.org`, `.io`, `.ai`, `.co` treated alike). But TLD affects user trust, click-through rates, and the editorial willingness of high-tier publishers to cite the site, which indirectly compounds backlink earning. Apply caution to: `.xyz`, `.top`, `.icu`, `.win`, `.cn` (spam-associated TLDs historically). Per Ahrefs glossary: *"some top-level domains (such as .xyz, .cn, or .biz) [are] associated with spam and black hat SEO tactics. These can negatively impact the trust and reliability of users visiting your site."* For ccTLDs (`.uk`, `.de`, `.fr`), expect geo-targeted traffic; mismatched ccTLD vs. global English traffic is a flag.

### L. DOMAIN AGE vs AUTHORITY MISMATCH

A 4-month-old domain with DR 60 and 50k+ referring domains is implausibly fast organic growth — almost certainly redirect-chain inflation or PBN-fueled. Healthy benchmarks (per Launchcodex and consensus): new domains realistically reach DR 20-30 in 12-18 months with structured outreach; DR 50+ within a year requires either a major PR event or aggressive (often manipulative) link acquisition. Cross-check WHOIS creation date against current authority metrics.

---

## Relaxation Rules — When to Lower the Bar

Strict thresholds cannot apply uniformly. Relax (in writing, with the specific reason logged) when:

- **Narrow B2B / industrial niche**: traffic floors drop ~70% (a 1k/mo niche industrial publication is materially valuable; demanding 10k is unrealistic).
- **Local sites**: branded search and traffic floors drop; geo-alignment becomes the primary filter; <100 branded searches is acceptable for hyper-local businesses.
- **.gov / .edu / known-institution sites**: bypass DR/traffic floors entirely; accept on institutional identity. Verify the link will sit on a genuine institutional page, not a hijacked subdomain (subdomain takeovers are common on edu/gov properties — verify via the `site:` operator that the link page is real institutional content).
- **Recognized major brand or industry leader**: bypass traffic/DR floors; treat editorial mention as the value.
- **Brand-new but legitimate niche site (<12 months old)**: relax authority floors, but tighten content-quality and author-identity checks instead.

Always **never relax**: hacked-page footprint, NAP inconsistency that suggests fraud, anchor profile with >20% exact-match commercial anchors, evidence the prospect is currently under a manual action proxy, or outbound profile showing >40% recipient-penalized share.

---

## Workflow Design — Human-Filled CSV + Claude-Performed Checks

### Split of labor

**Human fills (cannot be automated reliably):**
- Initial prospect URL
- Target page on user's site
- Target/anchor keyword preferences
- User's primary geo market
- User's niche / vertical tags
- Authority-metric snapshots from the user's chosen tool (DR/DA/TF/CF, organic traffic estimate, referring domains count, ranking keywords count, top countries) — pulled manually because tool APIs vary
- Spam Score reading
- Pricing / contact / placement type offered
- Wayback Machine snapshot URL (one representative)
- Trustpilot / G2 / Crunchbase URL if any

**Claude performs (operator-based and reasoning):**
- All `site:` operator checks (hacked, adult/CBD/casino, indexing freshness, total pages estimate)
- Brand-variant enumeration and branded-search inference
- Typosquatting check (`"brand"` SERP top result)
- Identity consistency (About / Contact / Privacy / Terms cross-read)
- Topical dedication ratio computation from keyword list
- Traffic-to-keyword ratio computation
- DR-DA gap / TF-CF ratio computation
- Outbound link forensic analysis from human-supplied data
- Penalty-history fingerprint (compare drop dates against update calendar)
- AI-content saturation read of 3-5 sample posts
- Author E-E-A-T spot-check
- TLD class and age-vs-authority mismatch
- Final weighted score and verdict

### CSV Schema (columns)

| Column | Filled by | Description |
|---|---|---|
| `prospect_url` | Human | The domain being vetted |
| `user_target_url` | Human | The user's page the link will point to |
| `user_target_anchor` | Human | Preferred anchor (or "branded" / "natural") |
| `user_market_geo` | Human | Primary target country (ISO 2-letter) |
| `user_niche_tags` | Human | Comma-separated niche / vertical tags |
| `dr_value` | Human | DR/DA-style score from tool |
| `da_value` | Human | DA (if pulled) |
| `tf_value` | Human | Majestic Trust Flow |
| `cf_value` | Human | Majestic Citation Flow |
| `organic_traffic_est` | Human | Monthly organic traffic estimate |
| `ranking_keywords_count` | Human | Total ranking keywords |
| `referring_domains` | Human | Inbound referring domains count |
| `outbound_dofollow_domains` | Human | Total unique outbound dofollow linked domains |
| `top_3_traffic_countries` | Human | Comma-separated (e.g., "US, UK, CA") |
| `traffic_share_target_geo` | Human | % of traffic from `user_market_geo` |
| `traffic_trend_12mo` | Human | "rising" / "stable" / "declining" / "volatile" |
| `largest_drop_date` | Human | Date of largest sudden traffic drop, or "none" |
| `largest_drop_percent` | Human | % drop on that date |
| `spam_score_pct` | Human | Moz Spam Score (0-100%) |
| `wayback_first_snapshot` | Human | Year of earliest Wayback snapshot |
| `wayback_niche_consistency` | Human | "consistent" / "pivot" / "gap" / "mixed" |
| `trustpilot_url` | Human | Trustpilot URL or "none" |
| `g2_or_crunchbase_url` | Human | One link or "none" |
| `social_profiles_active` | Human | Count of active branded social profiles |
| `social_pct_of_backlinks` | Human | % of inbound backlinks from social platforms |
| `placement_type_offered` | Human | "in-content" / "author-bio" / "sidebar" / "footer" / "comment" |
| `placement_attribute` | Human | "dofollow" / "sponsored" / "nofollow" / "ugc" |
| `pricing_or_swap` | Human | Cost, or "swap" / "free" |
| `recent_outbound_recipients_csv` | Human | Pasted list of 20-50 recent recipient domains (last 90d) for forensic check |
| `claude_brand_variants` | Claude | Enumerated brand-name variants |
| `claude_branded_search_total` | Claude | Sum of branded search volume across variants |
| `claude_typosquat_check` | Claude | "pass" / "fail with #1=<domain>" |
| `claude_hacked_check` | Claude | "clean" / list of suspicious patterns |
| `claude_spam_footprint_check` | Claude | "clean" / list of categories detected |
| `claude_indexing_fresh_check` | Claude | "active" / "stale" / "abandoned" |
| `claude_identity_consistency` | Claude | "consistent" / list of contradictions |
| `claude_topical_dedication_pct` | Claude | % of top-100 keywords in user's niche |
| `claude_kw_traffic_ratio` | Claude | Traffic ÷ keywords ratio + interpretation |
| `claude_dr_da_gap` | Claude | DR − DA; flag if >25 |
| `claude_tf_cf_ratio` | Claude | TF ÷ CF; flag if <0.4 |
| `claude_outbound_forensic_score` | Claude | "clean" / "mixed" / "farm" + % of recipients penalized |
| `claude_penalty_fingerprint` | Claude | Update-alignment of `largest_drop_date` |
| `claude_ai_content_read` | Claude | "human" / "edited-AI" / "raw-AI" |
| `claude_eeat_author_check` | Claude | "verified" / "weak" / "anonymous" |
| `claude_anchor_distribution_flag` | Claude | "healthy" / "exact-match heavy" / "category-toxic" |
| `claude_placement_value` | Claude | Weight based on `placement_type_offered` |
| `claude_tld_age_flag` | Claude | "ok" / "mismatch (age X, DR Y)" |
| `claude_relaxation_applied` | Claude | List of relaxation rules triggered |
| `claude_score` | Claude | 0-100 weighted score |
| `claude_verdict` | Claude | PASS / CONDITIONAL / FAIL |
| `claude_reasoning` | Claude | One-paragraph rationale |
| `claude_recommended_action` | Claude | Concrete next step |

### Scoring Rubric (aggregated)

Hard auto-fail conditions (any one of these → FAIL regardless of other scores):

- Hacked-page footprint detected.
- Hollow brand: zero branded search across all variants + claimed traffic >5k.
- Identity fraud (NAP fundamentally inconsistent across pages).
- Active redirect/cloaking detected.
- >40% of recent outbound dofollow recipients are penalized (post-HCU/spam-update).
- Anchor profile shows >20% exact-match commercial anchors, with the exact phrase appearing on >30% of referring domains.
- Site lost own-brand-name SERP to scrapers.
- Topical dedication ratio <5% AND prospect explicitly markets cross-niche guest posts.
- Domain-age vs authority mismatch (e.g., <6 months old with DR >50).

Weighted scoring (only if no auto-fail):

| Category | Weight |
|---|---|
| Authority + corroboration (DR, traffic, branded search, third-party) | 20 |
| Topical dedication | 18 |
| Outbound forensics (recipient health) | 15 |
| Site health (publishing freshness, Wayback consistency, technical) | 10 |
| Anchor & placement (in-content vs sidebar, dofollow ratio) | 10 |
| Penalty fingerprint (clean traffic curve, no update-aligned drops) | 10 |
| Identity & E-E-A-T (author, social, NAP) | 7 |
| Geo alignment | 5 |
| Spam-score / TLD / domain-age sanity | 5 |

Verdict bands:

- **80-100 → PASS** (proceed; high-confidence link).
- **60-79 → CONDITIONAL** (proceed only if relaxation rule applies, or if 1-2 fixable issues — e.g., negotiate in-content placement instead of sidebar; verify author on YMYL niche).
- **<60 → FAIL** (decline).

---

## Recommendations

### Stage 1 (immediate): Wire the SOP
- Implement the CSV schema as the canonical intake. Train Claude with this `project.md` as its system prompt and the user's earlier TRAFFIC module as a paired context.
- Build a Claude prompt template that takes one CSV row + the prospect URL and emits the entire claude_* column suite plus reasoning.
- Run the SOP on 20 historical prospects (already accepted, already rejected) to calibrate the scoring weights. If your prior accept/reject rate diverges materially from the score band, adjust weights — not the auto-fail conditions.

### Stage 2 (30 days): Tooling integration
- Standardize on one DR/DA tool, one Spam Score source, one outbound-link source. Document which (Ahrefs Site Explorer + Ahrefs Batch Analysis + Moz Spam Score is the most common stack for the workflow described).
- Build a recipient-health bulk-checker mini-workflow: paste recent outbound recipients → Batch Analysis → flag any with >50% drop on Sept 14 2023, March 5 2024, Aug 26 2025.
- Maintain a running list of "known-suppressed" sites in your niche (the competitor-contagion list); when a prospect's outbound recipients hit that list, auto-flag.

### Stage 3 (quarterly): Calibrate
- Re-audit accepted links 90 and 180 days post-placement. Track which prospects' links produced (a) ranking lift, (b) no change, (c) ranking loss. The pattern will tell you which weights to adjust.
- After each major Google update (core or spam), refresh penalty-fingerprint dates and re-score any conditional prospects from the last 6 months.

### Benchmarks that would change the recommendations
- If Google publishes a confirmed change in how outbound-link signals propagate (e.g., a Penguin-style algorithm explicitly transferring recipient penalties to linkers), criterion 16 jumps to weight 25 and becomes a top-3 filter.
- If a third-party authority tool publishes a verified "anti-DR-inflation" score, deprecate the DR-DA-gap heuristic in favor of the new score.
- If branded search consistently fails to be available (e.g., GSC API restrictions deepen), shift weight from criterion 2 onto criterion 8 (third-party corroboration).

---

## Caveats

- DR, DA, TF, CF, Spam Score, and organic-traffic estimates are **vendor estimates**, not Google ranking factors. Treat directionally, never as ground truth.
- Operator-based date filters (`daterange:`) are unreliable and officially deprecated per multiple expert sources (Ahrefs, Ignite Visibility); use the UI date filter or `before:`/`after:` in YYYY-MM-DD format.
- `site:` indexed-count totals are Google's approximation — use them as relative signal, not exact counts.
- The Surfer SEO / Kasra Dash 12,000-site study (Nov 20, 2025) showing correlation between toxic-link percentage and HCU traffic drops is **correlation, not proven causation**. Google's stated position in 2025 is that outbound links to bad neighborhoods primarily cause *link devaluation* of the linker rather than transferred penalty, unless an unnatural-outbound-links manual action is issued.
- AI-content detection is heuristic. Many high-quality sites use AI-assisted drafting today; the line is editor review and added value, not the production method. Be careful not to false-positive a well-edited AI-assisted publisher.
- The exact-match anchor and inbound:outbound ratio thresholds in this SOP are consensus heuristics, not Google-published values. They are calibration starting points; adjust based on your audit experience in your specific vertical.
- This SOP is intentionally tool-agnostic in language. Concrete tool examples (Ahrefs, Semrush, Majestic, Moz, Screaming Frog) are illustrative, not prescriptive — the underlying check is what matters.
- Several cited case studies (HouseFresh, GGRecon, the Digitaloft 671-publisher study, Laura Jawad) represent real, named, documented events but their generalizability across niches is limited; treat as illustrative pattern evidence, not statistical proof. The Brockbank/Digitaloft study covers travel publishers specifically — other verticals may exhibit different demotion patterns.