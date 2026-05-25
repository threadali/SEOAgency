# MODULE 10 — Internal Linking Strategy
## How Pages Connect to Build Topical Authority Signals

> **Purpose of this module:** Internal links are not navigation aids. They are semantic signals. Every internal link you place tells Google three things simultaneously: that two pages share a semantic relationship, what the relationship is (through the anchor text), and which page is the authority on the linked topic (through the link direction and weight distribution). A correctly built internal link structure amplifies topical authority across the entire site. An incorrectly built one dilutes it — or worse, creates semantic conflicts that confuse Google about which page should rank for which query. This module teaches you to build the Internal Linking Map — the document that governs every link decision before any writer creates a link.

---

## LESSON 10.1 — Why Internal Linking Is a Semantic Signal

### The Two Outdated Beliefs About Internal Links

**Outdated belief 1:** Internal links exist to help users navigate.
**Reality:** Navigation is a byproduct. The primary function of internal links is to communicate semantic relationships between pages to search engine crawlers.

**Outdated belief 2:** More internal links = more authority distributed.
**Reality:** More links = less weight per link. A page with 3 carefully chosen internal links sends a stronger signal per link than a page with 30 links sprinkled throughout.

### What Google Reads in an Internal Link

When Google crawls an internal link, it reads four things:

**1. The source page** — what entity-attribute pair is the source page about? What is its authority level in the site hierarchy?

**2. The anchor text** — what does the anchor text say the target page is about? Does it match the target page's title and macro context?

**3. The target page** — what entity-attribute pair does the target page actually cover? Does it match what the anchor text implied?

**4. The link direction** — is this a link from a higher-authority page to a lower one (passing authority down), or from a lower-authority page to a higher one (building authority up)?

When all four signals are consistent — source context matches, anchor text matches target title, target content matches anchor promise, direction supports the hierarchy — the link creates a genuine semantic connection. When any signal conflicts, the link creates noise.

### Internal Links as Semantic Cluster Builders

Google's document grouping system (covered in Module 0) clusters related pages together. Internal links are the primary signal that pages belong in the same cluster.

When page A links to page B with anchor text that matches page B's title, Google concludes:
1. Pages A and B are semantically related
2. Page B is the authority on the topic named in the anchor text
3. Pages A and B belong in the same semantic cluster

When a cluster of 10 pages all link to a central pillar page using consistent anchor text, Google builds a strong cluster signal: this pillar page is the authority on this topic within this site's knowledge domain.

**This is the mechanism behind topical authority accumulation.** It is not built by publishing many articles. It is built by correctly linking those articles into coherent semantic clusters.

---

## LESSON 10.2 — The Five Types of Internal Links

Not all internal links serve the same function. Understanding the five types allows you to build each type correctly and use it in the right context.

### Type 1 — Hierarchical Links (Upward)

**Direction:** From supporting article → to parent pillar page → to category page → to ontology root

**Function:** Builds authority on higher-level pages. Signals to Google that the source page is a sub-topic of the target page.

**Anchor text rule:** Use a phrase that names the broader entity-attribute pair of the target page — the hypernym of the source page's topic.

```
Source: Infrared Gas Heater Article
Target: Gas Heater Types Pillar
Anchor text: "gas heater types in Pakistan"

Source: Gas Heater Types Pillar
Target: Gas Heater Category Page (/heaters/gas-heater/)
Anchor text: "gas heaters in Pakistan"

Source: Gas Heater Category Page
Target: Ontology Root (/heaters/)
Anchor text: "home heaters Pakistan"
```

**Every article links upward at least once.** No article is an island. Every article connects back to its parent through at least one hierarchical upward link.

---

### Type 2 — Hierarchical Links (Downward)

**Direction:** From ontology root → to pillar pages → to supporting articles

**Function:** Distributes authority to lower-level pages. Signals to Google that the target page is a sub-topic of the source page. Accelerates discovery and indexing of deeper pages.

**Anchor text rule:** Use the exact title phrase of the target page, or the entity-attribute pair it covers — the hyponym of the source page's topic.

```
Source: Gas Heater Types Pillar
Target: Infrared Gas Heater Article
Anchor text: "infrared gas heater Pakistan"

Source: Gas Heater Types Pillar
Target: Blue Flame Gas Heater Article
Anchor text: "blue flame gas heater Pakistan"

Source: Ontology Root (/heaters/)
Target: Gas Heater Types Pillar
Anchor text: "gas heater types"
```

**Every pillar page links down to all its child articles.** The pillar page is the hub. Its child articles are the spokes. All spokes connect to the hub.

---

### Type 3 — Lateral Links (Sibling Links)

**Direction:** Between articles at the same level that share the same parent

**Function:** Builds topical cluster density. Signals to Google that all sibling pages belong to the same semantic cluster. Keeps users within the cluster, increasing session depth.

**Anchor text rule:** Use the entity-attribute pair of the target sibling — different from the source page's entity-attribute.

```
Source: Infrared Gas Heater Article
→ Links to: Blue Flame Gas Heater Article
   Anchor: "blue flame convection gas heater Pakistan"

Source: Infrared Gas Heater Article
→ Links to: Catalytic Gas Heater Article
   Anchor: "catalytic gas heater indoor safety"
```

**Sibling link rule:** Every article links to at least one sibling. Not all siblings link to each other (that creates link equity dilution) — each article links to the most relevant sibling based on topical proximity.

**Topical proximity test:** Which sibling article would a user reading this article most likely want to read next? That is the sibling link target.

---

### Type 4 — Cross-Cluster Links (Outer → Core)

**Direction:** From Outer section article → to Core section pillar page

**Function:** Builds authority on Core section pages from the Outer section. Reinforces the Core page's authority on its entity-attribute from multiple angles.

**The fundamental rule from Module 7:** Outer section articles always link to Core section articles. Core section articles never link exclusively to Outer section articles.

```
Source: Gas Heater for Small Apartments (Outer)
→ Links to: Gas Heater Wattage Guide Pillar (Core)
   Anchor: "gas heater wattage for room size Pakistan"

Source: First-Time Buyer's Heater Guide (Outer)
→ Links to: Gas Heater Types Pillar (Core)
   Anchor: "gas heater types Pakistan"
→ Links to: Gas Heater Brands Pillar (Core)
   Anchor: "best gas heater brands Pakistan"
→ Links to: Gas Heater Price Pillar (Core)
   Anchor: "gas heater price list Pakistan"
```

Cross-cluster links are what make Outer section content contribute to topical authority rather than just expanding query coverage. Without them, Outer articles are isolated pages with no authority pathway.

---

### Type 5 — Deep Section Links (Hash Links)

**Direction:** From any article → to a specific section within another article

**Function:** Connects users (and crawlers) directly to the exact relevant section of a target page, rather than the top of the page. Reduces bounce rate from mismatched landing sections. Strengthens the semantic connection between specific sections.

**Format:** Target URL + `#section-id`

```
Source: Gas Heater Safety Article, section on CO risk
→ Links to: Infrared Gas Heater Article, section on catalytic safety
   Anchor: "catalytic heaters and lower CO risk"
   URL: /heaters/gas-heater/types/infrared-gas-heater/#catalytic-safety

Source: Gas Heater Wattage Guide, section on 1500W performance
→ Links to: Gas Heater Price Article, section on mid-range prices
   Anchor: "1500W gas heater price in Pakistan"
   URL: /heaters/gas-heater/price/#mid-range-prices
```

**When to use hash links:** When the relevant content is deeper in the target page, not at the top. When the anchor text references a specific topic covered in a section, not the entire page.

---

## LESSON 10.3 — The Four Internal Linking Rules

### Rule 1 — Anchor Text Must Match Target Page Title

The anchor text of an internal link must contain the primary keyword phrase from the target page's title. This is the most important anchor text rule in semantic SEO.

**Why:** Google uses anchor text to understand what the target page is about — from the perspective of the source page. If the anchor text and the target page title agree, the semantic signal is clear. If they disagree, Google receives a conflicting signal about the target page's topic.

```
TARGET PAGE TITLE: Gas Heater Price in Pakistan — 2025 Brand-wise Complete Price List

CORRECT anchor texts (contain primary entity-attribute from title):
✓ "gas heater price Pakistan"
✓ "gas heater price list Pakistan"
✓ "gas heater cost in Pakistan"
✓ "how much gas heaters cost in Pakistan"

INCORRECT anchor texts (do not reflect title's entity-attribute):
✗ "click here for prices"
✗ "our heater store"
✗ "affordable options"
✗ "check this out"
✗ "read more about heaters" ← hypernym mismatch — title is about price, not heaters generally
```

**The context matching rule:** The section of the source article where the link appears must be discussing the same entity-attribute as the anchor text. A link to the gas heater price article must appear in a section that is already discussing price — not in a random section about safety.

```
CORRECT placement:
Source article section: H2 "What is the Price of an Infrared Gas Heater?"
Body: "Infrared gas heaters in Pakistan retail at PKR 12,000–28,000.
      For a complete brand-wise breakdown, see the [gas heater price
      list Pakistan]."
Link: anchor = "gas heater price list Pakistan" → target = price pillar

INCORRECT placement:
Source article section: H2 "How Does Infrared Heating Work?"
Body: "The quartz tube emits radiant energy. [gas heater price list Pakistan]"
Link: anchor = "gas heater price list Pakistan" → appears in wrong context
```

---

### Rule 2 — Fewer Links = More Weight Per Link

Every internal link on a page distributes that page's authority to the target. The more links a page has, the less authority each individual link passes.

**The link budget concept:** Every page has a finite link budget — the total authority it can pass through outbound links. Spreading this budget across 30 links passes ~3.3% to each. Concentrating it in 6 links passes ~16.7% to each.

For standard content pages, maintain these link counts:

| Article Type | Recommended Internal Link Count |
|---|---|
| Core pillar page (2,000–3,000 words) | 5–8 outbound internal links |
| Supporting article (1,200–2,000 words) | 3–6 outbound internal links |
| Outer section article (800–1,400 words) | 3–5 outbound internal links |
| Ontology root page (comprehensive) | 8–12 outbound internal links (one per sub-section/pillar) |
| Category page | 4–8 outbound internal links (one per child page) |

**The minimum rule:** Every article needs minimum 2 outbound internal links — one upward (to parent) and one lateral (to sibling) or cross-cluster (to Core, if Outer).

---

### Rule 3 — No External Citation Links Inline

External citations (links to research papers, statistics sources, or authority sites) must not appear as inline links within the body content. They reduce the page's internal link equity by passing authority outward to external sites.

**Two correct approaches for citations:**

**Approach A — Reference without linking (preferred):**
State the source as text without hyperlinking.
```
"According to research from Pakistan Institute of Development Economics (2024),
gas-heated households in Lahore report 23% lower heating costs than
electric-heated households of equivalent size."
```

The source is cited but no outbound link passes authority away.

**Approach B — Footnote/endnote citation:**
Number the citation in text and list all sources at the bottom of the article, below the FAQ section. Links at the bottom carry the least link equity weight.

```
Body: "Gas-heated households report 23% lower heating costs [1]."
Bottom: [1] Pakistan Institute of Development Economics, Energy Report 2024.
```

**What never to do:**
```
"A study by [Stanford University researchers] found that..."
→ This is an inline outbound link passing authority to stanford.edu.
   Remove the hyperlink. Keep the text citation.
```

---

### Rule 4 — Consistent Anchor Text Across the Site

The same target page should receive consistent anchor text from multiple source pages. Anchor text variation signals to Google that different pages interpret the target page as being about different things — creating a diluted or ambiguous authority signal.

**Consistent anchor text example:**

Target page: Gas Heater Types Pillar (`/heaters/gas-heater/types/`)

All pages linking to it use one of these anchors:
```
"gas heater types Pakistan"
"types of gas heaters in Pakistan"
"gas heater types"
```

All three anchors contain the same entity-attribute pair (gas heater + types + Pakistan). They are synonym variations — consistent, not conflicting.

**Inconsistent anchor text example (what not to do):**

```
Article 1 → links with anchor: "gas heater types"
Article 2 → links with anchor: "different gas heaters available"
Article 3 → links with anchor: "heater options for your home"
Article 4 → links with anchor: "read our heating guide"
```

Article 2's anchor introduces vague language. Article 3's anchor introduces "home" — a different context. Article 4's anchor contains no entity-attribute information. These four anchors collectively weaken the authority signal on the target page.

**The anchor text consistency rule:** Maintain a master anchor text list for every Core and pillar page. Every new article that links to that page uses an anchor from the approved list — never invents a new one.

---

## LESSON 10.4 — Crawl Path Design Through Internal Links

### Why Internal Links Control Crawl Priority

Google's crawler follows links. A page that receives many internal links from high-authority pages is crawled more frequently and assigned higher initial authority. A page with no internal links from other pages — an orphan — may not be crawled at all, regardless of how well-written it is.

The internal link structure is the primary crawl path mechanism on a site. The CMap defined the structural crawl path (Module 6). Internal links within the Topical Map articles extend that crawl path to every article.

### The Authority Flow Diagram

```
Homepage (Depth 1, highest authority)
    │
    ├── Ontology Root (/heaters/) — Depth 2
    │       │ receives links from: all category pages, all pillar pages
    │       │ passes authority to: all pillar pages
    │       │
    │       ├── Gas Heater Types Pillar — Depth 4
    │       │       │ receives links from: ontology root,
    │       │       │   all child articles, Outer section articles
    │       │       │ passes authority to: all child articles
    │       │       │
    │       │       ├── Infrared Heater Article — Depth 5
    │       │       │       links up to: Types Pillar, Safety Pillar
    │       │       │       links lateral to: Blue Flame Article
    │       │       │
    │       │       └── Blue Flame Heater Article — Depth 5
    │       │               links up to: Types Pillar
    │       │               links lateral to: Infrared Article
    │       │
    │       └── Gas Heater Price Pillar — Depth 4
    │               receives links from: ontology root,
    │                   price comparison articles, Outer section articles
```

### How to Accelerate Crawl Priority for Important Pages

**Technique 1 — Ontology root links to all pillar pages**
The ontology root is at depth 2. Every page it links to is effectively at depth 2.5 in crawl terms — discovered on the second pass of the root page.

**Technique 2 — Navigation placement**
Any page in the main navigation header is at crawl depth 2. Gas Heater Types Pillar in the navigation = crawled as frequently as the homepage's direct children.

**Technique 3 — Multiple inbound links from peer pages**
A pillar page that receives 10 inbound links from sibling articles and Outer section articles is crawled more frequently than one that receives 2. Each new article that links to a pillar accelerates that pillar's crawl frequency.

**Technique 4 — Contextually early link placement**
A link that appears in the first 20% of a page's content carries more crawl priority signal than one buried in the footer. Place the most important internal links in the opening section or the first H2 of the article.

---

## LESSON 10.5 — Anchor Text Construction for Each Link Type

### Hierarchical Upward Link Anchor Text

Rule: Use the target page's entity + attribute pair. Contain the hypernym relative to the source page.

```
SOURCE: Infrared Gas Heater Article (entity: infrared gas heater)
TARGET: Gas Heater Types Pillar (entity: gas heater, attribute: types)

ANCHOR: "gas heater types in Pakistan"
→ "gas heater" is the hypernym of "infrared gas heater" ✓
→ "types" is the attribute of the target pillar ✓
→ "Pakistan" is the context qualifier ✓
```

### Hierarchical Downward Link Anchor Text

Rule: Use the target page's exact entity-attribute hyponym phrase.

```
SOURCE: Gas Heater Types Pillar
TARGET: Infrared Gas Heater Article

ANCHOR: "infrared gas heater Pakistan"
→ "infrared gas heater" is the hyponym of "gas heater types" ✓
→ "Pakistan" is the context qualifier ✓
→ Does NOT say "gas heater types" (that is the source, not the target) ✓
```

### Lateral Sibling Link Anchor Text

Rule: Use the sibling's entity-attribute pair, distinct from the source page's entity-attribute.

```
SOURCE: Infrared Gas Heater Article (infrared type)
TARGET: Blue Flame Gas Heater Article (blue flame type)

ANCHOR: "blue flame convection gas heater Pakistan"
→ "blue flame convection" distinguishes the target from the source ✓
→ "gas heater Pakistan" maintains the shared parent context ✓
```

### Cross-Cluster Outer → Core Link Anchor Text

Rule: Use the Core target's primary entity-attribute phrase — the same phrase that appears in the Core page's title.

```
SOURCE: Small Apartment Heater Guide (Outer)
TARGET: Gas Heater Wattage Pillar (Core)

ANCHOR: "gas heater wattage for room size Pakistan"
→ Matches the Core pillar's primary keyword and title phrase ✓
→ The Outer article's context (small apartments, room size) connects
   naturally to the wattage attribute ✓
```

### Deep Section (Hash Link) Anchor Text

Rule: Use the specific entity-attribute of the TARGET SECTION — not the entire target page.

```
SOURCE: Gas Heater Maintenance Guide, section on annual servicing
TARGET: Gas Heater Safety Pillar, section on ODS sensor

ANCHOR: "how ODS sensors work in gas heaters"
TARGET URL: /heaters/gas-heater/safety/#ods-sensor-explained
→ Anchor names the specific section topic (ODS sensors) ✓
→ Hash link delivers user directly to the ODS section ✓
→ Does NOT use the general title of the safety article ✓
```

---

## LESSON 10.6 — Templatic Phrase Linking

Templatic phrase linking applies whenever two pages share a structural phrase template — "X to Y", "X vs Y", "X for Y", "Best X in Y".

### The X vs Y Rule (Antonymous Pairs)

Any page with a comparison title (`gas heater vs electric heater`) must link to its inverse:
- The page about gas heaters alone
- The page about electric heaters alone
- The inverse comparison page if it exists (`electric heater vs gas heater`)

```
Page: Gas Heater vs Electric Heater Pakistan
Links to:
→ /heaters/gas-heater/ — "gas heaters Pakistan" (upward to gas heater category)
→ /heaters/electric-heater/ — "electric heaters Pakistan" (lateral to competing entity)
```

### The X for Y Rule (User Segment Templates)

Any page with a "for [segment]" structure links to sibling "for [different segment]" pages:

```
Page: Best Gas Heater for Small Apartments Pakistan
Links to:
→ Best Gas Heater for Large Rooms Pakistan (sibling — different segment)
→ Best Gas Heater for Elderly Users Pakistan (sibling — different segment)
```

### The X to Y Rule (Conversion/Direction Templates)

Any page covering conversion or directional relationships links to:
- The inverse relationship page
- All sibling pages covering the same relationship type with different values

```
Page: LPG to Natural Gas Conversion for Heaters Pakistan
Links to:
→ Natural Gas to LPG Conversion for Heaters (inverse)
→ LPG Heater Running Cost Pakistan (sibling — same entity, different attribute)
```

---

## LESSON 10.7 — Building the Internal Linking Map Document

The Internal Linking Map is the deliverable for this module. It is a master reference document that specifies every internal link on every page of the site — source page, target page, anchor text, section placement, and link type. Writers consult this document when writing. Editors verify against it during QA.

### Internal Linking Map Structure

**Sheet 1 — Master Link Registry**

```
Column A  — Link ID (IL-001, IL-002, etc.)
Column B  — Source Page ID (CMap ID or Topical Map article ID)
Column C  — Source Page Title
Column D  — Source Page URL
Column E  — Section in Source (H2 or H3 heading where link appears)
Column F  — Anchor Text (exact, final)
Column G  — Target Page ID
Column H  — Target Page Title
Column I  — Target Page URL
Column J  — Hash Identifier (if deep section link — leave blank if not)
Column K  — Link Type (Upward / Downward / Lateral / Cross-cluster / Hash)
Column L  — Link Direction (Core→Core / Core→Outer / Outer→Core / etc.)
Column M  — Status (Planned / Implemented / Verified)
Column N  — Notes
```

**Sheet 2 — Page Link Budget Summary**

```
Column A  — Page ID
Column B  — Page Title
Column C  — Total outbound internal links
Column D  — Total inbound internal links
Column E  — Inbound from Core pages (count)
Column F  — Inbound from Outer pages (count)
Column G  — Upward links (count)
Column H  — Downward links (count)
Column I  — Lateral links (count)
Column J  — Cross-cluster links (count)
Column K  — Link budget status (within recommended range / over-linked / under-linked)
```

**Sheet 3 — Anchor Text Master List**

```
Column A  — Target Page ID
Column B  — Target Page Title
Column C  — Target Page Primary KW
Column D  — Approved Anchor Variation 1
Column E  — Approved Anchor Variation 2
Column F  — Approved Anchor Variation 3
Column G  — Prohibited Anchor Patterns (vague, mismatched, or conflicting phrases)
```

---

## LESSON 10.8 — The Internal Linking Audit

After the Internal Linking Map is built and articles begin going live, the audit process verifies that the planned links are correctly implemented.

### Five Audit Checks

**Check 1 — Orphan Page Detection**

An orphan page has zero inbound internal links. No page on the site should be orphaned after going live.

**Method:** Pull all URLs from Google Search Console or a site crawler. Cross-reference against the Internal Linking Map. Any URL with zero inbound links = orphan.

**Fix:** Add at least one inbound link from the most semantically relevant page using the approved anchor text.

---

**Check 2 — Broken Internal Link Detection**

A broken internal link (404 error target) wastes crawl budget and destroys the intended semantic signal.

**Method:** Use a site crawler (Screaming Frog, Ahrefs, or Search Console's coverage report) to identify all 4xx errors being linked to internally.

**Fix:** Update the link to the correct URL, or redirect the broken target URL.

---

**Check 3 — Anchor Text Consistency Verification**

Verify that all links pointing to each Core/pillar page use an anchor from the approved list — not invented variations.

**Method:** Pull all inbound internal links to each pillar page. Compare anchors used against the Anchor Text Master List (Sheet 3).

**Fix:** Update non-compliant anchors to match the approved list.

---

**Check 4 — Link Budget Overload Detection**

Identify pages with more internal links than their word count can support. A 1,200-word article with 20 internal links is diluting its link equity across too many targets.

**Method:** Review Sheet 2 (Page Link Budget Summary). Flag any page where total outbound links exceeds the recommended count for that article type.

**Fix:** Remove the lowest-priority links — those linking to Outer section pages or using vague anchors. Retain links to Core pages and parent pages.

---

**Check 5 — Core Page Inbound Link Sufficiency**

Every Core pillar page should receive inbound links from:
- Ontology root (1 link)
- All sibling pillar pages (1 link each)
- All child supporting articles (1 link each)
- Minimum 3 Outer section articles (1 link each)

A Core pillar with fewer than 6 total inbound internal links is under-linked and accumulating authority slowly.

**Method:** Review Sheet 2 (Page Link Budget Summary) Column D for each Core pillar. Flag pages below the minimum threshold.

**Fix:** Identify existing articles that could naturally include a link to the under-linked pillar. Add the link within a contextually appropriate section.

---

## LESSON 10.9 — Completed Internal Linking Map Excerpt

**Site:** PakHeaters.pk | Core Section Only

```
INTERNAL LINKING MAP — PakHeaters.pk (Excerpt)
═══════════════════════════════════════════════════════════════════════

SHEET 1 — MASTER LINK REGISTRY (Selected entries)

IL-001
Source: TM-01 (Gas Heater Types Pillar)
Source URL: /heaters/gas-heater/types/
Section: H2 "What is a Gas Heater?" — first paragraph
Anchor: "home heaters in Pakistan"
Target: C-01 (Ontology Root — /heaters/)
Type: UPWARD
Direction: Core → Core (upward to root)
Status: Planned

IL-002
Source: TM-01 (Gas Heater Types Pillar)
Section: H2 "What is the Price of Gas Heaters in Pakistan?"
Anchor: "gas heater price in Pakistan"
Target: TM-02 (Gas Heater Price Pillar — /heaters/gas-heater/price/)
Type: LATERAL (sibling pillar)
Direction: Core → Core (same level)
Status: Planned

IL-003
Source: TM-01 (Gas Heater Types Pillar)
Section: H2 "What is a Radiant Infrared Gas Heater?"
Anchor: "infrared gas heater Pakistan"
Target: TM-05 (Infrared Article — /heaters/gas-heater/types/infrared-gas-heater/)
Type: DOWNWARD
Direction: Core → Deep Core (pillar to supporting)
Status: Planned

IL-004
Source: TM-01 (Gas Heater Types Pillar)
Section: H2 "What is a Blue Flame Gas Heater?"
Anchor: "blue flame gas heater Pakistan"
Target: TM-04 (Blue Flame Article — /heaters/gas-heater/types/blue-flame-gas-heater/)
Type: DOWNWARD
Direction: Core → Deep Core
Status: Planned

IL-005
Source: TM-01 (Gas Heater Types Pillar)
Section: H2 "Is a Gas Heater Safe to Use Indoors?"
Anchor: "gas heater indoor safety Pakistan"
Target: P-04 (Safety Pillar — /heaters/gas-heater/safety/)
Type: LATERAL (sibling pillar)
Direction: Core → Core (same level)
Status: Planned

IL-006
Source: TM-01 (Gas Heater Types Pillar)
Section: H2 "Which Gas Heater Type Is Best for Pakistani Homes?"
Anchor: "gas heater wattage and room size Pakistan"
Target: TM-03 (Wattage Pillar — /heaters/gas-heater/wattage/)
Type: LATERAL (sibling pillar)
Direction: Core → Core (same level)
Status: Planned

─────────────────────────────────────────────────────────────────────

IL-007
Source: TM-04 (Blue Flame Gas Heater — supporting article)
Section: Opening paragraph
Anchor: "gas heater types in Pakistan"
Target: TM-01 (Gas Heater Types Pillar — parent)
Type: UPWARD
Direction: Deep Core → Core (supporting → pillar)
Status: Planned

IL-008
Source: TM-04 (Blue Flame Gas Heater)
Section: H3 "How Is Blue Flame Heating Different from Infrared?"
Anchor: "infrared gas heater Pakistan"
Target: TM-05 (Infrared Gas Heater Article — sibling)
Type: LATERAL
Direction: Deep Core → Deep Core (sibling)
Hash: /heaters/gas-heater/types/infrared-gas-heater/#comparison-with-blue-flame
Status: Planned

IL-009
Source: TM-04 (Blue Flame Gas Heater)
Section: H2 "What Is the Price of Blue Flame Gas Heaters in Pakistan?"
Anchor: "gas heater price list Pakistan"
Target: TM-02 (Gas Heater Price Pillar)
Type: CROSS-CLUSTER (supporting → Core pillar)
Direction: Deep Core → Core
Status: Planned

─────────────────────────────────────────────────────────────────────

IL-017
Source: TM-09 (Small Apartment Heater — OUTER section)
Section: Opening paragraph
Anchor: "gas heater wattage for room size Pakistan"
Target: TM-03 (Gas Heater Wattage Pillar — Core)
Type: CROSS-CLUSTER
Direction: Outer → Core
Status: Planned

IL-018
Source: TM-09 (Small Apartment Heater — OUTER)
Section: H2 "Which Gas Heater Type Is Best for Small Apartments?"
Anchor: "gas heater types Pakistan"
Target: TM-01 (Gas Heater Types Pillar — Core)
Type: CROSS-CLUSTER
Direction: Outer → Core
Status: Planned

IL-019
Source: TM-09 (Small Apartment Heater — OUTER)
Section: H2 "Is a Gas Heater Safe in a Small Apartment?"
Anchor: "gas heater indoor safety Pakistan"
Target: P-04 (Safety Pillar — Core)
Type: CROSS-CLUSTER
Direction: Outer → Core
Status: Planned

─────────────────────────────────────────────────────────────────────

SHEET 2 — PAGE LINK BUDGET SUMMARY (Selected)

TM-01 | Gas Heater Types Pillar
Outbound internal links: 6
  → C-01 (root): 1 upward
  → TM-02 (price sibling): 1 lateral
  → TM-03 (wattage sibling): 1 lateral
  → P-04 (safety sibling): 1 lateral
  → TM-04 (blue flame child): 1 downward
  → TM-05 (infrared child): 1 downward
Inbound internal links: 11
  From: C-01 (root), C-02 (gas heater category),
        TM-04 (blue flame), TM-05 (infrared), TM-06 (catalytic),
        TM-09 (small apt — outer), TM-10 (first buyer — outer),
        TM-11 (CO safety — outer), TM-12 (maintenance — outer),
        L-02 (comparison landing), P-01 (types CMap page)
Link budget status: WITHIN RANGE ✓

TM-04 | Blue Flame Gas Heater (Deep Core supporting)
Outbound internal links: 3
  → TM-01 (parent pillar): 1 upward
  → TM-05 (sibling — infrared): 1 lateral (hash link)
  → TM-02 (price pillar): 1 cross-cluster
Inbound internal links: 4
  From: TM-01 (parent pillar), C-02 (gas heater category),
        TM-09 (small apt outer), TM-10 (first buyer outer)
Link budget status: WITHIN RANGE ✓

TM-09 | Small Apartment Heater (Outer)
Outbound internal links: 3 (all cross-cluster to Core)
  → TM-03 (wattage Core): 1
  → TM-01 (types Core): 1
  → P-04 (safety Core): 1
Inbound internal links: 2
  From: P-03 (wattage CMap page), TM-03 (wattage pillar)
Link budget status: WITHIN RANGE ✓

─────────────────────────────────────────────────────────────────────

SHEET 3 — ANCHOR TEXT MASTER LIST (Selected)

TM-01 | Gas Heater Types Pillar
Primary KW: gas heater types pakistan
Approved anchors:
  1. "gas heater types in Pakistan"
  2. "types of gas heaters Pakistan"
  3. "gas heater types guide"
Prohibited: "heater guide", "different heaters", "click here", "read more",
            "heating options Pakistan" (too vague)

TM-02 | Gas Heater Price Pillar
Primary KW: gas heater price pakistan
Approved anchors:
  1. "gas heater price in Pakistan"
  2. "gas heater price list Pakistan"
  3. "gas heater cost Pakistan"
  4. "gas heater prices 2025 Pakistan"
Prohibited: "buy heaters", "cheap heaters", "affordable options", "prices here"

P-04 | Gas Heater Safety Pillar
Primary KW: gas heater safety
Approved anchors:
  1. "gas heater indoor safety Pakistan"
  2. "gas heater safety guide"
  3. "is gas heater safe indoors"
  4. "gas heater carbon monoxide safety"
Prohibited: "safety tips", "be careful", "important information about safety"
═══════════════════════════════════════════════════════════════════════
```

---

## LESSON 10.10 — The Internal Linking Audit Checklist

Before any article is published and after every batch of articles goes live, run this checklist:

```
INTERNAL LINKING AUDIT CHECKLIST
===================================

Pre-publish (per article):
[ ] All links in this article are in the Internal Linking Map
[ ] Anchor text for each link matches an approved variation from Sheet 3
[ ] Link placement is in the correct contextual section (not forced)
[ ] Total outbound links within recommended count for this article type
[ ] At least 1 upward link to parent CMap page included
[ ] Core article: at least 1 lateral link to sibling pillar included
[ ] Outer article: minimum 3 cross-cluster links to Core pages included
[ ] No external citation links inline (footnotes only)
[ ] Hash links include correct #section-id in target URL

Post-publish (per batch, monthly):
[ ] No new orphan pages (all live pages have inbound internal links)
[ ] No broken internal links (404 target pages)
[ ] All Core pillars have minimum 6 inbound internal links
[ ] Anchor text audit: no new unapproved anchor variations detected
[ ] Link budget: no pages exceed maximum outbound link count
[ ] New Outer articles: all 3+ cross-cluster links to Core verified live
[ ] Cross-cluster links from Outer to Core: verified correct anchor text
```

---

## MODULE 10 — SUMMARY

Internal linking is a semantic architecture tool — not a navigation feature.

**The five link types** (hierarchical upward, hierarchical downward, lateral sibling, cross-cluster, hash) each serve a distinct semantic function. Using the wrong type in the wrong direction sends incorrect signals about page hierarchy and authority distribution.

**The four rules** (anchor text matches target title, fewer links = more weight per link, no external citations inline, consistent anchor text across the site) ensure every link placed contributes a clear, unambiguous signal to Google's semantic cluster evaluation.

**The authority flow diagram** shows how internal links move authority from the homepage through the ontology root to pillar pages and from pillar pages to supporting articles. Every Outer section article closing the loop by linking to Core pages completes the authority circuit.

**The Internal Linking Map** — three sheets: Master Link Registry, Page Link Budget Summary, and Anchor Text Master List — is the production document that governs every link decision. No writer creates an internal link without consulting it. No editor approves an article without verifying against it.

**The audit process** catches orphan pages, broken links, anchor text drift, and authority dilution before they become ranking problems. Monthly audits prevent the structural decay that accumulates when internal links are managed reactively rather than proactively.

---

## MODULE 10 — KEY TERMS GLOSSARY

| Term | Definition |
|---|---|
| **Semantic cluster** | A group of related pages connected by internal links that Google evaluates collectively as a topical unit. |
| **Link budget** | The finite authority a page can distribute through its outbound internal links — divided equally among all link targets. |
| **Hierarchical upward link** | A link from a supporting article to its parent pillar or category page — builds authority on the higher-level page. |
| **Hierarchical downward link** | A link from a pillar page to its child supporting articles — distributes authority and accelerates discovery. |
| **Lateral sibling link** | A link between two articles at the same hierarchy level sharing the same parent — builds cluster density. |
| **Cross-cluster link** | A link from an Outer section article to a Core section pillar — the primary mechanism by which Outer articles contribute to topical authority. |
| **Hash link** | A link to a specific section within a target page using `#section-id` — connects specific topics across pages without landing at the top. |
| **Orphan page** | A live page that receives zero inbound internal links — undiscoverable by Google's crawler through internal navigation. |
| **Anchor text consistency** | The practice of using only pre-approved anchor text variations for each target page, ensuring all source pages send the same semantic signal about the target. |
| **Internal Linking Map** | The master document governing all internal link decisions — containing the Master Link Registry, Page Link Budget Summary, and Anchor Text Master List. |
| **Anchor text drift** | The accumulation of unapproved or inconsistent anchor text variations pointing to the same target page — dilutes the target page's topical signal. |
| **Link placement context** | The requirement that an internal link appears within a section of the source article that is topically relevant to the anchor text and target page. |

---

## MODULE 10 — SELF-ASSESSMENT QUESTIONS

1. A newly published article about `gas heater for elderly users Pakistan` (Outer section) contains these internal links:
   - Link 1: "gas heaters" → /heaters/gas-heater/ (category page)
   - Link 2: "safety features" → /heaters/gas-heater/safety/ (Core pillar)
   - Link 3: "affordable options" → /heaters/buy-gas-heater/ (landing page)
   Evaluate each link against the four internal linking rules. Which links are correct, which are incorrect, and why? Rewrite the incorrect anchors.

2. A Core pillar page about `gas heater price Pakistan` has 18 outbound internal links. Its word count is 2,400 words. What is the problem? How do you decide which links to remove?

3. Explain why an Outer section article that covers `gas heater for small apartments` but links only to other Outer articles (never to Core pillar pages) fails to contribute to topical authority — even if it is well-written and well-researched.

4. Build the complete internal linking plan for the article "Gas Heater Carbon Monoxide Safety Guide Pakistan" (Core/Outer classification = Core, parent pillar = Safety). Specify: all outbound links with anchor text, section placement, link type, and direction.

5. The Anchor Text Master List shows that `gas heater types pillar` has 3 approved anchor variations. A writer creates a new Outer section article and links to the types pillar with the anchor "complete heater buying guide". Is this compliant? If not, what is the impact and what must be done?

6. After a site audit, you discover that `Gas Heater Safety Pillar` has only 2 inbound internal links — both from other Core pillar pages. It has zero inbound links from Outer section articles. What is the problem and what is the solution? Name at least 4 Outer section articles that could naturally link to it.

7. Write the complete hash link (full URL + #section-id) and anchor text for a link from the `Gas Heater Maintenance Guide` article (section: "Annual Burner Cleaning Process") to a specific section in the `Gas Heater Safety Pillar` (section: "Gas Leak Prevention and Detection"). Explain why a hash link is more appropriate than a plain page link here.

---

*Next: Module 11 — Google Spam Policies and Penalty Avoidance*
