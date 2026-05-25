# MODULE 3 — Lexical Relationships
## The Vocabulary Architecture of Semantic Content

> **Purpose of this module:** Lexical relationships are the structural rules that govern how words relate to each other in a language — and how Google interprets those relationships when evaluating your content. This module teaches you to use these relationships deliberately: in title construction, heading hierarchies, URL structures, body content, and anchor text. A writer who understands lexical relationships does not just choose words — they engineer contextual signals at the word level.

---

## LESSON 3.1 — Why Word Relationships Matter to Google

### Words Are Not Equal

In traditional copywriting, words are interchangeable as long as the sentence makes sense. In semantic SEO, words are not interchangeable — every word choice carries a specific contextual signal to Google's NLP (Natural Language Processing) systems.

When Google's language models process your content, they are not just reading for meaning. They are identifying:

- **Which entity** this word refers to
- **What role** this word plays (is it the entity, an attribute, a value, a modifier?)
- **What relationship** exists between this word and the words around it
- **Which knowledge domain** this vocabulary belongs to

A writer who chooses words randomly produces a document with a weak, noisy vector. A writer who understands lexical relationships produces a document where every word contributes a clear, consistent signal that reinforces the entity-attribute structure Google is looking for.

### The Six Practical Applications of Lexical Relationships

Lexical relationships appear in SEO in six specific places:

| Application | Where Lexical Relationships Are Used |
|---|---|
| **Title construction** | Selecting the precise terms that signal the correct entity-attribute pair |
| **Heading hierarchy** | Moving from broad (hypernym) to narrow (hyponym) as H-level increases |
| **URL architecture** | Placing broad terms at seed level, narrow terms at node level |
| **Body vocabulary** | Including collocations and co-occurring words for vector completeness |
| **Anchor text selection** | Using synonyms and semantically related terms for varied but consistent linking |
| **Entity disambiguation** | Using polysemy and homonymy awareness to clarify which entity you mean |

Master these six applications and lexical relationships stop being theory — they become a production tool.

---

## LESSON 3.2 — Hyponymy and Hypernymy: The Hierarchy of Words

### The Definition

**Hypernym** = the broad, general category word. The parent.
**Hyponym** = the narrow, specific instance word. The child.

The relationship between them is called **hyponymy** — the "is a type of" relationship.

```
Hypernym:  Vehicle
Hyponyms:  Car, Bus, Bicycle, Motorcycle, Truck

Hypernym:  Heater
Hyponyms:  Gas Heater, Electric Heater, Oil-filled Heater, Fan Heater, Infrared Heater

Hypernym:  Coffee
Hyponyms:  Espresso, Americano, Latte, Kopi Luwak, Cold Brew

Hypernym:  Eye Care
Hyponyms:  Eye Exam, Prescription Glasses, Contact Lenses, LASIK, Dry Eye Treatment
```

### The SEO Architecture Rule

The hypernym-hyponym relationship maps directly onto your site's page hierarchy:

```
HYPERNYM → Root Page / Pillar Page (broad coverage of the entire category)
HYPONYM  → Supporting Page (specific coverage of one instance)
```

**Examples:**

```
Hypernym: Heater          → Root page: /heaters/ (covers all heater types)
Hyponym:  Gas Heater      → Pillar page: /heaters/gas-heater/ (covers gas heaters comprehensively)
Hyponym:  Electric Heater → Pillar page: /heaters/electric-heater/ (covers electric heaters)

Sub-hyponym: Gas Heater Price → Supporting page: /heaters/gas-heater/price/
Sub-hyponym: Gas Heater Safety → Supporting page: /heaters/gas-heater/safety/
```

Each level down the hierarchy narrows the contextual focus. The root page covers the hypernym. Pillar pages cover first-level hyponyms. Supporting articles cover second-level hyponyms (specific attribute pages for each entity instance).

### Applying Hypernymy in Title Construction

When writing titles, use the correct level of the hierarchy for the page's position in the site architecture:

| Page Level | Use | Example Title |
|---|---|---|
| Root page | Hypernym | "Home Heaters: Types, Prices, and Buying Guide for Pakistan" |
| Pillar page | First hyponym | "Gas Heaters: Complete Guide to Types, Wattage, and Prices in Pakistan" |
| Supporting article | First hyponym + attribute | "Gas Heater Price in Pakistan — Brand-wise Price List 2025" |
| Deep supporting article | Sub-hyponym + specific attribute | "Gree Gas Heater GH-1800 Price, Specifications, and Review" |

**The mistake to avoid:** Using the hypernym on a supporting article title.

A supporting article titled "Heater Guide: Gas Heater Price in Pakistan" sends a conflicting signal — the hypernym "heater" suggests broad coverage, but the content is specifically about gas heater prices. Google registers the mismatch and the page's vector is weakened.

### Hyponymy in Heading Structure

The same hypernym → hyponym logic governs heading levels within an article:

```
H1 (hypernym level):   Gas Heater Types in Pakistan
H2 (first hyponym):    What is a Convection Gas Heater?
H2 (first hyponym):    What is a Radiant Gas Heater?
H2 (first hyponym):    What is an Infrared Gas Heater?
H3 (sub-hyponym):      How Does Radiant Gas Heater Heat Distribution Work?
H3 (sub-hyponym):      Radiant Gas Heater vs Convection Gas Heater Efficiency
```

H1 names the category. H2s name specific instances of the category. H3s discuss specific attributes of those instances. The hierarchy is logical and consistent.

---

## LESSON 3.3 — Synonymy: Same Meaning, Different Signal

### The Definition

**Synonymy** = the relationship between words that share the same or very similar meaning.

```
Happy / Joyful / Content / Pleased
Big / Large / Huge / Enormous
Buy / Purchase / Acquire / Order
Guide / Manual / Handbook / Tutorial
```

### Why Synonyms Matter in Semantic SEO

Google's NLP systems understand synonymy. When a user searches `buy gas heater online` and your page uses the word `purchase` instead of `buy`, Google still matches the page to the query because it recognises `buy` and `purchase` as synonyms.

**This is why keyword stuffing died.** You do not need to repeat the exact keyword 15 times. You need to use the entity and its synonymous terms naturally — and Google connects them all.

The practical implication: **use synonym variation deliberately to serve multiple query phrasings within the same keyword group.**

### Applying Synonymy in Five Specific Places

**1. Title tags — using substitute terms to capture query variations**

Instead of forcing one exact phrase into a title, use the most representative form and let synonymy carry the rest:

```
Primary: "Gas Heater Price in Pakistan"
Synonymous queries served:
- "gas heater cost in Pakistan" (cost = price)
- "how much does a gas heater cost" (cost = price, how much = what is the price)
- "gas heater rates Pakistan" (rates = price)
```

The title "Gas Heater Price in Pakistan — 2025 Brand-wise List" serves all three query variations without needing to include all three phrasings.

**2. H2 and H3 headings — alternating between synonymous terms**

In a long article, alternating between synonymous terms for the same concept strengthens the semantic vector without creating repetition:

```
H2: What Does a Gas Heater Cost in Pakistan?
H3: Gas Heater Price Range by Brand
H3: Average Gas Heater Rates in Lahore vs Karachi
```

`Cost`, `price`, and `rates` are synonyms here. Using all three signals to Google that this section fully covers the price/cost attribute of gas heaters across multiple query phrasings.

**3. Anchor text — synonym variation in internal links**

Do not use the exact same anchor text for every internal link pointing to the same page. Use synonymous variations:

```
Links TO "Gas Heater Price Pakistan" article:
Anchor text 1: "gas heater price"
Anchor text 2: "gas heater cost"
Anchor text 3: "how much gas heaters cost"
```

Synonym variation in anchor text signals that the target page is broadly relevant to the concept, not just one specific phrasing.

**4. Body content — synonym substitution in TF-IDF vocabulary**

When your TF-IDF analysis reveals required terms, also include their synonyms. If `wattage` is a required term, also include `power consumption`, `energy output`, and `watt rating` — all synonymous in the heater context.

**5. Meta descriptions — synonyms for CTR signal diversity**

Your meta description may match a query Google shows it for. Including synonym variations increases the chance of a keyword match highlight in the SERP.

### The Synonym Trap: False Synonyms

Not all words that seem similar are true synonyms. In specific contexts, words that appear synonymous carry different semantic signals:

```
"Increase health" — correct collocation
"Improve health" — correct collocation
"Develop health" — INCORRECT — "develop" signals skill, not health

"Increase skill" — technically possible but weak
"Improve skill" — correct collocation
"Develop skill" — correct collocation
```

**Context determines which synonym is valid.** Choosing the wrong synonym — even if it means the same thing in everyday speech — produces a weaker contextual signal because it does not match the expected collocation pattern for that knowledge domain.

Check verb-noun collocations in Google Autocomplete before using them. If `develop health` does not appear as a suggestion and `improve health` does — use `improve`.

---

## LESSON 3.4 — Antonymy: Opposite Words as Semantic Partners

### The Definition

**Antonymy** = the relationship between words with opposite meanings.

```
Hot / Cold
Buy / Sell
Fast / Slow
Expensive / Affordable
Gas / Electric
New / Old
```

### Why Antonyms Strengthen Semantic Coverage

When you discuss one side of an antonymous pair, Google's NLP expects the other side to appear — because in natural language about most topics, both sides of a contrast are discussed.

An article about `affordable gas heaters` that never mentions `expensive heaters` or `premium heaters` is missing the semantic partner that natural, expert coverage would include. Its vector is incomplete.

**Including both sides of antonymous pairs signals comprehensive coverage.**

### The Three SEO Applications of Antonymy

**1. Comparison articles — antonymy defines the structure**

Comparison content is built on antonymous pairs:

```
Gas heater vs Electric heater     (fuel type antonyms)
Expensive heater vs Cheap heater  (price antonyms)
High wattage vs Low wattage       (specification antonyms)
New heater vs Old heater models   (temporal antonyms)
```

When building a comparison article, identify the antonymous pair first — that pair IS the article's macro context. Every H2 should compare both sides of the pair on one attribute at a time.

**2. URL symmetry — linking antonym pages to each other**

A page about `gas heaters` and a page about `electric heaters` are antonymous pairs. They must link to each other. A user reading about gas heaters is the same user who may want to compare electric heaters — serving the antonymous page is serving the user's natural next query.

This is also why `Meters to Centimeters` must link to `Centimeters to Meters` — the reverse conversion is the semantic partner. Not linking them is a structural gap in your content network.

**3. FAQ and PAA sections — anticipating antonymous questions**

Users who ask `what are the benefits of gas heaters` will also ask `what are the disadvantages of gas heaters`. Both questions are antonymous pairs that belong in the same article. Including both signals complete coverage of the entity's pro/con attribute.

---

## LESSON 3.5 — Polysemy and Homonymy: Disambiguation

### Polysemy — One Word, Multiple Related Meanings

**Polysemy** = a single word that has multiple related meanings depending on context.

```
"Bank"    → financial institution OR river bank
"Paper"   → writing material OR academic document OR newspaper
"Heater"  → home heating appliance OR a baseball pitch OR British slang for a gun
"Light"   → illumination OR low calorie OR not heavy
```

### Why Polysemy Creates SEO Risk

When your Central Entity has a polysemous name, Google must determine which meaning you intend. If your document does not establish context clearly in the opening paragraph, Google may associate your content with the wrong meaning — and return it for wrong queries while missing the right ones.

**The disambiguation rule:** Establish which meaning you intend in the first paragraph using entity qualifiers.

```
WEAK OPENING (polysemous risk):
"A heater is an important appliance for every home."

STRONG OPENING (disambiguated):
"A home heater is an electric or gas appliance that converts energy into heat
to warm indoor spaces during cold seasons."
```

The second version uses qualifiers: `home heater` (narrows scope), `electric or gas appliance` (technology type), `converts energy into heat` (function), `warm indoor spaces` (use context), `cold seasons` (temporal context). Six disambiguation signals in one sentence. Google's entity recognition is certain.

### Applying Polysemy Awareness in Title and H1 Construction

If your entity is polysemous, always qualify it in the title:

```
Polysemous:   "Heater Guide"
Qualified:    "Home Heater Guide"
More precise: "Gas Home Heater Buying Guide for Pakistani Households"
```

Each qualifier eliminates one alternative meaning. By the time you reach the fully qualified title, the entity's meaning is unambiguous.

### Homonymy — Same Word, Completely Different Meanings

**Homonymy** = words that share the same spelling and pronunciation but have completely unrelated meanings.

```
"Bat"  → baseball bat OR flying mammal
"Rose" → a flower OR past tense of "rise"
"Bark" → dog sound OR tree covering
"Fair" → just/equitable OR a carnival event OR light-coloured
```

Homonymy differs from polysemy in that the meanings are unrelated — they just happen to share a word form.

### Homonymy in SEO — Rare But Critical When It Occurs

Homonymy rarely affects most niches. But when your entity name is a homonym, it causes serious SERP confusion. Examples:

- A website about `cricket` (sport) vs `cricket` (insect)
- A website about `rust` (programming language) vs `rust` (oxidation) vs `Rust` (video game)
- A website about `sage` (herb) vs `Sage` (accounting software)

**The solution is identical to polysemy disambiguation:** establish entity identity in the opening with multiple qualifiers and use co-occurring terms from the correct knowledge domain throughout.

A website about Rust the programming language should use co-occurring terms like `memory safety`, `compiler`, `ownership model`, `cargo`, `crates.io` — vocabulary that belongs exclusively to the programming knowledge domain, not to oxidation or video games.

---

## LESSON 3.6 — Collocations and Co-Occurring Words

### Collocations — Words That Always Travel Together

**Collocations** = word pairs or phrases that native speakers and expert writers use together naturally. They are statistically predictable combinations.

```
Strong coffee        (not "powerful coffee")
Fast car             (not "speedy car" in most contexts)
Heavy rain           (not "weighty rain")
Make a decision      (not "do a decision" or "take a decision" in American English)
Run a business       (not "walk a business")
```

### Why Collocations Matter for Semantic Vectors

Google's language models are trained on billions of text documents. They have learned which word combinations are natural for each knowledge domain. When your content uses expected collocations, Google reads it as the work of a domain expert. When your content uses unnatural combinations — even if grammatically correct — Google reads it as non-expert content.

**Collocation examples for the heater knowledge domain:**

```
EXPECTED COLLOCATIONS:
- "heat output"           (not "heat production" in heater context)
- "room coverage"         (not "area coverage" in heater context)
- "energy efficiency"     (not "energy quality")
- "safety shut-off"       (not "safety turn-off")
- "wattage rating"        (not "watt number")
- "heating capacity"      (not "heating ability")
- "fuel consumption"      (not "fuel usage" — both acceptable but "consumption" is standard)
```

**How to find correct collocations for your knowledge domain:**

1. Read the top 10 ranking pages for your entity and note recurring two-word phrases
2. Use Google Autocomplete — if `heating capacity` appears as a suggestion but `heating ability` does not, `capacity` is the correct collocation
3. Check industry publications and manufacturer specifications — they use standard collocations

### Co-Occurring Words — Statistical Companions

**Co-occurring words** go one step beyond collocations. They are words that have a high statistical probability of appearing in the same document — even if not always in the same sentence.

```
In heater documents, these words co-occur:
wattage ↔ room size
gas ↔ LPG / natural gas ↔ ventilation
infrared ↔ radiant heat ↔ quartz
oil-filled ↔ fins ↔ thermostat ↔ silent operation
price ↔ PKR ↔ brand ↔ warranty
```

A document that contains `gas heater` and also contains `LPG`, `BTU`, `thermostat`, `ventilation`, and `safety shut-off` is statistically consistent with how expert gas heater content is structured. Google's language model recognises this and scores the document higher on the topicality dimension.

**Co-occurring words are the output of TF-IDF analysis.** The terms you find in 70%+ of top-ranking pages are not there because competitors chose to include them — they are there because those words co-occur naturally with the entity in expert content.

### Applying Collocations in Content Production

**Rule:** When writing about an entity, always use that entity's natural collocations — not generic synonyms that happen to fit grammatically.

**Wrong** (generic, unnatural):
> "The heater uses power in an efficient way."

**Right** (natural collocation):
> "The heater operates at high energy efficiency, consuming 1500W to deliver 5,118 BTU of heat output."

The second version uses three collocations: `energy efficiency`, `heat output`, and `BTU` in the same sentence as `1500W`. This is the vocabulary pattern that makes Google's language model classify this as expert heater content.

---

## LESSON 3.7 — Prototypes: Defining the Central Concept

### The Definition

**Prototype** = the most representative, central example of a category. The instance that best embodies what the category means.

When most people think of "bird," they think of a robin or sparrow — not an ostrich or penguin. The robin is the prototype. It has the most typical bird attributes: wings, feathers, flies, sings, small.

```
Category: Bird
Prototype: Robin / Sparrow (typical attributes — flies, small, sings)
Non-prototype members: Penguin (doesn't fly), Ostrich (doesn't fly, very large), Bat (not actually a bird)
```

### The SEO Application of Prototypes

On root pages and pillar pages that cover a broad entity category, you must **define the prototype clearly before discussing variants**.

The prototype is the answer to the question: *"What is the most typical, most common, most representative instance of this entity?"*

**For heaters:** The prototype home heater for most Pakistani buyers is a mid-range electric fan heater or a standard gas heater — not a high-end infrared panel or a commercial HVAC system. Your root page must define this prototype first, then move to variants.

**For eye care:** The prototype eye care interaction is a routine eye examination — not LASIK surgery or treatment for a rare condition. The root eye care page defines the prototype and then branches to more specific services.

**Why this matters:** When Google processes a broad query like `heater` or `eye care`, it expects the result to reflect the prototype of that category. A root page that immediately dives into niche variants (without first establishing the prototype) mismatches the intent of the broad query.

### How to Establish a Prototype on a Root Page

Structure:

```
H1: [Entity Category] — What It Is and How to Choose
First section: Define the prototype (most common type, typical use case, standard attributes)
Second section: Define the category's full range (all hyponyms)
Third section: Attribute comparison across all instances
```

The prototype section answers: *"For the average [audience], what is [entity] and what does a typical [entity] look like?"*

After the prototype is established, the full range of hyponyms makes contextual sense.

---

## LESSON 3.8 — Homophones: Sound-Alike Words

### The Definition

**Homophones** = words that sound the same but have different meanings and different spellings.

```
Flour / Flower
Their / There / They're
Heater / (no common homophone — low risk)
Site / Sight / Cite
Buy / By / Bye
Right / Write / Rite
```

### The SEO Relevance of Homophones

Homophones are primarily a quality signal, not a ranking mechanism. Their relevance in semantic SEO is narrow but important:

**1. Voice search queries**
When users speak a query to a voice assistant, homophones become ambiguous. `"Site" authority` vs `"Sight" problems` vs `"Cite" sources` — the voice assistant and Google must infer which word the user meant from context.

If your content is optimised for voice search on a topic where homophones are common, disambiguate through context. An SEO article about `site authority` should include enough web/SEO vocabulary that Google never confuses `site` with `sight`.

**2. Spelling consistency signals**
A document that mixes `their`, `there`, and `they're` incorrectly signals low content quality. While this is primarily a grammar issue, Google's quality assessment systems include content quality signals — and consistent grammatical errors negatively affect E-E-A-T evaluation.

**3. Homophone-based keyword intent mismatch**
If your target keyword is `flour types` (baking) and your content accidentally uses `flower types` in a heading due to autocorrect, Google may misclassify the document's macro context.

**The rule:** Homophones are a rare concern in most niches. When they appear, handle them with vocabulary context — surround the potentially ambiguous word with domain-specific co-occurring terms that eliminate ambiguity.

---

## LESSON 3.9 — Inferred Words: Serving What Users Mean, Not What They Type

### The Concept

Inferred words are the terms and concepts that a query implies — even though the user did not type them. Google infers these through query elongation (covered in Module 0) and the query network.

Understanding inferred words is how you anticipate content that your article must contain even when no keyword in your list explicitly asks for it.

### How Inference Works

```
User types:       "gas heater price"
Google infers:    price list, model-wise price, brand-wise price, price in PKR,
                  current price (2025), cheapest price, price comparison,
                  where to buy at lowest price
```

The user typed 3 words. Google inferred 8 additional content needs. An article that only contains the literal content of "gas heater price" — one price number — satisfies the typed query but fails all 8 inferred needs.

**An article that serves inferred words captures the full query cluster, not just the head phrase.**

### Common Inference Patterns

| User Types | Google Infers |
|---|---|
| `[entity] price` | price list, model comparison, brand comparison, current year price, cheapest option, price range by specification |
| `how to [action]` | step-by-step process, tools required, time required, common mistakes, expected result, when to seek professional help |
| `best [entity]` | ranking criteria, top brands, comparison table, what to look for, expert recommendation, specific use case recommendations |
| `[entity] types` | comprehensive list of all types, comparison of types, which type for which use case, most popular type, rarest type |
| `[entity] vs [entity]` | attribute-by-attribute comparison, cost comparison, performance comparison, verdict/recommendation, use case matching |
| `[entity] review` | pros and cons, specifications, real-world performance, price value assessment, who it is for, verdict |

### Serving Inferred Words in Content Structure

When building your content brief for any article, go through the inference pattern for your primary keyword and add the inferred content needs as H3 headings or FAQ sections.

**Example — brief expansion through inference:**

Primary keyword: `gas heater price Pakistan`
Inference: price list, brand comparison, model-wise price, cheapest option, price by specification

**Additional H3s added to brief:**
- `What is the price range of gas heaters in Pakistan? (FS target)`
- `Gas Heater Brand-wise Price List 2025`
- `Cheapest Gas Heater Under PKR 10,000 in Pakistan`
- `Gas Heater Price by Wattage in Pakistan`
- `Where to Buy Gas Heaters at the Lowest Price in Pakistan`

None of these H3s contain the exact keyword `gas heater price Pakistan` — but all of them serve inferred needs of that query. Together they make the article the most complete answer to the query cluster, not just the head phrase.

---

## LESSON 3.10 — Applying All Lexical Relationships: The Title Construction System

### Why Title Construction Is a Lexical Engineering Task

A title tag is not a creative exercise. It is the primary document-level signal that tells Google what entity-attribute pair this page covers. Every word in the title must be chosen deliberately using lexical relationship principles.

### The 11 Sources for Title Terms

Each source draws on a different lexical relationship:

| Source | Lexical Relationship | Example (Gas Heater Price Article) |
|---|---|---|
| **Central entity name** | Base entity | `Gas Heater` |
| **Prominent attribute** | Root attribute (EAV) | `Price` |
| **Substitute term** | Synonymy | `Cost` → serves `gas heater cost` queries |
| **Representative query** | Inferred words | `Price List` → serves `price list` inferred need |
| **Semantically similar term** | Semantic proximity | `Rates` → `gas heater rates Pakistan` |
| **Semantically related term** | Co-occurrence | `Brands` → price is related to brand comparison |
| **Co-occurring word** | Collocation | `PKR` → prices in Pakistan always in PKR |
| **Context expansion** | Hypernymy + specificity | `Pakistan 2025` → geographic + temporal context |
| **Conjunctive phrase** | Synonymy bridge | `Price and Cost` → covers both query phrasings |
| **Entity set** | Hyponymy | `Gree, Orient, Dawlance` → brand hyponyms |
| **Class → individual** | Hyponymy (specific) | `Gree GH-1800 Price` → individual model |

### Title Construction Formula

For a Core section article:

```
[Central Entity] [Attribute] in [Context]: [Inferred Need] — [Qualifying Detail]
```

Applied:
```
Gas Heater Price in Pakistan: Brand-wise Price List 2025 — Gree, Orient, Dawlance
```

Breaking this down:
- `Gas Heater` = central entity (hyponym of Heater)
- `Price` = root attribute
- `in Pakistan` = geographic context (from source context)
- `Brand-wise Price List` = inferred word (user expects brand comparison)
- `2025` = temporal qualifier (freshness signal)
- `Gree, Orient, Dawlance` = entity set (specific brand instances — serves navigational sub-queries)

**Every word earns its place through a lexical relationship principle.**

### The Bad Title Test

Run every title you write through this test:

1. Does it contain the central entity at the correct hyponymy level for this page?
2. Does it contain the primary attribute this page covers?
3. Does it include at least one synonym or substitute term for the attribute?
4. Does it include context (geographic, temporal, or audience)?
5. Does it serve at least one inferred need of the primary query?

If any answer is No — the title is incomplete. Revise before publishing.

**Bad title:** `Heater Guide 2025`
Fails: No attribute. No context. No inferred need. Hypernym level wrong for a supporting article.

**Weak title:** `Gas Heater Prices Pakistan`
Passes: Entity ✓, Attribute ✓. Fails: No context qualifier, no inferred need, no synonym.

**Strong title:** `Gas Heater Price in Pakistan — Complete 2025 Brand-wise Price List`
Passes all five tests.

---

## LESSON 3.11 — Lexical Relationships in URL Architecture

### The URL as a Lexical Hierarchy

A URL is a hierarchical structure. Each level of the URL should represent one level in the hypernym-hyponym chain:

```
Root (domain)    → No entity keyword (brand identity)
Seed (category)  → Hypernym keyword
Node (article)   → Hyponym + Attribute keyword
```

Applied to the heater site:

```
pakheaters.pk/                           → Root (brand)
pakheaters.pk/heaters/                   → Seed (hypernym: heaters)
pakheaters.pk/heaters/gas-heater/        → Node (first hyponym: gas-heater)
pakheaters.pk/heaters/gas-heater/price/  → Deep node (attribute: price)
```

### URL Lexical Rules

**Never duplicate terms across levels:**
```
WRONG: /heaters/heater-types/gas-heater/
The word "heater" appears three times across three levels — duplication.

RIGHT: /heaters/gas/
or: /heaters/gas-heater/
```

**Use the narrowest correct term at each level:**
```
WRONG: /heating-appliances/gas-heating-appliance-price/
"Heating appliances" is too wordy — "heaters" is the correct hyponym.

RIGHT: /heaters/gas-heater-price/
```

**Do not mix hierarchical levels:**
```
WRONG: /gas-heater-types-and-prices/
This puts two attributes (types + prices) at the same URL node — they have different macrocontexts and deserve separate nodes.

RIGHT: /heaters/gas-heater-types/
       /heaters/gas-heater-price/
```

**Use singular vs plural correctly:**
- Category/seed pages: plural (`/heaters/`)
- Specific entity pages: singular (`/gas-heater/`)
- Attribute pages: singular noun or gerund (`/price/`, `/buying-guide/`, `/maintenance/`)

---

## MODULE 3 — SUMMARY

Lexical relationships are not academic linguistics. They are the engineering system behind every word choice in semantic SEO.

**Hyponymy / Hypernymy** — The hierarchy that governs page architecture. Broad (hypernym) at root level. Narrow (hyponym) at supporting page level. This hierarchy runs through URLs, heading levels, and page depth simultaneously.

**Synonymy** — Variation without repetition. Use synonym pairs in titles, headings, anchor text, and body content to serve multiple query phrasings while maintaining natural language. Validate collocations before substituting synonyms.

**Antonymy** — Opposite pairs signal complete coverage. Include both sides of antonymous attributes. Link antonymous pages to each other. Build comparison articles explicitly around antonymous entity pairs.

**Polysemy and Homonymy** — Disambiguation is mandatory when your entity name has multiple meanings. Use qualifiers and co-occurring vocabulary from the correct knowledge domain to eliminate ambiguity in the opening paragraph.

**Collocations and Co-occurring words** — The expected vocabulary of a knowledge domain. Using natural collocations signals expert authorship. Co-occurring words fill the statistical vocabulary floor that Google expects in complete documents.

**Prototypes** — Root and pillar pages must establish the most typical instance of the entity category before discussing variants. This matches the intent of broad, category-level queries.

**Inferred words** — Serve what the user means, not just what they typed. Expand every primary keyword through its inference pattern to identify missing H3s and FAQ sections.

**Title construction** — A lexical engineering task. Every title word is chosen through one of 11 sources, each drawing on a specific lexical relationship. Titles that fail the five-point test are incomplete.

**URL architecture** — A hypernym-hyponym hierarchy expressed in URL slugs. No duplication across levels. Correct scope at each level. Singular/plural used consistently.

---

## MODULE 3 — KEY TERMS GLOSSARY

| Term | Definition |
|---|---|
| **Hyponym** | A narrow, specific word that is a type of a broader category word (hypernym). Car is a hyponym of Vehicle. |
| **Hypernym** | A broad category word under which specific instances (hyponyms) sit. Vehicle is the hypernym of Car, Bus, Bicycle. |
| **Synonymy** | The relationship between words with the same or very similar meanings. |
| **Antonymy** | The relationship between words with opposite meanings. |
| **Polysemy** | A word that has multiple related meanings depending on context. |
| **Homonymy** | Words that share the same spelling and pronunciation but have completely unrelated meanings. |
| **Collocation** | A word combination that native/expert speakers use predictably and naturally. |
| **Co-occurring words** | Words that have a high statistical probability of appearing in the same document as the central entity. |
| **Prototype** | The most representative, typical instance of a category — the mental default when the category name is mentioned. |
| **Inferred words** | Terms and concepts that a query implies but the user did not explicitly type. |
| **Entity disambiguation** | The process of establishing which specific meaning of a polysemous or homonymous word is intended, through qualifiers and domain-specific co-occurring vocabulary. |
| **Substitute term** | A synonym used in place of the primary keyword to serve alternative query phrasings without repetition. |

---

## MODULE 3 — SELF-ASSESSMENT QUESTIONS

1. You are building a site about `coffee`. Your Central Entity is coffee. Map the hypernym-hyponym hierarchy for coffee from root page down to two levels of supporting articles. Show at least 3 hyponyms at each level.

2. The keywords `heater cost Pakistan`, `heater price Pakistan`, and `heater rates Pakistan` all have the same intent. How does synonymy allow you to serve all three on one page? What synonym terms would you use and where?

3. Your article is about `AC maintenance`. Write a weak opening sentence (polysemous risk) and then rewrite it with full entity disambiguation in one sentence.

4. For the entity `eye exam`, identify:
   - 5 natural collocations from the eye care knowledge domain
   - 5 co-occurring words that should appear in any expert eye exam article
   - The prototype for `eye exam` that a root page must establish first

5. The keyword `gas heater` is not a homonym — but `gas` alone is polysemous (gas the fuel vs gas the state of matter vs gas as in gasoline). How would you write the opening paragraph of a gas heater article to disambiguate all three alternative meanings in one sentence?

6. Apply the inference pattern to `best baby food for 6 months`. What are the 6 most likely inferred needs Google adds to this query? How would you serve each as an H3 in a content brief?

7. Build a complete title for an article about `oil-filled heater price in Pakistan` using the 11-source title construction system. Identify which lexical relationship each term in your title draws from.

---

*Next: Module 4 — Entity Research and Attribute Evaluation*
