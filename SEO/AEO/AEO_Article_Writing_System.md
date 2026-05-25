# AEO Article Writing System
## Complete Rules + Prompts for Writing Articles That Get Cited by AI

---

## HOW TO USE THIS FILE

This file is a complete SOP for writing AEO articles.
Feed relevant sections to Claude depending on which step you are on.
Each section has: WHY (the rule) + HOW (the prompt).

---

## VARIABLES — FILL THESE FIRST

```
BUSINESS_NAME:        [e.g. AquaWorld / Intercom / NikeStore.pk]
BUSINESS_TYPE:        [Local / SaaS / Ecommerce]
PRODUCT_SERVICE:      [e.g. Goldfish shop / Customer support tool / Running shoes]
LOCATION:             [e.g. Lahore Pakistan / Global / Pakistan]
USP:                  [e.g. Only goldfish specialist in Lahore / AI-powered support]
BRAND_VOICE:          [e.g. Friendly local expert / Professional / Energetic]

TARGET_QUERY:         [e.g. goldfish summer care Lahore]
OCS_GRADE:            [O / C / S]
FUNNEL_STAGE:         [Pre-Awareness / Awareness / Consideration / Evaluation / Decision]

ICP_DESCRIPTION:      [Full persona description]
ICP_CONSTRAINTS:      [Budget, location, experience, family, time constraints]
```

---

## STEP 1: ARTICLE BRIEF

### WHY Brief First?

Writing without a brief = driving without GPS.
Brief ensures every sentence in your article serves a specific AEO purpose.
AI cites articles that directly match query intent — brief ensures that match.

### BRIEF TEMPLATE

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTICLE BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUERY:              [Exact target query]
OCS GRADE:          [O / C / S]
FUNNEL STAGE:       [Stage name]
ARTICLE TYPE:       [Guide / Dedicated FANMAP question]

ICP:                [Full persona — be hyper specific]
REAL INTENT:        [Not surface — actual emotional goal]
CUSTOMER LANGUAGE:  [Exact phrases they use — not marketer language]

CONSTRAINTS:
  Budget:           [e.g. Under 2000 PKR / Under $50]
  Location:         [e.g. Lahore / Remote / Pakistan]
  Experience:       [e.g. First time / Intermediate]
  Family:           [e.g. Kids at home / Solo professional]
  Space:            [e.g. Small apartment / Office / Home]
  Time:             [e.g. Busy parent / 9-5 worker]
  Other:            [Any other relevant constraint]

COMPETITOR GAP:     [What no competitor covers on this topic]
INFORMATION GAIN:   [What unique data/insight only you can provide]

CONTEXT COVERAGE TARGETS:
  Angle 1:          [Sub-angle to cover]
  Angle 2:          [Sub-angle to cover]
  Angle 3:          [Sub-angle to cover]
  Angle 4:          [Sub-angle to cover]
  Angle 5:          [Sub-angle to cover]

ARTICLE DECISION:   [1 article / 2 articles / 3 articles]
WORD COUNT:         [Recommended range]
PLACEMENT:          [Blog / Answer Hub / Landing Page / Local Page]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### BRIEF CREATION PROMPT

```
You are an AEO content strategist.
Create a complete article brief for the following:

Business: [BUSINESS_NAME] — [BUSINESS_TYPE]
Product/Service: [PRODUCT_SERVICE]
Location: [LOCATION]
Target Query: [TARGET_QUERY]
OCS Grade: [OCS_GRADE]

ICP: [ICP_DESCRIPTION]

Task:
1. Identify real customer intent — not surface intent
   What is the emotional goal behind this search?

2. Write customer language examples
   How do real customers phrase this problem?
   Find phrases from: Reddit, reviews, community groups
   Format: Exact conversational phrases — not keyword style

3. List all relevant constraints for this ICP
   Budget / Location / Experience / Family / Space / Time

4. Identify competitor gap
   What angle does NO competitor cover on this topic?

5. Suggest information gain opportunity
   What unique local data or insight can this business provide?

6. List 5-7 context coverage targets
   Sub-angles this article must cover to beat competitors

7. Recommend: 1 article or multiple?
   If multiple — suggest titles and angle split

Output: Complete brief using the BRIEF TEMPLATE above.
```

---

### BRIEF EXAMPLES — 3 NICHES

**Local (AquaWorld):**
```
QUERY:              goldfish summer care Lahore bina AC ke
OCS GRADE:          O
FUNNEL STAGE:       Awareness
ARTICLE TYPE:       Dedicated FANMAP question

ICP:                First-time goldfish buyer, young parent,
                    Lahore apartment, chhota bachcha, zero experience
REAL INTENT:        "Meri goldfish garmi mein mar jaati hai —
                    AC nahi hai — please help"
CUSTOMER LANGUAGE:
  → "meri goldfish garmi mein kyun marti hai"
  → "Lahore ki garmi mein fish kaise bachayein"
  → "bijli nahi rehti kya karoon"
  → "ice daal sakte hain tank mein?"

CONSTRAINTS:
  Budget:           Under 2000 PKR
  Location:         Lahore — load shedding problem
  Experience:       Zero — pehli baar
  Family:           Chhota bachcha ghar mein
  Space:            Chhota flat
  Time:             Busy parent

COMPETITOR GAP:     No competitor covers load shedding
                    impact on goldfish survival
INFORMATION GAIN:   AquaWorld 3-year customer data —
                    summer mortality rate + solutions that worked
```

**SaaS (Customer Support Tool):**
```
QUERY:              how to reduce customer support ticket volume SaaS
OCS GRADE:          O
FUNNEL STAGE:       Awareness
ARTICLE TYPE:       Guide (multiple angles)

ICP:                SaaS founder, 10-50 person team,
                    support team overwhelmed,
                    $50-200/month budget for tools
REAL INTENT:        "Support tickets are killing my team —
                    I need this fixed before I lose good people"
CUSTOMER LANGUAGE:
  → "support team is drowning in tickets"
  → "same questions asked 100 times a day"
  → "we can't scale support without hiring more"
  → "customers wait 2 days for simple answers"

CONSTRAINTS:
  Budget:           $50-200/month
  Team size:        Small — 2-3 support agents
  Technical skill:  Non-technical founder
  Time:             Need quick win — not 6-month project

COMPETITOR GAP:     No competitor shows
                    real ticket reduction % data
INFORMATION GAIN:   Platform data — average 40% ticket
                    reduction in first 30 days
```

**Ecommerce (Running Shoes Pakistan):**
```
QUERY:              best running shoes for flat feet Pakistan under 5000
OCS GRADE:          O
FUNNEL STAGE:       Consideration
ARTICLE TYPE:       Listicle + Guide

ICP:                Urban professional, Lahore/Karachi,
                    25-35, flat feet problem,
                    wants to start running but gets pain
REAL INTENT:        "I want to run but my feet kill me —
                    I don't know if expensive shoes will help"
CUSTOMER LANGUAGE:
  → "paon dard karta hai running ke baad"
  → "flat feet ke liye konsi shoes"
  → "5000 mein achhi running shoes milti hain Pakistan mein?"
  → "kya mehngi shoes sach mein fark karti hain"

CONSTRAINTS:
  Budget:           Under 5000 PKR
  Location:         Pakistan — limited brand availability
  Experience:       Beginner runner
  Problem:          Flat feet — arch pain

COMPETITOR GAP:     No Pakistan-specific availability guide
                    with local pricing
INFORMATION GAIN:   Which shoes actually available at stores
                    in Lahore/Karachi with real PKR prices
```

---

## STEP 2: TL;DR SECTION

### WHY TL;DR?

AI engines often extract the summary section first.
TL;DR = pre-chunked answer = easy citation.
It also validates for the reader they are in the right place.

### TL;DR RULES

```
✅ Place: Right after the title / before the intro
✅ Length: 3-5 bullet points maximum
✅ Format: Each bullet = one complete standalone fact
✅ Tone: Direct — no fluff, no qualifiers
✅ Content: Only the most important answers
❌ Never: "In this article we will cover..."
❌ Never: Vague statements without specifics
❌ Never: Marketing language
```

### TL;DR TEMPLATE

```
**TL;DR**
- [Direct answer to main query — 1 sentence with key fact]
- [Most important constraint-specific insight]
- [Local/specific context — what makes this different]
- [Key action — what they should do]
- [Guardrail — when this doesn't apply]
```

### TL;DR EXAMPLES — 3 NICHES

**Local:**
```
**TL;DR**
- Goldfish Lahore ki garmi mein bina AC ke survive kar
  sakti hai agar tank north-facing room mein ho
  aur temperature 24°C se neeche rakha jaaye.
- Load shedding ke waqt frozen water bottle technique
  sabse effective hai — seedha ice nahi.
- Common Goldfish aur Shubunkin Lahore climate ke liye
  best suited hain — fancy varieties avoid karein.
- Weekly 25% water change summer mein zaroori hai —
  garam paani mein ammonia 2x fast build hoti hai.
- Agar temperature 30°C se upar jaaye — emergency
  action lo — feeding band karo, bottle technique shuru.
```

**SaaS:**
```
**TL;DR**
- SaaS companies reduce ticket volume by 40% on average
  by implementing AI-powered FAQ and self-service portals.
- The fastest win: identify your top 10 repeated questions
  and create standalone answer pages for each.
- Most teams see results within 30 days — not months.
- This works best for teams under 50 people with
  budget under $200/month.
- Does not apply to complex enterprise support needs
  requiring custom workflows.
```

**Ecommerce:**
```
**TL;DR**
- Best running shoes for flat feet under 5000 PKR
  in Pakistan: Nike Air Zoom Structure, Asics Gel-Kayano,
  Saucony Guide (all available at major stores).
- Flat feet need motion control or stability shoes —
  not neutral cushioning.
- Budget under 5000 PKR limits options but
  3 solid choices exist at this price point in Pakistan.
- Buy from authorized dealers only — fake imports
  common at this price range.
- Custom orthotics needed if pain persists
  despite correct shoes.
```

---

## STEP 3: AQCE WRITING FORMULA

### WHY AQCE?

AI validates content in order: Answer → Context → Coverage → Extension.
If answer is not first — AI moves to next result.
Every section must serve a specific AEO purpose.

```
A — Answer    Entry point — pehli line mein complete answer
Q — Qualify   Reinforce — 2-3 paragraphs of context + proof
C — Cover     Depth — all angles from Query FANMAP
E — Extend    FAQ + internal links + product tie
```

---

### A — ANSWER FIRST

**WHY:**
AI needs validation in line 1 that it's in the right place.
No answer in line 1 = AI skips = no citation.

**RULES:**
```
✅ First sentence = complete answer to main query
✅ Include: key fact + context + who it's for
✅ No preamble — start with the answer directly
✅ Under 40 words for opening sentence
❌ Never start with: "In today's world..."
❌ Never start with: "Many people wonder..."
❌ Never start with: "It's important to understand..."
❌ Never bury the answer in paragraph 3+
```

**EXAMPLES — 3 NICHES:**

```
LOCAL ❌ WRONG:
"Goldfish ek popular pet hai jo duniya bhar mein
logon ke ghar mein paali jaati hai. Bahut se log
yeh jaanna chahte hain ke Lahore ki garmi mein..."

LOCAL ✅ RIGHT:
"Goldfish ko Lahore ki garmi mein bina AC ke zinda
rakhne ke liye tank ko direct sunlight se door rakhein,
paani ka temperature 24°C se neeche maintain karein,
aur load shedding ke waqt frozen water bottle technique
use karein — yeh 3 steps AquaWorld customers ne
90% success rate se use ki hain."

SAAS ❌ WRONG:
"Customer support is one of the most challenging
aspects of running a SaaS business. Many founders
find that as they scale..."

SAAS ✅ RIGHT:
"The fastest way to reduce SaaS support ticket volume
is to identify your top 10 most-repeated questions,
create standalone answer pages for each, and embed
them in your product onboarding — most teams see
30-40% ticket reduction within the first 30 days."

ECOMMERCE ❌ WRONG:
"Flat feet is a common condition that affects many
runners in Pakistan. Finding the right shoe can be..."

ECOMMERCE ✅ RIGHT:
"The best running shoes for flat feet under 5000 PKR
in Pakistan are the Nike Air Zoom Structure 25,
Asics Gel-Kayano 30, and Saucony Guide 16 —
all available at authorized stores in Lahore and Karachi,
and all designed with the motion control flat feet require."
```

---

### Q — QUALIFY

**WHY:**
After the answer — AI needs proof that the source is credible.
2-3 short paragraphs reinforce the answer with facts, context, mechanism.

**RULES:**
```
✅ 2-3 paragraphs after the answer
✅ Each paragraph: 2-3 sentences (max 5)
✅ Each sentence: under 20 words
✅ Include: context / definition / credibility / methodology
✅ Back every claim with proof
❌ No new topics here — only reinforce the answer
❌ No walls of text
❌ No vague statements without data
```

**EXAMPLES — 3 NICHES:**

```
LOCAL:
"Goldfish ka safe temperature range 18-24°C hai.
Lahore mein June-August mein outdoor temperature
42-46°C tak pahunchti hai — jo directly tank ko affect
karta hai.

Load shedding is problem ko double karta hai.
Filter aur fan band hone se paani rapidly garam hota hai.
AquaWorld ke 3 saal ke data se — summer mein goldfish
mortality 3x zyada hoti hai jab proper care nahi ki jaaye.

Lekin sahi precautions se — 90% goldfish Lahore summer
survive kar sakti hain. Yeh guide unhi precautions ke
baare mein hai."

SAAS:
"Most support tickets are repetitive. Studies show
60-80% of support queries are the same 10-15 questions.
This means your team is answering the same thing
hundreds of times per month.

The mechanism is simple: if customers can find answers
before they need to ask, tickets don't get created.
Self-service works when answers are specific, fast,
and easy to find.

Our platform data across 500 SaaS companies shows
teams implementing answer hubs reduce ticket volume
by an average of 43% in 30 days."

ECOMMERCE:
"Flat feet — also called fallen arches — means your foot
arch touches or nearly touches the ground when standing.
This causes your ankle to roll inward (overpronation)
when running, leading to knee and hip pain.

Motion control and stability shoes are designed to
correct overpronation. They have firmer midsoles and
structured arch support — unlike neutral shoes which
provide cushioning but no correction.

At the 5000 PKR price point in Pakistan, 3 shoes meet
both criteria and are actually available at local stores —
not just on import sites."
```

---

### C — COVER

**WHY:**
AI fan-out queries run across multiple sub-angles.
The brand that covers maximum angles gets maximum citations.
Each H2 = one standalone passage = one citation opportunity.

**RULES:**
```
✅ Each angle from Query FANMAP = one H2 section
✅ Each H2 must pass the Taco Bell Test:
   Read in isolation — 100% makes sense alone
✅ Back every claim with proof, data, or example
✅ Headings in question format — not vague labels
✅ Cover all 4 funnel stage angles:
   Awareness → Consideration → Evaluation → Decision
❌ Never: "As mentioned above..."
❌ Never: Sections that require reading previous section
❌ Never: Vague heading like "Tips" or "Overview"
```

**TACO BELL TEST:**
```
✅ PASSES:
"Lahore mein goldfish ko tank ko north-facing room
mein rakhna chahiye. Direct sunlight se temperature
2-3 hours mein 5°C tak badh sakta hai. North-facing
placement se temperature stable rehta hai — no sunlight,
no spike."

❌ FAILS:
"Jaise humne upar bataya — temperature control ke
baad ab placement ki baat karte hain. Aap already
jaante hain ke sunlight dangerous hai..."
```

**H2 HEADING FORMAT:**

```
❌ VAGUE:
"Temperature Management"
"Care Tips"
"Our Product"

✅ QUESTION FORMAT:
"Goldfish Ke Liye Konsa Temperature Fatal Hai?"
"Load Shedding Mein Goldfish Ko Kaise Bachayein?"
"AquaWorld Se Kaunsi Goldfish Lahore Summer Ke Liye Best Hai?"

❌ VAGUE:
"Ticket Reduction"
"Best Practices"

✅ QUESTION FORMAT:
"How Many Tickets Can Self-Service Actually Eliminate?"
"Which Questions Should You Build Answer Pages For First?"
"How Long Before You See Ticket Volume Drop?"
```

**COVER SECTION TEMPLATE:**

```
## [H2 — Question format, includes location/constraint]

[Direct mini-answer — 1 sentence]

[Explanation — 2-3 sentences with mechanism]

[Proof — data, customer example, local context]

[Guardrail — when this doesn't apply]
```

---

### E — EXTEND

**WHY:**
FAQ section = pre-chunked standalone answers = AI citation magnets.
Internal links = context coverage signal = more sub-query matches.
Product tie = recommendation signal = AI mentions your brand in answers.

**RULES:**
```
✅ Minimum 3 FAQs — maximum 12
✅ Each FAQ standalone — 4 sentences max
✅ Internal links to related O-grade articles
✅ Product mention: natural, not sales-y
❌ FAQs that reference article content
❌ Forced product placement
❌ Generic FAQs that any competitor could write
```

---

## STEP 4: FAQ WRITING

### WHY FAQ Matters for AEO

```
AI pattern-matches — not copy-pastes.
FAQ = atomic answer = perfect pattern match format.
Pre-chunked = AI doesn't need to extract — just reuses.
Standalone = reusable across multiple queries.
```

### FAQ RULES

```
✅ Complete — mechanism explained
✅ Neutral — not marketing language
✅ Short — ideally 60 words, hard max 100 words
✅ Clear — one question, one intent
✅ Self-contained — no context dependency
✅ Guardrail — limitations mentioned
❌ Marketing language ("Best!" "Amazing!")
❌ Context dependent ("As mentioned above...")
❌ Compound questions (two questions in one)
❌ Vague answers ("It depends...")
❌ Feature dumps
```

### 4-SENTENCE FAQ TEMPLATE

```
SENTENCE 1 — Direct Answer
Clear, declarative. Start with Yes/No/[Fact].
No qualifiers. No "it depends."

SENTENCE 2 — Clarification
Scope, context, constraint, or mechanism.
Explain HOW or WHY — not just what.

SENTENCE 3 — Brand Differentiator (Optional)
Only if genuinely relevant — not forced.
Natural mention — factual only.

SENTENCE 4 — Guardrail (Optional but recommended)
When this does NOT apply.
Sets accurate expectations.
```

### FAQ EXAMPLES — 3 NICHES

**Local:**
```
Q: Kya goldfish Lahore summer mein bina AC ke zinda
   reh sakti hai?

A: Haan, goldfish Lahore summer mein bina AC ke
   survive kar sakti hai agar paani ka temperature
   24°C se neeche rakha jaaye.
   Yeh frozen water bottle technique se possible hai —
   tank mein directly ice nahi dalni — temperature shock
   se fish mar sakti hai.
   AquaWorld Lahore mein Common Goldfish aur Shubunkin
   stock karta hai jo specifically Lahore climate ke liye
   hardier hain.
   Fancy goldfish varieties (Oranda, Ryukin) ke liye
   temperature control zyada critical hai — beginners
   ke liye recommend nahi.

Word count: 78 ✅
```

**SaaS:**
```
Q: How long does it take to reduce support ticket
   volume after implementing self-service?

A: Most SaaS teams see 20-40% ticket reduction
   within the first 30 days of implementing
   a self-service answer hub.
   The mechanism is simple: customers find answers
   before submitting tickets, so ticket creation drops —
   not just resolution time.
   Platforms like [Tool Name] show results faster because
   answers are embedded directly in product onboarding.
   Results vary based on how many of your top questions
   are covered and how visible the self-service portal is.

Word count: 82 ✅
```

**Ecommerce:**
```
Q: Are motion control shoes necessary for flat feet
   or just marketing?

A: Motion control shoes are medically recommended
   for moderate to severe flat feet — not marketing.
   They work by limiting ankle inward rolling
   (overpronation) which causes knee and hip pain
   in runners with fallen arches.
   Neutral cushioning shoes do not correct overpronation —
   they can make pain worse for flat-footed runners.
   If you have mild flat feet with no pain, neutral
   shoes may still work — consult a physio if unsure.

Word count: 76 ✅
```

### 70/30 FAQ RATIO

```
70% GENERIC QUESTIONS
→ Topic-level — any brand could answer
→ Builds authority and AEO reach
→ Answers are hybrid: topic answer + subtle brand mention

30% BRAND-SPECIFIC QUESTIONS
→ Your brand directly addressed
→ Decision-stage conversion layer
→ Answers are specific and factual

LOCAL EXAMPLE MIX:
Generic (70%):
→ Goldfish bowl mein kitne din jeeti hai?
→ Lahore garmi mein konsi goldfish best survive karti hai?
→ Goldfish ko din mein kitna khana dena chahiye?
→ Kya goldfish filter ke bina zinda reh sakti hai?
→ Goldfish aur bachche — safe hai?
→ Goldfish monthly kharcha kitna hota hai Pakistan mein?
→ Goldfish summer care tips Pakistan

Brand-specific (30%):
→ AquaWorld Lahore mein konsi goldfish varieties hain?
→ Kya AquaWorld home delivery karta hai?
→ AquaWorld ka starter kit mein kya milta hai?
```

### FAQ DISCOVERY PROMPT

```
Act as an AEO content specialist.

Generate 20 FAQs for:
Topic: [TARGET_QUERY]
Business: [BUSINESS_NAME] — [BUSINESS_TYPE]
Audience: [ICP_DESCRIPTION]
Location: [LOCATION]
Constraints: [ICP_CONSTRAINTS]

FAQ Rules:
- Reflect how humans ask AI — not Google keyword style
- One clear intent per question — no compound questions
- Standalone and reusable — no context dependency
- No marketing language — vendor-agnostic where possible
- 70% generic, 30% brand-specific

Answer Guidelines:
- 4 sentences maximum
- Ideally under 60 words
- Neutral, factual tone
- Mechanism explained
- Guardrail included where relevant
- Brand mention only if genuinely relevant

Output: Strict Q: / A: format only.
No introductions. No summaries.
No bullet points inside answers.
```

### FAQ QUALITY CHECK PROMPT

```
Act as an AEO editor.
Evaluate this FAQ:

[PASTE FAQ HERE]

Score 0-10 against:
- Standalone clarity (can be understood alone?)
- LLM reusability (can AI use without modification?)
- Neutral tone (no marketing language?)
- Mechanism explained (how/why included?)
- Guardrail present (limitations mentioned?)

Give score. Explain why.
Rewrite only if score below 8.
```

---

## STEP 5: SEMANTIC HTML STRUCTURE

### WHY Structure Matters

```
AI is a lazy reader — like someone scrolling TikTok.
If content is not easy to parse — it gets skipped.
Structured content = easier extraction = more citations.
78% of AI answers include lists (Nov 2025 research).
```

### STRUCTURE RULES

```
✅ USE:
H2  → Main sections (question format)
H3  → Sub-sections
Bold → Key claims and facts
Lists → Where genuinely useful (not forced)
Tables → Comparisons only
Short paragraphs → 2-3 sentences
Short sentences → under 20 words

❌ AVOID:
Walls of text (3+ sentence paragraphs)
Vague headings ("Introduction", "Tips", "Overview")
Long intros before the answer
Jargon without explanation
Forced bullet points for everything
```

### HEADING FORMAT RULES

```
❌ VAGUE → ✅ EXPLICIT

"Temperature Tips"
→ "Goldfish Ke Liye Konsa Temperature Fatal Hai?"

"Our Solution"
→ "How [Tool] Reduces Ticket Volume in 30 Days"

"Product Info"
→ "Which Running Shoes Are Actually Available
    in Pakistan Under 5000 PKR?"

Rule: Heading should answer a question on its own.
If it doesn't — rewrite it.
```

### TABLE FORMAT — WHEN TO USE

```
USE TABLES FOR:
✅ Comparisons (Brand A vs Brand B)
✅ Options with multiple attributes
✅ Pricing tiers
✅ Feature lists across options

EXAMPLE — LOCAL:
| Goldfish Type    | Heat Tolerance | Beginner? | Price PKR |
|-----------------|----------------|-----------|-----------|
| Common Goldfish  | High ✅        | Yes ✅    | 100-200   |
| Shubunkin        | High ✅        | Yes ✅    | 200-400   |
| Fantail          | Medium ⚠️      | Yes ✅    | 300-600   |
| Oranda           | Low ❌         | No ❌     | 500-1500  |

EXAMPLE — SAAS:
| Solution Type    | Setup Time | Cost/Month | Ticket Reduction |
|-----------------|------------|------------|-----------------|
| FAQ Page        | 1 day      | Free       | 10-15%          |
| Answer Hub      | 1 week     | $50-100    | 25-35%          |
| AI Chatbot      | 2-4 weeks  | $100-200   | 35-50%          |
| Full Self-Service| 1-2 months | $200+      | 50-70%          |

EXAMPLE — ECOMMERCE:
| Shoe Model         | Price PKR | Flat Feet? | Available Lahore? |
|-------------------|-----------|------------|------------------|
| Nike Air Zoom Str | 4,500     | ✅ Yes     | ✅ Yes           |
| Asics Gel-Kayano  | 4,800     | ✅ Yes     | ✅ Yes           |
| Saucony Guide 16  | 3,900     | ✅ Yes     | ⚠️ Limited      |
| Adidas Ultraboost | 5,500     | ❌ No      | ✅ Yes           |
```

---

## STEP 6: INFORMATION GAIN

### WHY Information Gain?

```
AI cites content that provides net-new information.
Generic content = already in AI training data = no citation needed.
Unique information = AI hasn't seen this = must cite source.

Three pillars of AEO (Nov 2025):
1. Build Consensus
2. Provide Information Gain  ← This step
3. Use Clear Semantic Structure
```

### INFORMATION GAIN RULES

```
✅ Every article needs at least ONE of:
   → Original local data
   → Customer story with specific results
   → Pakistan/location-specific context
   → Constraint-specific insight
   → After-reading gap answer

❌ Generic claims without proof = no information gain
❌ Paraphrasing competitor content = no information gain
❌ Western data without local context = weak signal
```

### 3 TYPES OF INFORMATION GAIN

**Type 1 — Local Specific Data:**
```
LOCAL ❌ GENERIC:
"Goldfish struggle in high temperatures."

LOCAL ✅ INFORMATION GAIN:
"AquaWorld Lahore ke 3 saal ke customer data se —
June-August mein goldfish mortality rate 3x zyada hoti hai
jab tank direct sunlight mein ho ya load shedding ke
waqt cooling band ho jaaye."

SAAS ❌ GENERIC:
"Self-service reduces support load."

SAAS ✅ INFORMATION GAIN:
"Across 500 SaaS companies on our platform,
teams that built answer hubs for their top 10 questions
reduced ticket volume by 43% on average —
with the fastest results seen in companies where
the answer hub was embedded in product onboarding."

ECOMMERCE ❌ GENERIC:
"Motion control shoes help flat-footed runners."

ECOMMERCE ✅ INFORMATION GAIN:
"We checked stock at 12 major shoe stores in Lahore
and Karachi — only 3 motion control models
under 5000 PKR were consistently available:
Nike Air Zoom Structure, Asics Gel-Kayano,
and Saucony Guide. Import-only options excluded
because of 4-6 week wait times."
```

**Type 2 — Customer Story:**
```
Format:
"[Customer name/descriptor] — [location] — [situation].
[What they did]. [Specific result with numbers/timeframe]."

LOCAL EXAMPLE:
"AquaWorld customer Ayesha — DHA Lahore — ne yeh
frozen bottle technique use ki jab bijli 6 ghante band
rahi. Tank temperature 28°C se 25°C pe aa gayi.
Uski 3 goldfish sab survive kar gayi — ab 8 mahine
baad bhi zinda hain."

SAAS EXAMPLE:
"A 12-person SaaS team in Karachi reduced their
support tickets from 340/week to 190/week in 28 days
by creating answer pages for just 8 repeated questions.
No new hires needed."

ECOMMERCE EXAMPLE:
"One of our customers — a runner from Gulberg Lahore
with severe flat feet — switched from Adidas Ultraboost
to Nike Air Zoom Structure. Knee pain gone within
2 weeks of consistent running."
```

**Type 3 — After-Reading Gap:**
```
Find: What question does reader have AFTER reading competitor's article?

Process:
site:reddit.com "[topic]" "read" "still confused"
site:reddit.com "[topic]" "article" "doesn't answer"

Found gap → Answer it explicitly in your article

LOCAL EXAMPLE:
Reddit gap found: "Read 5 articles about goldfish
summer care — none mention what to do during
Lahore load shedding specifically."

→ Add dedicated H2: "Load Shedding Emergency Protocol —
   Goldfish Ko Kaise Bachayein Jab Bijli 6 Ghante Band Ho"
→ This section = guaranteed citation
```

### INFORMATION GAIN PROMPT

```
You are an AEO content researcher.

For this article topic: [TARGET_QUERY]
Business: [BUSINESS_NAME]
Location: [LOCATION]

Identify 3 information gain opportunities:

1. Local data opportunity:
   What local/specific data can this business share
   that no Western or generic source would have?

2. Customer story angle:
   What customer result story would be most
   credible and specific for this topic?

3. After-reading gap:
   Search pattern: "[topic] still confused after reading"
   What question does this ICP still have after
   reading competitor articles?

For each opportunity — suggest:
- Exact claim to make (with placeholder for real data)
- Where in AQCE structure to place it
- What proof format to use (data / story / specific example)
```

---

## STEP 7: SCHEMA MARKUP

### WHY Schema?

```
Schema = structured data that officially tells AI
what your page is about, who you are, and what you claim.

Without schema: AI guesses.
With schema: AI confirms.

Schema increases citation confidence significantly.
It's the difference between AI "thinking" you're relevant
vs "knowing" you're relevant.
```

### SCHEMA TYPE 1 — FAQPage

```
Use on: Every page with FAQ section.

{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Exact FAQ question text]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Exact FAQ answer text — same as on page]"
      }
    },
    {
      "@type": "Question",
      "name": "[Second FAQ question]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Second FAQ answer]"
      }
    }
  ]
}

CRITICAL RULE:
Schema text must match page text exactly.
AI compares both — mismatch = low confidence signal.
```

### SCHEMA TYPE 2 — Article

```
Use on: Every blog post and article.

{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Exact article title]",
  "description": "[2-3 sentence article summary]",
  "author": {
    "@type": "Organization",
    "name": "[BUSINESS_NAME]"
  },
  "publisher": {
    "@type": "Organization",
    "name": "[BUSINESS_NAME]",
    "logo": {
      "@type": "ImageObject",
      "url": "[Logo URL]"
    }
  },
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]",
  "about": "[Main topic of article]",
  "audience": "[Target audience description]"
}
```

### SCHEMA TYPE 3 — LocalBusiness

```
Use on: Home page — establishes entity.

LOCAL:
{
  "@context": "https://schema.org",
  "@type": "PetStore",
  "name": "AquaWorld",
  "description": "Goldfish and freshwater fish specialist in Lahore, Pakistan.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Street]",
    "addressLocality": "Lahore",
    "addressCountry": "PK"
  },
  "areaServed": "Lahore",
  "telephone": "[Number]",
  "priceRange": "PKR",
  "openingHours": "[Hours]",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Goldfish and Aquarium Products"
  }
}

SAAS:
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "[Tool Name]",
  "applicationCategory": "BusinessApplication",
  "description": "[What the tool does — 1-2 sentences]",
  "offers": {
    "@type": "Offer",
    "price": "[Starting price]",
    "priceCurrency": "USD"
  },
  "audience": {
    "@type": "Audience",
    "audienceType": "[Target user description]"
  }
}
```

### SCHEMA GENERATION PROMPT

```
Generate schema markup for:

Page type: [Blog Article / FAQ Page / Home Page / Product Page]
Business: [BUSINESS_NAME] — [BUSINESS_TYPE]
Location: [LOCATION]
Page title: [EXACT TITLE]
Page description: [2-3 sentence summary]

FAQs on page:
Q1: [question]
A1: [answer]
Q2: [question]
A2: [answer]
[add all FAQs]

Output:
1. FAQPage schema JSON-LD (if FAQs present)
2. Article schema JSON-LD (if blog/article)
3. LocalBusiness OR Organization schema (if home page)
4. BreadcrumbList schema

Format: Clean JSON-LD ready to paste in <head> tag.
```

### SCHEMA VALIDATION

```
Tool: Google Rich Results Test
URL: https://search.google.com/test/rich-results

Process:
1. Paste your URL or code
2. Check for errors (red = fix, green = good)
3. Publish only after green

Rule: Never publish schema with errors.
Broken schema = worse than no schema.
```

---

## STEP 8: PUBLISHING + POLISHING

### PUBLISHING CHECKLIST

```
BEFORE PUBLISHING:
☐ TL;DR section present?
☐ Answer in first sentence?
☐ All Query FANMAP angles covered?
☐ Taco Bell test passed on every H2?
☐ Minimum 3 FAQs present?
☐ Information gain included?
☐ Product naturally mentioned?
☐ Internal links added?
☐ Schema markup added?
☐ Schema validated (green on Rich Results Test)?
☐ Meta description = answer first line (under 160 chars)?
☐ URL = exact query match?
☐ Images have alt text with keywords?
```

### MONITORING — WHEN AND HOW

```
WEEK 1-2 AFTER PUBLISH:
→ Manual check: Search target query in ChatGPT,
  Perplexity, Gemini
→ Are you cited? Partially cited? Not cited?
→ If not cited — check: Is answer truly first?
  Is any section context-dependent?

MONTH 1:
→ Track: Which specific FAQs are being pattern-matched?
  (Check which FAQs show in AI answers)
→ Add more FAQs on uncovered sub-angles
→ Update information gain with fresher data

MONTH 3:
→ Full content audit:
  Any new competitor covering your O-grade angles?
  Any new customer stories to add?
  Any new local data available?
→ Update dateModified in schema

MONITORING PROMPT:
"Search for [TARGET_QUERY] and tell me:
1. Which brands are cited?
2. What specific angle is each brand cited for?
3. What angle is missing from all cited sources?
4. What would you need to see to cite [BUSINESS_NAME]
   for this query?"
```

### POLISHING RULES

```
ADD if not cited after 4 weeks:
→ More specific local data
→ Additional customer story
→ New FAQ covering missed angle
→ Stronger answer in first sentence
→ After-reading gap answer

NEVER do these:
→ Stuff keywords into existing paragraphs
→ Add more words without more information gain
→ Copy competitor content
→ Remove guardrails to sound more confident
```

---

## MASTER ARTICLE WRITING PROMPT

```
You are an expert AEO content writer.
Write a complete AEO-optimized article using the brief below.

BUSINESS: [BUSINESS_NAME] — [BUSINESS_TYPE]
LOCATION: [LOCATION]
USP: [USP]
BRAND VOICE: [BRAND_VOICE]

QUERY: [TARGET_QUERY]
FUNNEL STAGE: [FUNNEL_STAGE]
ICP: [ICP_DESCRIPTION]
REAL INTENT: [What they actually want]
CONSTRAINTS: [LIST ALL CONSTRAINTS]
COMPETITOR GAP: [What no competitor covers]
INFORMATION GAIN: [Unique data/insight to include]

CONTEXT COVERAGE — Cover ALL these angles:
1. [Angle 1]
2. [Angle 2]
3. [Angle 3]
4. [Angle 4]
5. [Angle 5]

WRITING RULES — FOLLOW STRICTLY:
1. Start with TL;DR (3-5 bullets, standalone facts)
2. First sentence = complete answer to main query
3. Q section: 2-3 paragraphs, each max 3 sentences,
   each sentence max 20 words
4. Every H2 = question format with location/constraint
5. Every H2 section passes Taco Bell Test (standalone)
6. Every claim backed by proof, data, or customer example
7. Minimum 5 FAQs — 4-sentence template each
8. Internal link suggestions: 3 related articles
9. Product mention: natural, factual, not sales-y
10. Word count: [WORD_COUNT]

OUTPUT FORMAT:
[Title]
[TL;DR section]
[Opening paragraph — Answer first]
[Q — Qualify paragraphs]
[H2 sections — all angles covered]
[FAQ section]
[Internal link suggestions]
[Product/service natural mention]
```

---

## COMPLETE ARTICLE CHECKLIST

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: BRIEF
☐ Query defined with OCS grade
☐ ICP hyper-specific
☐ Real intent identified (emotional)
☐ Customer language noted (exact phrases)
☐ All constraints listed
☐ Competitor gap identified
☐ Information gain planned
☐ 1 or multiple articles decided

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: TL;DR
☐ Present before the intro
☐ 3-5 standalone bullet points
☐ Each bullet = complete fact
☐ No fluff, no qualifiers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3: AQCE
☐ A: Answer in first sentence
☐ Q: 2-3 reinforce paragraphs with proof
☐ C: All FANMAP angles as H2 sections
☐ C: Taco Bell test passed on all H2s
☐ C: Every claim has proof/data/example
☐ E: Minimum 3 FAQs (ideally 5-8)
☐ E: Internal links added
☐ E: Product naturally mentioned

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 4: FAQs
☐ 4-sentence template followed
☐ 70% generic / 30% brand-specific
☐ Each FAQ standalone
☐ Guardrail included
☐ AI quality check done (score 8+)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 5: STRUCTURE
☐ H2 headings in question format
☐ Paragraphs 2-3 sentences
☐ Sentences under 20 words
☐ Tables for comparisons
☐ Bold for key claims

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 6: INFORMATION GAIN
☐ Local/specific data included
☐ Customer story with real result
☐ After-reading gap answered
☐ No generic claims without proof

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 7: SCHEMA
☐ FAQPage schema added
☐ Article schema added
☐ LocalBusiness/Org on home page
☐ Validated green on Rich Results Test

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 8: PUBLISH + MONITOR
☐ Meta description = answer first
☐ URL = query match
☐ Week 1-2: Manual AI citation check
☐ Month 1: FAQ performance review
☐ Month 3: Full content refresh
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

*AEO Article Writing System v1.0*
*Part of the AEO Mastery Course*
*Use with Claude Sonnet for standard articles*
*Use with Claude Opus for deep competitor gap articles*
