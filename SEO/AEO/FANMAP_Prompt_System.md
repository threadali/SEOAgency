# FANMAP Generation System
## Prompt File for Claude — Generates Complete Fan Maps with 10+ Topics Per Phase

---

## HOW TO USE THIS FILE

Feed this entire file to Claude and fill in the `[VARIABLES]` at the top.
Claude will generate a complete FANMAP based on your business type.

---

## STEP 0 — FILL THESE VARIABLES FIRST

```
BUSINESS_NAME:        [e.g. AquaWorld]
BUSINESS_TYPE:        [Ecommerce / Local / SaaS / Event / Education]
PRODUCT_OR_SERVICE:   [e.g. Goldfish and freshwater fish]
LOCATION:             [e.g. Lahore, Pakistan — or "Global" if online]
DELIVERY_CONSTRAINT:  [e.g. Delivery only within Lahore / Worldwide / Digital only]
PRICE_RANGE:          [e.g. Budget (under 2000 PKR) / Mid / Premium]

ICP_1_NAME:           [e.g. First-Time Family Buyer]
ICP_1_WHO:            [e.g. Young parent, Lahore, 25-35]
ICP_1_PROBLEM:        [e.g. Child wants goldfish, no experience]
ICP_1_TRIGGER:        [e.g. Child's birthday / school project]
ICP_1_SUCCESS:        [e.g. Fish stays alive, easy to maintain]

ICP_2_NAME:           [e.g. Home Decor Enthusiast]
ICP_2_WHO:            [e.g. Urban professional, new flat]
ICP_2_PROBLEM:        [e.g. Wants aesthetic tank for home]
ICP_2_TRIGGER:        [e.g. Home renovation]
ICP_2_SUCCESS:        [e.g. Beautiful tank, minimal effort]

ICP_3_NAME:           [e.g. Serious Hobbyist]
ICP_3_WHO:            [e.g. Experienced keeper, 30-45]
ICP_3_PROBLEM:        [e.g. Wants rare breeds not available locally]
ICP_3_TRIGGER:        [e.g. Upgrading existing tank]
ICP_3_SUCCESS:        [e.g. Rare breeds, expert guidance]
```

---

## MASTER PROMPT — PASTE THIS INTO CLAUDE

```
You are an expert AEO (Answer Engine Optimization) content strategist.

Your task is to generate a complete FANMAP for the business below.
A FANMAP is a Fan-Out Map — it identifies every possible query angle
across different ICPs and funnel stages so we can maximize AI citations.

---

BUSINESS CONTEXT:
Business Name:       [BUSINESS_NAME]
Business Type:       [BUSINESS_TYPE]
Product/Service:     [PRODUCT_OR_SERVICE]
Location:            [LOCATION]
Delivery:            [DELIVERY_CONSTRAINT]
Price Range:         [PRICE_RANGE]

ICP 1: [ICP_1_NAME]
- Who: [ICP_1_WHO]
- Problem: [ICP_1_PROBLEM]
- Trigger: [ICP_1_TRIGGER]
- Success: [ICP_1_SUCCESS]

ICP 2: [ICP_2_NAME]
- Who: [ICP_2_WHO]
- Problem: [ICP_2_PROBLEM]
- Trigger: [ICP_2_TRIGGER]
- Success: [ICP_2_SUCCESS]

ICP 3: [ICP_3_NAME]
- Who: [ICP_3_WHO]
- Problem: [ICP_3_PROBLEM]
- Trigger: [ICP_3_TRIGGER]
- Success: [ICP_3_SUCCESS]

---

FANMAP RULES:
1. Generate MINIMUM 10 queries per funnel stage per ICP
2. Queries must reflect how humans ask AI — not Google keyword style
3. Each query must be specific — no generic broad queries
4. Apply layering: location, person type, budget, problem, comparison,
   negative, use case, outcome, time, demographic, qualifier
5. Flag hallucination probability: HIGH / MEDIUM / LOW
   HIGH = AI likely gives weak/generic answer = your opportunity
6. Follow the funnel stage rules exactly as defined below

---

FUNNEL STAGE DEFINITIONS:

PRE-AWARENESS:
Goal: User doesn't know they have a problem yet — personal query
Query pattern: "Why is my X not working?" / "Why does Y happen?"
AEO tactic: Pure education — no selling
Content format: Story blog, Problem explainer
Hallucination rate: HIGHEST — almost always O-grade

AWARENESS:
Goal: Problem-based searches — capture them early
Query pattern: "How do I X?" / "What causes Y?" / "What is best way to Z?"
AEO tactic: Educational — brand mention subtle
Content format: Blog, How-to, FAQ

CONSIDERATION:
Goal: Present solutions — position yourself at the top
Query pattern: "Best X for Y" / "Top solutions for Z" / "X for [type of person]"
AEO tactic: Position in every listicle
Content format: Listicle, Comparison table

EVALUATION:
Goal: Reduce brand doubt — suggest yourself as better alternative
Query pattern: "Brand A vs Brand B" / "Brand alternative" / "Brand pros and cons"
AEO tactic: Suggest yourself as better alternative
Content format: VS page, Alternative landing page, Comparison page

DECISION:
Goal: Convert high-intent users — capture competitor buyers too
Query pattern: "Buy X" / "X near me" / "Brand reviews" / "Is Brand legit?"
Pro tip: Cover "Can [Competitor] do X?" to capture competitor buyers
Content format: Product page, Local page, Landing page

---

OUTPUT FORMAT — GENERATE EXACTLY THIS STRUCTURE:

═══════════════════════════════════════════════
FANMAP: [BUSINESS_NAME]
Generated for: [BUSINESS_TYPE]
═══════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ICP 1: [ICP_1_NAME]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STAGE 1: PRE-AWARENESS (minimum 10 queries)
Format: | # | Query | Layer Applied | Hallucination | Content Type |

| 1  | [query] | [layer] | HIGH/MED/LOW | [format] |
| 2  | [query] | [layer] | HIGH/MED/LOW | [format] |
... (minimum 10)

STAGE 2: AWARENESS (minimum 10 queries)
[same table format]

STAGE 3: CONSIDERATION (minimum 10 queries)
[same table format]

STAGE 4: EVALUATION (minimum 10 queries)
[same table format]

STAGE 5: DECISION (minimum 10 queries)
[same table format]

[Repeat for ICP 2 and ICP 3]

═══════════════════════════════════════════════
PRIORITY CONTENT LIST — TOP 20 O-GRADE TOPICS
═══════════════════════════════════════════════
[List top 20 queries with HIGH hallucination
ranked by: opportunity + business relevance]

| Priority | Query | ICP | Stage | Why O-Grade |
|----------|-------|-----|-------|-------------|

═══════════════════════════════════════════════
FANMAP SUMMARY
═══════════════════════════════════════════════
Total queries generated: [X]
HIGH hallucination (O-grade): [X]
MEDIUM hallucination (C-grade): [X]
LOW hallucination (S-grade): [X]
Recommended Phase 1 articles: [X]
Recommended Phase 2 articles: [X]
```

---

## FANMAP TYPE VARIATIONS

### TYPE 1: STANDARD BUSINESS FANMAP
**Use when:** New client, starting from scratch
**Covers:** All ICPs × All funnel stages
**Output:** 150+ queries minimum

Use master prompt above as-is.

---

### TYPE 2: SINGLE ICP DEEP FANMAP
**Use when:** One ICP is primary revenue driver
**Covers:** One ICP × All stages × Deep layering
**Output:** 80+ queries for one persona

```
Additional instruction to add to master prompt:

"Focus ONLY on ICP 1: [ICP_NAME].
Go deeper than standard — generate minimum 15 queries
per funnel stage.
Apply every layer type at least once per stage:
Location, Person Type, Demographic, Budget, Problem,
Time, Comparison, Negative, Use Case, Outcome, Qualifier.
For each query also suggest: exact article title if published."
```

---

### TYPE 3: SINGLE STAGE FANMAP
**Use when:** Need to dominate one specific funnel stage
**Covers:** All ICPs × One stage × Maximum depth
**Output:** 50+ queries for that stage

```
Additional instruction to add to master prompt:

"Focus ONLY on the [STAGE NAME] stage.
Cover all 3 ICPs but stay within this stage only.
Generate minimum 20 queries per ICP for this stage.
For each query:
- Suggest exact content format
- Suggest exact placement (blog/landing/answer hub)
- Flag if competitor likely covers this already
- Suggest 1 unique angle competitors probably miss"
```

---

### TYPE 4: QUERY FANMAP (Single Topic Deep Dive)
**Use when:** One O-grade query needs full article planning
**Covers:** One query × All possible angles
**Output:** Article brief with 8-12 sub-angles

```
Replace master prompt with this for Query FANMAP:

You are an AEO content strategist.

Run a deep Query FANMAP for:

QUERY: [exact query]
BUSINESS: [business name and description]
ICP: [exact persona with constraints]
LOCATION: [city/region]
CONSTRAINTS: [budget, space, experience, family situation etc]
OCS GRADE: [O / C / S]

Task:
1. Fan out this query into minimum 10 sub-angles
2. For each angle — identify:
   - What the user actually wants to know
   - What competitors probably cover
   - What competitors probably miss
   - Hallucination probability
3. Group angles into article clusters:
   - Which angles belong in 1 article?
   - Which angles need separate articles?
4. For each article — generate:
   - Exact title (with location + constraint)
   - H2 headings list
   - FAQ questions (minimum 3)
   - Recommended word count
5. Identify the "after-reading gap":
   - What question will reader still have after reading competitors?

OUTPUT FORMAT:

QUERY FANMAP: [query]
━━━━━━━━━━━━━━━━━━━━━

ANGLE MAP:
| # | Angle | User Want | Competitor Covers? | Gap? | Hallucination |
|---|-------|-----------|-------------------|------|---------------|

ARTICLE DECISION: 1 article / 2 articles / 3 articles
Reason: [why]

ARTICLE 1:
  Title: [exact SEO + AEO optimized title]
  Target query: [exact query]
  Word count: [recommended]
  H2 sections:
    1. [H2]
    2. [H2]
    3. [H2]
    4. [H2]
    5. [H2]
  FAQ questions:
    Q1: [exact customer language]
    Q2: [exact customer language]
    Q3: [exact customer language]
  After-reading gap: [what question remains]
  Information gain opportunity: [what unique data you can add]

[Repeat for Article 2, 3 if needed]
```

---

### TYPE 5: COMPETITOR GAP FANMAP
**Use when:** Competitor is already ranking — need to find what they missed
**Covers:** Competitor's content × Your gaps
**Output:** Exclusive angle list

```
Additional instruction to add to master prompt:

"I have a competitor: [COMPETITOR NAME/URL]
They are known for covering: [list their known topics]
They consistently rank for: [list their ranking queries]

Task:
1. Generate standard FANMAP first
2. Then for each query — flag:
   COVERED: Competitor likely covers this
   GAP: Competitor likely misses this
   EXCLUSIVE: Only we can cover this (local/specific/constraint-based)
3. Output a separate 'GAP LIST' at the end:
   Queries competitor misses that we can own immediately
   Sort by: hallucination probability × business relevance"
```

---

### TYPE 6: SEASONAL/TIME-BASED FANMAP
**Use when:** Business has seasonal patterns
**Covers:** Time-layered queries across all stages
**Output:** Content calendar mapped to seasons

```
Additional instruction to add to master prompt:

"Apply time-based layering to all queries.
Seasons/events relevant to this business: [list them]
Example: Lahore summer, Eid season, back to school, winter

For each funnel stage — generate:
- 5 evergreen queries (no time dependency)
- 5 seasonal queries (time-specific)
- Flag which month each seasonal query peaks

Output additional table:
CONTENT CALENDAR:
| Month | Query | Stage | ICP | Action |
|-------|-------|-------|-----|--------|"
```

---

## LAYERING REFERENCE — USE IN ANY FANMAP

Apply these layers to every base query to unlock deeper queries:

| Layer | Formula | Hallucination Rate |
|---|---|---|
| **Location** | [Topic] + [City/Area/Country] | HIGH — very specific |
| **Person Type** | [Topic] + [Who they are] | HIGH — persona specific |
| **Demographic** | [Topic] + [Age/Gender/Life stage] | HIGH — narrow audience |
| **Budget** | [Topic] + [Price sensitivity] | HIGH — constraint specific |
| **Problem** | [Topic] + [Specific pain point] | HIGH — problem specific |
| **Time** | [Topic] + [Season/Urgency] | HIGH — time specific |
| **Comparison** | [Topic] + [vs something] | MEDIUM — some coverage |
| **Negative** | Why not [Topic] / Worst [Topic] | HIGH — rarely covered |
| **Use Case** | [Topic] + [Specific scenario] | HIGH — scenario specific |
| **Outcome** | [Topic] + [Desired result] | MEDIUM — some coverage |
| **Qualifier** | Best/Easiest/Fastest + [Topic] + [Context] | MEDIUM — competitive |
| **Anti-Audience** | [Topic] + [Who it's NOT for] | HIGH — almost never covered |

---

## HALLUCINATION GRADING GUIDE

Use this to grade every query in your FANMAP:

```
HIGH HALLUCINATION (O-Grade) — TARGET IMMEDIATELY
Signs AI gives bad answer:
→ Generic response — no local context
→ "I don't have specific information about..."
→ Query angle completely changed
→ Wrong or outdated information
→ Cited sources irrelevant to query
→ No specific brand/location cited

MEDIUM HALLUCINATION (C-Grade) — PLAN FOR PHASE 2
Signs AI gives partial answer:
→ Some competitors cited but inconsistently
→ AI modifies query slightly but stays relevant
→ Answer exists but misses key angles
→ Local context missing but topic covered

LOW HALLUCINATION (S-Grade) — LONG TERM ONLY
Signs AI gives strong answer:
→ Specific brands consistently cited
→ Local context present
→ Data and proof included
→ Confident, direct recommendation
→ Same answer across ChatGPT, Perplexity, Gemini
```

---

## FUNNEL STAGE RULES — DETAILED

### PRE-AWARENESS
```
User state:    Doesn't know they have a problem
Query style:   Personal observation — not product search
Examples:      "Why is my goldfish not eating?"
               "Why do my feet hurt after long walks?"
               "Why is my churn rate increasing?"
AEO power:     HIGHEST — almost always O-grade
               AI has very little local/specific data here
Content:       Story blog, Problem explainer
               No selling — pure education
Placement:     Blog, Social media
```

### AWARENESS
```
User state:    Knows problem — looking for solutions broadly
Query style:   How-to, What is, Educational
Examples:      "How to keep goldfish alive as beginner?"
               "Do goldfish need filters?"
               "How to reduce customer churn?"
AEO power:     HIGH — specific angles often O-grade
Content:       How-to blog, Educational FAQ
               Subtle brand mention acceptable
Placement:     Blog, Answer Hub
```

### CONSIDERATION
```
User state:    Evaluating options — comparing solutions
Query style:   Best X for Y, Top solutions, Listicles
Examples:      "Best goldfish for beginners Pakistan"
               "Best running shoes for flat feet"
               "Best live chat software for startups"
AEO power:     MEDIUM — more competition here
Content:       Listicle, Comparison table
               Position yourself in every list
Placement:     Blog, Listicle pages
```

### EVALUATION
```
User state:    Narrowing down — comparing specific brands
Query style:   Brand A vs Brand B, Alternatives, Pros/cons
Examples:      "AquaWorld vs local pet shop Lahore"
               "Common goldfish vs Fantail"
               "Intercom vs Drift"
AEO power:     MEDIUM — gap exists in local comparisons
Content:       VS page, Alternative landing page
               Position as better alternative
Placement:     Comparison pages, Alternative pages
```

### DECISION
```
User state:    Ready to buy — needs final validation
Query style:   Buy, Near me, Reviews, Is X legit?, Pricing
Examples:      "Where to buy goldfish in Lahore"
               "AquaWorld reviews"
               "Is AquaWorld reliable?"
PRO TIP:       Also cover "Can [Competitor] do X?"
               to capture competitor's ready buyers
AEO power:     HIGH for local — very specific intent
Content:       Product page, Local page, Review page
Placement:     Landing pages, Local pages
```

---

## OUTPUT VALIDATION CHECKLIST

After Claude generates your FANMAP — verify:

```
QUANTITY CHECK:
☐ Minimum 10 queries per stage per ICP?
☐ All 5 stages covered?
☐ All 3 ICPs covered?
☐ Minimum 150 total queries for full business FANMAP?

QUALITY CHECK:
☐ Queries sound like how humans ask AI — not keyword phrases?
☐ Location-specific queries included?
☐ Constraint-based queries included (budget, space, experience)?
☐ Negative + anti-audience queries present?
☐ Pre-awareness queries are problem-based (not product-based)?
☐ Decision queries include competitor capture angles?

HALLUCINATION CHECK:
☐ Each query has hallucination grade (HIGH/MED/LOW)?
☐ At least 30% of queries are HIGH hallucination?
☐ Priority content list has 20 O-grade topics?

OUTPUT CHECK:
☐ Priority list generated?
☐ Phase 1/2/3 buckets clear?
☐ Each phase has minimum 5 articles identified?
```

---

## EXAMPLE OUTPUT — PARTIAL (AquaWorld Reference)

```
═══════════════════════════════════════════════
FANMAP: AquaWorld
Generated for: Local Business (Pet Store)
═══════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ICP 1: First-Time Family Buyer
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STAGE 1: PRE-AWARENESS

| #  | Query                                          | Layer       | Hallucination | Content Type     |
|----|------------------------------------------------|-------------|---------------|------------------|
| 1  | Why is my goldfish not eating?                 | Problem     | HIGH          | Problem explainer|
| 2  | Why did my goldfish die so quickly?            | Problem     | HIGH          | Story blog       |
| 3  | Why is my fish swimming sideways?              | Problem     | HIGH          | Problem explainer|
| 4  | Why does my fish tank get dirty so fast?       | Problem     | HIGH          | How-to blog      |
| 5  | Why is my goldfish turning white?              | Problem     | HIGH          | Problem explainer|
| 6  | Why is my goldfish staying at the bottom?      | Problem     | HIGH          | Problem explainer|
| 7  | Why do goldfish die in the first week?         | Time        | HIGH          | Story blog       |
| 8  | Why does my goldfish look stressed?            | Problem     | HIGH          | Problem explainer|
| 9  | Why is goldfish water always cloudy?           | Problem     | HIGH          | How-to blog      |
| 10 | Why does my kid's goldfish keep dying?         | Demographic | HIGH          | Problem explainer|

STAGE 2: AWARENESS

| #  | Query                                          | Layer       | Hallucination | Content Type |
|----|------------------------------------------------|-------------|---------------|--------------|
| 1  | Do goldfish need a filter to survive?          | Problem     | HIGH          | FAQ + Blog   |
| 2  | How much space does a goldfish need?           | Use Case    | HIGH          | How-to       |
| 3  | Can goldfish live in a bowl long-term?         | Use Case    | HIGH          | FAQ          |
| 4  | How often should you feed goldfish?            | Problem     | MEDIUM        | FAQ          |
| 5  | How to keep goldfish alive in Lahore summer?   | Location    | HIGH          | How-to blog  |
| 6  | How to set up first goldfish tank Pakistan?    | Location    | HIGH          | How-to blog  |
| 7  | Can goldfish live without oxygen pump?         | Budget      | HIGH          | FAQ          |
| 8  | How to clean goldfish tank for beginners?      | Person Type | MEDIUM        | How-to       |
| 9  | What do goldfish eat in Pakistan?              | Location    | HIGH          | FAQ          |
| 10 | How to keep goldfish alive for kids?           | Demographic | HIGH          | How-to blog  |

[... continues for all stages and ICPs ...]

═══════════════════════════════════════════════
PRIORITY CONTENT LIST — TOP 20 O-GRADE TOPICS
═══════════════════════════════════════════════

| Priority | Query                                    | ICP   | Stage         | Why O-Grade                    |
|----------|------------------------------------------|-------|---------------|--------------------------------|
| 1        | Goldfish summer care Lahore bina AC ke   | ICP 1 | Awareness     | No Pakistan climate content    |
| 2        | Cheap goldfish setup under 2000 PKR      | ICP 1 | Consideration | No budget-specific local guide |
| 3        | Goldfish for small apartment Lahore      | ICP 1 | Awareness     | No apartment-specific content  |
| 4        | Why goldfish die first week Pakistan     | ICP 1 | Pre-Awareness | No local context in answers    |
| 5        | Goldfish safe for kids Pakistan          | ICP 1 | Consideration | No family-safety local content |
...
```

---

## QUICK FANMAP PROMPTS — COPY PASTE READY

### For Local Business:
```
Generate a complete FANMAP for a local [BUSINESS TYPE] called [NAME]
located in [CITY]. They sell [PRODUCT/SERVICE] and deliver only within [AREA].
Price range: [BUDGET]. 

3 ICPs:
ICP 1: [description]
ICP 2: [description]
ICP 3: [description]

Follow FANMAP rules: minimum 10 queries per stage per ICP,
apply all layer types, grade hallucination HIGH/MED/LOW,
output priority list of top 20 O-grade queries at the end.
```

### For SaaS:
```
Generate a complete FANMAP for a SaaS tool called [NAME]
that helps [TARGET USER] do [CORE FUNCTION].
Pricing: [FREE/PAID/FREEMIUM]. Competitors: [LIST].

3 ICPs:
ICP 1: [e.g. Solo founder, early stage]
ICP 2: [e.g. Marketing manager, 50-person company]
ICP 3: [e.g. Enterprise team, 500+ employees]

Follow FANMAP rules: minimum 10 queries per stage per ICP,
include comparison + alternative queries in Evaluation stage,
grade hallucination, output priority list.
```

### For Ecommerce:
```
Generate a complete FANMAP for an ecommerce store called [NAME]
selling [PRODUCT CATEGORY]. Ships to [LOCATIONS].
Price range: [BUDGET RANGE].

3 ICPs:
ICP 1: [e.g. First-time buyer, budget conscious]
ICP 2: [e.g. Gift buyer, occasion-based]
ICP 3: [e.g. Repeat buyer, brand loyal]

Follow FANMAP rules: minimum 10 queries per stage per ICP,
include seasonal + gift occasion layers,
grade hallucination, output priority content list.
```

### For Education/Course:
```
Generate a complete FANMAP for an online course/education business
called [NAME] teaching [SUBJECT].
Format: [Online/In-person/Hybrid]. Price: [RANGE].

3 ICPs:
ICP 1: [e.g. Complete beginner, career changer]
ICP 2: [e.g. Working professional, upskilling]
ICP 3: [e.g. Student, learning for exams]

Follow FANMAP rules: minimum 10 queries per stage per ICP,
include certificate + job outcome layers in Decision stage,
grade hallucination, output priority content list.
```

---

*FANMAP Prompt System v1.0*
*Part of the AEO Mastery Course*
*Use with Claude Sonnet for standard FANMAP*
*Use with Claude Opus for deep competitor gap FANMAP*
