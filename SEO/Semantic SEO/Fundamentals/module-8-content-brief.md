# MODULE 8 — Content Brief Construction
## The Document That Makes or Breaks the Article Before a Word Is Written

> **Purpose of this module:** A content brief is not a writing prompt. It is a precision engineering document. When a writer opens a brief, every structural decision has already been made: what the article covers, how deep it goes, which headings it has, which format each section uses, which entities must appear, which terms are required by TF-IDF analysis, which data points create information gain, where internal links go, and what the featured snippet target looks like. The writer's job is execution — not planning. The brief planner's job is everything in this module.

---

## LESSON 8.1 — What a Brief Must Accomplish

### The Three Guarantees of a Complete Brief

A well-built content brief guarantees three things before the writer types a single word:

**Guarantee 1 — Scope control**
The brief defines exactly what this article covers and what it does not cover. A writer who finishes a brief-compliant article has produced an article with exactly one macro context, the correct entity-attribute focus, and no scope creep into adjacent topics.

**Guarantee 2 — Quality floor**
The brief sets a minimum quality standard through TF-IDF required terms, information gain targets, format codes, and entity coverage requirements. An article that satisfies every brief requirement meets the quality floor of a competitive ranking document.

**Guarantee 3 — Architectural integrity**
The brief connects the article to the site's architecture — the correct URL, the correct parent CMap page, the correct internal links with the correct anchor text. A brief-compliant article integrates into the site's semantic cluster without creating structural conflicts.

### What a Brief Is Not

A brief is **not** a content outline the writer fills with their own knowledge. It is a specification document — the equivalent of an architect's blueprint that a builder follows. The builder does not redesign the building. The writer does not redesign the article.

If the brief is wrong, the article is wrong — no matter how skilled the writer. Brief quality is the primary determinant of article quality in any system that produces content at scale.

---

## LESSON 8.2 — The 20 Components of a Complete Brief

A complete brief has 20 components. Every component is mandatory. A brief with missing components is an incomplete brief — it will produce an incomplete article.

### Component 1 — Topic Statement

**What it is:** The entity + attribute + context that this article covers, expressed as a plain statement — not a keyword, not a title.

**Why it exists:** Forces the brief builder to confirm the exact scope before any other decision is made. If the topic cannot be stated as a clear entity-attribute-context triplet, the article has no macro context and cannot be briefed.

**Format:**
```
Topic: Entity: [name] | Attribute: [name] | Context: [qualifier]

Example:
Topic: Entity: Gas Heater | Attribute: Types | Context: Pakistan, residential buyers
```

---

### Component 2 — Section Classification

**What it is:** Core or Outer — carried forward from the Topical Map entry.

**Why it exists:** Determines the depth standard, the quality threshold, and the information gain requirement for this article.

```
Core → Maximum depth. Full EAV coverage. Mandatory information gain.
Outer → Adequate coverage. Accurate and useful. Lower depth standard.
```

---

### Component 3 — Parent CMap Page

**What it is:** The exact CMap page ID and URL that this article sits beneath.

**Why it exists:** Locks the URL inheritance, confirms the crawl depth position, and defines which page this article links upward to.

```
Parent CMap Page: P-01 | /heaters/gas-heater/types/
```

---

### Component 4 — Target URL

**What it is:** The exact URL for this article — inheriting from the parent CMap URL.

**Rules applied:**
- No duplication of terms from parent URL
- Correct depth level for this article's position
- Hyponym-level term at node position
- Short, logical, entity-attribute aligned

```
Target URL: /heaters/gas-heater/types/infrared-gas-heater/
```

---

### Component 5 — Title Tag (H1)

**What it is:** The final title — not a working title. Built using the 11-source title construction system from Module 3.

**The 5-point title test (must pass before brief is finalised):**
```
1. Contains central entity at correct hyponymy level for this page? ✓/✗
2. Contains the primary attribute this page covers? ✓/✗
3. Includes at least one synonym or substitute term for the attribute? ✓/✗
4. Includes context (geographic, temporal, or audience qualifier)? ✓/✗
5. Serves at least one inferred need of the primary query? ✓/✗
```

Any fail = revise before brief is issued.

```
Title: Infrared Gas Heater in Pakistan — How It Works, Price Range, and Best Models 2025
Test: Entity (Infrared Gas Heater) ✓ | Attribute (How It Works + Price) ✓ |
      Synonym (Price Range) ✓ | Context (Pakistan + 2025) ✓ | Inferred (Best Models) ✓
```

---

### Component 6 — Meta Description

**What it is:** The 150–160 character description that appears in the SERP. Contains three elements: primary entity-attribute, key value proposition, and a qualifying signal (price, brand, or context).

**Format rule:** No opinion, no superlative claims ("best in the world"), no promises you can't verify. Factual + specific + actionable.

```
Meta: "Infrared gas heaters provide instant directional heat for Pakistani homes.
Compare how they work, price range (PKR 12,000–28,000), and top models from
Gree and Orient." [152 characters]
```

---

### Component 7 — Primary and Secondary Keywords

**What it is:** The primary keyword group this article targets (from Module 2 keyword grouping) and all secondary keywords served within the same macro context.

**Format:**
```
Primary KW: infrared gas heater pakistan
Secondary KWs: radiant gas heater pakistan, quartz gas heater,
               infrared heater price pakistan, best infrared gas heater,
               how does infrared heater work
```

The primary keyword is the highest-volume, most representative query from the keyword group. Secondary keywords are all other queries in the same group.

---

### Component 8 — Search Intent and Query Path Stage

**What it is:** The intent classification and the query path stage this article serves.

```
Intent: Informational (sub-intent: How-to + Definition + Comparison)
Query Path Stage: Education → Evaluation
```

This determines the format codes that dominate the article. Informational + Education = definitions, factual propositions, comparison tables. Transactional + Evaluation = product comparisons, price tables, CTAs.

---

### Component 9 — Macro Context Statement

**What it is:** One sentence — exactly — that defines what this article covers and what it does not cover. This is the brief's scope boundary. If a section a writer proposes is not within the macro context statement, it does not belong in this article.

```
Macro Context Statement:
"This article explains what infrared gas heaters are, how infrared radiant
heating works, which Pakistani brands make infrared models, what their price
range is in PKR, and which room types they are best suited for."
```

**What this statement explicitly excludes:**
- Other heater types (covered in parent pillar)
- Installation guides (separate article)
- General gas heater safety (covered in safety pillar)

---

### Component 10 — Heading Structure (H1 → H2 → H3)

This is the most labour-intensive component of the brief. Every heading must be pre-determined — the writer follows the heading structure, not invents one.

#### H1
Already defined in Component 5 (Title Tag = H1).

#### H2 Construction Rules

Every H2 must be:
- A direct component of the H1 topic (not a tangent)
- Phrased as a question (Google converts headings to questions — do it yourself)
- A unique question not copied from PAA or competitor headings
- Short-form where possible (one concept per question)
- Ordered from most fundamental to most specific (macro to micro within the article)

**The H2 ordering principle:**
```
H2 order: Definition → How it works → Types/Variants → Attributes → Comparison →
          Practical guidance → FAQ
```

Not every article needs all seven stages — but the order is always this direction. Never start with comparison before definition. Never put FAQ before the main content.

#### H3 Construction Rules

Every H3 must be:
- A contextual bridge from its parent H2 (not a topic jump)
- More specific than the H2 (hyponym of the H2's concept)
- Also phrased as a question
- Assigned a format code

**The contextual bridge rule:**
```
H2: How Does an Infrared Gas Heater Work?
  H3: What is Radiant Heat? (defines the underlying mechanism — bridges from H2)
  H3: How Does Quartz Tube Infrared Heating Work? (specific instance — bridges from H3-1)
  H3: How Is Infrared Heat Different from Convection Heat? (comparison — bridges from H3-2)
```

Each H3 narrows the focus established by the H2. The reader can follow the logic: H2 asks about the mechanism → H3-1 defines the mechanism → H3-2 explains a specific type of it → H3-3 contrasts it with an alternative.

#### Full Heading Structure Example — Infrared Gas Heater Article

```
H1: Infrared Gas Heater in Pakistan — How It Works, Price Range,
    and Best Models 2025

H2: What is an Infrared Gas Heater?
    [Format: DA + NER — definitive answer with full entity qualification]
  H3: How is an Infrared Gas Heater Different from a Convection Gas Heater?
      [Format: CE — comparative entity, side-by-side]

H2: How Does an Infrared Gas Heater Produce Heat?
    [Format: FP + EE — factual proposition + expansion of evidence]
  H3: What is Radiant Heat?
      [Format: DA — definitional answer, FS target]
  H3: How Do Quartz Tubes in Infrared Heaters Work?
      [Format: IL — instruction-style process explanation]

H2: What are the Types of Infrared Gas Heaters Available in Pakistan?
    [Format: UL with intro + items + outro]
  H3: Short-Wave Infrared Gas Heaters in Pakistan
      [Format: DA + SE]
  H3: Long-Wave Infrared (Catalytic) Gas Heaters in Pakistan
      [Format: DA + SE]

H2: What is the Price of Infrared Gas Heaters in Pakistan?
    [Format: Table — intro sentence + data + outro]
  H3: Infrared Gas Heater Price by Brand in Pakistan
      [Format: Table — brand, model, wattage, PKR price]
  H3: What Does an Infrared Gas Heater Cost to Run per Month in Pakistan?
      [Format: SE + CP — statistical + conditional]

H2: Which Infrared Gas Heater is Best for Pakistani Homes?
    [Format: DA + CE]
  H3: Best Infrared Gas Heater for Small Rooms Under 150 sq ft
      [Format: FS target — 40 words]
  H3: Best Infrared Gas Heater for Medium Rooms 150–250 sq ft
      [Format: FS target — 40 words]

H2: Is an Infrared Gas Heater Safe to Use Indoors in Pakistan?
    [Format: FP — definitive yes/no with qualification]
  H3: Does an Infrared Gas Heater Require Ventilation?
      [Format: PAA — single sentence answer first]
  H3: Does an Infrared Gas Heater Produce Carbon Monoxide?
      [Format: PAA + EE]

H2: Frequently Asked Questions About Infrared Gas Heaters in Pakistan
    [Format: FAQ — H3 questions with immediate answers]
  H3: Can an infrared gas heater heat an entire room?
  H3: How long does an infrared gas heater last?
  H3: Which infrared gas heater brand is most reliable in Pakistan?
```

---

### Component 11 — Format Codes Per Section

Every H2 and H3 in the heading structure is assigned a format code from the reference table. The format code tells the writer exactly how to structure the answer for that section.

**Format code reference (from Module 7 context):**

| Code | Format | When to Use |
|---|---|---|
| **FS** | Featured Snippet — 40 words max, 320 char limit | Direct factual questions with a single best answer |
| **PAA** | People Also Ask — single definitive sentence first | Questions that appear in PAA boxes |
| **DA** | Definitive Answer — full long-form with qualifiers | Complex definitions needing full entity coverage |
| **IL** | Instruction List — ordered, same PoST on first word | Process or how-to questions |
| **UL** | Unordered List — intro + items + outro | Category-level coverage of multiple instances |
| **Table** | Data table — definition sentence + data + outro | Attribute comparisons across multiple entities/values |
| **FAQ** | Question + immediate answer + expansion | FAQ sections and PAA-targeted questions |
| **CE** | Comparative Entity — side-by-side | Direct entity vs entity comparison |
| **SE** | Statistical Evidence — numeric + source + context | Any claim that benefits from specific data |
| **EE** | Expansion of Evidence — fact → effect → importance | After a factual statement — deepening understanding |
| **FP** | Factual Proposition — certain, no modals | Any indisputable fact stated as a declaration |
| **CP** | Conditional Proposition — declaration first, condition second | If-then relationships and conditional advice |
| **NER** | Named Entity Recognition — no pronouns, full names | Any section introducing a new entity |

**The format competition rule:** Do not use the same format for every section. Do not place the same format twice in a row unless unavoidable. Google extracts different signals from different formats — an article that is entirely paragraphs competes differently than one that mixes FS, tables, and lists strategically.

**The format placement principle:** Use the most competitive format (FS, PAA, Table) at the sections where you most want SERP feature extraction. Do not waste FS format on low-priority sections.

---

### Component 12 — Entity List with EAV Coverage

**What it is:** Every entity that must appear in this article, with its required attribute-value coverage.

This component ensures that no entity required for the article's macro context is accidentally omitted by the writer.

```
ENTITY LIST — Infrared Gas Heater Article

Entity 1: Infrared Gas Heater
  Required attributes + values:
  - Heat mechanism: radiant/infrared emission (not convection)
  - Element type: quartz tube, ceramic plate, catalytic burner
  - Wattage range: 800W–3000W
  - BTU output: 2,730–10,236 BTU
  - Pakistani brands: Gree, Orient (infrared models specifically)
  - Price range: PKR 12,000–28,000 (2025)
  - Room size suitability: 100–300 sq ft depending on wattage
  - Safety features: ODS, tip-over switch, FFD
  - Ventilation requirement: yes — partial ventilation required

Entity 2: Radiant Heat (mechanism entity)
  Required attributes + values:
  - Definition: electromagnetic wave heat transfer without convection medium
  - Wavelength: short-wave (near-infrared) vs long-wave (far-infrared)
  - Heat direction: directional (heats objects and people, not air first)

Entity 3: Quartz Tube (component entity)
  Required attributes + values:
  - Material: fused quartz
  - Function: infrared emitter when heated by gas combustion
  - Temperature: 900–1100°C operating temperature
  - Lifespan: 3,000–5,000 hours

Entity 4: Gree (brand entity — Pakistani context)
  Required attributes + values:
  - Brand type: Chinese manufacturer, Pakistan distribution
  - Infrared models available in Pakistan: GH-IR800, GH-IR1500 [verify current]
  - Price range: PKR 14,000–22,000 (infrared range)
  - Warranty: 1 year

Entity 5: Carbon Monoxide (safety risk entity — related entity)
  Required attributes + values:
  - Risk level for infrared gas heaters: present but lower than blue flame
  - Why: more complete combustion in quartz tube
  - Mitigation: partial room ventilation required
  - ODS sensor: shuts off heater at O₂ levels below 18%
```

---

### Component 13 — TF-IDF Required Terms

**What it is:** The 10–15 terms from competitor TF-IDF analysis that must appear in this article for it to be statistically complete.

These are not keywords to stuff — they are vocabulary signals. Each term appears naturally in the correct contextual position.

```
TF-IDF REQUIRED TERMS — Infrared Gas Heater Article

Must appear (70%+ competitor frequency):
1. radiant heat / radiant heating
2. quartz tube
3. infrared emission / infrared waves
4. BTU (British Thermal Unit)
5. room coverage / coverage area
6. ODS (Oxygen Depletion Sensor)
7. tip-over protection
8. fuel consumption / gas consumption
9. thermostat
10. directional heat / focused heat

Should appear (50–70% competitor frequency):
11. short-wave infrared / near-infrared
12. catalytic combustion
13. flameless operation
14. heat distribution pattern
15. ignition type (electronic / manual)
```

---

### Component 14 — Information Gain Targets

**What it is:** The specific data points, attributes, or angles that competing articles do not cover — the ceiling above TF-IDF.

Every Core section brief must have a minimum of 3 documented information gain targets. Outer section briefs need a minimum of 1.

```
INFORMATION GAIN TARGETS — Infrared Gas Heater Article

Target 1 (HIGH VALUE):
Gap: No competitor provides monthly gas running cost for infrared heaters
     in Pakistan using SNGPL/SSGC tariff rates.
Deliverable: Table showing PKR monthly running cost per wattage level at
             current 2025 gas tariff rates.
Expected benefit: Ranks for "infrared heater running cost pakistan" cluster

Target 2 (MEDIUM VALUE):
Gap: No competitor compares short-wave vs long-wave infrared heaters
     specifically for Pakistani room types (compact urban apartments).
Deliverable: Section "Which Infrared Type Suits Pakistani Apartments Best?"
             with sq ft guidance for each infrared sub-type.
Expected benefit: Serves apartment-specific user segment not covered elsewhere

Target 3 (MEDIUM VALUE):
Gap: No competitor mentions quartz tube lifespan or replacement cost in Pakistan.
Deliverable: 2 sentences in the quartz tube H3: "Quartz tubes in gas heaters
             last 3,000–5,000 operating hours. Replacement quartz tubes cost
             PKR 800–1,500 in Pakistan."
Expected benefit: Captures post-purchase query cluster "infrared heater
                  quartz tube replacement pakistan"
```

---

### Component 15 — Featured Snippet Targets

**What it is:** The specific sections in the heading structure that are targeting featured snippet extraction, with the 40-word / 320-character limit enforced.

Not every section targets a featured snippet. Only the sections with the highest likelihood of snippet extraction — direct definitional or factual questions — are assigned FS format.

```
FEATURED SNIPPET TARGETS

FS Target 1:
Heading: "What is an Infrared Gas Heater?"
Target answer (≤40 words, ≤320 chars):
"An infrared gas heater is a portable heating appliance that burns LPG or
natural gas to heat quartz tubes, which emit infrared radiation to directly
warm people and objects in a room without heating the air first."
[Word count: 38 ✓ | Char count: 218 ✓]

FS Target 2:
Heading: "What is Radiant Heat?"
Target answer (≤40 words, ≤320 chars):
"Radiant heat is electromagnetic energy transferred directly from a hot surface
to cooler objects and people without warming the surrounding air. Infrared gas
heaters produce radiant heat through quartz tubes heated by gas combustion."
[Word count: 39 ✓ | Char count: 234 ✓]

FS Target 3:
Heading: "Best Infrared Gas Heater for Small Rooms Under 150 sq ft"
Target answer (≤40 words, ≤320 chars):
"For rooms under 150 sq ft in Pakistan, an 800W–1000W infrared gas heater is
the correct size, producing 2,730–3,412 BTU. The Gree GH-IR800 and Orient
infrared 1000W models are the most widely available options."
[Word count: 38 ✓ | Char count: 220 ✓]
```

---

### Component 16 — PAA Targets

**What it is:** Questions from Google's People Also Ask box for the primary keyword — formatted as H3 headings with immediate single-sentence answers.

PAA sections use the FAQ format code: immediate definitive sentence first, then expansion.

```
PAA TARGETS — Infrared Gas Heater Article

PAA Question 1: "Does an infrared gas heater require ventilation?"
H3 heading: Does an Infrared Gas Heater Require Ventilation in Pakistan?
First sentence: "An infrared gas heater requires partial ventilation — keep
                one window slightly open during operation."
Expansion: Explain why (CO risk, O₂ consumption), ODS role, apartment considerations.

PAA Question 2: "Is infrared heater better than convection heater?"
H3 heading: Is an Infrared Gas Heater Better than a Convection Gas Heater?
First sentence: "Infrared gas heaters heat objects and people directly at higher
                efficiency for small, occupied rooms; convection heaters distribute
                heat more evenly in larger enclosed spaces."
Expansion: Use-case comparison table.

PAA Question 3: "How long does infrared heater last?"
H3 heading: How Long Does an Infrared Gas Heater Last in Pakistan?
First sentence: "An infrared gas heater lasts 8–12 years with annual servicing;
                the quartz tube element requires replacement every 3,000–5,000
                operating hours."
Expansion: Maintenance factors, brand warranty, Pakistan service availability.
```

---

### Component 17 — Internal Links Plan

**What it is:** Every internal link the article will contain — target URL, proposed anchor text, and the heading under which the link appears in the article.

Pre-planned before writing. Writers do not decide where to link. The brief decides.

```
INTERNAL LINKS PLAN

Outbound links from this article:

Link 1:
Target: /heaters/gas-heater/types/ (parent pillar — Gas Heater Types)
Anchor: "gas heater types in Pakistan"
Location: H2 "What is an Infrared Gas Heater?" — first paragraph

Link 2:
Target: /heaters/gas-heater/price/ (price pillar)
Anchor: "gas heater price in Pakistan"
Location: H2 "What is the Price of Infrared Gas Heaters in Pakistan?" — intro sentence

Link 3:
Target: /heaters/gas-heater/safety/ (safety pillar)
Anchor: "gas heater indoor safety"
Location: H2 "Is an Infrared Gas Heater Safe to Use Indoors?" — first paragraph

Link 4:
Target: /heaters/gas-heater/types/catalytic-gas-heater/ (sibling article)
Anchor: "catalytic gas heater Pakistan"
Location: H3 "Long-Wave Infrared (Catalytic) Gas Heaters in Pakistan" — last paragraph

Link 5:
Target: /heaters/gas-heater/types/ + #blue-flame-section (hash link)
Anchor: "blue flame convection heater"
Location: H2 comparison section — when contrasting with convection type

Maximum links in this article: 5–6
(Core article at depth 5 — link budget is moderate)
```

---

### Component 18 — Image Brief

**What it is:** The image requirement for the article — how many images, what each should show, and the exact alt tag for each.

Alt tags follow the representative image rule: entity + attribute + context that matches the nearest heading.

```
IMAGE BRIEF

Image 1 (H1 hero image):
Subject: An infrared gas heater in use in a Pakistani home setting
Alt tag: "infrared gas heater Pakistan — quartz tube radiant heater in home"
Placement: Below H1, above first paragraph

Image 2 (Quartz tube close-up):
Subject: Close-up of glowing quartz tube infrared element
Alt tag: "quartz tube infrared gas heater element glowing"
Placement: Under H3 "How Do Quartz Tubes in Infrared Heaters Work?"

Image 3 (Price comparison table):
Subject: Screenshot or designed table of infrared heater prices by brand
Alt tag: "infrared gas heater price Pakistan 2025 — Gree Orient brand comparison"
Placement: Adjacent to price table section

Note: No stock images of generic heaters. Images must show the specific
entity (infrared/quartz type) clearly.
```

---

### Component 19 — Content Length Guidance

**What it is:** The minimum necessary and maximum efficient word count based on attribute depth, competitor coverage, and information gain targets.

Not a target — a guardrail. Writers write what the content requires, within these bounds.

```
Content Length Guidance:

Minimum necessary: 1,400 words
Rationale: Full EAV coverage of infrared heater entity requires minimum
           12 H2+H3 sections × ~110 words average + tables and lists

Maximum efficient: 2,200 words
Rationale: All information gain targets, all FS/PAA sections, and all entity
           coverage can be completed within this range. Content beyond
           2,200 words will either dilute the semantic vector or repeat
           information already covered.

Do not exceed 2,200 words unless a new information gain opportunity
is identified that genuinely requires additional coverage.
```

---

### Component 20 — Publish Date and Author Assignment

**What it is:** The planned publish date (from Topical Map prioritisation) and the assigned author with their credential note.

```
Planned Publish Date: [Phase 3 — after Gas Heater Types pillar is live]
Author: [Name]
Credential note for byline: "Home appliance specialist with 5 years
                             reviewing heating products for the Pakistani market"
```

---

## LESSON 8.3 — The Macro Context Statement as Brief Anchor

The Macro Context Statement (Component 9) is the most important single sentence in the entire brief. Every other component is derived from it or checked against it.

**The Macro Context Statement test:**

After the full brief is built, read the Macro Context Statement and then read every H2 heading. Ask for each H2: *"Is this heading fully and exclusively within the scope defined by the Macro Context Statement?"*

```
Macro Context Statement:
"This article explains what infrared gas heaters are, how infrared radiant
heating works, which Pakistani brands make infrared models, what their price
range is in PKR, and which room types they are best suited for."

H2: What is an Infrared Gas Heater? → IN SCOPE ✓ (definition of entity)
H2: How Does an Infrared Gas Heater Produce Heat? → IN SCOPE ✓ (mechanism)
H2: What are the Types of Infrared Gas Heaters in Pakistan? → IN SCOPE ✓
H2: What is the Price of Infrared Gas Heaters in Pakistan? → IN SCOPE ✓
H2: Which Infrared Gas Heater is Best for Pakistani Homes? → IN SCOPE ✓
H2: Is an Infrared Gas Heater Safe to Use Indoors? → IN SCOPE ✓ (safety is core to purchase decision)
H2: How to Install an Infrared Gas Heater? → OUT OF SCOPE ✗ (installation is a separate article)
H2: How to Maintain an Infrared Gas Heater? → OUT OF SCOPE ✗ (maintenance is a separate article)
```

Any out-of-scope H2 is removed. Its content will be covered in the appropriate dedicated article. **This is how the brief enforces the one-page-one-macro-context rule.**

---

## LESSON 8.4 — The H2 Ordering Principle in Practice

### The Seven-Stage Content Flow

Every article in the Topical Map follows the same macro content flow. The stages that apply to a specific article depend on its entity-attribute focus — but the order never changes.

```
Stage 1 — DEFINITION
What is [entity/attribute]? Define it precisely with NER format.
Every article starts here (unless the entity is already well-established
in a supporting article where the parent pillar has already defined it).

Stage 2 — MECHANISM / HOW IT WORKS
How does [entity/attribute] work? The underlying process or principle.
Use FP + EE format. This is where information gain from entity research shines.

Stage 3 — TYPES / VARIANTS
What types or sub-categories of [entity/attribute] exist?
Use UL or IL format. Introduces the hyponyms beneath the H2's concept.

Stage 4 — ATTRIBUTES / SPECIFICATIONS
What are the key specifications of [entity/attribute]?
Use Table or DA + SE format. Numeric values required throughout.

Stage 5 — COMPARISON
How does [entity/attribute] compare to alternatives?
Use CE or Table format. Serves commercial investigation intent.

Stage 6 — PRACTICAL GUIDANCE
How does the user apply this knowledge to their decision/purchase/use?
Use IL or CP format. The action-oriented section.

Stage 7 — FAQ
What remaining questions do users have?
Use FAQ format. Answers PAA questions. Each H3 = one PAA-targeted question.
```

### Applying the Seven-Stage Flow

**Informational article (Education stage):** Stages 1, 2, 3, 4 are heavy. Stage 5 is present but lighter. Stage 6 is a brief practical guide. Stage 7 covers remaining informational questions.

**Commercial investigation article (Evaluation/Comparison stage):** Stage 1 is brief (entity is known). Stage 2 is absent or minimal. Stage 3 may be present. Stages 4 and 5 are heavy. Stage 6 is strong (decision guidance). Stage 7 covers comparison-specific questions.

**Transactional article (Transaction stage):** Stages 1–3 absent or minimal. Stage 4 is a product specification table. Stage 5 is a brief competitor comparison. Stage 6 is the primary purchase guide. Stage 7 covers objection-handling questions.

---

## LESSON 8.5 — Two Complete Briefs

### Brief A — Core Section Pillar Article

```
═══════════════════════════════════════════════════════════════════════════
CONTENT BRIEF — CORE SECTION
PakHeaters.pk | TM-01
═══════════════════════════════════════════════════════════════════════════

COMPONENT 1 — TOPIC STATEMENT
Entity: Gas Heater | Attribute: Types | Context: Pakistan, residential buyers

COMPONENT 2 — SECTION CLASSIFICATION
CORE — Maximum depth. Full EAV coverage. Mandatory information gain (3+).

COMPONENT 3 — PARENT CMAP PAGE
P-01 | /heaters/gas-heater/types/

COMPONENT 4 — TARGET URL
/heaters/gas-heater/types/

COMPONENT 5 — TITLE TAG
Gas Heater Types in Pakistan — Convection, Radiant, and Infrared Explained
[Test: Entity ✓ | Attribute ✓ | Synonym (Radiant = Infrared) ✓ |
Context (Pakistan) ✓ | Inferred (Explained) ✓]

COMPONENT 6 — META DESCRIPTION
"Compare 5 gas heater types in Pakistan: blue flame convection, radiant
infrared, catalytic, flueless, and flued. Includes wattage range, room size,
price, and which type suits each home." [159 chars]

COMPONENT 7 — KEYWORDS
Primary: gas heater types pakistan
Secondary: types of gas heaters, which type of gas heater is best,
           convection vs infrared heater pakistan, gas heater for home pakistan

COMPONENT 8 — INTENT + STAGE
Intent: Informational (Definition + Classification + Comparison)
Stage: Education

COMPONENT 9 — MACRO CONTEXT STATEMENT
"This article defines and classifies all gas heater types available in Pakistan,
covering how each produces heat, its strengths and weaknesses, the room size
and budget it is best suited for, and which Pakistani brands offer each type."

COMPONENT 10 — HEADING STRUCTURE

H1: Gas Heater Types in Pakistan — Convection, Radiant, and Infrared Explained

H2: What is a Gas Heater? [DA + NER + FS target]
  H3: How Is a Gas Heater Different from an Electric Heater? [CE]

H2: How Many Types of Gas Heaters Are Available in Pakistan? [FS target — UL]

H2: What is a Blue Flame (Convection) Gas Heater? [DA + FP]
  H3: How Does Blue Flame Convection Heating Work? [FP + EE]
  H3: What Room Size Is a Blue Flame Heater Best For? [SE + Table]
  H3: Which Pakistani Brands Make Blue Flame Gas Heaters? [UL + NER]

H2: What is a Radiant (Infrared) Gas Heater? [DA + FP]
  H3: How Does Radiant Infrared Heating Work? [FP + EE]
  H3: What Room Size Is an Infrared Heater Best For? [SE + Table]
  H3: Which Pakistani Brands Make Infrared Gas Heaters? [UL + NER]

H2: What is a Catalytic Gas Heater? [DA + FP]
  H3: Is a Catalytic Heater the Safest Gas Heater for Indoor Use? [FP + PAA]

H2: What is the Difference Between a Flueless and a Flued Gas Heater? [CE + Table]

H2: Which Type of Gas Heater Is Best for Pakistani Homes? [DA + CE]
  H3: Best Gas Heater Type for Small Rooms Under 150 sq ft [FS target]
  H3: Best Gas Heater Type for Medium Rooms 150–300 sq ft [FS target]
  H3: Best Gas Heater Type for Open-Plan Living Spaces [FS target]

H2: Gas Heater Types Comparison — Pakistan Price, Wattage, and Room Size
    [Table: type | wattage range | BTU | room size | PKR price range | brands]

H2: Frequently Asked Questions About Gas Heater Types
  H3: Can I use any gas heater type with LPG? [PAA]
  H3: Which gas heater type is most energy efficient? [PAA]
  H3: Are all gas heater types safe to use indoors in Pakistan? [PAA]

COMPONENT 11 — FORMAT CODES
[Mapped to each heading above — see heading structure]

COMPONENT 12 — ENTITY LIST WITH EAV COVERAGE
Entities required:
1. Gas Heater (category entity) — type classification, wattage range,
   fuel type, BTU output, room size, Pakistani availability
2. Blue Flame Gas Heater — mechanism, wattage (800W–3000W), brands (Orient,
   Super Asia, Dawlance), price range (PKR 8,500–22,000)
3. Infrared/Radiant Gas Heater — quartz tube, wattage, BTU, directional heat,
   brands (Gree, Orient), price (PKR 12,000–28,000)
4. Catalytic Gas Heater — flameless combustion, lower CO risk, premium price
5. Convection (mechanism entity) — air heating, circulation, even distribution
6. Radiant Heat (mechanism entity) — electromagnetic, directional, object heating
7. ODS (Oxygen Depletion Sensor) — all certified types must have it
8. Pakistani brands: Gree, Orient, Dawlance, Super Asia, Nasgas, Waves

COMPONENT 13 — TF-IDF REQUIRED TERMS
convection, radiant heat, infrared, quartz tube, BTU, wattage, room size,
ODS (Oxygen Depletion Sensor), thermostat, fuel consumption, LPG,
natural gas, catalytic, flueless, flued

COMPONENT 14 — INFORMATION GAIN TARGETS
1. Full 5-type classification (competitors cover 2–3 types only)
2. Pakistan-specific brands for each type (not generic international brands)
3. Three-way comparison table with PKR prices — unique in Pakistani SERP
4. Room size guide in sq ft calibrated to Pakistani housing — not available elsewhere

COMPONENT 15 — FEATURED SNIPPET TARGETS
FS-1: "What is a Gas Heater?" — 38 words maximum
FS-2: "How Many Types of Gas Heaters Are Available in Pakistan?" — 35 words
FS-3–5: Best type for small/medium/large rooms — 40 words each

COMPONENT 16 — PAA TARGETS
"Can I use any gas heater type with LPG?" → immediate Yes/No + which need conversion
"Which gas heater type is most energy efficient?" → immediate answer + percentage
"Are all gas heater types safe to use indoors?" → immediate No + which types + why

COMPONENT 17 — INTERNAL LINKS PLAN
→ /heaters/ (ontology root): "home heaters in Pakistan" — opening paragraph
→ /heaters/gas-heater/price/: "gas heater price comparison Pakistan" — price table section
→ /heaters/gas-heater/safety/: "gas heater indoor safety guide" — FAQ safety section
→ /heaters/gas-heater/types/infrared-gas-heater/ (child): "infrared gas heater Pakistan" — infrared H2
→ /heaters/gas-heater-vs-electric-heater/ (CMap landing): "gas heater vs electric heater" — H2 definition
Max links: 6

COMPONENT 18 — IMAGE BRIEF
Image 1 (hero): Side-by-side of blue flame and infrared heater
  Alt: "gas heater types Pakistan — blue flame vs infrared comparison"
Image 2: Diagram of convection heat circulation pattern
  Alt: "convection gas heater heat distribution Pakistan"
Image 3: Close-up of quartz tube glowing in infrared heater
  Alt: "infrared gas heater quartz tube Pakistan"
Image 4: Comparison table screenshot (or styled table image)
  Alt: "gas heater types price comparison table Pakistan 2025"

COMPONENT 19 — CONTENT LENGTH GUIDANCE
Minimum: 2,200 words (Core pillar — full 5-type coverage + 3-way table + FAQ)
Maximum: 3,200 words
Do not exceed 3,200 — information above this threshold dilutes the vector.

COMPONENT 20 — PUBLISH DATE + AUTHOR
Phase: 2 — First wave (before any Phase 3 or Phase 4 articles)
Author: [Name] — Home appliance expert, 5+ years Pakistani market coverage
═══════════════════════════════════════════════════════════════════════════
```

---

### Brief B — Outer Section Article (condensed format for comparison)

```
═══════════════════════════════════════════════════════════════════════════
CONTENT BRIEF — OUTER SECTION
PakHeaters.pk | TM-09
═══════════════════════════════════════════════════════════════════════════

TOPIC: Gas Heater | User Segment: Small Apartments | Context: Pakistan

SECTION: OUTER — adequate depth, accurate and useful, links to 3+ Core articles

PARENT CMAP: P-03 (/heaters/gas-heater/wattage/)

URL: /heaters/gas-heater/wattage/small-apartment-heater/

TITLE: Best Gas Heater for Small Apartments in Pakistan — Under 200 sq ft Guide
[Test: Entity ✓ | Attribute (best for segment) ✓ | Synonym (Guide) ✓ |
Context (Pakistan + sq ft) ✓ | Inferred (top picks) ✓]

META: "Choosing a gas heater for a small Pakistani apartment under 200 sq ft?
      800W–1000W models, safety considerations, and top picks from Gree
      and Orient." [149 chars]

PRIMARY KW: gas heater for small room pakistan
SECONDARY KWs: small apartment heater pakistan, 800w heater, 1000w heater room size

INTENT: Commercial | STAGE: Evaluation → Comparison

MACRO CONTEXT: "This article helps Pakistani residents of small apartments
under 200 sq ft select the correct gas heater wattage and model, covering
safety precautions specific to small enclosed spaces."

HEADING STRUCTURE:
H1: Best Gas Heater for Small Apartments in Pakistan — Under 200 sq ft Guide
H2: What Wattage Gas Heater Is Needed for a Room Under 200 sq ft? [FS — 40 words]
H2: Is a Gas Heater Safe in a Small Apartment in Pakistan? [FP + PAA]
  H3: What Ventilation Does a Gas Heater Need in a Small Room? [CP]
  H3: Does Room Size Affect Carbon Monoxide Risk from a Gas Heater? [FP + SE]
H2: Best Gas Heater Models for Small Pakistani Apartments [Table]
  H3: Best 800W Gas Heater Pakistan [DA + SE]
  H3: Best 1000W Gas Heater Pakistan [DA + SE]
H2: Gas Heater vs Oil-Filled Heater for Small Apartments in Pakistan [CE]
H2: Frequently Asked Questions [FAQ]
  H3: Can a gas heater heat a 10x10 ft room in Pakistan?
  H3: Is an infrared or convection heater better for a small room?

ENTITY LIST: Gas Heater (800W, 1000W models), small apartment (Pakistani
             urban context, 100–200 sq ft), ODS sensor, ventilation,
             Gree (specific 800W/1000W models), Orient (specific models)

TF-IDF TERMS: wattage, room size, sq ft, BTU, ventilation, ODS,
              thermostat, energy consumption, small room, compact

INFO GAIN: Pakistani apartment sq ft benchmark table (100–200 sq ft range).
           Ventilation guidance specifically for small enclosed spaces.
           CO risk by room volume (cubic metres) — no competitor covers this.

FS TARGETS: "What wattage for under 200 sq ft?" — 38 words maximum

PAA TARGETS: "Is gas heater safe in small room?" | "Which heater for 10x10 room?"

INTERNAL LINKS: (3 Core articles minimum)
→ /heaters/gas-heater/wattage/ — "gas heater wattage guide Pakistan" (parent)
→ /heaters/gas-heater/types/ — "gas heater types Pakistan"
→ /heaters/gas-heater/safety/ — "gas heater safety indoors Pakistan"

CONTENT LENGTH: 900–1,400 words (Outer — adequate, not exhaustive)

PHASE: 4 — After Core section complete
═══════════════════════════════════════════════════════════════════════════
```

---

## MODULE 8 — SUMMARY

The content brief is a precision engineering document — not a prompt, not a topic suggestion, not a rough outline.

**20 mandatory components** ensure that every brief, regardless of writer, produces an article with:
- Correct scope (macro context statement as anchor)
- Correct structure (heading hierarchy with contextual bridges)
- Correct depth (TF-IDF floor + information gain targets)
- Correct format (format codes per section)
- Correct entity coverage (EAV entity list)
- Correct competitive positioning (featured snippet + PAA targets)
- Correct architecture integration (internal links plan + URL + parent)

**The seven-stage content flow** (Definition → Mechanism → Types → Attributes → Comparison → Practical Guidance → FAQ) provides the macro ordering logic for heading sequences across all article types.

**The macro context statement** is the single most powerful element of the brief. It defines scope. It prevents scope creep. It is the test against which every heading is measured.

**Brief A and Brief B** demonstrate how the same 20-component system produces very different briefs depending on whether the article is Core (deep, comprehensive, multiple information gain targets, high word count) or Outer (adequate depth, links to Core, lower word count, faster to write).

When a writer receives a brief from this system, they have one job: execute. Every structural, topical, and architectural decision is already made.

---

## MODULE 8 — KEY TERMS GLOSSARY

| Term | Definition |
|---|---|
| **Content Brief** | A precision engineering document containing 20 mandatory components that fully specifies an article before a word is written. |
| **Macro Context Statement** | The single-sentence scope definition of a brief — the anchor against which every heading is tested for inclusion. |
| **Seven-Stage Content Flow** | The universal heading ordering principle: Definition → Mechanism → Types → Attributes → Comparison → Practical Guidance → FAQ. |
| **Format Code** | A 2–3 letter code (FS, PAA, DA, IL, UL, Table, etc.) assigned to each heading section specifying exactly how the answer must be structured. |
| **TF-IDF Required Terms** | The 10–15 vocabulary terms that 70%+ of top-ranking competitor pages include — the statistical vocabulary floor of a complete document. |
| **Information Gain Target** | A specific data point, attribute, or angle not covered by competing articles — the ceiling above TF-IDF. Every Core brief requires minimum 3 targets. |
| **Featured Snippet Target** | A pre-written answer of maximum 40 words / 320 characters assigned to a specific heading — targeting Google's featured snippet extraction. |
| **PAA Target** | A People Also Ask question formatted as an H3 with an immediate single-sentence answer — targeting PAA box extraction. |
| **Internal Links Plan** | The pre-determined set of internal links (target URL + anchor text + article location) that every article will contain. |
| **Content Length Guardrail** | The minimum necessary and maximum efficient word count — not a target, but a range within which the article must stay. |

---

## MODULE 8 — SELF-ASSESSMENT QUESTIONS

1. A writer receives a brief with only these elements: title, keyword list, and a list of competitor URLs to reference. What is missing? List every missing component by name and explain what failure each missing component causes.

2. The macro context statement for a brief reads: *"This article covers everything about gas heaters in Pakistan."* What is wrong with this statement? Rewrite it correctly for an article about gas heater wattage.

3. A brief builder proposes this H2 sequence for an article on gas heater types:
   - H2: Gree Gas Heater Review
   - H2: What are the Types of Gas Heaters?
   - H2: Gas Heater vs Electric Heater
   - H2: How to Install a Gas Heater
   Identify the violations against the seven-stage flow and the macro context rule. Rewrite the heading sequence correctly.

4. Write a complete featured snippet target (≤40 words, ≤320 characters) for the question: *"What is the correct gas heater wattage for a 250 sq ft room in Pakistan?"*

5. The TF-IDF analysis for `baby food for 6 months` reveals these 10 terms appear in 7+ of the top 10 competitor articles: `iron`, `zinc`, `vitamin D`, `puree`, `texture`, `allergen`, `WHO guidelines`, `serving size`, `organic`, `cereal`. A writer's draft article does not include `allergen`, `WHO guidelines`, or `serving size`. What is the ranking impact and what must be done?

6. Write a complete internal links plan for an article titled "Gas Heater Maintenance Guide Pakistan" (Outer section, parent: Gas Heater Types pillar). Include: 4 link targets with anchor text and placement location.

7. Explain why the content length for a Core section pillar should be expressed as a guardrail (minimum + maximum) rather than a single word count target. What happens when writers are given a fixed word count target instead?

---

*Next: Module 9 — Writing the Article*
