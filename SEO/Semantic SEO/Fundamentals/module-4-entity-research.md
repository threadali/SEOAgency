# MODULE 4 — Entity Research and Attribute Evaluation
## The EAV Model in Practice

> **Purpose of this module:** If Module 2 maps the query territory and Module 3 teaches the vocabulary system, Module 4 teaches you what to actually put inside the content. Entity research is the process of discovering everything Google already knows about your subject — and then structuring your content to confirm, extend, and be consistent with that knowledge. The EAV model (Entity → Attribute → Value) is the framework that makes this systematic. By the end of this module, you produce a complete entity map for your central entity — the document that feeds every content brief you ever write.

---

## LESSON 4.1 — What is an Entity?

### The Technical Definition

An entity is any distinct, clearly defined thing that exists in the world and can be uniquely identified. Entities can be:

- **Physical objects** — a gas heater, a car, the Eiffel Tower
- **People** — Imran Khan, Marie Curie, a doctor
- **Places** — Lahore, Pakistan, the Sahara Desert
- **Organisations** — Gree Electric, Google, University of Oxford
- **Concepts** — inflation, photosynthesis, democracy
- **Events** — Eid, the 2024 Olympics, a product launch
- **Products** — iPhone 16, Gree GH-1800 gas heater, Panadol
- **Services** — eye examination, LASIK surgery, SEO consulting

**The defining characteristic of an entity:** it can be given a unique identifier in Google's Knowledge Graph. It is distinct from all other things. It has known attributes with known values.

### Entities vs Keywords — The Practical Difference

This distinction was introduced in Module 0. In Module 4, you apply it at the research level.

| Thinking in Keywords | Thinking in Entities |
|---|---|
| "My keyword is gas heater price Pakistan" | "My entity is Gas Heater. My target attribute is Price. My context is Pakistan." |
| "I need to use this phrase 15 times" | "I need to cover all root attributes of Gas Heater with verified values" |
| "Write about gas heater" | "Cover Entity: Gas Heater — Attributes: Type, Wattage, Fuel, Safety, Price, Brand, Room Size, Maintenance — with specific Values for each" |
| "Length = 2,000 words" | "Completeness = all root attributes covered with numeric values and examples" |

The entity thinking column produces documents that rank. The keyword thinking column produces documents that miss ranking by just enough that you can never figure out why.

### Google's Knowledge Graph and Your Content

Google's Knowledge Graph is a database of billions of entities and the relationships between them. Every entity in the graph has:

- A unique identifier (e.g. `Q193741` for "heater" in Wikidata)
- Known attributes (properties that belong to this entity)
- Known values for those attributes (data associated with each property)
- Relationships to other entities (a gas heater is manufactured by Gree, which is headquartered in Zhuhai, China)

When Google processes your article, it is extracting EAV triplets from your content and comparing them against its Knowledge Graph. It asks:

1. **Is this content consistent with what we know about this entity?** (Accuracy check)
2. **Does this content cover the attributes we expect expert coverage to include?** (Completeness check)
3. **Does this content add new, verifiable information about this entity?** (Information gain check)

Pass all three checks and your document is ranked as authoritative. Fail any one and your document is ranked below those that pass.

---

## LESSON 4.2 — The EAV Model: Entity → Attribute → Value

### The Structure

Every piece of rankable information can be expressed as one EAV triplet:

```
Entity     →    Attribute           →    Value
--------        ---------                -----
Gas Heater  →   Type                →    Convection, Radiant, Infrared
Gas Heater  →   Wattage             →    800W, 1000W, 1500W, 2000W, 3000W
Gas Heater  →   Fuel Type           →    LPG (Liquefied Petroleum Gas), Natural Gas
Gas Heater  →   Room Coverage       →    150 sq ft (1500W), 250 sq ft (2000W)
Gas Heater  →   Safety Features     →    ODS (Oxygen Depletion Sensor), Tip-over switch, Auto shut-off
Gas Heater  →   Price Range (PKR)   →    PKR 8,500 – PKR 45,000
Gas Heater  →   Top Brands (Pak)    →    Gree, Orient, Dawlance, Super Asia, Nasgas
Gas Heater  →   Heat Output         →    2,730 BTU (800W), 5,118 BTU (1500W)
Gas Heater  →   Energy Efficiency   →    75%–92% depending on heater type
Gas Heater  →   Weight              →    3.5 kg – 12 kg depending on model
Gas Heater  →   Dimensions          →    Varies by model; avg 35cm × 25cm × 50cm
Gas Heater  →   Warranty (Pakistan) →    1 year parts + labour (standard), 2 years (premium)
Gas Heater  →   Maintenance         →    Annual servicing, burner cleaning, filter check
Gas Heater  →   Installation        →    No fixed installation (portable), or flue pipe required
Gas Heater  →   Indoor Safety       →    Ventilation required; CO risk without ODS
```

This is an entity map. It is not an article outline. It is a **complete inventory of what an expert knows about this entity** — before any content is written.

### Why You Build the Entity Map Before the Brief

The content brief is derived from the entity map — not the other way around. Most agencies write briefs based on competitor content analysis. The problem: if competitors are all missing the same attributes, every brief derived from competitor analysis will miss those same attributes.

**Entity research is independent of competitor content.** You research the entity directly — from manufacturer specifications, academic sources, industry standards, and Google's Knowledge Graph itself — and produce a complete attribute map. Then you check competitors to see which attributes they cover. The gap between competitor coverage and your entity map is your **information gain opportunity**.

### EAV in Practice — The Three Working Documents

Entity research produces three working documents that feed directly into Module 5 (Mind Map), Module 7 (Topical Map), and Module 8 (Content Brief):

**Document 1 — Master EAV Table**
All attributes of the central entity with all known values. This is the complete knowledge base.

**Document 2 — Attribute Priority Rankings**
Each attribute evaluated against the three-criteria framework (Prominent / Popular / Relevant). Determines Core vs Outer placement.

**Document 3 — Information Gain Audit**
For each attribute, a comparison of what top competitors cover vs what your entity map contains. Gap = information gain opportunity.

---

## LESSON 4.3 — The Three Types of Attributes

Not all attributes are equal. Attributes differ in how universally they apply to instances of the entity, and that difference determines how you use them in your content architecture.

### Type 1 — Root Attributes

**Definition:** Attributes that appear in ALL instances of the entity. Every single instance of this entity has this attribute — without exception.

**SEO value: Highest.** Root attributes define what the entity fundamentally is. A document that does not cover root attributes is incomplete by definition — no matter how long it is.

**Examples for Gas Heater:**

| Root Attribute | Why It Is Root (Universal) |
|---|---|
| Wattage / Heat Output | Every gas heater has a wattage rating |
| Fuel Type | Every gas heater uses a specific fuel |
| Safety Features | Every gas heater (by legal standard) has safety mechanisms |
| Physical Dimensions | Every gas heater has measurable dimensions |
| Weight | Every gas heater has a weight |
| Price | Every gas heater has a retail price |
| Manufacturer / Brand | Every gas heater is made by a brand |
| Intended Use | Every gas heater is designed for a specific use context |

**Where to use root attributes:** Core section articles — pillar pages and the ontology root page. These are the attributes that define the entity at its most fundamental level. Pillar page coverage must include ALL root attributes.

### Type 2 — Rare Attributes

**Definition:** Attributes that appear in SOME instances of the entity, but not all.

**SEO value: Medium.** Rare attributes differentiate specific sub-types or models. They are valuable for supporting articles targeting specific instances or niches.

**Examples for Gas Heater:**

| Rare Attribute | Why It Is Rare (Not Universal) |
|---|---|
| Electronic ignition | Only some models (many use manual ignition) |
| Remote control | Only premium models |
| Smart connectivity (WiFi) | Only smart heaters |
| Built-in timer | Only select models |
| Dual fuel compatibility | Only some models support both LPG and natural gas |
| Flue pipe requirement | Only some types (flueless vs flued heaters) |
| Catalytic converter | Only catalytic infrared heaters |

**Where to use rare attributes:** Supporting articles targeting specific model types or premium feature comparisons. Example: "Gas Heaters with Remote Control in Pakistan" or "Smart WiFi Gas Heaters: Is the Premium Worth It?"

### Type 3 — Unique Attributes

**Definition:** Attributes that apply to ONLY one specific instance of the entity — or a very small subset.

**SEO value: Targeted.** Unique attributes are the raw material for long-tail content, product review pages, model-specific comparison articles, and FAQ answer generation.

**Examples for Gas Heater:**

| Unique Attribute | Why It Is Unique |
|---|---|
| Gree GH-1800 flame colour | Specific to one model |
| Orient OGH-2300 gas consumption rate | Specific to one model |
| Nasgas NG-DELUXE ceramic panel technology | Specific to one brand/model |
| Colour options for Dawlance DH-1500 | Specific to one product line |

**Where to use unique attributes:** Product review articles, model specification pages, and model comparison articles. These are the deepest nodes in the URL architecture.

**Critical rule:** Unique attributes are never placed on pillar pages. They belong at the deepest supporting article level. Placing model-specific unique attributes on a pillar page dilutes the pillar page's macro context and pulls it toward a product review instead of category authority.

### The Attribute Type Map

```
ENTITY: Gas Heater
│
├── ROOT ATTRIBUTES (cover on all pillar + core pages)
│   Wattage, Fuel Type, Safety Features, Price, Brand, Dimensions,
│   Heat Output, Intended Use, Weight
│
├── RARE ATTRIBUTES (cover on specific supporting pages)
│   Electronic ignition, Remote control, WiFi, Timer, Dual fuel,
│   Flue pipe, Catalytic converter
│
└── UNIQUE ATTRIBUTES (cover on deep supporting / review pages)
    Model-specific specs, Brand-specific technologies,
    SKU-level colour options, Specific model gas consumption rates
```

---

## LESSON 4.4 — The Three-Criteria Attribute Evaluation Framework

Having a complete list of all attributes is necessary but not sufficient. You must evaluate each attribute to determine whether it deserves a place in the Core section, the Outer section, or should be excluded from the topical map entirely.

The three-criteria framework evaluates every attribute on three dimensions. All three must be satisfied for Core section placement.

### Criterion 1 — Prominent

**Question:** Is this attribute so central to the entity that the entity cannot be fully understood without it?

**Test:** Remove this attribute from your knowledge of the entity. Is the entity now fundamentally incomplete? Is a user who searches for this entity likely to be left with an unanswered question if this attribute is absent?

**Yes = Prominent.**

```
Gas Heater — Prominent attributes:
✓ Wattage — you cannot evaluate a heater without knowing its power output
✓ Fuel Type — fundamentally changes what the heater is and how it is used
✓ Safety Features — a non-negotiable concern for any buyer
✓ Price — a purchase decision is impossible without it

Gas Heater — Non-prominent attributes:
✗ Colour options — cosmetic; does not affect function or purchase decision
✗ Remote control availability — a nice-to-have, not a core need
✗ Smart connectivity — only relevant to a small user segment
```

### Criterion 2 — Popular

**Question:** Does this attribute have meaningful search demand? Do users actually search for information about this attribute in relation to the entity?

**Test:** Check Google Autocomplete for `[entity] [attribute]`. Check PAA and search volume data. Is there a query cluster around this attribute?

**Yes = Popular.**

```
Gas Heater — Popular attributes:
✓ Price — "gas heater price Pakistan" → significant search volume
✓ Types — "types of gas heaters" → significant search volume
✓ Wattage — "gas heater wattage" → significant search volume
✓ Safety — "is gas heater safe indoors" → significant PAA coverage

Gas Heater — Non-popular attributes:
✗ Manufacturing date codes — no user searches for this
✗ Packaging dimensions — no user searches for this
✗ Factory country of origin — minimal search volume
```

### Criterion 3 — Relevant

**Question:** Is this attribute connected to your Source Context and Central Search Intent?

**Test:** Does covering this attribute serve the audience defined in your Website Identity Document? Does it connect to the monetisation model and the user purpose you defined in Module 1?

**Yes = Relevant.**

```
Gas Heater — Relevant attributes (heater retailer, Pakistan, price-conscious buyers):
✓ Price — directly serves the "most affordable price" source context
✓ Energy Cost — directly serves the buyer's concern about running costs
✓ Pakistani Brands — directly serves the Pakistan market context
✓ Room Size Matching — directly serves the buyer's practical decision need

Gas Heater — Non-relevant attributes (for this specific source context):
✗ Industrial BTU ratings — wrong audience (commercial, not residential)
✗ HVAC integration — wrong audience (professional installer, not homeowner)
✗ Export regulations — irrelevant to Pakistani retail buyer
```

### The Evaluation Matrix

For every attribute in your master EAV table, score it:

```
ATTRIBUTE EVALUATION MATRIX
============================
Entity: Gas Heater
Source Context: Pakistani home appliance retailer, affordable, residential buyers

Attribute              | Prominent | Popular | Relevant | Section     | Priority
-----------------------|-----------|---------|----------|-------------|----------
Type                   |     ✓     |    ✓    |    ✓     | CORE        | HIGH
Wattage                |     ✓     |    ✓    |    ✓     | CORE        | HIGH
Price                  |     ✓     |    ✓    |    ✓     | CORE        | HIGH
Safety Features        |     ✓     |    ✓    |    ✓     | CORE        | HIGH
Fuel Type              |     ✓     |    ✓    |    ✓     | CORE        | HIGH
Room Size Coverage     |     ✓     |    ✓    |    ✓     | CORE        | HIGH
Pakistani Brands       |     ✓     |    ✓    |    ✓     | CORE        | HIGH
Energy Cost            |     ✓     |    ✓    |    ✓     | CORE        | HIGH
Maintenance            |     ✗     |    ✓    |    ✓     | OUTER       | MEDIUM
Installation           |     ✗     |    ✓    |    ✓     | OUTER       | MEDIUM
Electronic Ignition    |     ✗     |    ✓    |    ✗     | OUTER       | LOW
Remote Control         |     ✗     |    ✓    |    ✗     | OUTER       | LOW
Smart WiFi             |     ✗     |    ✓    |    ✗     | OUTER       | LOW
Colour Options         |     ✗     |    ✗    |    ✗     | EXCLUDE     | —
Factory Date Codes     |     ✗     |    ✗    |    ✗     | EXCLUDE     | —
Packaging Dimensions   |     ✗     |    ✗    |    ✗     | EXCLUDE     | —
```

**Three ✓ = Core section**
**Two ✓ = Outer section or targeted supporting article**
**One or zero ✓ = Excluded from topical map**

---

## LESSON 4.5 — How to Find Attributes: Five Research Methods

The evaluation framework is only as good as your initial attribute list. An incomplete attribute list produces an incomplete topical map — regardless of how well you evaluate what you do find. These five methods ensure you find everything.

### Method 1 — Google's Knowledge Graph and Structured Data

**Source:** Google search itself. When you search an entity, Google's Knowledge Panel (the box on the right side of SERP) shows the attributes Google already associates with this entity.

**What to extract:**
- Every field in the Knowledge Panel
- "People also search for" suggestions inside the panel
- The schema type Google assigns to the entity (Product, Person, Place, etc.)

**Why it matters:** If Google has a Knowledge Panel attribute for your entity, it expects authoritative content to cover that attribute. Ignoring it means your content is less complete than Google's own data.

### Method 2 — Wikipedia and Wikidata

**Source:** Wikipedia article for your entity + Wikidata entry (wikidata.org — search your entity name).

**What to extract from Wikipedia:**
- Every section heading — each represents one attribute Google considers notable
- Infobox fields (the data table on the right of Wikipedia articles)
- "See also" section — adjacent entities that are related

**What to extract from Wikidata:**
- Every property listed for the entity (`P31` = instance of, `P18` = image, `P585` = point in time, etc.)
- Related entity connections (`P176` = manufacturer, `P17` = country, `P31` = type)

**Why it matters:** Wikipedia is a primary source for Google's Knowledge Graph. Its structure of knowledge about an entity closely mirrors how Google organises that entity internally.

### Method 3 — Manufacturer Specifications and Technical Standards

**Source:** Official product pages, specification sheets, industry standards bodies (ISO standards, safety certification bodies).

**What to extract:**
- Every specification listed in a product datasheet
- Technical standards that apply to this entity class (e.g. safety standards for gas appliances)
- Certification requirements (what must be tested and verified)

**Why it matters:** Manufacturer spec sheets contain the complete root attribute set for physical product entities. They are the authoritative source for technical values — wattage, BTU output, dimensions, safety certifications, fuel consumption rates.

**Example — gas heater specification sheet fields:**
```
Model number, wattage, BTU output, fuel type, gas consumption rate (m³/h),
heating coverage area, heat distribution type, safety certifications (ISO, PSB),
oxygen depletion sensor (ODS), anti-tilt switch, thermostat range, ignition type,
weight, dimensions (H × W × D), flame type, colour, warranty period
```

Every field on this spec sheet = one attribute in your EAV model.

### Method 4 — Competitor Content Analysis (Attribute Gap Mapping)

**Source:** Top 10 ranking articles for each core query cluster.

**Process:**
1. List every H2 and H3 heading from each competitor article
2. Convert each heading into an attribute name (it is the attribute being discussed)
3. Add all attributes you find to your master EAV table
4. Note which attributes appear in all 10 competitors (must-cover), which appear in 5–9 (should-cover), which appear in 1–4 (optional but differentiating)

**Why it matters:** Competitor analysis reveals the attribute floor — the minimum coverage standard the SERP currently requires. But it does not reveal the ceiling. Attributes that competitors all miss are your information gain opportunities.

**Critical distinction:** You are extracting attribute names from competitor headings, not copying their content. The values you assign to those attributes come from your own research.

### Method 5 — User-Generated Content and Forum Analysis

**Source:** Reddit, Quora, Pakistani forums (PakWheels, Hamariweb forums), product Q&A sections on e-commerce platforms (Daraz.pk for Pakistani niche).

**What to extract:**
- Questions users ask that do not appear in any competitor article
- Problems users report that no guide addresses
- Comparisons users request that no article makes
- Confusion users express about specific attributes

**Why it matters:** Forum content reveals the **rare and unique attributes** that formal competitor analysis misses. A question that appears 50 times on Daraz.pk product Q&A (`"does this heater work with natural gas or only LPG?"`) is a rare attribute (`dual fuel compatibility`) that is clearly popular with real users — but may not appear in a single competitor article.

These are your highest-value information gain opportunities.

---

## LESSON 4.6 — Information Gain: The Ceiling Above TF-IDF

### The Definition

Information gain is the unique, accurate, specific information your document contains that competing documents do not.

TF-IDF (covered in Module 2) defines the floor — the vocabulary and attribute coverage baseline that all ranking documents share.

Information gain defines the ceiling — the additional coverage that makes your document better than all competitors.

**The formula:**

```
Ranking Potential = TF-IDF Floor Compliance + Information Gain Score
```

A document that only meets the TF-IDF floor is as complete as every competitor. It has no competitive advantage. It will rank somewhere in the middle of a competitive SERP — not at the top.

A document that meets the TF-IDF floor AND adds information gain is the most complete document in the SERP. Google's information gain score rewards this with a ranking advantage.

### How Google Measures Information Gain

Google's systems assess information gain by comparing your document against the existing documents indexed for that query cluster. Specifically:

- **Unique entity-attribute-value triplets** — EAV triplets in your document that do not appear in competing documents
- **Unique statistical data** — percentages, measurements, study results not found elsewhere
- **Unique examples** — specific, named examples that illustrate the attribute in a way competitors do not
- **Unique comparisons** — entity-to-entity comparisons that competitors have not made
- **Unique perspectives** — user group-specific angles that existing content ignores

### Practical Information Gain Strategies

**Strategy 1 — Cover attributes competitors skip**

From your attribute gap audit (Method 4 in Lesson 4.5), identify attributes that appear in zero to two competitor articles. These are your information gain targets.

Example: All 10 competitor articles about gas heaters cover Types, Price, and Safety. Only 1 covers `Gas Consumption Rate (m³/h)` — the specific amount of gas a heater consumes per hour. This is an information gain opportunity. A buyer asking "how much will this cost to run per month?" needs this number. Your article includes it. Competitors do not.

**Strategy 2 — Add specific numeric values**

Competitors say: *"Gas heaters are available in various wattage options."*
You say: *"Gas heaters in Pakistan are available in 5 standard wattages: 800W, 1000W, 1500W, 2000W, and 3000W. A 1500W gas heater in a 200 sq ft room raises room temperature by approximately 10°C within 15–20 minutes at an average gas consumption of 0.18 m³ per hour."*

The second version contains five specific numeric values that the first does not. Each numeric value is a unique EAV triplet that adds to your information gain score.

**Strategy 3 — Add market-specific values**

For a Pakistani site, general information about gas heaters is the TF-IDF floor. Pakistan-specific values — prices in PKR, brands available in Pakistan, gas tariff rates by SNGPL/SSGC, typical room sizes in Pakistani housing, seasonal gas availability issues — are information gain because international competitors do not provide them.

**Strategy 4 — Add post-purchase and maintenance coverage**

Most commercial articles about products cover pre-purchase attributes only (types, price, comparison). Post-purchase content (maintenance schedules, common problems, repair cost estimates, spare parts availability in Pakistan) is almost universally absent from competitor coverage — making it a high-value information gain zone.

**Strategy 5 — Cover rare attributes for specific user segments**

A section on `gas heater safety for households with infants` or `gas heater suitability for small enclosed Pakistani apartments` serves specific user sub-groups that general competitor articles ignore entirely. These sections add information gain for searches from those specific user groups.

---

## LESSON 4.7 — Contextual Domains: Placing Your Content at the Right Depth

### The Three-Layer Model

Every entity exists within a hierarchy of contextual layers that moves from broad to specific:

```
Knowledge Domain   → The broadest field this entity belongs to
Contextual Domain  → A focused subset of the knowledge domain
Contextual Layer   → A specific depth level within the contextual domain
```

**Examples:**

| Entity | Knowledge Domain | Contextual Domain | Contextual Layer |
|---|---|---|---|
| Gas Heater | Home Appliances | Heating Appliances | Portable Gas Heaters for Pakistani Homes |
| Kopi Luwak | Beverages | Coffee | Premium Fermented Single-Origin Coffee |
| LASIK | Healthcare | Eye Care | Laser Refractive Surgical Correction |
| Ethereum | Finance | Cryptocurrency | Smart Contract Platform Assets |

### Why Contextual Layer Matters for Ranking

Google evaluates every document not just for entity-attribute coverage but for **which contextual layer the document addresses**. A document about gas heaters that addresses the Knowledge Domain level (home appliances broadly) rather than the Contextual Layer level (portable gas heaters for Pakistani homes specifically) is too broad for specific queries.

**Each page of your site should signal exactly one contextual layer.**

The root page signals the Contextual Domain level: *"This is a site about heating appliances."*
The pillar pages signal the first Contextual Layer: *"This page is about gas heaters specifically."*
The supporting articles signal the deepest Contextual Layer: *"This page is about gas heater safety for indoor use in Pakistan."*

### How Contextual Domains Connect to Source Context

The contextual layer you choose for each page must be consistent with your Source Context. A Pakistani heater retailer's contextual layer is always grounded in Pakistan-specific attributes:

- Pakistani climate patterns
- Pakistani housing types (urban apartments, single-floor homes)
- Pakistani gas infrastructure (SNGPL, SSGC networks)
- Pakistani price points (PKR)
- Pakistani brands and availability

A content that discusses gas heaters without grounding values in the Pakistani context is operating at the wrong contextual layer for its source context. It may rank internationally but not specifically for the Pakistani queries its Source Context targets.

---

## LESSON 4.8 — Question Types from Attribute Types

One of the most powerful applications of the EAV model is question generation. Each attribute type generates a predictable set of question formats. Understanding this relationship allows you to build H-tag structures in content briefs without needing to research competitors for heading ideas.

### Root Attributes → Question Types

Root attributes are universal — they generate definitional and comparative questions:

| Question Type | Example |
|---|---|
| **Definitional** (`what is`) | "What is gas heater wattage?" |
| **Enumerative** (`what are / how many`) | "What are the safety features of a gas heater?" |
| **Comparative** (`which / what is the difference`) | "Which gas heater wattage is right for my room?" |
| **Boolean** (`is / does / can`) | "Does a gas heater need ventilation?" |
| **Quantitative** (`how much / how many`) | "How much gas does a 1500W gas heater consume per hour?" |

### Rare Attributes → Question Types

Rare attributes are present only in some instances — they generate conditional and feature-specific questions:

| Question Type | Example |
|---|---|
| **Conditional** (`if / when`) | "If a gas heater has a remote control, does it cost more?" |
| **Feature-specific** (`which / what models`) | "Which gas heaters in Pakistan have electronic ignition?" |
| **Evaluation** (`is it worth`) | "Is a gas heater with WiFi connectivity worth the extra cost in Pakistan?" |

### Unique Attributes → Question Types

Unique attributes apply to specific instances — they generate model-specific and review questions:

| Question Type | Example |
|---|---|
| **Specification** (`what is the [spec] of`) | "What is the gas consumption rate of the Gree GH-1800?" |
| **Review** (`is the [model] good`) | "Is the Orient OGH-2300 gas heater good for a 300 sq ft room?" |
| **Comparison** (`[model A] vs [model B]`) | "Gree GH-1800 vs Orient OGH-2300: Which is Better?" |
| **Problem** (`[model] problem / issue`) | "Why does my Gree gas heater keep switching off?" |

### Building H-Tags from Attribute Types

This is the direct connection between entity research and content brief construction (covered in full in Module 8).

**For a Core pillar page — `Gas Heaters in Pakistan: Complete Buying Guide`:**

```
H1: Gas Heaters in Pakistan: Types, Wattage, Price, and Buying Guide 2025

H2: What is a Gas Heater? (Root attribute: Definition — Definitional question)
H2: What are the Types of Gas Heaters Available in Pakistan? (Root attribute: Type — Enumerative question)
H2: What Wattage Gas Heater Do I Need for My Room? (Root attribute: Wattage — Comparative question)
H2: How Much Does a Gas Heater Cost in Pakistan? (Root attribute: Price — Quantitative question)
H2: Which Gas Heater Brands are Available in Pakistan? (Root attribute: Brand — Enumerative question)
H2: Is a Gas Heater Safe to Use Indoors? (Root attribute: Safety — Boolean question)
H2: How Much Gas Does a Gas Heater Consume? (Root attribute: Fuel Consumption — Quantitative question)

H2: Gas Heaters with Remote Control in Pakistan (Rare attribute: Remote control — Feature-specific question)
H2: Smart Gas Heaters with WiFi in Pakistan (Rare attribute: Smart connectivity — Feature-specific question)
```

Notice:
- Root attribute questions appear first (mandatory coverage)
- Rare attribute questions appear lower (they narrow the contextual layer)
- No unique attributes appear on this pillar page (they belong on dedicated supporting articles)

---

## LESSON 4.9 — Building the Master Entity Map

### The Deliverable for This Module

The Master Entity Map is the document that feeds every content brief, every topical map entry, and every mind map branch for your central entity. It is built once per entity — and updated as new attributes or values are discovered.

### Master Entity Map Template

```
MASTER ENTITY MAP
==================
Entity: [Central Entity Name]
Entity Type: [Product / Service / Concept / Place / Person / Event]
Knowledge Domain: [Broad field]
Contextual Domain: [Focused subset]
Source Context Contextual Layer: [Your specific site's depth level]

---

SECTION A — ROOT ATTRIBUTES
(Cover on ALL Core section pages and pillar pages)

Attribute 1: [Name]
  Type: Root
  Evaluation: Prominent ✓ | Popular ✓ | Relevant ✓
  Values: [All known values with specific data]
  Questions generated: [List question types this attribute produces]
  Information gain opportunity: [What competitors miss about this attribute]

Attribute 2: [Name]
  [Same structure]

[Continue for all root attributes]

---

SECTION B — RARE ATTRIBUTES
(Cover on specific targeted supporting articles)

Attribute X: [Name]
  Type: Rare
  Evaluation: Prominent ✗ | Popular ✓ | Relevant ✓
  Appears in: [Which instances / sub-types]
  Values: [Values for applicable instances]
  Questions generated: [List question types]
  Target page: [Which supporting article covers this]

[Continue for all rare attributes]

---

SECTION C — UNIQUE ATTRIBUTES
(Cover on deep supporting articles / product review pages)

Attribute Y: [Name]
  Type: Unique
  Applies to: [Specific instance / model / brand]
  Values: [Specific values for this instance]
  Questions generated: [Model-specific questions]
  Target page: [Product/review page]

[Continue for all unique attributes]

---

SECTION D — ENTITY RELATIONSHIPS
(Related entities that share semantic connections)

Related Entity 1: [Name]
  Relationship type: [is manufactured by / is used with / competes with / is a type of]
  Relevance to source context: [Why this relationship matters for your site]
  Content opportunity: [What article or section this relationship generates]

[Continue for all related entities]

---

SECTION E — INFORMATION GAIN OPPORTUNITIES
(Attributes and values that competitors miss)

Gap 1: [Attribute/value competitors miss]
  Evidence: [Which competitor articles lack this]
  Opportunity: [How to cover it in your content]
  Expected gain: [Which query cluster this helps rank for]

[Continue for all gaps identified]

---

SECTION F — CONTEXTUAL DOMAIN MAP
(How this entity connects to adjacent knowledge)

Knowledge domain intersections: [Other fields this entity touches]
Contextual layer for source context: [Exact depth this site operates at]
Out-of-scope contextual layers: [Layers this site must not enter]
```

---

## LESSON 4.10 — Completed Entity Map Example

**Entity:** Gas Heater
**Source Context:** Pakistani home appliance retailer, affordable residential, urban buyers

```
MASTER ENTITY MAP
==================
Entity: Gas Heater
Entity Type: Product
Knowledge Domain: Home Appliances / Heating Technology
Contextual Domain: Portable Heating Appliances
Source Context Contextual Layer: Affordable portable gas heaters
                                 for Pakistani urban residential use

---

SECTION A — ROOT ATTRIBUTES

Attribute: Type
  Type: Root
  Evaluation: Prominent ✓ | Popular ✓ | Relevant ✓
  Values: Convection, Radiant/Infrared, Catalytic Infrared,
          Blue Flame (natural convection), Flueless, Flued
  Questions: What are the types of gas heaters? (Enumerative)
             Which type of gas heater is best for home? (Comparative)
  Info gain: Most competitors only list 2–3 types.
             Full list of 6 types with use-case matching is the gap.

Attribute: Wattage / Heat Output
  Type: Root
  Evaluation: Prominent ✓ | Popular ✓ | Relevant ✓
  Values: 800W (2,730 BTU), 1000W (3,412 BTU), 1500W (5,118 BTU),
          2000W (6,824 BTU), 3000W (10,236 BTU)
  Questions: What wattage gas heater do I need for my room? (Comparative)
             How much heat does a 1500W gas heater produce? (Quantitative)
  Info gain: Competitors give wattage without BTU equivalent or
             room size recommendation. Add both = significant gap.

Attribute: Room Size Coverage
  Type: Root
  Evaluation: Prominent ✓ | Popular ✓ | Relevant ✓
  Values: 800W → 100–120 sq ft | 1000W → 130–160 sq ft |
          1500W → 180–220 sq ft | 2000W → 250–300 sq ft |
          3000W → 350–450 sq ft
  Questions: What size heater do I need for my room? (Comparative)
  Info gain: No Pakistani competitor provides sq ft guidelines.
             All give vague "small/medium/large room" categories.

Attribute: Price Range (Pakistan)
  Type: Root
  Evaluation: Prominent ✓ | Popular ✓ | Relevant ✓
  Values: Budget (PKR 8,500–14,000), Mid-range (PKR 14,000–25,000),
          Premium (PKR 25,000–45,000+) — as of 2025
  Questions: How much does a gas heater cost in Pakistan? (Quantitative)
             What is the cheapest gas heater in Pakistan? (Comparative)
  Info gain: Most articles have outdated prices. Current PKR prices
             with brand-wise breakdown = high information gain.

Attribute: Safety Features
  Type: Root
  Evaluation: Prominent ✓ | Popular ✓ | Relevant ✓
  Values: ODS (Oxygen Depletion Sensor), Tip-over auto-shutoff,
          Thermostat overheating protection, Flame failure device (FFD),
          Anti-freeze function (premium models)
  Questions: Is a gas heater safe to use indoors? (Boolean)
             What safety features should a gas heater have? (Enumerative)
  Info gain: Most competitors mention ODS without explaining
             what it does or how to verify a heater has one.

Attribute: Pakistani Brands
  Type: Root (for Pakistan-contextual layer)
  Evaluation: Prominent ✓ | Popular ✓ | Relevant ✓
  Values: Gree (Chinese brand, Pakistani distribution),
          Orient (Pakistani brand, market leader in budget segment),
          Dawlance (Pakistani brand, acquired by Arçelik),
          Super Asia (Pakistani brand, value segment),
          Nasgas (Pakistani brand, gas appliance specialist),
          Waves (Pakistani brand)
  Questions: Which gas heater brands are available in Pakistan? (Enumerative)
             Which is the best gas heater brand in Pakistan? (Comparative)
  Info gain: Complete brand histories + ownership + warranty
             service networks = zero competitors cover this fully.

---

SECTION B — RARE ATTRIBUTES

Attribute: Electronic Ignition
  Type: Rare
  Evaluation: Prominent ✗ | Popular ✓ | Relevant ✓
  Appears in: Mid-range and premium models; not present in budget models
  Values: Piezoelectric ignition (manual press), Electronic auto-ignition
  Target page: "Gas Heaters with Electronic Ignition in Pakistan"

Attribute: Remote Control
  Type: Rare
  Evaluation: Prominent ✗ | Popular ✓ | Relevant ✗ (niche audience)
  Appears in: Premium models only (PKR 30,000+)
  Target page: Not a standalone page; FAQ section in buying guide.

---

SECTION C — UNIQUE ATTRIBUTES (Sample)

Attribute: Gree GH-1800 Gas Consumption Rate
  Type: Unique
  Applies to: Gree GH-1800 model specifically
  Values: 0.18 m³/h at full power; 0.11 m³/h at thermostat minimum
  Target page: "Gree GH-1800 Review: Specifications, Price, and Gas Consumption"

---

SECTION D — ENTITY RELATIONSHIPS

Related Entity: LPG (Liquefied Petroleum Gas)
  Relationship: Gas heater uses LPG as primary fuel
  Content opportunity: "LPG vs Natural Gas for Heaters in Pakistan"

Related Entity: SNGPL / SSGC (Pakistani gas utilities)
  Relationship: Gas availability infrastructure context
  Content opportunity: "Gas Heater Running Cost in Pakistan: SNGPL/SSGC Tariff Guide"

Related Entity: Carbon Monoxide
  Relationship: Safety risk entity associated with gas combustion
  Content opportunity: "Carbon Monoxide Risk from Gas Heaters: What Pakistani Homeowners Must Know"

---

SECTION E — INFORMATION GAIN OPPORTUNITIES

Gap 1: Wattage-to-room-size guide (Pakistan sq ft standard)
  Evidence: Zero competitors provide specific sq ft figures
  Opportunity: Original table with Pakistani room size benchmarks
  Expected gain: Ranks for "what size heater for X room" query cluster

Gap 2: Monthly gas running cost calculator
  Evidence: No competitor provides PKR running cost estimates
  Opportunity: Table of monthly gas cost by wattage + SNGPL/SSGC tariff rate
  Expected gain: Ranks for "gas heater running cost Pakistan" cluster

Gap 3: Brand warranty and service network comparison
  Evidence: No competitor covers post-purchase service availability
  Opportunity: Table of brand + warranty period + service centre cities
  Expected gain: Ranks for "gas heater warranty Pakistan" queries
```

---

## MODULE 4 — SUMMARY

Entity research is not competitor analysis. It is the systematic discovery of everything an entity is — every attribute, every value, every relationship — built from primary sources before a single competitor page is consulted.

**The EAV model** structures all knowledge about an entity into Entity → Attribute → Value triplets. Every article is built from a selection of these triplets.

**Three attribute types** determine where each attribute appears in your site:
- Root attributes → Core / pillar pages (mandatory coverage)
- Rare attributes → Targeted supporting articles
- Unique attributes → Deep review / model-specific pages

**The three-criteria evaluation framework** (Prominent, Popular, Relevant) determines which attributes earn a place in the Core section, the Outer section, or nowhere at all.

**Five research methods** ensure complete attribute discovery: Knowledge Graph, Wikipedia/Wikidata, manufacturer specs, competitor gap analysis, and user-generated content.

**Information gain** is the ceiling above TF-IDF. It comes from covering attributes competitors miss, adding specific numeric values, adding market-specific data, and serving user sub-groups that general content ignores.

**Contextual domains** ensure every page operates at the correct depth level for its position in the site hierarchy and its source context.

**Question generation from attribute types** transforms the entity map directly into H-tag structures for content briefs — eliminating the need to copy competitor headings.

---

## MODULE 4 — KEY TERMS GLOSSARY

| Term | Definition |
|---|---|
| **Entity** | Any distinct, uniquely identifiable thing: physical object, person, place, concept, product, service, or event. |
| **EAV model** | Entity → Attribute → Value. The three-part structure of all indexable information. |
| **Root attribute** | An attribute that applies to ALL instances of an entity. Mandatory coverage on core/pillar pages. |
| **Rare attribute** | An attribute that applies to SOME instances of an entity. Covered on targeted supporting articles. |
| **Unique attribute** | An attribute that applies to only ONE specific instance. Covered on deep review/model pages. |
| **Prominent** | First criterion: the entity cannot be fully understood without this attribute. |
| **Popular** | Second criterion: meaningful search demand exists for this attribute in relation to the entity. |
| **Relevant** | Third criterion: the attribute connects to your source context and central search intent. |
| **Information gain** | The unique, accurate, specific data your document contains that competing documents do not. |
| **TF-IDF floor** | The baseline attribute and vocabulary coverage that all ranking documents share. |
| **Knowledge Graph** | Google's internal database of entities, their attributes, values, and inter-entity relationships. |
| **Contextual layer** | The specific depth level at which a document operates within its contextual domain. |
| **Knowledge domain** | The broadest field an entity belongs to. |
| **Contextual domain** | A focused subset of the knowledge domain. |
| **Entity map** | The complete structured document of all attributes and values for a central entity — the foundation of all content briefs. |

---

## MODULE 4 — SELF-ASSESSMENT QUESTIONS

1. An agency says: *"We researched our competitors' articles and built a content brief from their headings."* What is the structural problem with this approach from an entity research perspective? What should they have done instead?

2. Build a partial EAV table for the entity `Eye Exam`. Include at minimum: 5 root attributes with values, 3 rare attributes with values, and 2 unique attributes. Classify each as Root/Rare/Unique and explain why.

3. Apply the three-criteria framework to these 5 attributes of `Baby Food`:
   - Nutritional content
   - Age range suitability
   - Packaging colour
   - Organic certification
   - Brand country of origin
   For each: score Prominent/Popular/Relevant and assign to Core, Outer, or Exclude.

4. You are researching `baby food` for a Pakistani retailer. Competitor articles all cover Types, Age Range, and Brands. Your Wikidata and manufacturer research reveals these attributes no competitor covers: protein content per serving, shelf life without refrigeration, heavy metal testing certifications, and recommended daily serving frequency by WHO guidelines. Classify each as information gain opportunity. Which query clusters would each help rank for?

5. A gas heater article uses this sentence: *"Gas heaters are available in various heating capacities."* Rewrite it using two specific EAV triplets to produce an information gain score above competitors.

6. Why must unique attributes never appear on pillar pages? Give a concrete example of what goes wrong when they do.

7. What is the difference between a contextual domain and a contextual layer? Give one example where operating at the wrong contextual layer causes a page to rank for the wrong queries.

---

*Next: Module 5 — The Mind Map*
