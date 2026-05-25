# MODULE 6 — CMap (Category and Landing Page Architecture)
## All the Structural Pages a Site Needs Before Blog Content

> **Purpose of this module:** Before you write a single article, your website needs a skeleton. The CMap defines every structural page that must exist — category pages, landing pages, root pages, and pillar pages — along with their URLs, hierarchy, and purpose. These are not content pieces. They are the load-bearing walls of your site's architecture. Get them wrong and every article you build on top of them is sitting on an unstable foundation. Get them right and every article you publish strengthens the entire structure.

---

## LESSON 6.1 — What a CMap Is

### The Definition

A CMap (Category Map) is the complete inventory of all structural, non-article pages that a website requires. It is the architectural blueprint of the site — the pages that define what the site IS before any content explains what the site KNOWS.

A CMap contains:

- The **Ontology Root Page** — the single page that defines the central entity comprehensively
- **Category pages** — pages that organise content by entity type or attribute cluster
- **Pillar pages** — pages that cover one entity-attribute pair in depth
- **Landing pages** — pages designed to convert specific user intents (purchase, contact, location)
- **Structural pages** — pages that exist for navigation, trust, or legal requirements (About, Contact, Privacy Policy)

### What a CMap Is Not

The CMap does not contain:

- Blog articles (those go in the Topical Map, Module 7)
- Supporting articles (same — Topical Map)
- Individual product pages (listed separately — they follow the CMap structure but are generated from product inventory)
- Temporary campaign pages (outside the permanent architecture)

### Why the CMap Comes Before the Topical Map

Most agencies plan articles first and add structural pages later — or never. This is backwards.

Structural pages define the URL architecture, navigation, crawl path, and topical signal of the entire site. Every article that comes later is mapped to a structural page. Its URL inherits from the structural URL. Its crawl depth is determined by its position in the structural hierarchy.

If you build articles before the CMap, you will discover structural conflicts later:
- Articles at the wrong URL depth
- Category pages that conflict with existing article URLs
- Navigation labels that don't match any URL
- Pillar pages missing from the architecture, leaving clusters of articles with no parent

**Build the structure first. Then fill it with content.**

---

## LESSON 6.2 — The Five Page Types in a CMap

### Page Type 1 — Ontology Root Page

**What it is:** The single most comprehensive page on the site about the central entity. It defines what the entity is, covers all root attributes at a summary level, and links to every pillar page below it. It is the entry point Google uses to understand what the site is about.

**What it covers:** All root attributes — briefly. It does not go deep on any single attribute. Its purpose is breadth, not depth. It establishes the entity's complete identity in one place.

**URL pattern:** The category root — usually the seed level.
```
pakheaters.pk/heaters/
```

**Content characteristics:**
- Defines the entity (what is a heater?)
- Lists all types (hyponym overview)
- Covers all root attributes at summary level (wattage, safety, price, brands)
- Links to every pillar page beneath it
- Targets broad head queries: `heaters pakistan`, `home heater guide`

**Position in crawl path:** Closest to homepage after the homepage itself. Google discovers this page on the first or second crawl pass.

**Example — Heater retailer Pakistan:**
```
Page: Home Heater Guide — Types, Price, and Buying Advice for Pakistan
URL: pakheaters.pk/heaters/
Purpose: Ontology root for all heater content
Links to: All pillar pages (/heaters/gas-heater/, /heaters/electric-heater/, etc.)
```

---

### Page Type 2 — Category Pages

**What it is:** A page that groups a set of related pages under a parent label. Category pages serve two purposes simultaneously:
1. Navigation — they help users find the content cluster they need
2. Topical signal — they tell Google that all pages beneath this category share a semantic relationship

**What it covers:** The category at a summary level — enough to establish the macro context of the category and introduce the pages within it. Not a comprehensive guide (that is the pillar page's job).

**URL pattern:** Seed or mid-level nodes.
```
/heaters/gas-heaters/
/heaters/electric-heaters/
/heaters/heater-brands/
/heaters/heater-safety/
```

**Content characteristics:**
- Brief definition of what this category covers
- List of pages within the category with context-rich link text
- 1–3 key facts about this category (not an exhaustive guide)
- Internal links pointing upward (to ontology root) and downward (to pillar pages)

**The common mistake:** Leaving category pages as empty index pages with no content. An empty category page sends no topical signal. Every category page needs minimum 150–300 words of genuine content establishing its macro context.

---

### Page Type 3 — Pillar Pages

**What it is:** The deepest structural page — covering one entity + one root attribute comprehensively. Pillar pages are the expert authority pages for each major attribute of the central entity.

**What it covers:** Everything about one specific attribute. This is the page that ranks for the primary query cluster associated with that attribute. It covers all root values, all rare attribute variations, comparison tables, and links to supporting articles (which go in the Topical Map).

**URL pattern:** Node level under the relevant category.
```
/heaters/gas-heater-types/
/heaters/gas-heater-price/
/heaters/gas-heater-safety/
/heaters/gas-heater-wattage/
/heaters/best-gas-heater-brands/
```

**Content characteristics:**
- Full coverage of the attribute (all values, all comparisons, all sub-types)
- Numeric data and specific examples throughout
- Internal links: up to category page, across to sibling pillar pages, down to supporting articles
- Targets mid-tier queries: `gas heater types pakistan`, `gas heater price guide`

**Position in site hierarchy:**
```
Homepage
    └── Ontology Root Page (/heaters/)
            └── Category Page (/heaters/gas-heaters/)
                    └── Pillar Page (/heaters/gas-heater-types/)
                            └── [Supporting articles — Topical Map]
```

---

### Page Type 4 — Landing Pages

**What it is:** A page designed to convert a specific user intent. Landing pages in a CMap are permanent, evergreen pages — not campaign-specific. They serve users at the Transaction or commercial investigation stage of the query path.

**Four subtypes of landing pages:**

**A. Product/Service Landing Pages**
For e-commerce or service businesses — one page per product category or service type.
```
/heaters/buy-gas-heater/
/heaters/buy-electric-heater/
```

**B. Comparison Landing Pages**
Pages where users at the commercial investigation stage compare two options.
```
/heaters/gas-heater-vs-electric-heater/
/heaters/gree-vs-orient-heater/
```

**C. Location Landing Pages**
For businesses serving specific geographic areas. Each city or region gets a dedicated page.
```
/heaters/gas-heater-lahore/
/heaters/gas-heater-karachi/
/heaters/gas-heater-islamabad/
```

**D. Intent-Specific Landing Pages**
Pages that serve a specific transactional intent that doesn't fit product or location categories.
```
/heaters/cheapest-gas-heater-pakistan/
/heaters/gas-heater-online-delivery/
```

**Content characteristics for all landing pages:**
- Directly serves the conversion intent of the page
- Contains product listings, pricing tables, or service descriptions
- Minimal informational content — calls to action are dominant
- Internal links to relevant pillar pages and supporting articles for users who need more information before converting

---

### Page Type 5 — Structural/Trust Pages

**What it is:** Pages that exist for site legitimacy, legal compliance, and user trust — not for ranking specific queries. These pages are mandatory for E-E-A-T signalling.

**Required structural pages:**
```
/about-us/          → Brand identity, team, expertise signals, founding story
/contact/           → Physical address, phone, email, contact form (NAP consistency)
/privacy-policy/    → Legal compliance (required for Google's trust assessment)
/terms-of-service/  → Legal compliance
/sitemap/           → Navigation aid + crawl signal
```

**Optional but recommended:**
```
/author/[name]/     → Author bio pages (E-E-A-T authorship signals)
/reviews/           → Customer reviews (social proof + trust signal)
/warranty-policy/   → Post-purchase trust signal (relevant for product retailers)
/delivery-info/     → Transaction support (reduces friction at purchase stage)
```

**Why these matter for SEO:**
Google's Quality Rater Guidelines explicitly evaluate whether a site has identifiable authorship, a physical address, and transparent policies. Sites missing these pages receive lower E-E-A-T scores, which suppresses ranking even when content quality is high.

---

## LESSON 6.3 — How Source Context Determines Which CMap Pages Must Exist

Not every site needs the same CMap structure. The pages required depend directly on the Source Context defined in Module 1.

### Source Context → CMap Page Requirements

**E-commerce retailer (e.g. Pakistani heater retailer):**

Must have: Ontology root, category pages (by product type), pillar pages (by attribute: types, price, brands, safety), product landing pages (buy pages), location landing pages (city-specific), structural pages (About, Contact, Privacy, Delivery, Warranty).

Does not need: Service description pages, appointment booking pages.

**Service business (e.g. eye care clinic):**

Must have: Ontology root (/eye-care/), service category pages (/eye-care/exams/, /eye-care/treatments/), service landing pages (/eye-care/lasik/, /eye-care/eye-exam-booking/), location landing pages (/eye-care/sydney/, /eye-care/melbourne/), structural pages (About, Contact, Privacy, Booking confirmation).

Does not need: Product category pages, price list pages (unless service pricing is published).

**Information publisher (e.g. water brand with educational content):**

Must have: Ontology root (/water/), topic category pages (/water/hydration/, /water/water-quality/), pillar pages (/water/mineral-water-benefits/, /water/water-purification/), structural pages (About, Contact, Privacy).

Does not need: Location landing pages, product buy pages (if no e-commerce).

**Content + affiliate site (e.g. heater review site):**

Must have: Ontology root, category pages (by heater type, by brand), comparison landing pages, review pillar pages, structural pages.

Does not need: Direct purchase/buy landing pages (links out to retailers instead).

### The Source Context Filter

For every page you propose to add to the CMap, run it through this filter:

```
1. Does this page type match my monetisation model?
   (A retailer needs buy pages; a content site doesn't)

2. Does this page serve my defined audience at a documented stage of their query path?
   (Map it to one of the 7 journey stages from Module 1)

3. Does this page operate within my Source Context's contextual layer?
   (A Pakistani affordable heater retailer does not need a commercial HVAC page)

4. Does this page create a clear URL hierarchy that connects to existing structure?
   (No orphan pages — everything has a parent)

All four Yes = include in CMap.
Any No = exclude or revise.
```

---

## LESSON 6.4 — URL Architecture: Building the CMap URL Structure

The URL structure of the CMap defines the URL structure of the entire site. Every article in the Topical Map will inherit its URL path from the CMap hierarchy established here.

### The Three-Level URL System

```
Level 1: ROOT (domain only)
  pakheaters.pk/

Level 2: SEED (main entity category)
  pakheaters.pk/heaters/
  pakheaters.pk/about-us/
  pakheaters.pk/contact/

Level 3: NODE (specific entity or attribute)
  pakheaters.pk/heaters/gas-heater/
  pakheaters.pk/heaters/electric-heater/
  pakheaters.pk/heaters/heater-types/
  pakheaters.pk/heaters/heater-price/
  pakheaters.pk/heaters/heater-brands/

Level 4: DEEP NODE (specific attribute + context)
  pakheaters.pk/heaters/gas-heater/price/
  pakheaters.pk/heaters/gas-heater/types/
  pakheaters.pk/heaters/gas-heater/safety/
  pakheaters.pk/heaters/gas-heater/brands/
```

### URL Design Rules for CMap Pages

**Rule 1 — No term duplication across levels**

```
WRONG: /heaters/heater/gas-heater/gas-heater-price/
       "heater" appears three times across levels.

RIGHT: /heaters/gas-heater/price/
       Each level adds new information, never repeats.
```

**Rule 2 — Seed level = hypernym. Node level = hyponym.**

```
WRONG: /gas-heater/heaters/types/
       Hyponym (gas-heater) before hypernym (heaters) = illogical.

RIGHT: /heaters/gas-heater/types/
       Hypernym (heaters) → Hyponym (gas-heater) → Attribute (types)
```

**Rule 3 — Separate concerns at separate nodes**

```
WRONG: /heaters/gas-heater-types-and-prices/
       Two macro contexts (types + prices) combined in one URL.

RIGHT: /heaters/gas-heater/types/
       /heaters/gas-heater/price/
       Each macro context gets its own URL.
```

**Rule 4 — Category pages use plural. Specific pages use singular.**

```
Category (plural):  /heaters/ (covers all heaters)
Specific (singular): /heaters/gas-heater/ (covers one type)
Attribute (noun):   /heaters/gas-heater/price/ (covers one attribute)
```

**Rule 5 — Landing pages use intent-aligned slugs**

```
Buy intent:        /heaters/buy-gas-heater/
Location intent:   /heaters/gas-heater-lahore/
Comparison intent: /heaters/gas-heater-vs-electric-heater/
```

**Rule 6 — Structural pages stay at root level**

```
/about-us/
/contact/
/privacy-policy/
```
These do not sit inside the entity URL hierarchy. They are site-level pages, not entity-level pages.

### The URL Hierarchy Test

For every URL in the CMap, run this test:

```
1. Does each level of the URL add new, non-duplicated information?
2. Does the URL read as a logical hierarchy from broad to narrow?
3. Can a user infer the page's topic from the URL alone?
4. Is the URL as short as it can be while remaining unambiguous?
5. Does the URL's entity-attribute match the page's macro context?

All five Yes = good URL.
Any No = revise.
```

---

## LESSON 6.5 — Crawl Path Optimisation

### What Crawl Path Means

The crawl path is the sequence in which Google's crawler discovers and evaluates pages on your site. Pages closer to the homepage are crawled more frequently and assigned higher initial authority. Pages buried deep in the hierarchy are crawled less frequently and take longer to accumulate authority.

**The crawl path principle:** Your highest-quality, most important pages must be as close to the homepage as possible.

### Crawl Depth and Page Value

```
Depth 1: Homepage              → Crawled daily (or multiple times daily for large sites)
Depth 2: Direct homepage links → Crawled frequently (2–3 times per week)
Depth 3: Category pages        → Crawled regularly (weekly)
Depth 4: Pillar pages          → Crawled regularly (weekly to bi-weekly)
Depth 5: Supporting articles   → Crawled periodically (bi-weekly to monthly)
Depth 6+: Deep nodes           → Crawled infrequently (monthly or less)
```

Every additional level of depth reduces crawl frequency and authority accumulation speed.

### The CMap and Crawl Path Design

The CMap must be designed so that:

**Core section pages (pillar pages) are at maximum depth 4.**
If a pillar page is buried at depth 6 because of intermediate category levels that add no value, the pillar page will rank slowly.

**Structural pages are at depth 2 (directly linked from homepage).**
About, Contact, and Privacy pages must be in the footer or header — accessible from every page, one click from the homepage.

**Landing pages are at depth 3–4.**
Buy pages and comparison pages need to be reachable quickly. Deep-buried landing pages lose conversion opportunity.

### Navigation as Crawl Path Design

The site navigation is the primary crawl path signal. Every page in the navigation header is at crawl depth 2 — Google reaches it from the homepage on the first click.

**Navigation structure for a heater retailer:**

```
Main Navigation:
├── Gas Heaters      → /heaters/gas-heater/          (Depth 2 — pillar)
├── Electric Heaters → /heaters/electric-heater/     (Depth 2 — pillar)
├── Heater Brands    → /heaters/heater-brands/       (Depth 2 — category)
├── Heater Guide     → /heaters/                     (Depth 2 — ontology root)
└── Buy Heaters      → /heaters/buy-gas-heater/      (Depth 2 — landing)

Footer Navigation:
├── About Us         → /about-us/
├── Contact          → /contact/
├── Delivery         → /delivery-info/
└── Privacy Policy   → /privacy-policy/
```

Every page in the main navigation is at crawl depth 2. Core pillar pages and the ontology root are in the main navigation. The blog/article section (Topical Map content) is accessed from category pages at depth 3 — which means articles are at depth 4, not depth 5 or 6.

### Internal Links as Crawl Path Amplifiers

Every internal link from a high-crawl-frequency page to a lower-crawl-frequency page accelerates discovery of the linked page. This is why:

- The ontology root page (depth 2) links to all pillar pages (moves them from depth 3 to effectively depth 2.5)
- Pillar pages link to their supporting articles (moves articles from depth 5 to effectively depth 3.5)
- Outer section articles link to Core section pillar pages (reinforces crawl priority of Core pages)

---

## LESSON 6.6 — Boilerplate Content on CMap Pages

Each structural page type has specific boilerplate requirements. Boilerplate is not an afterthought — it is a topical signal that Google reads on every single page it crawls.

### Ontology Root Page Boilerplate

**What must appear:**
- H1 containing Central Entity + primary attribute n-grams
- Opening paragraph: definition of entity + source context statement (what this site covers and for whom)
- Navigation links to all sub-categories (with descriptive anchor text, not generic "click here")
- Footer: full site boilerplate (entity + source context + geographic signal)

**What must not appear:**
- Promotional language in the informational opening
- Unrelated entity mentions
- Generic e-commerce banners that dilute the topical focus

### Category Page Boilerplate

**What must appear:**
- H1 containing the category's hypernym + context modifier (e.g. "Gas Heaters in Pakistan")
- 150–300 words defining the category and what this section covers
- A table or list of all pages within the category (descriptive titles + 1-sentence descriptions)
- Breadcrumb: Homepage > Heaters > Gas Heaters
- Footer: site boilerplate

### Pillar Page Boilerplate

**What must appear:**
- H1: entity + attribute + context (the full title formula from Module 3)
- Breadcrumb: full path from root to this page
- Table of contents (for long pillar pages) with anchor links
- "Related guides" sidebar or section (links to sibling pillar pages)
- Author byline with expertise indicator
- Last updated date (freshness signal)
- Footer: site boilerplate

### Landing Page Boilerplate

**What must appear:**
- H1: intent-aligned (e.g. "Buy Gas Heater Online in Pakistan — Fast Delivery")
- Trust signals: delivery information, return policy, payment methods
- Contact or support information (reduces purchase anxiety)
- Footer: full site boilerplate including physical address (NAP)

**What must not appear:**
- Long informational content (this is a conversion page, not a guide)
- External links to competitors
- Navigation that takes users away from the conversion path

---

## LESSON 6.7 — Building the CMap Document

### CMap Document Structure

The CMap document is a structured spreadsheet or table. It has one row per page and the following columns:

```
Column A  — Page ID (sequential number for reference)
Column B  — Page Type (Ontology Root / Category / Pillar / Landing / Structural)
Column C  — Page Name (descriptive name for internal use)
Column D  — URL (full URL path)
Column E  — H1 (the exact H1 for this page)
Column F  — Meta Description (150–160 characters)
Column G  — Parent Page URL (which page is one level above in hierarchy)
Column H  — Child Pages (URLs of pages directly below this one)
Column I  — Primary Target Keyword(s)
Column J  — Search Intent (Informational / Commercial / Transactional)
Column K  — User Journey Stage (Awareness / Evaluation / Transaction / etc.)
Column L  — CMap Section (Core / Outer / Structural)
Column M  — Navigation Placement (Main nav / Footer / None)
Column N  — Crawl Depth (1 / 2 / 3 / 4 / 5)
Column O  — Priority (High / Medium / Low — determines build order)
Column P  — Status (Planned / In Progress / Live)
Column Q  — Notes
```

### Build Order for CMap Pages

Pages are built in strict priority order. Never publish articles before the structural framework is in place.

```
PRIORITY 1 — Build immediately (before any content):
[ ] Homepage (if new site)
[ ] About Us
[ ] Contact (with physical address)
[ ] Privacy Policy
[ ] Sitemap

PRIORITY 2 — Build before first article:
[ ] Ontology Root Page
[ ] Main navigation category pages
[ ] At least one pillar page per core attribute (minimum 3)

PRIORITY 3 — Build alongside first content wave:
[ ] Remaining category pages
[ ] All pillar pages
[ ] Primary landing pages (buy/compare)

PRIORITY 4 — Build as content matures:
[ ] Location landing pages
[ ] Secondary comparison pages
[ ] Author bio pages
```

---

## LESSON 6.8 — Completed CMap Example

**Site:** PakHeaters.pk — affordable home heater retailer, Pakistan

```
CMap — PakHeaters.pk
=====================================================================

STRUCTURAL PAGES (Priority 1)
=====================================================================

ID: S-01
Type: Structural
Name: Homepage
URL: pakheaters.pk/
H1: Pakistan's Most Affordable Gas and Electric Heaters —
    Buy Online with Fast Delivery
Intent: Mixed (brand + category awareness)
Stage: Awareness
Nav: Not in nav (IS the nav root)
Depth: 1
Priority: HIGH

ID: S-02
Type: Structural
Name: About Us
URL: pakheaters.pk/about-us/
H1: About PakHeaters.pk — Pakistan's Dedicated Home Heater Store
Intent: Navigational / Trust
Nav: Footer
Depth: 2
Priority: HIGH

ID: S-03
Type: Structural
Name: Contact
URL: pakheaters.pk/contact/
H1: Contact PakHeaters.pk — Lahore Showroom + Online Support
Intent: Navigational
Nav: Footer
Depth: 2
Priority: HIGH

ID: S-04
Type: Structural
Name: Privacy Policy
URL: pakheaters.pk/privacy-policy/
Nav: Footer
Depth: 2
Priority: HIGH

=====================================================================

ONTOLOGY ROOT PAGE (Priority 2)
=====================================================================

ID: C-01
Type: Ontology Root
Name: Home Heater Guide — Master Category
URL: pakheaters.pk/heaters/
H1: Home Heaters in Pakistan — Types, Prices, Brands, and Buying Guide 2025
Meta: "Find the right home heater for your room size and budget.
      Complete guide to gas heaters, electric heaters, prices in Pakistan,
      and top brands — Gree, Orient, Dawlance."
Target KWs: heaters pakistan, home heater guide, best heater pakistan
Intent: Informational (category-level)
Stage: Awareness
Parent: Homepage
Children: All category pages
Nav: Main nav ("Heater Guide")
Depth: 2
Priority: HIGH

=====================================================================

CATEGORY PAGES (Priority 2–3)
=====================================================================

ID: C-02
Type: Category
Name: Gas Heaters Category
URL: pakheaters.pk/heaters/gas-heater/
H1: Gas Heaters in Pakistan — Complete Guide and Price List
Meta: "Everything about gas heaters in Pakistan: types, wattage,
      safety, top brands like Gree and Orient, and 2025 prices."
Target KWs: gas heater pakistan, gas heaters
Intent: Informational / Commercial
Stage: Education → Evaluation
Parent: /heaters/
Children: All gas heater pillar pages
Nav: Main nav ("Gas Heaters")
Depth: 3
Priority: HIGH

ID: C-03
Type: Category
Name: Electric Heaters Category
URL: pakheaters.pk/heaters/electric-heater/
H1: Electric Heaters in Pakistan — Types, Wattage, and Price Guide
Parent: /heaters/
Nav: Main nav ("Electric Heaters")
Depth: 3
Priority: HIGH

ID: C-04
Type: Category
Name: Heater Brands Category
URL: pakheaters.pk/heaters/heater-brands/
H1: Best Heater Brands in Pakistan — Gree, Orient, Dawlance Compared
Parent: /heaters/
Nav: Main nav ("Heater Brands")
Depth: 3
Priority: HIGH

=====================================================================

PILLAR PAGES (Priority 2–3)
=====================================================================

ID: P-01
Type: Pillar
Name: Gas Heater Types Pillar
URL: pakheaters.pk/heaters/gas-heater/types/
H1: Gas Heater Types in Pakistan — Convection, Radiant, and Infrared Explained
Meta: "Compare the 3 main types of gas heaters in Pakistan: convection,
      radiant, and infrared. Includes wattage, room size, and price range."
Target KWs: gas heater types pakistan, types of gas heaters, which type
           of gas heater is best
Intent: Informational
Stage: Education
Parent: /heaters/gas-heater/
Children: [Supporting articles from Topical Map — to be assigned]
Nav: None (accessed from category page)
Depth: 4
Priority: HIGH

ID: P-02
Type: Pillar
Name: Gas Heater Price Pillar
URL: pakheaters.pk/heaters/gas-heater/price/
H1: Gas Heater Price in Pakistan — 2025 Brand-wise Price List
Meta: "Current gas heater prices in Pakistan for Gree, Orient, Dawlance,
      and Super Asia. Budget (PKR 8,500+) to premium (PKR 45,000+) range."
Target KWs: gas heater price pakistan, gas heater price list, gas heater
           cost pakistan
Intent: Commercial
Stage: Evaluation
Parent: /heaters/gas-heater/
Depth: 4
Priority: HIGH

ID: P-03
Type: Pillar
Name: Gas Heater Wattage Pillar
URL: pakheaters.pk/heaters/gas-heater/wattage/
H1: Gas Heater Wattage Guide — Which Size Heater for Which Room?
Target KWs: gas heater wattage, heater room size pakistan,
           what wattage heater for room
Intent: Informational
Stage: Education
Parent: /heaters/gas-heater/
Depth: 4
Priority: HIGH

ID: P-04
Type: Pillar
Name: Gas Heater Safety Pillar
URL: pakheaters.pk/heaters/gas-heater/safety/
H1: Gas Heater Safety Guide — Indoor Use, Carbon Monoxide, and
    Ventilation in Pakistan
Target KWs: gas heater safety, is gas heater safe indoors,
           gas heater carbon monoxide
Intent: Informational
Stage: Education
Parent: /heaters/gas-heater/
Depth: 4
Priority: HIGH

ID: P-05
Type: Pillar
Name: Best Gas Heater Brands Pillar
URL: pakheaters.pk/heaters/heater-brands/gas-heater-brands/
H1: Best Gas Heater Brands in Pakistan — Gree vs Orient vs Dawlance Review
Target KWs: best gas heater brand pakistan, gree vs orient heater,
           gas heater brands pakistan
Intent: Commercial
Stage: Comparison
Parent: /heaters/heater-brands/
Depth: 4
Priority: HIGH

=====================================================================

LANDING PAGES (Priority 3)
=====================================================================

ID: L-01
Type: Landing — Purchase
Name: Buy Gas Heater Online
URL: pakheaters.pk/heaters/buy-gas-heater/
H1: Buy Gas Heater Online in Pakistan — Same-day Dispatch Lahore, Karachi
Meta: "Order gas heaters online in Pakistan. Gree, Orient, Dawlance —
      lowest price guaranteed. Fast delivery Lahore, Karachi, Islamabad."
Intent: Transactional
Stage: Transaction
Parent: /heaters/gas-heater/
Nav: Main nav ("Buy Heaters")
Depth: 4
Priority: HIGH

ID: L-02
Type: Landing — Comparison
Name: Gas Heater vs Electric Heater
URL: pakheaters.pk/heaters/gas-heater-vs-electric-heater/
H1: Gas Heater vs Electric Heater in Pakistan — Which is Better for Your Home?
Target KWs: gas heater vs electric heater pakistan, gas or electric heater
Intent: Commercial
Stage: Comparison
Parent: /heaters/
Depth: 3
Priority: HIGH

ID: L-03
Type: Landing — Location
Name: Gas Heater Lahore
URL: pakheaters.pk/heaters/gas-heater-lahore/
H1: Gas Heater Price in Lahore — Buy Online with Same-day Delivery
Intent: Transactional + Local
Stage: Transaction
Parent: /heaters/
Depth: 3
Priority: MEDIUM

ID: L-04
Type: Landing — Location
Name: Gas Heater Karachi
URL: pakheaters.pk/heaters/gas-heater-karachi/
[Same structure as L-03 for Karachi]
Depth: 3
Priority: MEDIUM

=====================================================================

COMPLETE CMap SUMMARY
=====================================================================

Total CMap pages: 18
  Structural pages: 4
  Ontology root: 1
  Category pages: 3
  Pillar pages: 5+
  Landing pages: 5+

URL depth distribution:
  Depth 1: 1 (Homepage)
  Depth 2: 4 (Structural + Ontology Root)
  Depth 3: 4 (Category + Comparison/Location landing pages)
  Depth 4: 9+ (Pillar pages + Buy landing pages)

Core section coverage: Types ✓ | Price ✓ | Wattage ✓ | Safety ✓ | Brands ✓
All core attributes covered at pillar level before Topical Map begins.
```

---

## MODULE 6 — SUMMARY

The CMap defines the skeleton of your website before a single article is written. It answers four questions simultaneously:

**What pages must exist?** The five page types — ontology root, category, pillar, landing, and structural — each serve a distinct function that cannot be replaced by another type.

**What URL should each page have?** The three-level URL system (root/seed/node) with no duplication, hypernym-to-hyponym logic, and intent-aligned slugs for landing pages.

**How deep should each page sit?** Crawl path optimisation ensures that core pillar pages are at maximum depth 4 and structural trust pages are at depth 2. Navigation design is the primary tool for controlling crawl depth.

**In what order should pages be built?** Structural pages first. Ontology root and navigation categories second. Pillar pages third. Landing pages fourth. Articles (Topical Map) only after all of the above are live.

Without the CMap, the Topical Map is a list of articles with no home. With the CMap, every article has a clear parent, a clear URL, and a clear crawl path.

---

## MODULE 6 — KEY TERMS GLOSSARY

| Term | Definition |
|---|---|
| **CMap** | Category Map — the complete inventory of all structural, non-article pages a website requires. |
| **Ontology Root Page** | The single most comprehensive page on the site about the central entity — broad coverage of all root attributes, linking to all pillar pages beneath it. |
| **Category page** | A page that groups related pages under a parent label, serving navigation and topical signal functions simultaneously. |
| **Pillar page** | The deepest structural page, covering one entity + one root attribute comprehensively. The expert authority page for a single attribute. |
| **Landing page** | A structural page designed to convert a specific user intent — purchase, comparison, or location-specific queries. |
| **Structural page** | A site-level page existing for trust, legal compliance, or navigation (About, Contact, Privacy Policy). |
| **Crawl depth** | The number of clicks from the homepage required to reach a page. Lower depth = higher crawl frequency = faster authority accumulation. |
| **Crawl path** | The sequence in which Google's crawler discovers pages on a site, determined by link structure and navigation. |
| **NAP** | Name, Address, Phone — the three contact details that must appear consistently across the site for local E-E-A-T signalling. |
| **Build order** | The mandatory sequence of page creation: structural → ontology root → categories → pillar pages → landing pages → articles. |

---

## MODULE 6 — SELF-ASSESSMENT QUESTIONS

1. A new baby food retailer in Pakistan asks you to start writing blog articles immediately. They have no About page, no category structure, and no pillar pages. Using the build order framework, explain exactly what must happen before the first article is published and why.

2. A heater site's current URL structure is `/blog/gas-heater-types/` and `/blog/gas-heater-prices/`. What are the two structural problems with these URLs? Redesign them using the CMap URL architecture.

3. Explain why a category page that contains only a list of links (no descriptive content) is an SEO liability. What minimum content must it contain and why?

4. A pillar page about `gas heater safety` is buried at depth 6 in the site hierarchy. The URL is `/heaters/gas-heaters/indoor-heaters/portable-heaters/safety-guides/gas-heater-safety/`. What are the crawl path consequences? How would you restructure this in the CMap?

5. An eye care clinic's CMap includes a page at `/eye-care/industrial-eye-safety/`. Their Source Context is a consumer optometry clinic serving everyday Australians. Apply the source context filter: should this page be in the CMap? Justify with all four filter questions.

6. A comparison landing page is being proposed at `/heaters/gas-heater-vs-oil-heater-vs-electric-heater-vs-infrared-heater/`. What is wrong with this URL from the CMap URL design rules perspective? Redesign it correctly and explain what happens to the content that doesn't fit the URL.

7. Write the complete boilerplate requirements (H1, meta description, breadcrumb, navigation, footer) for a pillar page covering `gas heater wattage` for a Pakistani heater retailer. Every element must follow the rules from this module.

---

*Next: Module 7 — Topical Map Construction*
