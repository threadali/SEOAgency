# SaaS SEO Course
## Module 12 — Measuring SaaS SEO: KPIs, Attribution, and Reporting

**Prerequisite:** Modules 1-11 complete.
**Module outcome:** A functioning SaaS SEO measurement stack — GA4 configured, KPIs defined by funnel stage, attribution model chosen, and a client reporting template that leads with signups, not traffic.

---

## The Measurement Problem in SaaS SEO

Most SaaS SEO programmes are measured wrong from the start. The default metrics — organic traffic, keyword rankings, domain authority — are inputs, not outputs. They measure activity, not business impact.

The correct output metric for SaaS SEO is organic signups or organic demo requests. Everything else is a leading indicator that explains why signups are changing, or a lagging indicator that confirms the programme is compounding. Rankings and traffic explain. Signups prove.

A programme that grows traffic by 40% while signups stay flat has optimised for the wrong variable. A programme that grows signups by 15% from organic while traffic grows only 8% has built a higher-converting content architecture. The second is better. Most reporting frameworks would not show it.

This module builds the measurement stack that shows it.

---

## Lesson 12.1 — The SaaS SEO KPI Stack

KPIs organise into three tiers. Primary KPIs prove business impact. Secondary KPIs explain why primary KPIs are moving. Diagnostic KPIs identify where the system has a problem.

**Tier 1 — Primary KPIs (report these first, always)**

| KPI | Definition | Source | Benchmark |
|---|---|---|---|
| Organic signups | Free trial sign-ups sourced to organic | GA4 conversion events | Depends on product — establish a baseline in month 1, then track trend |
| Organic demo requests | Demo form submissions sourced to organic | GA4 conversion events | Same — establish baseline, track trend |
| Organic CAC | Total SEO programme cost ÷ new customers acquired from organic | Finance + GA4 | B2B SaaS: $205 organic CAC vs $341 paid CAC benchmark (Growthner, 2025) |
| Organic MRR contribution | MRR from customers whose first touch or last touch was organic | CRM + GA4 | Established SaaS: 40-60% of new MRR from organic |

**Tier 2 — Secondary KPIs (explain the primary KPIs)**

| KPI | What it explains | Source |
|---|---|---|
| Organic sessions by funnel layer | Whether BOFU and MOFU traffic is growing relative to TOFU | GA4 by page segment |
| BOFU page conversion rate | Whether high-intent pages are converting at benchmark rates | GA4 by page |
| MOFU page conversion rate | Whether comparison and alternative pages are producing sign-ups | GA4 by page |
| Organic CTR | Whether title tags and meta descriptions are earning clicks at search position | Search Console |
| Keyword position changes | Which pages are entering or leaving the top 10 | Search Console |

**Tier 3 — Diagnostic KPIs (identify problems)**

| KPI | Problem it diagnoses | Source |
|---|---|---|
| Pages indexed | Indexing failures — are all published pages in the index? | Search Console Coverage |
| Core Web Vitals | Page experience failures that suppress rankings | Search Console Core Web Vitals |
| Crawl errors | Architecture problems Google is encountering | Search Console Coverage |
| Branded vs non-branded traffic split | Over-reliance on brand (signals weak TOFU/MOFU programme) | Search Console — filter by brand queries |
| Bounce rate by funnel layer | Content-intent mismatch — buyers leaving without engaging | GA4 engagement rate |

**The benchmark that matters most: BOFU conversion rate**

BOFU pages — pricing, trial, demo, comparison, alternatives — should convert at 8-20% from organic traffic specifically. If any BOFU page is below 5%, investigate before publishing new content. The problem is either a traffic quality issue (wrong queries landing on the page) or a conversion architecture issue (the page is not answering what the buyer came for).

---

**Common Mistake: Reporting domain authority as a primary KPI**

Domain authority is a third-party metric derived from backlink data. It does not directly correlate to signups. It is not a Google metric. Reporting it as evidence of SEO progress tells clients nothing about whether the programme is generating revenue. Replace it with organic signups and organic CAC. Report domain authority only if a client explicitly requests it and only with the explanation that it is a directional proxy, not a business outcome.

---

**Summary**

- Three KPI tiers: primary (signups, CAC), secondary (session and conversion rate by funnel layer), diagnostic (indexing, Core Web Vitals, crawl errors).
- BOFU conversion rate is the most important single metric after organic signups. Below 5% on any BOFU page requires investigation before new content is produced.
- Report primary KPIs first. Rankings and traffic are supporting context, not headline metrics.

*Next: GA4 setup — the specific configuration that connects organic sessions to conversion events.*

---

## Lesson 12.2 — GA4 Configuration for SaaS

Most SaaS companies have GA4 installed but not configured for the measurement questions SaaS SEO requires. Default GA4 tracks pageviews and sessions. SaaS SEO requires conversion events, organic source attribution, and funnel-stage segmentation.

**The five GA4 configuration requirements**

**1. Conversion events**

Set up conversion events for every business-critical action:

| Action | GA4 event name | Trigger |
|---|---|---|
| Free trial sign-up | `trial_signup` | Thank you page view OR form submission confirmation |
| Demo request | `demo_request` | Form submission confirmation |
| Pricing page visit | `pricing_page_view` | Page view: /pricing/ |
| Feature page visit (high-intent) | `feature_page_view` | Page view: /features/* |
| Newsletter sign-up | `newsletter_signup` | Form submission confirmation |

Mark `trial_signup` and `demo_request` as conversions in GA4 (toggle to "Key event"). These are the events primary KPIs are built from.

**2. Organic traffic segmentation**

Default GA4 groups all organic traffic (Google, Bing, DuckDuckGo) together. SaaS reporting needs:
- Organic search — all organic
- Organic search — non-branded (queries that do not contain the product name)
- Organic search — branded (queries containing the product name)

Create two custom channel groups or use comparison segments in GA4 Explore. Non-branded organic growth shows the programme is capturing new audiences. Branded organic growth shows the brand is strengthening.

**3. Funnel-layer page grouping**

Create content groups in GA4 that map to funnel layers:

| Content group name | Pages included | Funnel layer |
|---|---|---|
| BOFU — Pricing | /pricing/ | Layer 3 |
| BOFU — Trial | /free-trial/, /start/ | Layer 3 |
| BOFU — Demo | /demo/ | Layer 3 |
| MOFU — Comparison | /compare/* | Layer 2 |
| MOFU — Alternatives | /alternatives/* | Layer 2 |
| MOFU — Features | /features/* | Layer 2-3 |
| TOFU — Blog | /blog/* | Layer 1 |
| Integration pages | /integrations/* | Layer 2-4 |

With these groups, the question "which funnel layer is driving signups?" has a direct answer in GA4.

**4. Conversion path exploration**

For B2B SaaS with cycles longer than 7 days, the last-click conversion event does not tell the full attribution story. Set up a Path Exploration in GA4 Explore:

- Starting point: First organic session
- Ending point: `trial_signup` or `demo_request` conversion event
- Max steps: 5

This reveals the most common content journeys before a conversion. The typical finding: comparison or alternatives page appears in the path before the majority of conversions, even when the last click is on the pricing or trial page directly.

**5. Search Console integration**

Connect Search Console to GA4. This adds the Search Console dimensions (query, page, impressions, CTR, position) to GA4's acquisition data. The combined view shows: for each organic landing page, which queries are bringing traffic AND whether that traffic converts.

A blog post with 5,000 organic sessions/month but zero conversions is visible in the integrated view. The same post converting at 3% from 400 sessions is also visible. The second is worth six times more to the programme.

---

**Common Mistake: Measuring conversion rate against total sessions instead of organic sessions**

A pricing page that converts 12% overall may convert 20% from organic and 5% from direct. Reporting the blended rate hides the channel-specific performance. Always filter by organic source when reporting BOFU conversion rates.

---

**Summary**

- Five GA4 requirements: conversion events, organic segmentation, funnel-layer page grouping, path exploration, and Search Console integration.
- Non-branded organic growth shows the programme captures new audiences. Branded growth shows brand strengthening. Both matter but they measure different things.
- Always filter by organic source when reporting BOFU conversion rates. Blended rates hide channel-specific performance.

*Next: Attribution models for B2B SaaS — how to connect organic content to closed revenue in long sales cycles.*

---

## Lesson 12.3 — Attribution for Long B2B Sales Cycles

A B2B SaaS buyer with a 90-day cycle reads a comparison article in week one, visits the integration page in week three, asks a colleague who finds the case study in week six, and requests a demo in week ten. Last-click attribution credits the demo page. First-click attribution credits the comparison article. Neither is the full story.

The correct attribution model for SaaS SEO reporting depends on the sales cycle length.

**Attribution model by sales cycle**

| Sales cycle | Attribution model | Rationale |
|---|---|---|
| Under 7 days (PLG/B2C) | Last-click | Most conversions happen in one or two sessions. Last-click is accurate enough. |
| 7-30 days (SMB B2B) | Linear or data-driven | Multiple touchpoints contribute. Spread credit across the journey. |
| 30-90 days (mid-market) | First-click + last-click combined | Report both. First-click identifies which content starts the journey. Last-click identifies which content closes it. |
| 90+ days (enterprise) | First-touch assisted + CRM pipeline data | GA4 cannot fully track 90-day multi-stakeholder journeys. CRM pipeline attribution is required. |

**The practical attribution report for agency clients**

For most agency SaaS clients (typically SMB to mid-market), report three attribution data points per month:

1. **Organic last-click conversions.** From GA4 standard conversion report, filtered to organic source. This shows signups where organic was the final touchpoint.

2. **Organic assisted conversions.** From GA4 Explore, path exploration. This shows conversions where organic appeared in the path but was not the final touchpoint.

3. **Total organic-influenced conversions.** Sum of last-click + assisted. This is the total pipeline organic content contributed to, regardless of whether it was the closing touchpoint.

The difference between last-click and total organic-influenced is often a factor of two to three. Reporting only last-click understates the programme's contribution to revenue by that margin.

**CRM pipeline attribution for enterprise accounts**

For enterprise SaaS clients with 90-day-plus cycles, GA4 alone is insufficient. The CRM must track organic first-touch. The process:

1. UTM parameters on all organic conversion forms: `utm_source=organic`, `utm_medium=seo`, `utm_content=[page-slug]`
2. CRM captures UTM parameters at lead creation
3. At deal close, the CRM records the organic first-touch source
4. Monthly report pulls: "Of closed-won deals this month, how many had an organic first touch?"

This connects the SEO programme to closed revenue — the metric the CFO actually cares about.

---

**Common Mistake: Abandoning attribution reporting because it is complicated**

Some agencies report only rankings and traffic because organic revenue attribution is technically complex. This is operationally understandable and strategically destructive. A client who does not see organic signups in the report will eventually question why they are paying for SEO. Rankings and traffic do not justify the investment. Signups and pipeline do. Build the attribution infrastructure in month one, before the content programme generates enough data to make it worth reporting.

---

**Summary**

- Attribution model choice depends on sales cycle length. Last-click suffices for PLG/B2C. Multi-touch attribution is required for B2B.
- Three monthly attribution data points: organic last-click conversions, organic assisted conversions, total organic-influenced conversions.
- For enterprise accounts, CRM UTM tracking is required to connect organic to closed revenue.

*Next: The client reporting structure — what SaaS clients need to see and how to present it.*

---

## Lesson 12.4 — The SaaS SEO Client Report

Most agency SEO reports are designed to demonstrate activity: we published 8 articles, we built 12 links, 47 keywords moved into the top 20. These reports do not answer the question the client is actually asking: is this investment generating revenue?

The SaaS SEO client report is structured to answer that question first, then provide the evidence that explains how.

**The one-page monthly report structure**

```
SAAS SEO MONTHLY REPORT
========================
Client: [Name]
Month: [Month Year]
Report prepared by: [Name]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 1 — HEADLINE METRICS (top of every report, every month)

Organic signups this month: [N]    vs last month: [N]    vs 3-month avg: [N]
Organic demo requests this month: [N]    vs last month: [N]
Organic-influenced pipeline: $[N]    (last-click + assisted combined)

Note: "Organic-influenced pipeline" uses last-click + assisted attribution
from GA4. It represents all deals where organic content appeared in the
buyer's journey before conversion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 2 — FUNNEL LAYER PERFORMANCE

| Layer | Sessions (organic) | MoM change | Conversions | Conversion rate |
|---|---|---|---|---|
| BOFU (pricing, trial, demo) | | | | |
| MOFU (compare, alternatives, features) | | | | |
| TOFU (blog) | | | | |

Key insight: [One sentence — which layer drove the most signup change and why]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3 — TOP CONVERTING PAGES THIS MONTH

| Page URL | Layer | Organic sessions | Signups | Conversion rate |
|---|---|---|---|---|
| 1. | | | | |
| 2. | | | | |
| 3. | | | | |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 4 — SEARCH VISIBILITY (explains traffic changes)

Keywords entered top 10 this month: [N]
Keywords entered top 3 this month: [N]
Keywords dropped from top 10: [N]
Notable movement: [2-3 specific keyword changes worth flagging]

Branded vs non-branded organic split:
  Branded: [N]% of organic sessions
  Non-branded: [N]% of organic sessions
  MoM change in non-branded share: [+/-N%]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 5 — CONTENT PUBLISHED THIS MONTH

| Title | URL | Layer | Status |
|---|---|---|---|
| | | | Indexed / Ranking / Converting |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 6 — NEXT MONTH PLAN

Content publishing plan: [titles, layers, expected impact]
Pages scheduled for optimisation: [URLs and planned changes]
Technical issues to address: [from diagnostic KPIs]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 7 — PROGRAMME HEALTH (quarterly only)

Organic CAC this quarter: $[N]    vs paid CAC: $[N]
Organic MRR contribution: $[N]    ([N]% of total new MRR)
SEO ROI: [Revenue from organic - SEO costs] / SEO costs × 100 = [N]%
```

**The narrative rule**

The report contains one interpretive sentence per section. Not a paragraph. One sentence that tells the client what the numbers mean. "Organic signups grew 18% this month, driven by three comparison pages entering the top 5 for their primary keywords." This sentence is more useful than five paragraphs of data explanation.

**Frequency and format**

Monthly report: Sections 1-6. One page. Email or slide format.
Quarterly review: Full report including Section 7. Thirty-minute call to discuss programme health and next quarter priorities.
Annual review: Full programme retrospective — what was built, what ranked, what converted, what the organic CAC was versus alternatives.

---

**Common Mistake: Over-reporting positive data while under-reporting problems**

A BOFU page that is not converting at benchmark, a cluster that ranked and then dropped, a keyword cannibalisation issue that appeared in the previous month — these belong in the report even when they reflect poorly on the programme. Clients who receive only positive data in monthly reports are not being served. Clients who receive honest programme health reporting — including problems and the planned fixes — build trust in the agency.

---

**Summary**

- The report leads with organic signups and pipeline, not traffic and rankings. Traffic and rankings explain the signups.
- One interpretive sentence per section. The data is in the table. The sentence tells the client what it means.
- Report problems. Clients who receive only positive reporting eventually stop trusting the positive data.

---

## Module 12 Summary

Three decisions determine whether a SaaS SEO measurement stack actually serves the client:

- **Primary KPIs are signups and organic CAC.** Rankings and traffic explain why signups are moving. They do not prove the programme is working. Build the measurement infrastructure around conversion events before the content programme generates enough data to matter.
- **Attribution model must match the sales cycle.** Last-click attribution for PLG and B2C. Multi-touch for mid-market B2B. CRM pipeline tracking for enterprise. The right attribution model shows two to three times more organic-influenced pipeline than last-click alone.
- **The report leads with impact, not activity.** Eight articles published and 12 links built is an activity report. 23 organic signups from comparison pages, representing 18% growth month-over-month, is an impact report. One of these justifies the retainer. The other invites the cancellation conversation.

---

## Module 12 Deliverable: SaaS SEO Reporting Template

The template above (Lesson 12.4) is the deliverable. Copy it. Populate Section 1 first every month, before any other data is pulled. If Section 1 data is not available because GA4 conversion events are not configured, stop and configure GA4 before producing any other content.

```
GA4 CONFIGURATION CHECKLIST (complete before first report)

[ ] trial_signup conversion event configured and firing
[ ] demo_request conversion event configured and firing
[ ] pricing_page_view event configured
[ ] Organic source filter verified (organic sessions only, not all sessions)
[ ] Non-branded segment created (excludes brand name queries)
[ ] Content groups created for BOFU, MOFU, TOFU, Integrations
[ ] Path Exploration report configured in GA4 Explore
[ ] Search Console property linked to GA4
[ ] UTM parameters on all conversion forms (organic source, SEO medium)
[ ] CRM configured to capture UTM parameters at lead creation (B2B accounts)

Sign-off: GA4 configuration verified by: _________________ Date: _________
First report can be produced: [ ] Yes  [ ] No (complete configuration first)
```

---

*Module 13 covers the Execution Sequence: the exact order in which the full SaaS SEO system is built — from day one through to a compounding organic programme.*
