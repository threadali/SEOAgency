# MODULE 2 — Keyword Research for Topical Authority
## Not Finding Keywords — Mapping Query Territory

> **Purpose of this module:** Traditional keyword research finds a list of phrases to target. Semantic keyword research maps an entire territory of query relationships — paths, clusters, intent stages, and contextual layers — then allocates each piece of that territory to the correct page. By the end of this module, you produce a master keyword spreadsheet that is the raw material for every topical map and content brief that follows.

---

## LESSON 2.1 — The Problem With Traditional Keyword Research

### What Most People Do

Most agencies run a keyword tool, sort by volume, pick the highest-volume keywords, and start writing articles. This produces a list of targets with no structural relationship to each other.

The result: a website with 30 articles that are semantically disconnected — each competing in a different SERP, sending mixed topicality signals, building authority on nothing in particular.

### What Semantic Keyword Research Does Instead

Semantic keyword research treats keywords as **evidence of user intent at different stages of a query journey**. The goal is not to collect keywords. The goal is to map the complete territory of queries that surround your Central Entity — then determine which page on your site should serve each zone of that territory.

**The output is not a keyword list. It is a query map.**

A query map shows:
- Every query path a user can take through your topic
- Which queries belong together on one page
- Which queries require their own dedicated page
- Which queries signal a stage of the user journey
- Which queries are cannibalising each other on your current site

### The Core Principle

**Different intent = different page.**
**Same intent, different phrasing = same page.**

This single rule governs every grouping decision in keyword research. Violate it and you either fragment your authority (too many pages for same intent) or dilute your relevance (too many topics on one page).

---

## LESSON 2.2 — Seed Entity Extraction

### Starting Point: The Entity, Not the Keyword

Every keyword research process in semantic SEO begins with the Central Entity defined in your Website Identity Document — not with a keyword tool.

The seed entity is the single word or short phrase that names your Central Entity. Everything else in keyword research grows from this seed.

```
Central Entity → Seed Entity → Query Paths → Intent Clusters → Keyword Groups → Page Allocations
```

**Examples:**

| Website Type | Central Entity | Seed Entity |
|---|---|---|
| Heater retailer (Pakistan) | Heater | `heater` |
| Eye care clinic (Australia) | Eye Care | `eye care` |
| Water brand | Mineral Water | `mineral water` |
| SEO agency | SEO | `semantic seo` |
| Baby food retailer | Baby Food | `baby food` |

### Why One Seed Entity Matters

Starting from one seed entity forces every keyword you research to connect back to that entity. This prevents scope creep — the gradual expansion into unrelated topics that dilutes Source Context.

As you research, you will find keywords that look attractive but don't trace back to your seed entity. These go into a separate "future entity" list — they are not part of this topical map.

---

## LESSON 2.3 — The Five Keyword Extraction Sources

You do not use one tool. You use five sources systematically, and then combine and deduplicate the output.

### Source 1 — Google Autocomplete

**What it gives you:** Real queries that users type, including the most common refinements and modifiers.

**How to use it:**
Type your seed entity into Google Search and do not press Enter. Record every suggestion. Then add one letter at a time after the seed entity and record suggestions again.

```
heater [space]           → heater price, heater wattage, heater types...
heater p                 → heater price Pakistan, heater price in Lahore...
heater w                 → heater wattage, heater with thermostat...
heater f                 → heater for room, heater for small room...
heater b                 → heater brands, heater brands in Pakistan...
```

Also use prefix modifiers:

```
best heater...
cheap heater...
how to [heater]...
what is [heater]...
which heater...
```

**What to record:** Every suggestion, verbatim, into your spreadsheet with column: `Source = Autocomplete`.

### Source 2 — Google People Also Ask (PAA)

**What it gives you:** Questions users ask in relation to your seed entity. These are high-value because Google has already classified them as semantically related — they are candidates for FAQ sections, H3 headings, and PAA-targeted answer formats.

**How to use it:**
Search your seed entity. Scroll to the PAA box. Click on every question to expand it — expanding one question triggers new related questions to appear. Repeat until you have exhausted the visible question set.

**Important:** PAA questions reveal the user's informational anxieties and the specific attributes they care about most. A PAA question about `gas heater safety indoors` tells you that user anxiety about indoor gas safety is real and common — it belongs in your content.

**What to record:** Every question, verbatim. Column: `Source = PAA`.

### Source 3 — Google Related Searches

**What it gives you:** Semantically related queries that share the same or adjacent user intent. These are the queries users search immediately after searching your seed entity — strong candidates for sequential query clusters.

**How to use it:**
Search your seed entity. Scroll to the bottom of the SERP. Record all 8 related searches. Then search each related search and record its related searches. Go 2–3 levels deep.

**What to record:** All related searches at each level. Column: `Source = Related Searches`.

### Source 4 — Competitor URL Analysis

**What it gives you:** Topics that are already generating traffic in your niche — proven by the fact that competitors are ranking for them.

**How to use it:**
Identify the top 5–10 competitors in your niche. Do not copy them — analyse them.

Steps:
1. Pull each competitor's sitemap (usually at `domain.com/sitemap.xml`)
2. List every URL slug that relates to your Central Entity
3. Extract the topic from each URL slug
4. Record it as a keyword candidate

**What you are finding:** Topics your competitors thought worth covering — giving you a baseline of what the query territory looks like from the SERP's perspective.

**Important distinction:** You are not copying their topical map. You are identifying the territory they have mapped, so you can map it more completely, more accurately, and with greater depth.

**What to record:** URL slug + inferred topic. Column: `Source = Competitor URLs`.

### Source 5 — Keyword Research Tools

**What it gives you:** Volume data, keyword difficulty, additional long-tail variations, and SERP feature data (who ranks, what features appear).

**Tools to use:**
- Google Search Console (your own site — existing query performance)
- Google Keyword Planner (volume estimates)
- Ahrefs / SEMrush / Ubersuggest (volume + difficulty + related KWs)
- Answer the Public (question-format keyword mapping)

**How to use tools correctly in semantic SEO:**

Tools are for **validating and enriching** your keyword map — not for building it from scratch. You already have most of your keywords from Sources 1–4. Tools add:
- Monthly search volume estimates (priority signal)
- Keyword difficulty (competitive effort required)
- Click-through rate estimates
- Additional long-tail variations you missed

**What to record:** Keyword + volume + difficulty + SERP feature notes. Column: `Source = Tool`.

---

## LESSON 2.4 — Query Path Mapping

### What is a Query Path?

A query path is the sequence of searches a single user performs as they move from initial awareness to final action. Each step in the path is a **refinement** — the user gets more specific as their intent clarifies.

Understanding query paths is what separates a keyword list from a topical map. A keyword list gives you 200 isolated phrases. A query path map shows you the journey those phrases represent.

### The Anatomy of a Query Path

Every query path has the same structure:

```
STAGE 1 — Awareness (Head query)
    ↓
STAGE 2 — Category Exploration (What types exist?)
    ↓
STAGE 3 — Attribute Investigation (What features matter?)
    ↓
STAGE 4 — Comparison (Which option is best for me?)
    ↓
STAGE 5 — Validation (Is this specific choice correct?)
    ↓
STAGE 6 — Transaction (Where do I buy / how do I get it?)
    ↓
STAGE 7 — Post-action (How do I use / maintain / troubleshoot it?)
```

### Full Query Path Example — Heater

```
STAGE 1  heater                                         (Awareness)
         ↓
STAGE 2  types of heaters for home                      (Category exploration)
         heater types Pakistan
         ↓
STAGE 3  gas heater wattage                             (Attribute investigation)
         heater electricity consumption
         heater room size
         heater safety features
         ↓
STAGE 4  gas heater vs electric heater                  (Comparison)
         oil filled heater vs fan heater
         best heater brand Pakistan
         ↓
STAGE 5  Gree gas heater review                         (Validation)
         Orient heater review Pakistan
         Gree GH-1800 specifications
         ↓
STAGE 6  buy gas heater online Pakistan                 (Transaction)
         gas heater price Lahore
         heater delivery Pakistan
         ↓
STAGE 7  how to maintain gas heater                     (Post-purchase)
         gas heater not heating properly
         heater cleaning guide
```

### How to Build Your Query Path Map

**Step 1:** Place your seed entity at Stage 1.

**Step 2:** For each stage, ask: *"What would a user search next, as they get more specific about this entity?"*

**Step 3:** Populate each stage with keywords from your five extraction sources.

**Step 4:** Identify which keywords naturally cluster at the same stage — these are candidates for the same page or the same section of a page.

**Step 5:** Identify where the path branches — where different user types diverge into different sub-paths.

**Branching example for heaters:**
At Stage 3 (Attribute Investigation), the path branches:
- Price-sensitive users → `heater price Pakistan`, `cheap heater under 5000`
- Technical users → `heater wattage calculation`, `BTU for room size`
- Safety-conscious users → `gas heater safety indoors`, `carbon monoxide heater risk`

Each branch represents a distinct user group within your Central Search Intent. Your content must serve all branches — not just the highest-volume one.

### One Query Path Per Niche Is Not Enough

A product with multiple user types, use cases, or variants will have multiple parallel query paths. Map them all.

**Gas heater — two parallel paths:**

```
PATH A — Residential buyer
heater → home heater types → gas heater for room → gas heater price Pakistan → buy gas heater

PATH B — Technical/specification-focused user
heater → heater wattage → gas heater BTU calculation → gas heater vs electric efficiency → gas heater energy cost Pakistan
```

Both paths exist simultaneously. Both deserve coverage. A topical map that only follows Path A misses all the users travelling Path B.

---

## LESSON 2.5 — Intent Classification

### The Four Primary Intent Types

Every keyword maps to one of four intent categories. The intent category determines what type of page must serve it.

**1. Informational Intent**
The user wants to learn something. They have a question, a knowledge gap, or a problem to understand.

Signals: `how`, `what`, `why`, `when`, `guide`, `explained`, `meaning of`, `types of`

Examples:
- `how does a gas heater work`
- `what wattage heater for small room`
- `types of heaters for home`
- `why is my heater not heating`

Page type: Blog article, guide, explainer, FAQ page

**2. Navigational Intent**
The user wants to reach a specific website, brand, or resource.

Signals: Brand name + website, `login`, `official site`, `download`

Examples:
- `Gree Pakistan official website`
- `Orient Electronics heater`
- `PakHeaters.pk`

Page type: Brand page, homepage — navigational queries are NOT content opportunities unless you are the brand being searched.

**3. Commercial Investigation Intent**
The user is evaluating options before making a decision. They are comparing, reviewing, listing.

Signals: `best`, `vs`, `review`, `comparison`, `top`, `which is better`, `worth buying`

Examples:
- `best gas heater Pakistan 2025`
- `gas heater vs electric heater`
- `Gree vs Orient heater`
- `oil filled heater worth buying`

Page type: Comparison article, review, buying guide, top-X list

**4. Transactional Intent**
The user is ready to act — buy, download, sign up, contact.

Signals: `buy`, `price`, `order`, `cheap`, `discount`, `where to buy`, `online`

Examples:
- `buy gas heater online Pakistan`
- `gas heater price Lahore`
- `heater delivery same day Karachi`

Page type: Product page, category page, landing page

### Sub-Intent Classification

Within each primary intent, sub-intents further specify the type of content needed.

**Informational sub-intents:**

| Sub-Intent | Signal | Example |
|---|---|---|
| Definition | `what is`, `meaning of` | `what is a gas heater` |
| Process | `how to`, `steps to` | `how to install a gas heater` |
| Reason | `why`, `reason for` | `why is my heater not working` |
| Comparison | `difference between` | `difference between gas and electric heater` |
| List | `types of`, `kinds of` | `types of heaters available in Pakistan` |
| Troubleshooting | `not working`, `problem`, `fix` | `gas heater flame keeps going out` |

**Commercial sub-intents:**

| Sub-Intent | Signal | Example |
|---|---|---|
| Ranking | `best`, `top` | `best gas heater Pakistan` |
| Versus | `vs`, `or`, `compared to` | `gas heater vs electric heater` |
| Review | `review`, `worth it` | `Gree gas heater review` |
| Feature-based | `[attribute] heater` | `heater with thermostat` |

### Intent Classification at Scale

When processing hundreds of keywords, classify them systematically:

**Step 1:** Look at the SERP for the keyword. The SERP format Google chooses reveals the intent classification.
- Article list → Informational
- Product pages → Transactional
- Review sites → Commercial Investigation
- Official brand sites → Navigational

**Step 2:** Check the modifier words in the keyword.
- Question words (`how`, `what`, `why`) = Informational
- Action words (`buy`, `order`, `get`) = Transactional
- Evaluation words (`best`, `vs`, `review`) = Commercial

**Step 3:** When in doubt — search it. What Google returns is the definitive answer about intent.

---

## LESSON 2.6 — TF-IDF Analysis: The Vocabulary of a Ranking Document

### What TF-IDF Actually Measures

TF-IDF stands for **Term Frequency × Inverse Document Frequency**.

In practice, for content strategy, it answers one question:

> *"Which terms appear consistently across top-ranking pages for this query, but are rare enough to be meaningfully associated with this topic specifically?"*

A term like "the" scores low — it appears everywhere on the web (low IDF). A term like `gas heater wattage calculation` scores high — it appears frequently in heater content specifically (high TF in relevant documents) but rarely outside that topic (high IDF).

**TF-IDF is a measure of statistical relevance, not of keyword importance.**

### Why TF-IDF Matters for Completeness

When Google evaluates your article about gas heaters, it runs an implicit TF-IDF check: does this document contain the vocabulary that expert gas heater content always contains?

If your article about gas heaters does not include terms like `BTU`, `wattage`, `room size`, `thermostat`, `oxygen depletion sensor`, `fuel consumption`, and `heat distribution` — Google's evaluation is: **this document is incomplete**. Not because it's short. Because it lacks the vocabulary that defines expert coverage of this entity.

**TF-IDF gives you the minimum vocabulary floor of a ranking document.**

### How to Conduct a Manual TF-IDF Analysis

**Step 1 — Pull the top 10 ranking pages**
Search your target keyword. Copy the URLs of the top 10 organic results (exclude ads, featured snippets from sites already in the 10, and Wikipedia unless it's directly relevant).

**Step 2 — Extract common phrases from each page**
For each page, identify:
- Repeated noun phrases (these are entity attribute signals)
- Consistent supporting terms (these are co-occurring vocabulary)
- Question formats used as headings (these signal what Google expects the article to answer)
- Table headers and list items (these signal the attributes Google expects covered)

**Step 3 — Find terms that appear in 7 or more of the 10 pages**
Any term appearing in 70%+ of top-ranking pages is statistically expected. Your document must include it.

**Step 4 — Build your TF-IDF Required Terms list**
This list goes directly into the content brief as mandatory vocabulary. Writers who omit these terms produce incomplete documents regardless of word count.

### TF-IDF Example — `gas heater types Pakistan`

After analysing 10 top-ranking pages, the TF-IDF required terms extracted:

```
ENTITY TERMS (appear in 9–10 pages):
- gas heater, natural gas, LPG (liquefied petroleum gas)
- wattage, BTU (British Thermal Unit)
- room size, coverage area, square feet
- thermostat, temperature control
- flame, burner, heat distribution

ATTRIBUTE TERMS (appear in 7–8 pages):
- oxygen depletion sensor (ODS)
- tip-over protection, safety shut-off
- infrared, radiant heat, convection
- fuel efficiency, gas consumption
- installation, ventilation, flue

MARKET TERMS (appear in 7–9 pages):
- Gree, Orient, Dawlance, Super Asia (Pakistani brands)
- price in Pakistan, PKR
- winter, seasonal, heating season

QUESTION PATTERNS (appear as headings in 6+ pages):
- which type of gas heater is best for home?
- how much gas does a heater consume?
- is gas heater safe to use indoors?
- what size heater do I need for my room?
```

Every term in this list is mandatory in the article. Their absence is a ranking disadvantage.

### TF-IDF is the Floor, Not the Ceiling

Meeting TF-IDF requirements makes your document as complete as your competitors. It does not make it better.

**Information gain** — the unique, accurate, specific data your document contains that competitors do not — is what makes your document better. Module 4 covers entity research and information gain in depth. TF-IDF is the prerequisite.

---

## LESSON 2.7 — Keyword Grouping: One Intent, One Page

### The Grouping Principle

Keyword grouping is the process of allocating keywords from your master list to specific pages. Each group represents one page.

**The grouping rule:**
- Keywords with the **same intent** + **same entity-attribute focus** → same page
- Keywords with **different intent** → different page
- Keywords with **same intent** but **different entity-attribute focus** → different page

### The Three Grouping Tests

For any two keywords, run these three tests to determine if they belong on the same page:

**Test 1 — Intent Test**
Do both keywords have the same primary intent (Informational / Commercial / Transactional)?
- Yes → Pass. Continue to Test 2.
- No → Fail. Different pages.

**Test 2 — Entity-Attribute Test**
Do both keywords refer to the same entity-attribute pair?
- `gas heater price` and `gas heater cost` → Same entity (gas heater) + same attribute (price) → Same page
- `gas heater price` and `gas heater wattage` → Same entity but different attributes → Different pages
- Yes → Pass. Continue to Test 3.
- No → Fail. Different pages.

**Test 3 — SERP Overlap Test**
Search both keywords. Do the same pages appear in the top 5 results for both?
- 3 or more overlapping URLs → Google treats these as the same query cluster → Same page
- 0–2 overlapping URLs → Google treats these as distinct → Different pages

All three tests pass → same page.
Any one test fails → different pages.

### Keyword Grouping in Practice — Heater Examples

**Group 1 (same page):**
- `gas heater price Pakistan`
- `gas heater cost Pakistan`
- `gas heater price list Pakistan`
- `how much does a gas heater cost in Pakistan`

Rationale: All four share Informational/Commercial intent, same entity (gas heater), same attribute (price), same context (Pakistan). SERP test: all four return identical top-5 results.

→ One article: "Gas Heater Price in Pakistan — Complete 2025 Price List"

**Group 2 (same page):**
- `gas heater vs electric heater`
- `gas heater or electric heater which is better`
- `difference between gas and electric heater`
- `gas vs electric heater Pakistan`

Rationale: All four share Commercial Investigation intent (comparison), same entity pair (gas heater / electric heater). SERP overlap is high.

→ One article: "Gas Heater vs Electric Heater: Which is Better for Pakistani Homes?"

**Group 3 (different pages — do not combine):**
- `gas heater types` → Different attribute (types) → separate page
- `gas heater wattage` → Different attribute (wattage) → separate page
- `gas heater maintenance` → Different intent (post-purchase informational) → separate page
- `buy gas heater online Pakistan` → Different intent (transactional) → product/category page

### The Most Common Grouping Mistakes

**Mistake 1 — Grouping by keyword similarity instead of intent**
`heater guide` and `heater review` both contain "heater" but have different intents. They are not the same group.

**Mistake 2 — Creating a page for every keyword variation**
`gas heater price Lahore` and `gas heater price Karachi` have different geographic modifiers — but if the SERP test shows the same pages ranking for both, they belong on one page that covers both cities.

**Mistake 3 — Putting all informational keywords on one "mega guide"**
`heater types`, `heater wattage`, `heater maintenance`, and `heater safety` are all informational — but they are four different entity-attribute pairs. They require four different pages (or at minimum, four distinct macro context sections if combining).

---

## LESSON 2.8 — Keyword Cannibalism: Detection and Prevention

### What is Keyword Cannibalism?

Keyword cannibalism occurs when multiple pages on your site compete for the same query. Google cannot determine which page is the most relevant answer, so it ranks both poorly instead of ranking one strongly.

**Cannibalism is not just a ranking problem. Under Google's 2024 spam policies, publishing multiple articles for the same keyword to manipulate rankings is a soft spam signal.**

### How Cannibalism Happens

1. **Fragmented query path coverage** — writing one article for `gas heater types` and another for `types of gas heaters` (same intent, different phrasing → should be one page)
2. **Overlapping category + blog content** — a category page titled "Gas Heaters" and a blog article titled "Guide to Gas Heaters" compete for the same query
3. **Historical content accumulation** — publishing multiple articles on the same topic over different years without consolidating them
4. **Template-based publishing** — using the same content structure for slightly different keyword variations, producing near-duplicate pages

### How to Detect Existing Cannibalism

**Method 1 — Google Site Search**
Search `site:yourdomain.com gas heater` in Google. If multiple pages appear, check if any are competing for the same intent.

**Method 2 — Search Console Query Analysis**
In Google Search Console, filter by query. If the same query is showing impressions across 3+ different URLs on your site, those URLs are cannibalising each other.

**Method 3 — Intent Audit**
List all pages on your site related to your Central Entity. Classify each by intent and entity-attribute pair. Any two pages with identical classifications are cannibalising.

### How to Fix Cannibalism

| Situation | Solution |
|---|---|
| Two pages with identical intent and attribute | Merge into one page. 301 redirect the weaker page to the stronger. |
| Category page and blog article competing | Redefine the blog article's macro context. Change its entity-attribute focus to something the category page doesn't cover. |
| Multiple thin articles on same topic | Consolidate all into one comprehensive article. 301 redirect all thin versions to the comprehensive one. |
| Near-duplicate programmatic pages | Add genuinely unique content to each, or noindex/consolidate the duplicates. |

---

## LESSON 2.9 — The Master Keyword Spreadsheet

### Structure of the Spreadsheet

Every keyword extracted from your five sources is entered into a single master spreadsheet. This is the deliverable for this module — the raw data that feeds Module 6 (CMap), Module 7 (Topical Map), and Module 8 (Content Briefs).

**Columns:**

```
Column A  — Keyword (exact phrase)
Column B  — Monthly Search Volume (from tool)
Column C  — Keyword Difficulty (from tool)
Column D  — Primary Intent (Informational / Commercial / Transactional / Navigational)
Column E  — Sub-Intent (Definition / Process / Comparison / Troubleshooting / Ranking / Review / etc.)
Column F  — Entity
Column G  — Attribute
Column H  — Query Path Stage (Awareness / Education / Evaluation / Comparison / Validation / Transaction / Post-purchase)
Column I  — Source (Autocomplete / PAA / Related Searches / Competitor URLs / Tool)
Column J  — Group ID (assign a number to keyword group — same number = same page)
Column K  — Page Type (Blog article / Category page / Product page / Landing page / FAQ)
Column L  — Priority (High / Medium / Low — based on volume + difficulty + intent alignment with source context)
Column M  — Notes (cannibalism flags, SERP feature observations, seasonal signals)
```

### Sorting and Filtering Protocol

**After populating all columns:**

**Sort 1 — By Group ID** to see all keywords allocated to each page together.

**Sort 2 — Within each group, by search volume descending** to identify the primary keyword (highest volume) and supporting keywords (all others in the group).

**Filter 1 — High priority + Informational intent** → These are your Core section article candidates.

**Filter 2 — High priority + Commercial intent** → These are your comparison and review article candidates.

**Filter 3 — Transactional intent** → These are your CMap product/category page candidates.

**Filter 4 — Cannibalism flag in Column M** → These require resolution before the topical map is built.

### Quality Check Before Proceeding

Before moving to Module 3, verify:

- [ ] Every keyword has an intent classification
- [ ] Every keyword has an entity-attribute pair
- [ ] Every keyword has a query path stage
- [ ] Every keyword belongs to exactly one group (no orphan keywords)
- [ ] No two groups contain keywords with identical intent + entity-attribute pairs (cannibalism check)
- [ ] The keyword list reflects all stages of the query path (awareness through post-purchase)
- [ ] Navigational keywords have been separated and will not be used for content planning
- [ ] The total number of keyword groups = the approximate number of pages the topical map will contain

---

## MODULE 2 — SUMMARY

You now understand keyword research as territory mapping, not list building.

**Lesson 2.1 — The problem with traditional research:** volume-sorted keyword lists produce disconnected content with no topical architecture.

**Lesson 2.2 — Seed entity extraction:** research grows from your Central Entity, not from a tool. Everything traces back to one seed.

**Lesson 2.3 — Five extraction sources:** Autocomplete, PAA, Related Searches, Competitor URLs, and Keyword Tools — each reveals a different dimension of the query territory.

**Lesson 2.4 — Query path mapping:** keywords exist in sequences that reflect stages of user decision-making. Map the full path, including all branches for different user types.

**Lesson 2.5 — Intent classification:** intent determines page type. The four intent categories and their sub-intents are non-negotiable grouping criteria.

**Lesson 2.6 — TF-IDF analysis:** the vocabulary floor of a ranking document. Every term appearing in 70%+ of top-ranking competitor pages is mandatory in your document.

**Lesson 2.7 — Keyword grouping:** same intent + same entity-attribute + SERP overlap = same page. Violate this and you either fragment authority or dilute relevance.

**Lesson 2.8 — Cannibalism detection:** existing or planned page overlaps are detected and resolved before the topical map is built. Unresolved cannibalism produces soft spam signals.

**Lesson 2.9 — The master keyword spreadsheet:** the structured deliverable that every subsequent module draws from.

---

## MODULE 2 — KEY TERMS GLOSSARY

| Term | Definition |
|---|---|
| **Seed entity** | The single word or phrase that names the Central Entity — the starting point of all keyword extraction. |
| **Query path** | The sequence of searches a user makes as intent refines from broad awareness to specific action. |
| **Intent classification** | The categorisation of a keyword into Informational, Navigational, Commercial, or Transactional intent. |
| **TF-IDF** | Term Frequency × Inverse Document Frequency. A measure of which terms are statistically expected in a well-ranking document for a specific topic. |
| **Information gain** | The unique, accurate, specific data a document contains that competitor documents do not. The ceiling above TF-IDF's floor. |
| **Keyword group** | A cluster of keywords with identical intent, entity-attribute focus, and SERP overlap — allocated to one page. |
| **Keyword cannibalism** | Two or more pages on the same site competing for the same query cluster — diluting authority and creating soft spam risk. |
| **SERP overlap test** | Comparing the top 5 results for two keywords. High overlap confirms they belong in the same keyword group. |
| **Sub-intent** | A specific type within a primary intent category (e.g. Comparison is a sub-intent within Informational). |
| **Query path stage** | The stage of user decision-making a query represents: Awareness, Education, Evaluation, Comparison, Validation, Transaction, or Post-purchase. |
| **Master keyword spreadsheet** | The structured document containing all extracted keywords classified by intent, entity-attribute, query path stage, group ID, and page type. |

---

## MODULE 2 — SELF-ASSESSMENT QUESTIONS

1. A keyword tool returns 500 keywords for `baby food`. Explain the process of reducing these 500 keywords to a structured set of keyword groups without creating cannibalism.

2. The keywords `best gas heater Pakistan` and `top gas heater brands Pakistan` both have Commercial Investigation intent. Are they the same page or different pages? Run all three tests and explain your conclusion.

3. A site has published these two articles:
   - "Complete Guide to Gas Heaters" (published 2023)
   - "Best Gas Heaters in Pakistan 2025" (published 2025)
   Both rank for `gas heater Pakistan` but neither reaches page 1. What is the likely cause and what is the solution?

4. Your TF-IDF analysis of `how to maintain gas heater` reveals that 8 of the 10 top-ranking pages include the terms `burner cleaning`, `filter replacement`, `annual servicing`, and `gas pressure check`. None of these terms are in your current article draft. What is the impact on ranking and what must you do?

5. Map the complete query path for the seed entity `baby food` — from Awareness through Post-purchase. Include at least 3 keywords at each stage. Identify two points in the path where it branches for different user types.

6. A client wants to create separate articles for:
   - `oil filled heater vs fan heater`
   - `fan heater vs oil filled heater`
   - `which is better oil heater or fan heater`
   Are these three articles, two articles, or one article? Justify using the grouping rules.

7. What is the difference between TF-IDF and information gain? Why is one the floor and the other the ceiling?

---

*Next: Module 3 — Lexical Relationships*
