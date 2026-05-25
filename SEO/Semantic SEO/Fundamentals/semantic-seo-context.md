# SEMANTIC SEO ARTICLE WRITING — MASTER CONTEXT FILE
> Version 1.0 | Based on Koray Tugberk GUBUR methodology, Google Search Quality Guidelines, and internal agency standards

---

## SECTION 0 — HOW TO USE THIS FILE

This is the **operating manual** for every article produced by this agency. Read it fully before writing a single word. Every section is mandatory. Shortcuts produce penalty-eligible content.

**Workflow sequence — never skip steps:**

```
1. KW Research          → Extract all query paths
2. Angle Research       → Determine source context + central search intent
3. Mind Map             → Visualize entity-attribute network
4. Entity Research      → EAV mapping (Entity → Attribute → Value)
5. KW Grouping          → Cluster by intent; one cluster = one page
6. Topical Map          → Map Core vs Outer sections; assign URLs
7. Content Brief        → Full brief per article (macro context, H-tags, format codes)
8. Write                → Apply all writing rules below
9. QA Audit             → Check against penalty factors and content quality checklist
```

---

## SECTION 1 — FOUNDATIONAL THEORY

### 1.1 What is Semantic SEO?

Semantic SEO is the practice of configuring content according to logic and contextual relationships — not keyword repetition. Search engines rank **entities and their relationships**, not isolated keywords. A semantically optimised document gives Google enough structured information to extract, index, and associate your content with the correct knowledge domain.

**Core principle:** Every word, sentence, heading, and URL must serve a contextual purpose. If a word does not change meaning, delete it.

### 1.2 How Search Engines Process Content

Google operates in vectors. A paragraph converted to a vector can be compared against another paragraph's vector. If the dot product of two vectors equals 1, the content is identical. At 0.5, there is partial overlap. **Semantic distance = similarity of two things.** This is why contextless filler lowers your ranking — it dilutes the vector.

Google also processes the query itself: it elongates the query, infers intent, and maps it against a **query network** — a graph of how search queries relate to each other.

**Three types of search engine grouping:**

| Grouping Type | What It Does |
|---|---|
| Document grouping | Clusters related documents together |
| User grouping | Clusters users with similar search behaviour |
| Query grouping | Clusters semantically related queries |

### 1.3 Query Networks

A query network is the map of how queries relate to each other. Three relationship types matter for content planning:

- **Query path** — the sequence of searches a user performs to refine intent (e.g. `heater` → `heater price` → `heater price in Pakistan 2025`). Each step = intent refinement.
- **Correlated queries** — queries searched together in the same session. One query is nested inside another.
- **Sequential queries** — two queries from the same session state (same user mind at same stage of decision). These are candidates for the same article or tightly linked supporting articles.

### 1.4 Lexical Relationships (You Must Understand These for Titles and Content)

| Relationship | Definition | SEO Application |
|---|---|---|
| **Hyponymy** | Narrow word inside a broad word. Hypernym = broad (Vehicle), Hyponym = narrow (Car, Bus) | Use hyponyms in supporting articles; hypernym on root/pillar page |
| **Hypernymy** | Broad category word | Root-level pages and pillar pages |
| **Synonymy** | Words with similar meanings (Happy / Joyful) | Use in title variations, anchor text, H2/H3 alternates |
| **Antonymy** | Opposite words (Hot / Cold) | Comparison articles, FAQ sections |
| **Polysemy** | One word, multiple related meanings (Bank = financial / riverbank) | Disambiguate entity in first paragraph |
| **Homonymy** | Same spelling + pronunciation, different meaning (Bat) | Clarify context immediately in document |
| **Collocations** | Words that naturally appear together (Strong coffee, Fast car) | Include in body text naturally for vector reinforcement |
| **Co-occurring words** | Words with high probability of appearing together (Peanut Butter → Jelly) | TF-IDF research reveals these; include them |
| **Prototypes** | Central concept of a category (Bird → feathers + wings) | Define the prototype clearly on pillar/root pages |
| **Homophones** | Sound-alike, different meaning/spelling (Flour / Flower) | Rarely needed but disambiguate if entity is homophonic |

**Inferred words** — When a user searches "heater price", the inferred meaning includes "price list", "current price", "model-wise price". Detect and serve inferred intent inside the article.

---

## SECTION 2 — RESEARCH PHASE

### 2.1 Keyword Research Process

**Step 1 — Start with the head keyword.**
Extract the seed entity. Example: `heater`, `trimmer`, `AC`.

**Step 2 — Map all query paths.**
Use Google Autocomplete, Google Related Searches, Google PAA, and competitor SERP analysis.

```
Head KW → Feature refinements → Version refinements → Platform refinements → Problem refinements → Update refinements
```

Example for `capcut mod apk`:
```
capcut mod apk
capcut mod apk no watermark
capcut mod apk latest version
capcut mod apk for pc
capcut mod apk old version
capcut mod apk Jan 2026
```

**Step 3 — Classify every keyword by intent.**

| Intent Type | Description | Page Type |
|---|---|---|
| Informational | User wants to learn | Supporting article / blog |
| Navigational | User wants a specific site | Brand page |
| Commercial | User is comparing / evaluating | Comparison / review page |
| Transactional | User wants to buy / download | Money page / landing page |

**Sub-intents for download/app niche:**
- Download intent → Main page
- Update / version intent → Supporting page
- Platform intent → Supporting page (PC, iOS, Android)
- Information intent → Supporting article

**Step 4 — Remove n-gram keyword cannibals.**
If two keywords share the same intent and would produce the same content angle — they belong on **one page**. Separate pages for same-intent keywords = keyword cannibalism = soft spam risk.

**Rule of thumb:** Different intent = different page.

### 2.2 TF-IDF Analysis

TF-IDF (Term Frequency × Inverse Document Frequency) tells you which terms are statistically expected in a well-ranking document — not which terms to stuff.

**Process:**
1. Pull the top 10 ranking pages for your target keyword.
2. Extract: common phrases, repeated supporting terms, entity clusters.
3. Map the terms your content **must** include to be seen as complete.

Example — for `heater` articles, top pages naturally include:
- wattage, BTU, energy consumption, room size, safety features, thermostat, timer, price range, warranty, installation

If your content omits these, Google sees it as **incomplete** — even if it's longer.

**TF-IDF is a floor, not a ceiling.** Meeting TF-IDF requirements = baseline. Unique, expert information above that baseline = information gain.

### 2.3 Angle Research

The angle is **why your content deserves to exist** differently from everything already indexed.

Angle research questions:
- What do competitors miss in their coverage?
- What does the user actually want that no competitor delivers directly?
- What unique data, examples, or expert insight can you inject?
- Which user group is underserved (beginners vs. experts, buyers vs. researchers)?

**Angle ≠ opinion.** Angle = a unique, factual, complete perspective that serves a specific user group within the central search intent.

### 2.4 Entity Research (EAV Model)

Every article's knowledge graph is built on EAV: **Entity → Attribute → Value**

```
Entity:    Heater
Attribute: Wattage
Value:     1000W, 1500W, 2000W

Entity:    Heater
Attribute: Type
Value:     Oil-filled, Fan, Infrared, Ceramic, Gas
```

**Three types of attributes:**

| Attribute Type | Definition | SEO Value |
|---|---|---|
| **Root attributes** | Appear in ALL instances of the entity (e.g. every heater has wattage) | High — use in pillar/core pages |
| **Rare attributes** | Appear in only some instances | Medium — use in specific supporting pages |
| **Unique attributes** | Only apply to specific instances (for question generation) | Used for long-tail, comparison, and FAQ content |

**Attribute evaluation framework:**
- **Prominent** = attribute without which the entity cannot be fully defined ✓
- **Popular** = high search volume / user interest ✓
- **Relevant** = connected to source context and search intent ✓

Only attributes that score on all three dimensions qualify for Core section. Others go to Outer section or are discarded.

### 2.5 Contextual Domains

| Layer | Definition | Example |
|---|---|---|
| Knowledge domain | The broad field | Beverages |
| Contextual domain | A focused subset | Coffee |
| Contextual layer | A specific depth level | Expensive fermented coffee (Kopi Luwak) |

Your content should clearly signal which contextual layer it belongs to. The more specific and consistent your contextual layer, the stronger your topicality signal.

---

## SECTION 3 — TOPICAL MAP ARCHITECTURE

### 3.1 Foundation Elements (Define These Before Building the Map)

**1. Source Context**
Who is the website? How does it make money? What is its identity?
> Example: "Selling home appliances at the lowest affordable prices in Pakistan"

**2. Central Entity**
The single entity that appears across all pages of the topical map.
> Example: `Heater`

**3. Central Search Intent**
The unification of source context + central entity + user purpose.
> Example: "Help Pakistani buyers understand heaters — their types, features, and prices — so they can make informed purchase decisions at the best value"

The central search intent is NOT the product category. It is the **reason the user is searching**, including informational and evaluative stages, not just transactional.

**Central search intent creates site-wide n-grams.** These n-grams should appear in: H1, key H2s, introductions, footers, internal link anchor text, and boilerplate content.

### 3.2 Core Section vs Outer Section

```
Core Section = Central Entity + Source Context (direct attributes)
Outer Section = Central Entity + Predicates of Central Search Intent (peripheral attributes)
```

| Section | Purpose | Depth | Link Direction |
|---|---|---|---|
| **Core** | Build topical authority on primary attributes | Deep | Receives links from Outer |
| **Outer** | Expand query coverage, capture more sessions | Flat | Links to Core |

**Core pages** = quality, expert, authoritative articles. Place them closest to the homepage in the crawl path. Google discovers and evaluates these first.

**Outer pages** = supporting articles. Broader coverage. Less depth. Each links back to relevant Core pages.

### 3.3 Topical Map Dimensions

| Dimension | Description |
|---|---|
| **Vast (Width)** | How many topics you cover at the outer level |
| **Depth (Height)** | How deep you go on a specific attribute |
| **Momentum (Speed)** | How fast you publish and expand |

**Strategic rule:** If you cannot go wider, go deeper and faster. Go wide only when you can also go deep on specific attributes and contexts.

### 3.4 Topical Map Components (Per Article)

Each entry in the topical map must have:
1. Topic (Entity + Attribute pair — not all attributes, only qualified ones)
2. Title tag
3. Meta description
4. URL (structured, logical — see Section 5)
5. Image URL + alt tag
6. Publish date (important for temporal relevance signals)

### 3.5 Boilerplate Content

Boilerplate = content that appears across the entire website (header, footer, sidebars, navigation labels). This content **contributes to your contextual vector**. Ensure boilerplate reinforces:
- Central entity
- Source context
- Primary predicates of central search intent

### 3.6 Macro Context vs Micro Context

| Context Level | Definition | Changes Reflected In |
|---|---|---|
| **Macro context** | The primary semantic focus of a web page | Page topic, H1, main angle, SERP intent match |
| **Micro context** | Lexical-level adjustments within macro context | Word choice, phrase selection, synonym usage |

**One web page = one macro context.**
Under one macro context, discuss multiple related things — but they must all connect back to source context, central entity, and central search intent.

---

## SECTION 4 — CONTENT BRIEF CONSTRUCTION

### 4.1 Brief Structure

A complete brief contains:

```
[ ] Topic
[ ] Target URL
[ ] Target keyword(s)
[ ] Secondary / supporting keywords
[ ] Search intent classification
[ ] Macro context statement (1 sentence)
[ ] Core section or Outer section classification
[ ] H1 (verified against title formula rules)
[ ] H2 list (each as a question)
[ ] H3 list per H2 (contextual bridge from H2)
[ ] Format codes per section (see Section 4.4)
[ ] Internal link targets (with anchor text)
[ ] Entity list (with EAV)
[ ] TF-IDF required terms
[ ] Unique value opportunities (information gain)
[ ] Featured snippet targets (40 words / 320 chars)
[ ] PAA targets
[ ] Image brief (with alt tag formula)
[ ] Content length guidance (minimum necessary, maximum efficient)
[ ] Publish date
```

### 4.2 Title Construction Rules

A title is the **verbalisation of the topic**. Do not dilute it.

**Sources for title terms:**

| Source | Description |
|---|---|
| Conjunctive synonym phrase | Use AND-equivalent to join two synonymous angles |
| Substitute terms | Alternative phrasing for same concept |
| Prominent/popular attribute | Attribute that scores high on all three evaluation criteria |
| Representative query | How people actually search on Google — the extracted main term |
| Semantically similar terms | Two things that are actually close in meaning |
| Semantically related terms | How users connect two things (more important than similar) |
| Co-occurring words | Words that always appear together in collocations |
| Entity set | Plural entity + attributes discussed |
| Inferred terms | E.g. "heater price" → infers "price list", "price comparison" |
| Context expansion | Slightly expand context while staying related |
| Class → individual | Go from category to specific instance for long-tail |

**Bad title:** "Heater Guide"
**Good title:** "Gas Heater vs Electric Heater: Wattage, Price, and Energy Cost Comparison for Pakistani Homes"

### 4.3 URL Structure Rules

URLs have 3 logical parts:

```
Root  →  /  (homepage, establishes domain context)
Seed  →  /heaters/  (main entity / category)
Node  →  /heaters/gas-heater-price-pakistan/  (specific topic)
```

**Rules:**
- Use single or double word combinations only
- Do not duplicate terms across the URL path
- Use logical subsets (trimmer appears under which parent context?)
- Keep URLs as short as possible while remaining logical
- Structured URLs give better initial ranking signals
- Separate concerns cleanly: `/price/` is good, `/price-list/` is good — don't combine both on one node
- The crawl path must be clean: directly related items should be optimised and linked properly

**Good URL examples:**
```
/heaters/gas-heater/
/heaters/gas-heater/price/
/heaters/oil-filled-heater/
/heaters/heater-types/
```

**Bad URL examples:**
```
/heater-gas-heater-types-and-prices/
/blog/everything-about-heaters/
/heaters/heater/gas-heater-price/
```

### 4.4 Format Codes Reference

Use the correct format in the correct spot. Do not compete with your own answers.

| Code | Format | Use When |
|---|---|---|
| **FS** | Featured Snippet | 40 words max, 320 char limit. Direct answer to question |
| **PAA** | People Also Ask | Single definitive sentence. Certain, direct, no hedging |
| **DA** | Definitive Answer (long-form) | Full answer with qualifiers, signifiers, connections |
| **IL** | Instruction List | Ordered list of commands. Same PoST on first word of each item |
| **UL** | Unordered List | No prominence order. Give intro sentence + list + outro paragraph |
| **Table** | Data table | Preceded by definition sentence. Always followed by outro para |
| **FAQ** | Question + Answer pair | H3 question, immediate answer in first sentence, then expand |
| **CE** | Comparative Entity | Side-by-side entity comparison |
| **SE** | Statistical Evidence | Numeric value + source + context |
| **EE** | Expansion of Evidence | Fact → effect → function → importance |
| **FP** | Factual Proposition | Indisputable fact. No "will/should/might" modals |
| **CP** | Conditional Proposition | Condition-based declaration. Declaration first, then constraint |
| **NER** | Named Entity Recognition | Qualify every entity explicitly. No pronouns. |

---

## SECTION 5 — WRITING RULES (MANDATORY)

### 5.1 Structural Rules

**H1 = unification of all H2s.**
H1 is the macro context. Every H2 must be a direct component of the H1 topic.

**H2 to H3 = contextual bridge.**
There must be a logical connection between the H2 question and each H3 below it. Do not jump context.

**Contextual flow must be linear.**
H1 → H2 → H3 → body paragraph must travel in one direction. No backtracking, no context jumps.

**Repeat n-grams from opening in conclusion.**
The same key n-grams that open the document should appear at the end. This signals contextual consistency and a proper contextual vector to Google.

**Answer immediately. Never delay.**
The definitive answer appears in the **first sentence** after any question-based heading.

```
WRONG: "Vision boards are the boards for... To prepare a vision board... Benefits of vision boards..."
RIGHT: "There are 5 main benefits of vision boards for an entrepreneur: [list follows]"
```

### 5.2 Sentence-Level Rules

| Rule | Wrong | Right |
|---|---|---|
| **Be certain** | "Sun will rise tomorrow" | "Sun rises every day" |
| **Cut fluff** | "There is one more fact that every driver should know, and it is..." | "Electric charging time changes based on charger type." |
| **Use numeric values** | "There are many reasons" | "There are 7 main reasons" |
| **Qualify instances** | "Symptoms of X disease..." | "There are 6 severe symptoms and 3 rare symptoms of X disease." |
| **Conditional last** | "If A becomes B, do X" | "Do X, if A becomes B" |
| **Bold the answer, not the term** | A **penguin** is a flightless seabird | A penguin is a **flightless seabird** |
| **No co-reference** | "It is..." / "They are..." | Repeat the entity name. No pronouns. |
| **Short sentences** | Compound-complex construction | Break into two sentences at max |
| **Verb context** | "Improve" + health context | "Improve" signals skill+health. "Increase" signals health only. "Develop" signals skill only. |

### 5.3 Paragraph Rules

**Context vector per paragraph:**
Every word in a paragraph must have contextual relevance to the heading above it. No decorative language.

**No context break across paragraphs.**
Do not split one concept across multiple paragraphs if it fractures the dependency tree.

**Discourse integration:**
Sentences within a paragraph must connect logically. Sentence B should follow from Sentence A.

**Long dependency tree = diluted meaning.** Break long sentences.

### 5.4 Question Construction Rules

**Use short questions.** Word count is not the measure — concepts are.

Long question format (avoid where possible):
```
Question + Condition/Declaration
"What is the importance of life if we all die?"
```

If you must use long questions, structure them:
```
H2: Short grouper question
H3: Short sub-questions with qualifiers as separate headings
```

**Never copy questions from PAA or competitors.** Write unique questions based on entity attributes and user intent. Use Google Question Hub, autocomplete, and query path analysis.

**Represent multiple search behaviours in one article:**
```
"How many centimeters are in a meter?"
"How many centimeters are equal to 1 meter?"
Both serve different search behaviours but answer the same intent — include both forms.
```

### 5.5 List Rules

**Same Part of Speech (PoST) on first word of every list item:**
```
Ensure (Verb) + noun
Clear (Verb) + noun
Spend (Verb) + noun
```
All items must start with the same word class.

**Give examples after plural nouns:**
```
WRONG: "There are 40 different cryptocurrencies in Coinbase."
RIGHT: "There are 40 different cryptocurrencies in Coinbase, including Bitcoin, Ethereum, and Dogecoin."
```

**Every list needs:**
- Introductory sentence (context for the list)
- List items (with specific content, not vague labels)
- List outro (paragraph commenting on the list)

### 5.6 Anchor Text and Internal Linking Rules

**Match anchor text to target page title:**
```
Source page heading: "What is Sleep Efficiency?"
Target page title: "10 Ways to Improve Sleep Efficiency"
Anchor text: "Sleep Efficiency"
```

**Use URL + hash identifier for deep links:**
```
/heaters/gas-heater/#wattage-comparison
```

**Fewer links per document = more weight per link.**
Include internal links on the most important terms only. Do not link out to external citations inline.

**Templatic phrase linking rule:**
If your title uses "X to Y" (e.g. Meters to Centimeters), link to:
- All sibling pages (Meters to Miles, Meters to KM)
- The antonym page (Centimeters to Meters)

### 5.7 Table Rules

Every table must be preceded by a context definition sentence:
> "The table below compares 5 types of heaters by wattage, price range, and ideal room size."

Every table must be followed by an outro paragraph that comments on or summarises what the data shows.

Use specific, data-rich table values. Do not use placeholder text inside tables.

### 5.8 Content Length Rules

There are **only two rules** for content length:
1. Content should be as short as possible.
2. Content should be as long as necessary.

Long content is not an SEO signal. **Unique, complete, accurate information** is the signal. If a fact can be stated in 12 words, use 12. If a concept requires 400 words to complete, use 400.

**Snippet targets:** Answers targeting featured snippets should be 40 words max and 320 characters max.

### 5.9 Subordinate Text Rule

The first sentence after any heading must directly answer or address that heading. Do not redefine the heading in the first sentence.

```
Heading: "How to Do X"
WRONG first sentence: "X is a process that..."
RIGHT first sentence: "To do X, [action/steps follow]"
```

Match adjective, predicate, and noun order between the question and the answer.

### 5.10 Perspective Richness

After a complete factual answer, add **perspective richness** — the same answer from multiple relevant viewpoints.

```
Heading: "How to Learn English Fast?"
Answer: "There are X ways of learning English faster: [list]"
Then add perspectives: for children (from a teacher's view, a parent's view, an aunt's view)
```

Do not overdo perspectives — only use when they genuinely add coverage depth. Too many perspectives break semantic structure.

### 5.11 Style and Tone Rules

- Never give your opinion in an article.
- Never use everyday language (casual speech).
- Do not use analogies.
- Do not use unnecessary words.
- Never use "will", "should", "need to", "have to" for factual statements — these signal opinion, not fact.
- Use a "source" as authority before making a claim (e.g. "According to [University] research from [Department], [claim]").
- Bold the **answer**, not the search term.
- No promotion of products inside informational content. Informational pages must appear unbiased.
- Use CTAs that are visually differentiated from the surrounding content.

---

## SECTION 6 — CONTENT QUALITY CHECKLIST

Before publishing any article, verify all items below.

### 6.1 Entity and Context
- [ ] Single macro context per page — no topic mixing
- [ ] All entities named explicitly (no pronouns)
- [ ] EAV coverage complete for all root and prominent attributes
- [ ] Central entity appears in H1, first paragraph, key H2s, conclusion
- [ ] Source context is reflected in article framing
- [ ] Central search intent is served by this article's angle
- [ ] Contextual layer is clearly established in opening

### 6.2 Structure
- [ ] H1 unifies all H2s
- [ ] Each H2 has a contextual bridge to each H3 below it
- [ ] Contextual flow is linear from H1 to last heading
- [ ] No context jump between paragraphs
- [ ] Repeated n-grams appear in both opening and conclusion
- [ ] Questions are short-form or properly structured long-form
- [ ] No questions copied from PAA or competitors

### 6.3 Sentence Quality
- [ ] Every factual sentence uses certainty (present tense, no modals)
- [ ] No contextless words anywhere in the document
- [ ] Numeric values used for all quantifiable claims
- [ ] Instances qualified (6 severe symptoms, 3 rare symptoms)
- [ ] Examples given after every plural noun
- [ ] Conditional statements: declaration first, constraint second
- [ ] All list items use same PoST on first word
- [ ] Subordinate text directly addresses its heading in sentence 1
- [ ] Bold marks the answer, not the keyword

### 6.4 Completeness
- [ ] All root attributes of central entity covered
- [ ] Featured snippet sections at 40 words max
- [ ] PAA sections give single definitive sentence first
- [ ] Tables have intro sentence + data + outro paragraph
- [ ] All lists have intro sentence + items + outro paragraph
- [ ] Multiple examples, data points, statistics per information claim
- [ ] No unsupported claims (source attribution present)
- [ ] Unique information not available on competitors included

### 6.5 Internal Linking
- [ ] Anchor text matches target page title
- [ ] Hash identifiers used for deep section links
- [ ] Links fewer than document weight can support
- [ ] No external citation links inline
- [ ] Templatic phrases linked to sibling + antonym pages

### 6.6 On-Page Technical
- [ ] URL is structured (Root / Seed / Node)
- [ ] No duplicate terms in URL
- [ ] Title tag verbalises topic without dilution
- [ ] Meta description includes keyword + value proposition
- [ ] Image alt tags match heading context (representative image rule)
- [ ] Publish date set correctly
- [ ] Author byline present and consistent with site niche

---

## SECTION 7 — GOOGLE SPAM POLICIES AND PENALTY FACTORS

**This section is mandatory reading before publishing any content.** Violating these policies results in manual actions, algorithmic demotions, or complete removal from search results.

### 7.1 Official Google Policy Documents

| Resource | URL |
|---|---|
| Google Spam Policies (Main) | https://developers.google.com/search/docs/essentials/spam-policies |
| Google Search Essentials (formerly Webmaster Guidelines) | https://developers.google.com/search/docs/essentials |
| Helpful Content Guidance | https://developers.google.com/search/docs/fundamentals/creating-helpful-content |
| March 2024 Core Update + New Spam Policies | https://developers.google.com/search/blog/2024/03/core-update-spam-policies |
| Site Reputation Abuse Policy (Updated Jan 2025) | https://developers.google.com/search/blog/2024/11/site-reputation-abuse |
| Google Quality Rater Guidelines | https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf |
| Search Console Manual Actions | https://support.google.com/webmasters/answer/9044175 |

### 7.2 The Three New Spam Policies (March 2024, Enforced Ongoing)

**1. Scaled Content Abuse**
Creating large volumes of pages primarily to manipulate search rankings — whether by humans, AI, or a combination. This includes:
- Spun articles (template + noun swaps)
- Unedited AI output published at volume
- Programmatic thin category/tag pages
- Mass affiliate reviews rewriting manufacturer descriptions without original testing

*Penalty*: Algorithmic demotion and/or manual action.

**2. Expired Domain Abuse**
Buying expired domains with established link profiles to host new content and exploit historic authority. This is spam even if the new content is human-written.

**3. Site Reputation Abuse (Parasite SEO)**
Hosting third-party content on a trusted domain to piggyback on its ranking signals. No level of first-party involvement removes the violation. This includes white-label agreements, licensing arrangements, and partial ownership.

### 7.3 Core Spam Violations Checklist

**Never do any of the following:**

| Violation | Description |
|---|---|
| **Cloaking** | Showing different content to Googlebot vs users |
| **Hidden text/links** | White text on white background, CSS-hidden elements |
| **Doorway pages** | Low-value pages targeting specific keywords to funnel to one destination |
| **Link spam** | Buying links, excessive exchanges, automated backlink generation |
| **Keyword stuffing** | Unnatural repetition of keywords in content or metadata |
| **Scraping** | Copying and republishing others' content without original value |
| **Thin content** | Pages that exist only to match queries but deliver no real information |
| **Automated content at scale** | High-volume AI or template output published without expert review |
| **Misleading structured data** | Schema markup that misrepresents page content |
| **Auto-generated queries** | Using automated tools to send queries to Google |

### 7.4 Soft Spam Triggers (Algorithmic Risk)

The following do not necessarily produce manual actions but trigger algorithmic quality penalties:

- Multiple articles targeting the same keyword with same intent (keyword cannibalism)
- Articles without clear authorship or expertise signals on niche topics
- Content that beats around the bush before answering the primary query
- Poor UX + heavy ad placement
- Inconsistent brand voice and content style across documents
- Topic switching — publishing articles outside site's established topical domain
- N-gram repetition patterns that signal template-based writing
- Content length penalty: overly long content that adds no additional information value

### 7.5 August 2025 Spam Update Focus Areas

Google's August 2025 spam update (26 Aug – 21 Sep 2025, 27 days) reinforced the following:
- Scaled / thin content (near-duplicate templates)
- Expired domain abuse
- Third-party / parasite placements
- Mass AI-generated content without firsthand expertise

Recovery from this update requires: firsthand expertise signals, clear authorship, content audit, and removal or significant enrichment of thin pages.

### 7.6 E-E-A-T Requirements (Experience, Expertise, Authoritativeness, Trustworthiness)

| Signal | How to Build It |
|---|---|
| **Experience** | First-person testing, original data, real examples specific to your market |
| **Expertise** | Author credentials on page, depth of attribute coverage, accurate technical content |
| **Authoritativeness** | Consistent brand voice, industry citations of your content, author coverage in third-party media |
| **Trustworthiness** | Physical address, consistent NAP (Name/Address/Phone), no E-A-T negativity, transparent methodology |

**Negative E-A-T signals to eliminate:**
- No author on article
- No physical address or business identity on site
- Conflicting statements across pages (inconsistent declarations)
- Excessive affiliate links
- Content on topics outside your demonstrated expertise

---

## SECTION 8 — KNOWLEDGE GRAPH CONSTRUCTION

### 8.1 Information Graph Principle

**One web page = one focus = one macro context.**
Give Google enough information about **one entity** to rank on **one attribute**.

This is the EAV principle applied at page level:
```
Entity:    [your central entity for this page]
Attribute: [the single attribute this page covers]
Value:     [all the values, data, comparisons, context for that attribute]
```

### 8.2 Pillar Page vs Supporting Article Architecture

```
Ontology Root Page (Comprehensive coverage of central entity)
        │
        ├── Pillar Page 1 (Entity + Core Attribute 1)
        │       ├── Supporting Article 1a (Specific sub-attribute)
        │       ├── Supporting Article 1b (Specific sub-attribute)
        │       └── Supporting Article 1c (Specific sub-attribute)
        │
        ├── Pillar Page 2 (Entity + Core Attribute 2)
        │       ├── Supporting Article 2a
        │       └── Supporting Article 2b
        │
        └── Pillar Page 3 (Entity + Core Attribute 3)
```

**Interlinking rule:** Link hierarchically according to semantic relationships. Core section pages link down to supporting articles. Supporting articles link back up to Core section and Pillar pages. Outer section links into Core section.

### 8.3 Content Gap Principle

One page cannot satisfy all query paths. Each refined intent deserves either:
- A separate section within the article (if closely related)
- A separate supporting article (if the intent is distinct enough)

**Content coverage ≠ long article.** Coverage = correct allocation of intent to correct page.

---

## SECTION 9 — AUTHORITY RESOURCES FOR RESEARCH AND VERIFICATION

### 9.1 Semantic SEO and Patent Research

| Resource | URL | Value |
|---|---|---|
| **SEO by the Sea** (Bill Slawski — Google patents) | https://www.seobythesea.com | Primary source for Google patent analysis and algorithm research |
| SEO by the Sea Semantic Resources | https://www.seobythesea.com/recommended-seo-and-usability-reading/semantic-web-resources/ | Curated semantic marketing resources |
| **Holistic SEO** (Koray Tugberk GUBUR) | https://www.holisticseo.digital | Topical authority methodology, semantic content networks, case studies |
| Holistic SEO — Theoretical SEO | https://www.holisticseo.digital/theoretical-seo/ | Deep dives into semantic search, knowledge graphs, entity SEO |
| Holistic SEO — Semantic Search | https://www.holisticseo.digital/seo-research-study/semantic-search | Verbs of life, semantic content networks, predicate use |
| **OnCrawl — Koray Tugberk articles** | https://www.oncrawl.com/author/koray-tugberk/ | Quality threshold, semantic network case studies |

### 9.2 Content Quality Reference Examples

| Site | URL | What to Study |
|---|---|---|
| Svalbardi Water Guide | https://svalbardi.com/pages/water-guide | Contextual depth, entity coverage, factual sentence construction |
| Svalbardi Blog | https://svalbardi.com/blogs/water/benefit | No external citation links — study inline citation style |
| Oscar Wylee Eye Care | https://www.oscarwylee.com.au/eye-care.html | Flat outer section structure |

### 9.3 Semantic Content Writing Rules (Course Reference)

| Resource | URL |
|---|---|
| Semantic Content Writing Rules (Notion doc) | https://bow-dietician-9de.notion.site/Semantic-Content-Writing-Rules-8fd4c217721b424f9f7a5ce2dff5fa80 |
| Koray's SEO Course | https://seocourse.digital/courses/semantic-seo/ |

### 9.4 Google Official Documentation

| Resource | URL |
|---|---|
| Google Search Central (main) | https://developers.google.com/search |
| Spam Policies | https://developers.google.com/search/docs/essentials/spam-policies |
| Helpful Content | https://developers.google.com/search/docs/fundamentals/creating-helpful-content |
| March 2024 Spam Policy Announcement | https://developers.google.com/search/blog/2024/03/core-update-spam-policies |
| Site Reputation Abuse (Jan 2025 update) | https://developers.google.com/search/blog/2024/11/site-reputation-abuse |
| Search Quality Rater Guidelines | https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf |
| Google Search Central Blog | https://developers.google.com/search/blog |
| Search Status Dashboard | https://status.search.google.com |

### 9.5 Industry Tracking Resources

| Resource | URL | Use |
|---|---|---|
| Search Engine Land | https://searchengineland.com | Algorithm update tracking |
| Search Engine Roundtable (Barry Schwartz) | https://www.seroundtable.com | Real-time update impact reports |
| Lily Ray (Authority/E-A-T specialist) | https://lilyray.nyc | E-A-T analysis and case studies |
| Marie Haynes Consulting | https://www.mariehaynes.com | Algorithm impact analysis |
| Aleyda Solis | https://www.aleydasolis.com | Technical + international SEO |
| Gianluca Fiorelli | https://www.iqsem.com | Entity SEO, international semantic SEO |
| Jason Barnard (Brand SERP / Kalicube) | https://kalicube.com | Entity-based branding and knowledge panels |

---

## SECTION 10 — QUICK REFERENCE CHEAT SHEET

### Sentence Construction Quick Checks

```
✓ Present tense for facts (not "will")
✓ Numeric value present for any quantifiable claim
✓ Entity named in full — no pronouns
✓ Answer in first sentence after heading
✓ Conditions placed after declarations
✓ Lists: same PoST on first word of every item
✓ Examples follow every plural noun
✓ Bold on answer, not on search term
✓ Table has intro + data + outro
✓ All headings converted to questions
```

### Spam Risk Quick Checks

```
✗ Multiple pages targeting same intent? → Merge
✗ Thin content (no unique information)? → Enrich or delete
✗ AI content unedited and published at volume? → Penalty risk
✗ Articles outside site topical domain? → EAT signal damage
✗ Author missing from article? → Add + credential
✗ No original data or examples? → Information gain gap
✗ Content promoting product inside information article? → Remove promotion
```

### Attribute Evaluation Quick Check

```
Is the attribute PROMINENT? (entity can't be defined without it) ✓/✗
Is the attribute POPULAR? (high search volume / user interest)   ✓/✗
Is the attribute RELEVANT? (matches source context + intent)      ✓/✗

All three ✓ → Core section
Two ✓ → Outer section or supporting article
One or zero ✓ → Exclude from topical map
```

### Content Type → Format Code Map

```
Direct "what is" question          → DA + FS
"How to" question                  → IL (instruction list)
Comparison question                → CE + Table
"How many" / "what are" question   → UL or IL + numeric qualifier
Yes/No question                    → FP (factual proposition, one sentence)
Definition question                → NER + DA
Statistical question               → SE (statistical evidence)
Process / sequence question        → IL (ordered, same PoST)
```

---

*Last updated: May 2026 | Maintainer: Agency SEO Team*
*Primary methodology source: Koray Tugberk GUBUR — Holistic SEO & Digital*
*Patent research foundation: Bill Slawski — SEO by the Sea*
*Google policy compliance: Verified against March 2024 + August 2025 spam updates*
