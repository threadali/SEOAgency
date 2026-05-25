# MODULE 5 — The Mind Map
## Complete Research Visualisation Before Any Planning Begins

> **Purpose of this module:** Modules 1–4 produced four documents: the Website Identity Document, the Master Keyword Spreadsheet, the Lexical Relationship notes, and the Master Entity Map. The Mind Map is the document that unifies all four into a single visual structure — the complete picture of your topic's knowledge territory before a single content decision is made. It is not a planning document. It is a research document. Planning begins in Module 6. The Mind Map's job is to ensure nothing in your knowledge territory is invisible when planning starts.

---

## LESSON 5.1 — What a Mind Map Is (and What It Is Not)

### The Common Misunderstanding

Most people who hear "mind map" think of a brainstorming diagram — a central node with branches of loose ideas radiating outward. That is not what a Semantic SEO Mind Map is.

A Semantic SEO Mind Map is a **structured visual representation of an entity's complete knowledge territory** — every attribute, every value cluster, every related entity, every query path, every user group, and every contextual layer — organised according to the logical relationships between them.

It is built from research, not from brainstorming. Every node on the map has a source: the EAV table, the keyword spreadsheet, the lexical relationship analysis, or the Website Identity Document. Nothing is invented.

### The Mind Map vs Other Documents

Understanding the relationship between the Mind Map and the documents that come after it prevents confusion about what each document is for:

| Document | What It Is | Built From | Feeds Into |
|---|---|---|---|
| **Website Identity Document** | Foundation: source context, entity, intent | Module 1 | All subsequent documents |
| **Master Keyword Spreadsheet** | Query territory: all keywords, groups, intent | Module 2 | Mind Map, Topical Map |
| **Master Entity Map** | Knowledge territory: all attributes, values | Module 4 | Mind Map, Content Briefs |
| **Mind Map** | Visual unification of all research | Modules 1–4 | CMap (Module 6), Topical Map (Module 7) |
| **CMap** | Structural page architecture | Mind Map | Topical Map |
| **Topical Map** | Content allocation plan | Mind Map + CMap | Content Briefs |
| **Content Briefs** | Article-level production document | Topical Map + Entity Map | Writers |

The Mind Map sits at the centre of this chain. It is the last research document and the first planning document simultaneously. It closes research and opens planning.

### Why the Mind Map Exists at All

You could theoretically move from the Master Keyword Spreadsheet and Entity Map directly to a Topical Map. Some agencies do. The problem is that neither the keyword spreadsheet nor the entity map shows **relationships between things** — they show things in isolation.

The Mind Map reveals:
- How attributes of the central entity connect to each other
- Where query clusters overlap with entity attributes
- Which user groups correspond to which attribute branches
- Where knowledge domain intersections create content opportunities invisible in either spreadsheet
- Which parts of the knowledge territory are dense (many interrelated attributes) vs sparse (isolated attributes)
- Where the contextual layer of your source context is positioned within the full knowledge domain

Without this visual, you make topical map decisions in the dark. With it, you make them with full knowledge of the territory's shape.

---

## LESSON 5.2 — The Five Layers of a Semantic SEO Mind Map

A complete Mind Map has five structural layers. Each layer adds a different dimension of the knowledge territory.

### Layer 1 — The Central Entity (Core Node)

The central entity sits at the exact centre of the map. It is a single node. Everything else radiates from it.

```
                    [ GAS HEATER ]
                         |
        _________________|_________________
       |        |         |        |       |
   Attributes  Types  User Groups  Related  Query
                                   Entities  Paths
```

The central entity node should state:
- Entity name
- Entity type (Product)
- Contextual layer (Portable Gas Heater for Pakistani Residential Use)

### Layer 2 — Root Attribute Branches

The first ring of branches from the central entity consists of all root attributes identified in the Master Entity Map. Each root attribute becomes a primary branch.

```
                    [ GAS HEATER ]
                         |
    _____________________|____________________
   |          |         |        |     |     |
[TYPE]  [WATTAGE]  [PRICE]  [SAFETY]  [BRAND] [FUEL]
```

Each root attribute branch is labelled with:
- The attribute name
- The evaluation result (Core if all three criteria pass)
- The estimated number of supporting articles this attribute generates

### Layer 3 — Value Clusters

From each root attribute branch, the known values expand as sub-branches:

```
[WATTAGE]
    |
    ├── 800W → 2,730 BTU → covers 100–120 sq ft
    ├── 1000W → 3,412 BTU → covers 130–160 sq ft
    ├── 1500W → 5,118 BTU → covers 180–220 sq ft
    ├── 2000W → 6,824 BTU → covers 250–300 sq ft
    └── 3000W → 10,236 BTU → covers 350–450 sq ft
```

Value clusters contain the actual data from the Master Entity Map. They are what differentiates your Mind Map from a simple topic brainstorm — these are verified facts, not guesses.

Value clusters also reveal **natural article breaks**. When a value cluster becomes large enough that it requires its own extensive explanation, that cluster is a candidate for a dedicated supporting article rather than a subsection.

### Layer 4 — Query Path Overlays

From the Master Keyword Spreadsheet, the query paths for each attribute branch are overlaid as annotations. These show where the keyword research and the entity research intersect.

```
[PRICE] ─────────────────────────────────────────────────
    |
    ├── VALUE: PKR 8,500–14,000 (budget)
    │       Query overlay: "gas heater under 10000 pakistan" (Transactional, HIGH vol)
    │
    ├── VALUE: PKR 14,000–25,000 (mid-range)
    │       Query overlay: "best gas heater 15000 pakistan" (Commercial, MED vol)
    │
    ├── VALUE: PKR 25,000–45,000+ (premium)
    │       Query overlay: "premium gas heater pakistan" (Commercial, LOW vol)
    │
    └── INFERRED NEED: brand-wise price comparison
            Query overlay: "gree vs orient heater price" (Commercial, HIGH vol)
```

The query overlay answers the question: *"For this attribute and its values, what are users actually searching?"* It connects the knowledge territory (what the entity is) to the query territory (what users ask about it).

### Layer 5 — Related Entity Connections

The outermost layer of the Mind Map shows entities that are semantically related to the central entity. These are the entities from Section D of the Master Entity Map — things that connect to the central entity through the Knowledge Graph.

```
[ GAS HEATER ] ←────────────────────────────────────────────────────
       ↕                                                            |
[LPG / Natural Gas] ─── (fuel source entity)                       |
       ↕                                                            |
[SNGPL / SSGC] ─── (infrastructure entity — Pakistan-specific)     |
       ↕                                                            |
[Carbon Monoxide] ─── (safety risk entity)                         |
       ↕                                                            |
[Room Size / sq ft] ─── (sizing entity)                            |
       ↕                                                            |
[Electricity Bill / Gas Bill] ─── (running cost entity)            |
       ↕                                                            |
[Electric Heater] ─── (competing entity — antonymous pair) ────────┘
```

Related entity connections reveal **knowledge domain intersection articles** — content that bridges two entities. `Gas Heater + LPG` = an article about fuel types. `Gas Heater + Carbon Monoxide` = a safety article. `Gas Heater + Electric Heater` = a comparison article. These intersections are some of the highest-value content opportunities in the topical map because they serve users navigating between related query clusters.

---

## LESSON 5.3 — Three Additional Map Dimensions

Beyond the five structural layers, three additional dimensions are mapped across the entire structure. These are not separate layers — they are properties assigned to every node and branch.

### Dimension 1 — Core vs Outer Classification

Every node in the Mind Map is classified as Core or Outer using the evaluation results from Module 4.

**Visual representation:** Use two colours throughout the map.
- Core nodes: one colour (e.g. blue)
- Outer nodes: another colour (e.g. green)
- Excluded nodes: grey (still mapped but visually de-prioritised)

This colour-coding instantly reveals the **density of Core vs Outer content** in each attribute branch. An attribute branch that is entirely blue = a deep Core section with multiple supporting articles. An attribute branch that is mostly green = an Outer section with lighter coverage.

### Dimension 2 — User Group Segmentation

Different branches of the Mind Map serve different user groups. Mapping which user groups correspond to which attribute branches reveals whether your topical map will serve all user segments or leave some underserved.

**User groups for a Pakistani heater retailer:**
- Budget buyers (price-sensitive, first-time buyers)
- Technical buyers (specification-focused, want to understand wattage/BTU)
- Safety-conscious buyers (parents, elderly, indoor-safety focused)
- Post-purchase users (owners needing maintenance, troubleshooting)
- Commercial buyers (small shops, offices — borderline Outer section)

**Mapping user groups to attribute branches:**

```
[PRICE] branch ────────────────── → Budget buyers primarily
[WATTAGE / ROOM SIZE] branch ───── → Technical buyers primarily
[SAFETY FEATURES] branch ─────────→ Safety-conscious buyers primarily
[MAINTENANCE] branch ──────────── → Post-purchase users primarily
[BRANDS] branch ──────────────── → All user groups
[TYPES] branch ───────────────── → All user groups (awareness stage)
```

Any user group with no corresponding attribute branch = an underserved segment. That segment's queries will not be captured by your topical map. Identify and fill these gaps before building the topical map.

### Dimension 3 — Topical Map Density vs Depth

Every branch of the Mind Map has a density score — the number of viable articles that branch can generate — and a depth indicator — how many levels deep the content hierarchy for that branch can go.

```
[TYPES] branch
  Density: HIGH (6 heater types × multiple attributes each = 12–18 possible articles)
  Depth: 3 levels (root pillar → type-specific pillar → type + attribute)

[REMOTE CONTROL] branch
  Density: LOW (1–2 articles maximum)
  Depth: 1 level (single supporting article only)

[PRICE] branch
  Density: HIGH (brand-wise, budget range, city-wise, year-wise comparisons)
  Depth: 2 levels (price overview → brand-specific price pages)
```

Density and depth together determine where you invest content production effort. High density + high depth = major Core section cluster. Low density + low depth = single Outer section article.

---

## LESSON 5.4 — Tools and Format for Building the Mind Map

### Tool Options

The Mind Map can be built in any tool that supports hierarchical branching. What matters is not the tool — it is the content and structure.

| Tool | Strengths | Best For |
|---|---|---|
| **Whimsical** | Clean visual hierarchy, easy to share, supports colour coding | Teams, client presentation |
| **Miro** | Infinite canvas, rich annotation, supports overlays | Complex entities with many branches |
| **MindMeister** | Dedicated mind map tool, export options, collaboration | Standard mind map format |
| **XMind** | Local desktop, powerful export, structured format | Detailed technical maps |
| **Notion (nested pages)** | Text-based, easily linked to other documents | Teams already in Notion |
| **Google Slides** | Simple, shareable, no setup required | Quick lightweight maps |
| **Spreadsheet (Excel/Sheets)** | Most practical for large entities with many values | Data-heavy entities with many numeric values |

**Recommendation for this course:** Build the structural layer (Layers 1–3) in a visual tool (Whimsical or Miro). Build the query path overlay (Layer 4) in a spreadsheet. Keep related entity connections (Layer 5) in a separate reference doc or as annotations on the visual.

This hybrid approach keeps the visual clean while preserving the data richness of the keyword spreadsheet.

### Format Rules

Regardless of tool, these format rules apply:

**Rule 1 — Central entity at absolute centre.**
Every branch traces back to the central entity. No floating sub-clusters disconnected from the centre.

**Rule 2 — Attribute branches at Layer 2, never values.**
The first ring from the central entity is always attribute names — never specific values. Values live at Layer 3 and below. Mixing levels creates visual confusion and obscures the structural logic.

**Rule 3 — Core nodes visually distinct from Outer nodes.**
Colour code or use different shapes. The visual distinction must be immediately readable — someone who has not built the map should be able to identify Core vs Outer within 10 seconds of looking at it.

**Rule 4 — Query path annotations are inline, not separate.**
Query overlays live directly on the relevant value or attribute node — not in a separate legend. The reader should not need to cross-reference to understand what users search for this node.

**Rule 5 — Related entities connect with labelled relationships.**
Every line connecting a related entity to the central entity must be labelled with the relationship type: `uses`, `competes with`, `is manufactured by`, `creates risk of`, `is measured in`, etc.

**Rule 6 — The map has a reading direction.**
Organise branches so that the map can be read left-to-right or top-to-bottom with logical progression. Core attributes (most prominent) on the left or top. Outer attributes on the right or bottom. Related entities on the outer perimeter.

---

## LESSON 5.5 — How the Mind Map Reveals Topical Map Gaps

The primary value of the Mind Map over the spreadsheet is that it makes **structural gaps visible**. When looking at a spreadsheet, you can only see what is in it. When looking at a Mind Map, you can see what is missing because the shape of the map reveals it.

### Gap Type 1 — Orphan Attribute Branches

An attribute branch with no query overlay means the attribute has no corresponding keyword group in your Master Keyword Spreadsheet. This happens when:
- The attribute exists in the Knowledge Graph but users do not search for it directly
- You missed the corresponding query cluster in your keyword research

**Resolution:** Either add the missing query research, or flag the attribute as supplementary content (to be covered as a section within a larger article rather than its own page).

### Gap Type 2 — Dense Keyword Groups with Thin Entity Coverage

A section of the keyword spreadsheet with many keywords but few entity attribute values means you have identified high user interest in something you have not researched deeply enough in the Entity Map.

**Resolution:** Return to Module 4's five research methods and expand the entity research for that attribute branch before building the Topical Map.

### Gap Type 3 — Missing User Group Branches

If mapping user groups to attribute branches reveals a user group with no corresponding branch, your content will not serve that segment. This is a significant topical authority gap because Google's user grouping (from Module 0) will not associate your site with that user cluster's sessions.

**Resolution:** Identify which attributes serve the underserved user group and add them to the Mind Map as new branches — then evaluate them through the three-criteria framework.

### Gap Type 4 — Related Entity Isolation

A related entity with no corresponding attribute branch on the main entity means you have identified a knowledge domain intersection with no planned content. These intersections are often where users are underserved industry-wide — making them high-value information gain opportunities.

**Resolution:** For every related entity, ask: *"What article covers the relationship between [central entity] and [related entity]?"* If no article in your planned content answers this, add it.

### Gap Type 5 — Contextual Layer Mismatch

If large sections of the Mind Map operate at the wrong contextual layer for your Source Context — too broad, too technical, or wrong geography — these branches will produce content that does not align with your site's positioning.

**Resolution:** Review the contextual layer filter for every branch. Any branch operating outside your Source Context's contextual layer is either Outer section (if marginally related) or excluded (if clearly outside scope).

---

## LESSON 5.6 — From Mind Map to Topical Map: The Transition

The Mind Map is completed before Modules 6 and 7 begin. It feeds both. Understanding exactly how it feeds them prevents the common mistake of treating the Mind Map as an optional extra.

### What the CMap (Module 6) Takes from the Mind Map

The CMap (category and structural page architecture) is built from:
- The attribute branches classified as Core at the highest level → become category/pillar page topics
- The hypernym hierarchy revealed by the Layer 2 branches → becomes the URL and navigation structure
- The related entity connections → reveal which additional category pages are needed (e.g. a `Gas Heaters` category page AND a `Heater Types` category page)

### What the Topical Map (Module 7) Takes from the Mind Map

The Topical Map (all article topics) is built from:
- Every attribute branch at Layer 2 → one pillar page per root attribute
- Every value cluster at Layer 3 → potential supporting articles per significant value
- Every query overlay at Layer 4 → confirms search demand and assigns keyword groups
- Every related entity connection at Layer 5 → intersection articles

### The Transition Checklist

Before closing the Mind Map and moving to Module 6, verify:

```
MIND MAP COMPLETION CHECKLIST
==============================

Layer completeness:
[ ] Central entity node is fully defined (name, type, contextual layer)
[ ] All root attributes are mapped as Layer 2 branches
[ ] All rare attributes are mapped (colour-coded as Outer)
[ ] All unique attributes noted (linked to future review pages)
[ ] Value clusters populated for all Core attribute branches
[ ] Query overlays added for all Core attribute value clusters
[ ] Related entities mapped with labelled relationship types

Dimension completeness:
[ ] Core / Outer colour coding applied to ALL nodes
[ ] User group segments mapped to corresponding attribute branches
[ ] Density + depth scores assigned to major attribute branches
[ ] No user group is left with zero corresponding branches

Gap audit:
[ ] Orphan attribute branches investigated and resolved
[ ] Dense keyword groups with thin entity coverage addressed
[ ] Missing user group branches identified and filled
[ ] Related entity intersections have a corresponding article plan
[ ] Contextual layer alignment verified for all branches

Transition readiness:
[ ] Top-level attribute branches (Core) ready to become CMap pillar categories
[ ] URL hierarchy implied by branch structure is logical and clean
[ ] Keyword spreadsheet groups are reconciled with Mind Map branches
  (every keyword group maps to at least one node on the map)
[ ] Entity map is complete enough that every Mind Map branch has
  sufficient values to write a content brief from
```

---

## LESSON 5.7 — Full Mind Map Worked Example

**Entity:** Gas Heater
**Source Context:** Pakistani home appliance retailer, affordable residential buyers

Below is a text representation of the full Mind Map structure. In practice this is built visually, but this text version communicates the complete structure.

```
═══════════════════════════════════════════════════════════════════════
                    MIND MAP: GAS HEATER (Pakistan)
        Source Context: Affordable Home Appliance Retailer, Pakistan
═══════════════════════════════════════════════════════════════════════

CENTRE: Gas Heater [Product] [Contextual Layer: Portable Gas Heater,
                               Pakistani Residential, Affordable Segment]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRANCH 1 — TYPE [CORE ████] Density: HIGH | Depth: 3 levels
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ├── Convection (Blue Flame)
  │       Values: Natural convection, fan-assisted, flueless design
  │       Queries: "blue flame gas heater pakistan" (INFO, MED)
  │       User group: General buyers, first-time buyers
  │       → Article: Blue Flame Gas Heater: How It Works + Pakistan Prices
  │
  ├── Radiant / Infrared
  │       Values: Quartz tube, ceramic element, directional heat
  │       Queries: "infrared gas heater pakistan" (INFO, MED)
  │       User group: Technical buyers, instant-heat seekers
  │       → Article: Infrared Gas Heater: Direct Heat vs Convection Explained
  │
  ├── Catalytic Infrared
  │       Values: Flameless combustion, lower CO risk, higher cost
  │       Queries: "catalytic gas heater safe indoors" (INFO, LOW)
  │       User group: Safety-conscious buyers
  │       → Article: Catalytic Heaters: Safest Gas Heater Type for Indoor Use?
  │
  ├── Oil-Filled (Electric, related entity)
  │       [Note: Separate entity — links from this branch to oil-filled
  │        heater section for comparison]
  │
  └── [Pillar page: Gas Heater Types Pakistan — covers all 3 above]
      Queries: "types of gas heaters" (INFO, HIGH)
              "which type of gas heater is best" (COMM, HIGH)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRANCH 2 — WATTAGE / HEAT OUTPUT [CORE ████] Density: MED | Depth: 2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ├── 800W   → 2,730 BTU → 100–120 sq ft
  │       Queries: "small room heater wattage" (INFO, MED)
  ├── 1000W  → 3,412 BTU → 130–160 sq ft
  ├── 1500W  → 5,118 BTU → 180–220 sq ft
  │       Queries: "1500 watt gas heater pakistan" (COMM, HIGH)
  ├── 2000W  → 6,824 BTU → 250–300 sq ft
  │       Queries: "2000 watt gas heater" (COMM, MED)
  └── 3000W  → 10,236 BTU → 350–450 sq ft
          Queries: "large room heater pakistan" (COMM, MED)

  [Pillar page: Gas Heater Wattage Guide — Room Size Calculator Pakistan]
  Queries: "what wattage heater for room size" (INFO, HIGH)
           "gas heater room size pakistan" (INFO, HIGH)

  INFORMATION GAIN OPPORTUNITY:
  No competitor provides PKR-to-wattage efficiency table or
  gas consumption per watt per hour in Pakistani units

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRANCH 3 — PRICE [CORE ████] Density: HIGH | Depth: 2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ├── Budget: PKR 8,500–14,000
  │       Queries: "cheap gas heater pakistan under 10000" (TRANS, HIGH)
  │       Brands: Super Asia, Waves, Nasgas budget range
  ├── Mid-range: PKR 14,000–25,000
  │       Queries: "best gas heater 15000 pakistan" (COMM, HIGH)
  │       Brands: Orient, Dawlance, Gree standard range
  └── Premium: PKR 25,000–45,000+
          Queries: "premium gas heater pakistan" (COMM, MED)
          Brands: Gree premium, imported brands

  [Pillar page: Gas Heater Price in Pakistan — 2025 Brand-wise List]
  Queries: "gas heater price pakistan" (COMM, VERY HIGH)
           "gas heater price list pakistan" (COMM, HIGH)

  INFORMATION GAIN OPPORTUNITY:
  Monthly running cost in PKR (using SNGPL/SSGC tariff rates) by wattage
  Zero competitors provide this calculation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRANCH 4 — SAFETY [CORE ████] Density: MED | Depth: 2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ├── ODS (Oxygen Depletion Sensor)
  │       Values: Shuts off at O2 < 18%, mandatory in certified models
  │       Queries: "gas heater oxygen sensor" (INFO, MED)
  ├── Tip-over switch
  │       Values: Cuts gas supply on >45° tilt
  ├── Flame failure device
  │       Values: Thermocouple-based, shuts off on flame loss
  └── Ventilation requirement
          Values: 10–15% fresh air by volume; 1 window cracked minimum
          Queries: "gas heater safe indoors" (INFO, HIGH)
                   "gas heater carbon monoxide risk" (INFO, HIGH)
          Related entity: CARBON MONOXIDE → intersection article

  [Pillar page: Gas Heater Indoor Safety Guide — Pakistan]
  User group: Safety-conscious buyers, parents, elderly households

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRANCH 5 — BRANDS [CORE ████] Density: HIGH | Depth: 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ├── Gree (Chinese, Pakistani distribution via Gree Pakistan)
  │       Models: GH-800, GH-1200, GH-1800, GH-2000
  │       Queries: "gree gas heater price pakistan" (COMM, HIGH)
  │       → Supporting: Gree Gas Heater Review + Specs + Price
  ├── Orient (Pakistani brand, market leader mid-segment)
  │       Queries: "orient gas heater price pakistan" (COMM, HIGH)
  │       → Supporting: Orient Gas Heater Review Pakistan
  ├── Dawlance (Pakistani brand, Arçelik subsidiary)
  │       Queries: "dawlance heater price pakistan" (COMM, MED)
  │       → Supporting: Dawlance Gas Heater Models + Prices
  ├── Super Asia (Pakistani, budget segment)
  ├── Nasgas (Pakistani, gas appliance specialist)
  └── Waves (Pakistani, budget–mid segment)

  [Pillar page: Best Gas Heater Brands in Pakistan — Comparison Guide]
  Queries: "best gas heater brand pakistan" (COMM, VERY HIGH)
           "gree vs orient heater" (COMM, HIGH)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRANCH 6 — FUEL TYPE [CORE ████] Density: MED | Depth: 2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ├── LPG (Liquefied Petroleum Gas)
  │       Values: Propane/butane blend; 24.9 MJ/L; cylinder-fed
  │       Related entity: LPG CYLINDER → cost per cylinder Pakistan
  │       Queries: "lpg gas heater pakistan" (INFO, MED)
  ├── Natural Gas (pipeline)
  │       Values: Methane; 38.3 MJ/m³; SNGPL/SSGC supply
  │       Related entity: SNGPL/SSGC → tariff structure
  │       Queries: "natural gas heater pakistan" (INFO, MED)
  └── Dual Fuel (rare attribute)
          Values: Convertible regulator; requires technician adjustment
          Queries: "dual fuel gas heater pakistan" (INFO, LOW)

  [Pillar page: LPG vs Natural Gas Heater in Pakistan — Cost + Availability]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRANCH 7 — MAINTENANCE [OUTER ░░░░] Density: MED | Depth: 2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ├── Annual servicing schedule
  ├── Burner cleaning (DIY vs professional)
  ├── Filter replacement
  └── Common problems + fixes
          Queries: "gas heater not heating properly" (INFO, MED)
                   "how to clean gas heater pakistan" (INFO, MED)
          User group: Post-purchase owners

  [Supporting articles: Gas Heater Maintenance Guide Pakistan]
  [Supporting: Gas Heater Not Working — Common Problems + Fixes]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RELATED ENTITY CONNECTIONS (Layer 5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Gas Heater ──[uses]──────────→ LPG / Natural Gas
    → Intersection article: "LPG vs Natural Gas for Heaters: Pakistan Cost Guide"

  Gas Heater ──[creates risk of]→ Carbon Monoxide
    → Intersection article: "Gas Heater Carbon Monoxide Risk: Complete Safety Guide"

  Gas Heater ──[is supplied by]→ SNGPL / SSGC
    → Intersection article: "Gas Heater Running Cost Pakistan: SNGPL/SSGC Tariff Calculation"

  Gas Heater ──[competes with]──→ Electric Heater (antonymous entity)
    → Intersection article: "Gas Heater vs Electric Heater Pakistan: Full Comparison"

  Gas Heater ──[sized for]──────→ Room Size (sq ft / m²)
    → Intersection article: "How to Choose the Right Heater Size for Your Room in Pakistan"

  Gas Heater ──[measured by]────→ BTU / Wattage
    → Supports WATTAGE branch — already mapped

  Gas Heater ──[used in]────────→ Pakistani Homes (urban apartment context)
    → Contextual layer article: "Best Gas Heater for Small Apartments in Pakistan"
```

---

## MODULE 5 — SUMMARY

The Mind Map is the research document that makes the planning documents possible. It does five things no other document in the workflow does:

**It unifies.** The Website Identity Document, Master Keyword Spreadsheet, and Master Entity Map all exist as separate documents. The Mind Map brings them into one visual structure where their relationships are visible simultaneously.

**It reveals shape.** A spreadsheet shows data. A mind map shows the shape of that data — which branches are dense, which are sparse, which are isolated, which are deeply interconnected.

**It exposes gaps.** Orphan branches, missing user groups, dense keyword clusters with thin entity coverage, and related entity intersections are all invisible in spreadsheets but obvious on a mind map.

**It generates content opportunities.** Related entity connections reveal intersection articles — often the highest-value content because they serve users navigating between query clusters that no single competitor page covers.

**It makes planning decisions defensible.** When the Topical Map in Module 7 is questioned — why is this article included? why is this one excluded? — the Mind Map provides the answer. Every decision traces back to a node on the map with a rationale attached.

---

## MODULE 5 — KEY TERMS GLOSSARY

| Term | Definition |
|---|---|
| **Mind Map** | A structured visual representation of an entity's complete knowledge territory, built from research across Modules 1–4. |
| **Layer 1** | The central entity node at the exact centre of the map. |
| **Layer 2** | Root attribute branches — the first ring of primary branches from the central entity. |
| **Layer 3** | Value clusters — the specific known values for each attribute branch. |
| **Layer 4** | Query path overlays — keyword group annotations on each value or attribute node. |
| **Layer 5** | Related entity connections — semantically related entities mapped on the outer perimeter. |
| **Density score** | The number of viable articles a given attribute branch can generate. |
| **Depth indicator** | How many hierarchical levels the content for a branch can go (pillar → supporting → deep supporting). |
| **Orphan attribute branch** | An attribute in the entity map with no corresponding keyword group in the keyword spreadsheet. |
| **Knowledge domain intersection** | An article that bridges two related entities, serving users navigating between their respective query clusters. |
| **User group segmentation** | The mapping of specific user types (budget buyers, technical buyers, post-purchase owners) to the attribute branches that serve them. |
| **Contextual layer filter** | The process of verifying that every branch of the Mind Map operates at the correct contextual depth for the site's source context. |

---

## MODULE 5 — SELF-ASSESSMENT QUESTIONS

1. You have completed Modules 1–4 for a baby food retailer in Pakistan. Describe the complete structure of the Mind Map you would build. Name at least 5 root attribute branches with their Layer 3 value clusters and at least 3 related entity connections with their corresponding intersection articles.

2. Your Mind Map for an eye care clinic reveals a dense keyword group around `computer vision syndrome` with 12 high-volume keywords — but the Master Entity Map has only 2 attributes mapped for this condition. What gap type is this? What must you do before building the Topical Map?

3. A Mind Map for a heater retailer has no branches corresponding to post-purchase users (maintenance, troubleshooting, repair). What user group gap does this create? What happens to the site's ability to capture post-purchase query sessions?

4. The related entity connection `Gas Heater ──[creates risk of]──→ Carbon Monoxide` appears in the Mind Map's Layer 5. What intersection article does this generate? Write a proposed title using the title construction system from Module 3.

5. A mind map branch for `heater colour options` has been added by a content manager. Apply the contextual layer filter: should this branch remain in the map for a Pakistani affordable heater retailer? Justify your answer using source context rules from Module 1.

6. Explain the difference in what a Mind Map reveals vs what the Master Keyword Spreadsheet reveals. Why is it insufficient to skip the Mind Map and go directly from the keyword spreadsheet to the Topical Map?

7. The Mind Map for a gas heater site shows the `BRANDS` branch has density: HIGH, depth: 3. What does this mean for the Topical Map? How many articles minimum should this branch generate, and what type (pillar, supporting, deep supporting)?

---

*Next: Module 6 — CMap (Category and Landing Page Architecture)*
