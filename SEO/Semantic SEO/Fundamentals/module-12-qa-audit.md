# MODULE 12 — QA Audit and Publishing Workflow
## The Final Gate Before Anything Goes Live

> **Purpose of this module:** The QA audit is the system that catches every failure the production process missed — before it reaches Google's index. A brief can be flawless. A writer can be skilled. A reviewer can be experienced. And an article can still contain declaration conflicts, broken contextual flow, missing entity coverage, incorrect anchor text, or a modal verb in a factual statement. The QA audit is not a proofreading pass. It is a structured evaluation of the article against every standard this course has established. Nothing publishes without passing it. This module teaches you to run the audit, use the publishing workflow, and maintain the structural integrity of the site over time.

---

## LESSON 12.1 — Why QA Is a System, Not a Review

### The Difference Between Proofreading and QA

Proofreading catches grammar errors, spelling mistakes, and typos. A proofreader reads for fluency.

A QA audit catches:
- Semantic violations (contextless words, modal verbs in facts, pronoun co-reference)
- Structural violations (H2 without contextual bridge, context jumps, non-linear flow)
- Entity violations (missing EAV values, unqualified instances, entities without full names)
- Completeness violations (FS targets over 40 words, PAA sections without immediate answers, tables without outros)
- Internal linking violations (wrong anchor text, missing upward links, over-linked pages)
- Technical violations (wrong URL, missing author, incorrect schema)
- Spam compliance violations (modal-heavy content, thin sections, missing information gain)

A proofreader cannot catch semantic violations. A QA auditor — trained on this course — can.

### Why QA Must Be Systematic

Ad-hoc review produces inconsistent output. A reviewer who is tired misses the same things a reviewer who is rushed misses. A systematic checklist applied to every article produces consistent output — because the standard does not vary by reviewer or day.

**The QA system in this module has six audit stages.** Each stage has its own checklist. Each checklist is binary — pass or fail per item. No "partial passes". An article that fails any item on any checklist is returned to the writer with specific failure notes before it moves forward.

### Who Runs QA

In a small team, the brief builder runs QA — they know what the brief required, so they know what the article was supposed to produce.

In a larger team, a dedicated QA reviewer runs the audit against the brief. The reviewer does not need to know the topic — they need to know the audit system. They compare the article against the brief, not against their own knowledge of the subject.

**The QA reviewer's only question:** Does this article satisfy every requirement in the brief and every standard in the course? Not: "Is this a good article?" That is a subjective question. The QA question is structural and verifiable.

---

## LESSON 12.2 — Stage 1: Entity and Context Audit

This stage verifies that the article's macro context is correct, the central entity is properly established, and the contextual layer is consistent throughout.

### Stage 1 Checklist

```
STAGE 1 — ENTITY AND CONTEXT AUDIT
=====================================

Macro Context:
[ ] 1.1 The article covers exactly one entity-attribute pair — no topic mixing
[ ] 1.2 Every H2 is a direct component of the H1's stated entity-attribute pair
[ ] 1.3 No H2 introduces a new entity-attribute pair not stated in the H1
[ ] 1.4 The macro context statement from the brief matches the article's actual content
[ ] 1.5 No section of the article belongs in a different article in the Topical Map

Central Entity Coverage:
[ ] 1.6 Central entity appears in the H1 by name
[ ] 1.7 Central entity appears in the opening paragraph's first sentence
[ ] 1.8 Central entity appears in at least 3 H2 headings
[ ] 1.9 Central entity appears in the concluding section
[ ] 1.10 Central entity is never replaced with a pronoun anywhere in the document

EAV Coverage:
[ ] 1.11 All root attributes from the entity list (Brief Component 12) are covered
[ ] 1.12 Every attribute is covered with at least one specific numeric value or named instance
[ ] 1.13 No attribute is listed in the brief entity list but absent from the article

Source Context Alignment:
[ ] 1.14 The article's framing reflects the site's source context
         (Pakistani market, residential buyers, affordable segment — for the heater site)
[ ] 1.15 Geographic context appears where relevant (Pakistan, specific cities where appropriate)
[ ] 1.16 The audience framing matches the source context user group

Contextual Layer:
[ ] 1.17 The contextual layer is established in the opening paragraph
[ ] 1.18 The article does not drift into a broader or narrower contextual layer
         than specified in the brief
```

### Common Stage 1 Failures

**Failure: H2 introduces a new attribute not in the H1**
Article title is `Gas Heater Types Pakistan`. One H2 is `What Is the Best Gas Heater Price in Pakistan?` The attribute `price` is not in the H1 topic.
Fix: Remove the H2. Price belongs in the price pillar, linked from this article with anchor text.

**Failure: Central entity replaced with pronoun**
Article says: *"Gas heaters are available in 5 types. They produce heat through different mechanisms."*
The word "They" replaces "Gas heaters" — entity chain broken.
Fix: *"Gas heaters are available in 5 types. Gas heaters produce heat through different mechanisms."*

**Failure: Geographic context absent from Pakistan-targeted article**
Article discusses heater prices without once mentioning Pakistan, PKR, or Pakistani brands.
Fix: Add Pakistan context to every price reference. Verify all prices are in PKR.

---

## LESSON 12.3 — Stage 2: Structure Audit

This stage verifies the heading hierarchy, contextual flow, question construction, and opening/conclusion n-gram consistency.

### Stage 2 Checklist

```
STAGE 2 — STRUCTURE AUDIT
============================

Heading Hierarchy:
[ ] 2.1 H1 is present and matches the title tag from the brief exactly
[ ] 2.2 H1 passes the 5-point title test (entity ✓, attribute ✓, synonym ✓,
         context ✓, inferred need ✓)
[ ] 2.3 Every H2 is a question
[ ] 2.4 Every H3 is a question
[ ] 2.5 No H3 appears without a parent H2
[ ] 2.6 H2 ordering follows the seven-stage content flow:
         Definition → Mechanism → Types → Attributes → Comparison →
         Practical Guidance → FAQ

Contextual Bridges:
[ ] 2.7 Every H3 directly narrows or deepens the concept of its parent H2
[ ] 2.8 No H3 introduces a topic that is not a component of its H2
[ ] 2.9 The logical path H2 → H3 can be traced without a conceptual jump

Contextual Flow:
[ ] 2.10 The document flows from more fundamental to more specific
          (definition before comparison, content before FAQ)
[ ] 2.11 No backtracking — the document never returns to a concept
          covered in an earlier section
[ ] 2.12 No context jump between consecutive paragraphs under the same heading
[ ] 2.13 The transition between every pair of consecutive sections is logical

Opening and Conclusion:
[ ] 2.14 Opening paragraph establishes: entity, contextual layer, macro context
          (all three — in order)
[ ] 2.15 Opening paragraph contains the primary n-grams from the H1 title
[ ] 2.16 Conclusion contains at least 3 n-grams that appear in the opening paragraph
[ ] 2.17 Conclusion provides practical synthesis — not a heading summary
[ ] 2.18 Conclusion does not introduce new topics or entities

Question Quality:
[ ] 2.19 No questions copied verbatim from Google PAA or competitor articles
[ ] 2.20 Long questions (containing conditions or declarations) are restructured
          as H2 + H3 pairs where the H2 is the short grouper
[ ] 2.21 Multiple phrasings of the same question are present for key topics
          (serving different search behaviours within the same intent)
```

### Common Stage 2 Failures

**Failure: FAQ section appears before the main content**
The article opens with a 10-question FAQ section, then covers the substantive content.
Fix: Move FAQ to the final section. Content → FAQ, never FAQ → Content.

**Failure: H3 introduces a new entity outside the H2's scope**
H2: *"How Does an Infrared Gas Heater Produce Heat?"*
H3: *"What Is the Price of Infrared Gas Heaters in Pakistan?"*
The H3 introduces `price` — a different attribute than `heat production mechanism`.
Fix: Remove H3. Price belongs in a separate H2 section with its own H3s.

**Failure: Conclusion introduces new comparison not covered in article**
Last paragraph: *"While gas heaters are effective, electric heaters may suit some users better."*
`Electric heaters` is a new entity not in the article's macro context.
Fix: Remove the comparison. If needed, link to the comparison article instead.

---

## LESSON 12.4 — Stage 3: Sentence Quality Audit

This stage verifies every sentence-level rule from Module 9 — certainty, numerics, entity naming, word order, formatting.

### Stage 3 Checklist

```
STAGE 3 — SENTENCE QUALITY AUDIT
====================================

Certainty Rules:
[ ] 3.1 No modal verbs (will, should, might, could, need to, have to)
         used in factual statements
[ ] 3.2 All factual statements are in present tense declarative form
[ ] 3.3 No hedged claims ("it is generally believed", "most experts think",
         "it is often said")
[ ] 3.4 Every claim that can be stated as a fact is stated as a fact

Numeric and Specificity Rules:
[ ] 3.5 No vague quantifiers: "many", "several", "a number of", "various",
         "numerous" used without a specific number
[ ] 3.6 Every quantifiable claim (cost, time, size, frequency, percentage)
         has a specific numeric value
[ ] 3.7 All numeric values are consistent with the entity map and brief data
[ ] 3.8 All instance counts are qualified
         (e.g. "3 mandatory safety features" not "safety features")

Contextless Word Rules:
[ ] 3.9 No filler openers: "It is important to note that...",
         "In today's world...", "As we all know..."
[ ] 3.10 No redundant intensifiers: "very", "really", "quite",
          "extremely", "incredibly"
[ ] 3.11 No meta-commentary: "This section will cover...",
          "As mentioned above...", "Moving on to..."
[ ] 3.12 No empty descriptors: "important", "significant", "valuable",
          "useful" without specific evidence supporting the claim

Entity Naming Rules:
[ ] 3.13 No pronouns used to refer to any entity (no "it", "they", "this",
          "these", "those" where the entity should be named)
[ ] 3.14 Every entity is named in full at first mention with abbreviation
          if applicable (e.g. "Oxygen Depletion Sensor (ODS)")
[ ] 3.15 Subsequent mentions use the full name or an approved synonym —
          never a generic pronoun

Sentence Construction Rules:
[ ] 3.16 No sentence longer than 25 words (split anything longer)
[ ] 3.17 Conditional clauses appear after the declaration, not before
          ("Do X, if Y" — not "If Y, do X")
[ ] 3.18 Subordinate text (first sentence after each heading) directly
          addresses the heading — not context-setting about the heading
[ ] 3.19 Match: adjective-predicate-noun order between question headings
          and their first-sentence answers

Formatting Rules:
[ ] 3.20 Bold marks the answer or key data, not the search term or entity name
[ ] 3.21 No opinion expressed in factual sections
[ ] 3.22 No analogy that introduces an out-of-domain entity
[ ] 3.23 No casual/everyday language in any section
[ ] 3.24 Correct verb choice for the knowledge domain
          (verify against domain collocation patterns)

List-Specific Rules:
[ ] 3.25 Every list starts with an introductory sentence (count + qualifier + entity)
[ ] 3.26 All list items start with the same Part of Speech
[ ] 3.27 All list items contain specific content — no vague labels
[ ] 3.28 Every list ends with an outro paragraph (synthesis or insight)
[ ] 3.29 Examples given after every plural noun in body text

Table-Specific Rules:
[ ] 3.30 Every table preceded by a definition sentence
          (what is compared, how many, which dimensions)
[ ] 3.31 Every table cell contains specific data — no vague labels or "N/A" without explanation
[ ] 3.32 Every table followed by an outro paragraph (key insight from data)
[ ] 3.33 Column headers contain attribute name and unit where applicable
```

### Common Stage 3 Failures and Fixes

**Top 5 most commonly failed items in agency content:**

| Rank | Failure | Frequency | Fix |
|---|---|---|---|
| 1 | Modal verbs in factual statements (3.1) | Extremely common | Replace "should" with declarative: "Gas heaters require..." |
| 2 | Vague quantifiers instead of numbers (3.5) | Very common | Replace "many types" with "5 types" |
| 3 | Pronoun co-reference (3.13) | Very common | Replace "it" with entity name throughout |
| 4 | Filler opener phrases (3.9) | Common | Delete entire opener, begin with first substantive sentence |
| 5 | Bold on entity name instead of answer (3.20) | Common | Move bold to the answer portion of the sentence |

---

## LESSON 12.5 — Stage 4: Completeness Audit

This stage verifies that the article covers everything the brief required — entity attributes, featured snippet targets, PAA sections, unique data, and information gain.

### Stage 4 Checklist

```
STAGE 4 — COMPLETENESS AUDIT
================================

EAV Completeness:
[ ] 4.1 Every entity from Brief Component 12 appears in the article
[ ] 4.2 Every attribute listed for each entity is covered
[ ] 4.3 Every attribute is covered with its specific values from the entity map
[ ] 4.4 No root attribute has been omitted due to word count concerns

Featured Snippet Completeness:
[ ] 4.5 All FS-targeted headings from Brief Component 15 are present
[ ] 4.6 Every FS-targeted section's answer is 40 words or fewer
[ ] 4.7 Every FS-targeted answer is 320 characters or fewer
[ ] 4.8 FS answers are declarative (no modals, no hedging)
[ ] 4.9 FS answers begin with the entity name, not a pronoun or "This"

PAA Completeness:
[ ] 4.10 All PAA-targeted headings from Brief Component 16 are present
[ ] 4.11 Every PAA section's first sentence is a complete, direct answer
[ ] 4.12 Every PAA first sentence is 40 words or fewer
[ ] 4.13 PAA expansion (sentences 2+) provides supporting evidence with numerics

Information Gain Completeness:
[ ] 4.14 All information gain targets from Brief Component 14 are present
[ ] 4.15 Each information gain target contains specific data not found
          in competitor articles (verified before QA)
[ ] 4.16 For Core articles: minimum 3 information gain targets achieved
[ ] 4.17 For Outer articles: minimum 1 information gain target achieved

Format Compliance:
[ ] 4.18 Every section uses the format code assigned in Brief Component 11
[ ] 4.19 Format codes are not mixed within a single section without justification
[ ] 4.20 Tables appear only where the format code specified Table
[ ] 4.21 Instruction lists appear only where the format code specified IL
[ ] 4.22 No format is repeated more than 3 consecutive times without variation

TF-IDF Compliance:
[ ] 4.23 All 10–15 TF-IDF required terms from Brief Component 13 appear
          at least once in the article
[ ] 4.24 TF-IDF terms appear in contextually appropriate sections
          (not forced into unrelated sections)
[ ] 4.25 High-frequency TF-IDF terms appear in at least 2 different sections
```

### Running the Information Gain Verification

Information gain verification cannot be done by reading the article alone. It requires comparing the article against competitor content.

**Process:**
1. Open the top 3 ranking articles for the primary keyword
2. For each information gain target in the brief, confirm the specific data point is absent from competitors
3. Confirm the specific data point is present and accurate in the article being reviewed
4. If a claimed information gain target appears in a competitor article — it is no longer an information gain. Note it and determine if additional unique data can be added elsewhere.

---

## LESSON 12.6 — Stage 5: Internal Linking Audit

This stage verifies that all internal links match the Internal Linking Map (Module 10) and that the article integrates correctly into the site's semantic cluster.

### Stage 5 Checklist

```
STAGE 5 — INTERNAL LINKING AUDIT
====================================

Link Presence:
[ ] 5.1 All outbound internal links specified in Brief Component 17 are present
[ ] 5.2 At least 1 upward link to the parent CMap page is present
[ ] 5.3 For Core articles: at least 1 lateral link to a sibling pillar is present
[ ] 5.4 For Outer articles: minimum 3 cross-cluster links to Core pages are present
[ ] 5.5 No outbound link targets a page that does not yet exist (live)
[ ] 5.6 Total outbound internal links do not exceed the brief's maximum

Anchor Text Compliance:
[ ] 5.7 Every anchor text is an approved variation from the Anchor Text Master List
          (Internal Linking Map Sheet 3)
[ ] 5.8 No anchor text uses generic phrases:
         "click here", "read more", "this article", "here", "our guide"
[ ] 5.9 Anchor text for upward links uses the target page's entity-attribute pair
[ ] 5.10 Anchor text for downward links uses the target page's hyponym phrase
[ ] 5.11 Anchor text for cross-cluster links matches the Core page's primary keyword

Link Placement:
[ ] 5.12 Every link appears within a section that is topically relevant
          to the anchor text and target page
[ ] 5.13 No link appears in an unrelated section (wrong context for the anchor)
[ ] 5.14 The most important upward/cross-cluster link appears in the first
          40% of the article content

Hash Link Compliance:
[ ] 5.15 All deep-section links include the correct #section-id
[ ] 5.16 The #section-id in every hash link matches an actual section ID
          on the target page (not a placeholder)
[ ] 5.17 Hash links deliver to a section whose content matches the anchor text

External Link Compliance:
[ ] 5.18 No inline external citation links (sources cited as text, not hyperlinks)
[ ] 5.19 Any external links present are in footnotes or reference sections
          at the bottom of the article only
[ ] 5.20 No external links to competitor sites from within the article body
```

### The Link Verification Protocol

Every link in the article is verified by clicking it during QA review. This catches:
- Dead links (target page not yet published or URL changed)
- Wrong-target links (URL copied incorrectly)
- Hash links pointing to non-existent section IDs
- Anchor text that doesn't reflect the actual content at the link destination

**When a target page is not yet live:** The link must be removed from the article. It is re-added when the target page publishes. Unresolved links to non-existent pages are not published.

---

## LESSON 12.7 — Stage 6: On-Page Technical Audit

This stage verifies all on-page technical elements — URL, title, meta, images, schema, author, and publish date.

### Stage 6 Checklist

```
STAGE 6 — ON-PAGE TECHNICAL AUDIT
=====================================

URL:
[ ] 6.1 URL matches the target URL in the brief exactly
[ ] 6.2 URL follows the correct Root/Seed/Node hierarchy from the CMap
[ ] 6.3 No terms are duplicated across URL levels
[ ] 6.4 URL uses hyphens (not underscores) between words
[ ] 6.5 URL is lowercase throughout
[ ] 6.6 URL contains no stop words (and, the, of, in, for) where avoidable
[ ] 6.7 URL does not exceed 75 characters including domain

Title Tag:
[ ] 6.8 Title tag matches the H1 in the article exactly
          (or is a slight variation within title character limits)
[ ] 6.9 Title tag is 50–60 characters (optimal for SERP display)
[ ] 6.10 Title tag passes the 5-point title test
[ ] 6.11 Title tag contains the primary keyword from the brief
[ ] 6.12 Title tag is not duplicated anywhere else in the site

Meta Description:
[ ] 6.13 Meta description is 150–160 characters
[ ] 6.14 Meta description contains: primary entity-attribute, value proposition,
          and a context qualifier (Pakistan/year/audience)
[ ] 6.15 Meta description is unique — not duplicated on any other page
[ ] 6.16 Meta description contains no opinion, superlatives, or promises
          that the article does not substantiate

Images:
[ ] 6.17 Every image has an alt tag
[ ] 6.18 Alt tags follow the representative image formula:
          entity + attribute + context relevant to the nearest heading
[ ] 6.19 No alt tag contains keyword stuffing
[ ] 6.20 Hero/H1-level image alt tag contains the primary entity name
[ ] 6.21 No alt tags are left as file names (e.g. "IMG_20250112_093421.jpg")
[ ] 6.22 Images are optimised for web delivery (WebP or compressed JPEG/PNG)
[ ] 6.23 Image dimensions are appropriate for placement
          (hero images: 1200×630px minimum)

Structured Data (Schema):
[ ] 6.24 Article schema is present and correctly typed
          (Article, BlogPosting, or FAQPage as appropriate)
[ ] 6.25 FAQPage schema matches the FAQ section in the article exactly
          — questions and answers in schema match visible content
[ ] 6.26 Author in schema matches the named author on the article
[ ] 6.27 Publisher in schema matches the brand name and logo
[ ] 6.28 datePublished and dateModified are accurate
[ ] 6.29 No schema claims anything that is not visible in the page content

Authorship:
[ ] 6.30 Named author byline is present on the article
[ ] 6.31 Author name links to the author bio page
[ ] 6.32 Author bio page exists and is live
[ ] 6.33 Author's stated credentials match the niche of the article
[ ] 6.34 Author is not "Admin", "Team", "Staff", or a generic placeholder

Publication Metadata:
[ ] 6.35 Publish date is accurate (today's date on first publication)
[ ] 6.36 "Last updated" date is set to match publish date on first publication
[ ] 6.37 Canonical tag is present and points to the article's own URL
          (self-referencing canonical)
[ ] 6.38 Article is not noindexed (verify meta robots or CMS settings)
[ ] 6.39 Article is included in the XML sitemap
```

---

## LESSON 12.8 — The QA Failure Protocol

When an article fails any checklist item, it follows a specific protocol. Not all failures are equal. The severity classification determines what happens next.

### Severity Classification

**Severity 1 — Critical (Return to Writer)**
Failures that fundamentally compromise the article's ranking eligibility or spam compliance.

```
CRITICAL failures (any one = return to writer before further review):
- Modal verbs present in more than 5 factual statements
- Central entity replaced with pronouns throughout (>10 instances)
- More than 2 H2s outside the macro context
- Information gain targets absent (Core article with 0 of 3 targets met)
- Named author missing
- URL does not match the CMap architecture
- Article length below minimum necessary from brief
- Spam compliance checklist failures (Module 11 pre-publish checklist)
```

**Severity 2 — Significant (Return to Writer with Specific Fixes)**
Failures that reduce quality below the competitive standard but do not disqualify the article.

```
SIGNIFICANT failures (3+ = return to writer):
- 3–5 modal verbs in factual statements
- 1–2 vague quantifiers not replaced with numbers
- 1 H3 without contextual bridge to parent H2
- 1–2 missing TF-IDF required terms
- FS target exceeds 40 words in 1 section
- 1 list missing intro sentence or outro paragraph
- 1 table missing definition sentence or outro paragraph
- 1 internal link using unapproved anchor text
```

**Severity 3 — Minor (QA Editor Corrects Inline)**
Failures that the QA editor can correct directly without returning the article.

```
MINOR failures (editor corrects):
- 1–2 isolated contextless words (single "very" or "really")
- Single sentence over 25 words
- Single missing bold on an answer
- Meta description 1–2 characters over or under the target range
- Alt tag missing for 1 non-critical image
- Minor formatting inconsistency (one list item with slightly wrong PoST)
```

### The Return Note

When an article is returned to the writer, the QA editor provides a structured return note. The note contains:

```
RETURN NOTE FORMAT
===================
Article ID: [TM-XX]
Article Title: [Title]
Date Returned: [Date]
QA Stage Failed: [Stage number and name]

CRITICAL FAILURES (must fix before resubmission):
1. [Item number] — [Description of failure] — [Location in article: heading/section]
   Required fix: [Specific action required]

SIGNIFICANT FAILURES (must fix before resubmission):
1. [Item number] — [Description] — [Location]
   Required fix: [Specific action]

Writer resubmission deadline: [Date]
Re-QA assigned to: [QA editor name]
```

The return note contains no editorial opinions. It contains only checklist item references, failure descriptions, locations, and required fixes. This removes subjectivity from the revision process.

---

## LESSON 12.9 — The Publishing Sequence

Passing QA is necessary but not sufficient for publishing. The publishing sequence determines the order in which live articles and pages are released to Google's crawl — and this order affects how quickly topical authority accumulates.

### The Five-Step Publishing Sequence

**Step 1 — Structural Pages First (Pre-content phase)**

Before any article publishes, verify all CMap structural pages are live:

```
[ ] Homepage live
[ ] About Us live (with author/team information and credentials)
[ ] Contact live (with physical address — NAP consistency)
[ ] Privacy Policy live
[ ] Sitemap.xml live and submitted to Search Console
[ ] Ontology Root Page live
[ ] All main navigation category pages live
```

No article publishes before these seven pages are live. Crawling starts at the homepage. If the structural pages don't exist, Google's first crawl has no context for what the site is.

**Step 2 — Phase 2 Core Pillars (First wave)**

All Phase 2 Core pillar articles publish in priority score order (highest score first). Publish 1–2 articles per week — not all at once.

**Why not publish all at once:** A site that publishes 10 articles on the same day sends a velocity signal that can trigger algorithmic caution. Consistent, steady publication is the correct cadence.

```
Publishing cadence for Phase 2:
Week 1: Core Pillar 1 (highest priority score)
Week 2: Core Pillar 2
Week 3: Core Pillar 3
Week 4: Core Pillar 4
...continue until all Phase 2 articles are live
```

**Step 3 — Internal Link Verification Post-Publish**

After each article goes live:

```
[ ] Verify article URL is accessible (200 status code)
[ ] Verify all internal links in the article are live and correct
[ ] Verify all existing articles that should link TO this article
    have their links active (downward links from parent, lateral links from siblings)
[ ] Request indexing via Google Search Console URL Inspection
[ ] Confirm article appears in XML sitemap (auto-regenerated or manually added)
```

**Step 4 — Phase 3 Deep Core Supporting Articles**

Phase 3 articles publish only after their parent Phase 2 pillar is:
- Live
- Indexed (confirmed in Search Console)
- Receiving at least some impressions for target queries

**Why wait for indexing confirmation:** A supporting article that links upward to a parent that Google has not yet indexed loses the authority transmission from that link. Publishing after the parent is indexed ensures the semantic cluster is already established before the child article extends it.

```
Publishing condition check per Phase 3 article:
[ ] Parent pillar is indexed (Search Console → URL Inspection → "URL is on Google")
[ ] Parent pillar shows impressions in Search Console Performance
[ ] Article's outbound link to parent is verified live
```

**Step 5 — Phase 4 Outer Section Articles**

Phase 4 articles publish only after Phase 2 and Phase 3 are substantially complete (minimum 70% of planned Core articles live and indexed).

```
Publishing condition check per Phase 4 article:
[ ] All Phase 2 Core pillars are live and indexed
[ ] Phase 3 supporting articles for the parent cluster are live
[ ] The 3+ cross-cluster links in this Outer article point to pages that are live
[ ] Publishing this Outer article does not accelerate the publishing of
    any Core article that is not yet ready
```

---

## LESSON 12.10 — Post-Publish Monitoring Protocol

Publishing is not the end of the workflow. Post-publish monitoring tracks whether each article is indexing, appearing in queries, and performing at or above competitive baseline.

### The 90-Day Monitoring Framework

**Days 1–7 post-publish:**
```
[ ] Confirm article is indexed: Search Console → URL Inspection
[ ] Confirm article appears in sitemap.xml (check with Google Search Console
    → Sitemaps → view processed sitemap)
[ ] Check for crawl errors in Coverage report
[ ] Verify no duplicate content signal (canonical tag rendering correctly)
```

**Days 7–30 post-publish:**
```
[ ] Check for first impressions in Search Console → Performance
    (filter by page URL)
[ ] Note which queries are generating impressions
[ ] Compare queries to the primary and secondary keywords in the brief
    — are the correct queries driving impressions?
[ ] Check if any featured snippet position has been won
[ ] Verify rich result rendering in Search Console → Rich Results Test
```

**Days 30–90 post-publish:**
```
[ ] Track average position for primary keyword over time
[ ] Check click-through rate — is the title and meta description
    generating expected CTR for the position?
[ ] Identify any unexpected queries the article is ranking for
    — these are information gain signals (Google found additional value)
[ ] Identify any queries the article should be ranking for but isn't
    — these are gaps to address in the next revision
[ ] Check for pogo-sticking signals (high CTR but short dwell time in
    Analytics) — indicates delayed answer issue
```

### The 90-Day Decision Gate

At 90 days post-publish, each Core article is evaluated against these thresholds:

```
90-DAY DECISION GATE
=====================
Article is PERFORMING if:
  Average position ≤ 20 for primary keyword AND
  Impressions are growing week-over-week AND
  At least 1 query cluster is generating clicks

Article needs ENRICHMENT if:
  Average position > 20 for primary keyword AND
  Impressions are flat or declining AND
  Article has been indexed for 60+ days

Article needs STRUCTURAL REVIEW if:
  Impressions growing but CTR <1% at positions 1–10 → title/meta issue
  Impressions for wrong queries only → macro context drift
  Zero impressions after 45 days → indexing issue (check canonical, noindex)

Article needs CONSOLIDATION REVIEW if:
  A sibling article is outperforming this one for the same queries →
  potential cannibalism — apply Module 2 (Lesson 2.8) resolution
```

---

## LESSON 12.11 — Ongoing Site Maintenance: The Monthly Audit

Site quality degrades over time without maintenance. Prices change. Products discontinue. Declarations become outdated. New spam policy updates require reassessment of existing content. The monthly audit prevents structural decay.

### Monthly Audit Protocol

```
MONTHLY AUDIT CHECKLIST
=========================

Declaration Integrity:
[ ] Check for price changes in the Pakistani market — update all price
    references in articles that are more than 60 days old
[ ] Verify all product availability claims are current
    (discontinued models must be removed or annotated)
[ ] Check for declaration conflicts introduced by new articles
    (new articles may state values that conflict with older articles)
[ ] Update "last updated" dates on all articles where data was changed

Internal Linking Health:
[ ] Run site crawler — identify all 404 target pages in internal links
[ ] Fix all broken internal links (update URL or remove if page removed)
[ ] Check for orphan pages (pages with zero inbound internal links)
[ ] Verify all new articles from the past month have been added to
    the Internal Linking Map

Content Performance:
[ ] Review Search Console Performance for all articles published in the
    past 90 days — apply 90-day decision gate
[ ] Identify articles with declining impressions (possible algorithm
    quality signal) — schedule enrichment
[ ] Identify articles with sudden impression spikes — potential
    featured snippet win or new query cluster alignment
[ ] Identify new query clusters appearing in Search Console
    not yet addressed in the Topical Map — add to future planning

Technical Health:
[ ] Check Core Web Vitals in Search Console
[ ] Check Coverage report for new crawl errors
[ ] Verify sitemap is up to date (all new URLs included)
[ ] Confirm no new noindex tags introduced accidentally
[ ] Check for duplicate title tags or meta descriptions
    (created when new articles accidentally duplicate existing metadata)

Spam Compliance:
[ ] Review any articles written/edited in the past month against
    the pre-publish compliance checklist
[ ] Check for new topical drift (articles outside source context)
[ ] Verify no new declaration conflicts in recently published articles
```

---

## LESSON 12.12 — The Complete QA Summary Card

A single-page reference card for QA reviewers. Pinned at every reviewer's workstation.

```
╔══════════════════════════════════════════════════════════════════╗
║              QA AUDIT — 6 STAGES REFERENCE CARD                 ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  STAGE 1 — ENTITY AND CONTEXT          (19 items)               ║
║  ✓ Single macro context                                          ║
║  ✓ H2s are direct components of H1                              ║
║  ✓ Central entity named (no pronouns)                           ║
║  ✓ All EAV attributes from brief covered                        ║
║  ✓ Source context + geographic context present                  ║
║                                                                  ║
║  STAGE 2 — STRUCTURE                   (21 items)               ║
║  ✓ Every H2/H3 is a question                                    ║
║  ✓ H3 bridges H2 — no context jumps                            ║
║  ✓ Flow: Definition → Mechanism → Types → Attrs → Compare → FAQ ║
║  ✓ Opening: entity + layer + macro context                      ║
║  ✓ Conclusion: 3+ opening n-grams + practical synthesis         ║
║                                                                  ║
║  STAGE 3 — SENTENCE QUALITY            (33 items)               ║
║  ✓ No modals in facts (will/should/might)                       ║
║  ✓ No vague quantifiers — specific numbers only                 ║
║  ✓ No pronouns — entity names throughout                        ║
║  ✓ No contextless words                                         ║
║  ✓ Conditions after declarations                                ║
║  ✓ Bold on answer not keyword                                   ║
║  ✓ Lists: intro + items (same PoST) + outro                    ║
║  ✓ Tables: definition + data + outro                            ║
║                                                                  ║
║  STAGE 4 — COMPLETENESS                (25 items)               ║
║  ✓ All EAV values from brief present                            ║
║  ✓ FS answers ≤40 words / ≤320 chars                           ║
║  ✓ PAA first sentence = complete direct answer                  ║
║  ✓ Info gain targets achieved (3 Core / 1 Outer)               ║
║  ✓ All TF-IDF required terms present                            ║
║  ✓ All format codes applied correctly                           ║
║                                                                  ║
║  STAGE 5 — INTERNAL LINKING            (20 items)               ║
║  ✓ All brief links present + live                               ║
║  ✓ Anchors from approved master list only                       ║
║  ✓ No generic anchors (click here / read more)                  ║
║  ✓ Links in topically correct sections                          ║
║  ✓ Hash links verified live                                     ║
║  ✓ No inline external citations                                 ║
║                                                                  ║
║  STAGE 6 — ON-PAGE TECHNICAL           (39 items)               ║
║  ✓ URL: correct path, no duplication, <75 chars                 ║
║  ✓ Title: 50–60 chars, passes 5-point test                     ║
║  ✓ Meta: 150–160 chars, entity + value + qualifier              ║
║  ✓ Alt tags: entity + attribute + context per image             ║
║  ✓ Schema: accurate, matches visible content                    ║
║  ✓ Author: named, linked to bio, credentials match niche        ║
║  ✓ Publish date accurate, canonical self-referencing            ║
║                                                                  ║
║  SEVERITY GUIDE:                                                 ║
║  CRITICAL (1+ item) → Return to writer immediately              ║
║  SIGNIFICANT (3+ items) → Return to writer with fixes           ║
║  MINOR (isolated) → QA editor corrects inline                   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## MODULE 12 — SUMMARY

The QA audit is the final gate that converts a well-planned, well-written article into a publishable, ranking asset. It has six stages, 157 total checklist items, and a severity classification system that routes failures to the correct resolution path.

**Stage 1 — Entity and Context** verifies the macro context is correct, the central entity is properly established throughout, all EAV attributes are covered, and the source context and geographic framing are consistent.

**Stage 2 — Structure** verifies heading hierarchy, contextual bridges, linear flow, question quality, and opening/conclusion n-gram consistency.

**Stage 3 — Sentence Quality** verifies every sentence-level rule — certainty, numerics, entity naming, word order, conditional placement, bold formatting, list structure, and table structure.

**Stage 4 — Completeness** verifies EAV coverage, featured snippet targets, PAA answer structure, information gain achievement, TF-IDF compliance, and format code application.

**Stage 5 — Internal Linking** verifies all brief-specified links are present and live, all anchors are from the approved master list, link placement is contextually correct, and no inline external citations exist.

**Stage 6 — On-Page Technical** verifies URL structure, title tag, meta description, image alt tags, schema markup, authorship, and publication metadata.

**The publishing sequence** — structural pages first, Core pillars next, deep Core supporting articles after parent indexing confirmation, Outer articles after Core is established — ensures topical authority accumulates in the correct order.

**Post-publish monitoring** at 7, 30, and 90 days tracks indexing, impression growth, query alignment, and performance against the 90-day decision gate thresholds.

**Monthly maintenance** prevents declaration drift, broken link accumulation, orphan page creation, and spam compliance decay.

When this system operates correctly from Module 1 through Module 12, the output is a website that Google evaluates as a topical authority — not because it published the most content, but because it published the right content, in the right structure, with the right signals, in the right order.

---

## MODULE 12 — KEY TERMS GLOSSARY

| Term | Definition |
|---|---|
| **QA audit** | A structured six-stage evaluation of an article against all course standards — not proofreading, but systematic compliance verification. |
| **Severity 1 (Critical)** | A QA failure that fundamentally compromises ranking eligibility or spam compliance — returns article to writer immediately. |
| **Severity 2 (Significant)** | A QA failure that reduces quality below competitive standard — returns article to writer with specific fix instructions. |
| **Severity 3 (Minor)** | A small, isolated QA failure that the QA editor corrects inline without returning the article. |
| **Return note** | The structured document sent to the writer when an article fails QA — contains item references, failure descriptions, locations, and required fixes only. No editorial opinions. |
| **Publishing sequence** | The mandatory order of publication: structural pages → Core pillars → deep Core supporting articles → Outer articles. |
| **Indexing confirmation** | Verification via Google Search Console URL Inspection that a page has been crawled and added to Google's index — required before child articles publish. |
| **90-day decision gate** | The performance evaluation applied to every Core article at 90 days post-publish — determines whether the article is performing, needs enrichment, needs structural review, or needs consolidation. |
| **Declaration drift** | The gradual accumulation of outdated or conflicting factual claims across published articles as market data changes over time. |
| **Monthly audit** | The recurring maintenance check covering declaration integrity, internal linking health, content performance, technical health, and spam compliance. |
| **Information gain verification** | The process of confirming that an article's claimed information gain targets are absent from competitor articles and present in the article being reviewed. |

---

## MODULE 12 — SELF-ASSESSMENT QUESTIONS

1. A QA reviewer finds the following in an article about gas heater wattage:
   - 8 instances of "it" referring to the gas heater
   - 3 sentences beginning with "It is important to note that..."
   - 1 H2 that reads "Buy Gas Heaters Online in Pakistan" (not a question)
   - The FS target for "What wattage for 200 sq ft?" is 52 words
   - The author field shows "PakHeaters Team"
   Classify each failure by severity. What happens to this article?

2. A Core pillar article passes Stages 1–5 completely. Stage 6 reveals: the meta description is 178 characters, the URL contains the word "heater" twice (`/heaters/gas-heater-heater-types/`), and the FAQPage schema includes 2 questions not present in the visible article content. Classify each Stage 6 failure by severity and write the specific fix for each.

3. You are preparing to publish Phase 3 supporting articles for the Gas Heater Types pillar. The pillar has been live for 3 weeks. What specific checks must you run before publishing Phase 3 articles, and what is the condition that must be met?

4. An article about "Gas Heater Carbon Monoxide Safety Guide" passes all 6 QA stages. During post-publish monitoring at day 30, you find: the article is indexed, has 1,200 impressions, average position 34, but zero clicks. What does this signal and what action does it require?

5. At the 90-day decision gate, a Core pillar article about "Gas Heater Brands Pakistan" shows: average position 18, impressions growing week-over-week, but CTR of 0.4% at positions 12–18. What decision does the gate produce? What is the most likely cause and what specific fix addresses it?

6. Write a complete return note for an Outer section article about "Gas Heater for Small Apartments Pakistan" that has failed Stage 3 with these specific failures: 6 modal verbs in factual statements (items 3.1–3.2), 4 vague quantifiers (item 3.5), and 2 lists missing outro paragraphs (item 3.28).

7. Explain why the monthly declaration integrity audit is essential for a Pakistani heater retailer specifically. What external events (market conditions, policy changes, seasonal factors) create declaration drift risk in this niche, and how frequently should different article types be reviewed for this risk?

---

*Course complete. Proceed to the Course Introduction and Master Templates Pack.*
