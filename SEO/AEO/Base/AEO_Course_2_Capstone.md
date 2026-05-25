# AEO Course 2.0 — Capstone Labs
## Lab 4 and Lab 5

**Purpose:** The capstone labs convert course knowledge into demonstrated practitioner capability. Lab 4 produces a complete client deliverable. Lab 5 produces a running automation workflow. Both are portfolio pieces.

---

## Lab 4 — Full Client AEO Audit

### Overview

A complete AEO audit for a real or realistic business. This is the exact deliverable you would hand to a paying client at the end of a first engagement. It takes six to eight hours to complete. The quality of this lab determines whether you can pitch and charge for AEO professionally.

---

### Business Selection

Choose one of the following:

**Option A:** A real business you have access to (your own business, a client, a business owned by someone you know who gives permission)

**Option B:** A realistic hypothetical business with enough specificity to run genuine platform checks. "Digital marketing agency in Lahore" works. "Generic business" does not — the platform checks need to return real results.

The business must have: a website, a target query set you can run in AI platforms, and enough context to define three ICPs.

---

### Deliverable Structure

Submit a document containing all six sections below. Each section has a specific standard. A section that does not meet its standard needs to be resubmitted.

---

**Section 1: AI Visibility Baseline**

Run the business's top twenty queries across ChatGPT, Perplexity, Google AI Overview, and Gemini. Present results as a table.

Required columns: Query | ChatGPT | Perplexity | Google AIO | Gemini | OCS Grade

For each platform column: write the brand cited if the business is cited, write the competitor name if a competitor is cited, write "not cited / hallucination" if the answer is weak or the query was deflected.

*Standard:* Table is complete for all twenty queries across all four platforms. OCS grades are assigned and defensible based on the observed output pattern, not assumed.

---

**Section 2: Competitor Orbit Map**

Produce the Orbit Map from three journeys.

Journey 1 output: three to five Core Orbit competitors confirmed on two or more platforms across the base keywords.

Journey 2 output: three to five Active Competitors identified from layered queries, not appearing in Journey 1.

Journey 3 output: at minimum three O-grade or O+ grade queries where no meaningful competitor appears and AI gives a weak or deflected answer. These are the hallucination zones.

Topic Ownership Map: a table showing which topics each competitor owns, which are contested, and which are empty. Minimum fifteen rows.

*Standard:* Competitors are confirmed through live platform checks, not assumed. Every Outer Orbit entry has a documented AI answer pattern explaining why it is classified O-grade.

---

**Section 3: Hallucination Gap Inventory**

From the Orbit Map Journey 3 output and the FANMAP run for this business, produce a list of the top ten hallucination gap topics.

For each topic include: the exact query, the OCS grade, a one-sentence description of why AI currently handles it poorly, and the information gain source — what specific information the business has that would fill this gap.

*Standard:* Every O-grade topic has a documented information gain source. "General expertise" is not an information gain source. A specific data point, customer outcome, constraint-specific knowledge, or local context qualifies.

---

**Section 4: On-Page Assessment**

Select the top five existing articles on the business website (or create five brief descriptions for a hypothetical business). Run each through the AQCE audit from Module 5.

For each article: does the opening pass the Voice Test, is there a Qualify section with evidence and guardrail, does every H2 pass the Taco Bell Test, is the information gain score above zero, does a FAQ section exist, is FAQPage schema present and validated.

Produce a retrofit priority categorization: Category A (retrofit immediately), B (Phase 2), C (archive or redirect). Include the reasoning for each categorization.

*Standard:* The categorization reasoning references specific AQCE failure points, not general quality assessments. "Article is thin" is not a standard. "Article opening does not pass Voice Test and FAQ section is absent" is a standard.

---

**Section 5: Off-Page Assessment**

NAP consistency check: verify name, address, phone number across at minimum five platforms (website, Google Business Profile, two directories, one social profile). Document any inconsistencies.

Review assessment: volume, recency, and keyword content quality. Are reviews specific or generic? Do they contain location, product, and outcome language?

Entity establishment: is there a Wikidata entry? Is a Google Knowledge Panel present? Is it claimed?

Community presence: any Reddit or Quora mentions of the brand in the last twelve months? Note the nature and quality of those mentions.

*Standard:* All fields are based on actual checks, not assumptions. If a platform cannot be found, state that explicitly.

---

**Section 6: Phase 1 Recommendations**

Based on the five sections above, produce the Phase 1 action plan.

Eight articles: for each article, state the exact target query, the OCS grade, the content type (micro-answer, educational guide, VS page, problem explainer), the ICP it targets, the estimated information gain source, and the expected citation platform and timeline.

Three off-page priorities: the three most impactful off-page actions based on the Section 5 assessment. Each stated as a specific action (not "improve reviews" but "implement two-week post-purchase WhatsApp follow-up targeting twenty new reviews in sixty days with prompt focused on outcome language").

Schema priorities: which pages need which schema types in which order.

*Standard:* Every recommendation is traceable back to a finding in Sections 1 through 5. No generic recommendations. No recommendations that are not directly supported by the audit findings.

---

### Quality Check Before Submitting

Before submitting the audit, run through this checklist:

- Does Section 1 table contain all twenty queries across all four platforms with genuine platform check results?
- Does Section 2 contain documented evidence for each competitor type, not just names?
- Does Section 3 have a specific information gain source for every O-grade topic?
- Does Section 4 cite specific AQCE failure points for every retrofit categorization?
- Does Section 5 include actual NAP comparison results?
- Does Section 6 contain eight fully specified articles and three fully specified off-page actions?

A section that contains "research needed" or "TBD" has not been completed. The audit is submitted only when all six sections meet their standard.

---

## Lab 5 — Automation Buildout

### Overview

A complete working automation stack for the AEO workflow. This lab converts Module 10's automation framework from theoretical to operational. By the end, you have five Claude Projects set up, tested, and producing consistent output.

This lab is completed alongside Lab 4 — run the automation on the Lab 4 business.

---

### Deliverable 1: Five Claude Projects Set Up

Set up all five Claude Projects from Module 10. For each project, document:

**Project name and purpose**
**System context installed** — paste the full system context you installed in the project, with all variables filled in for the Lab 4 business
**Test run result** — paste one complete output from each project run on the Lab 4 business
**Quality gate result** — did the output meet the benchmark standard? What specifically needed editing before it was usable?

Download all five project prompts and context templates from: rankarrow.com/aeo-automation

*Standard:* Each project must produce at least one output that has been run through the quality gate and documented as either passing or failing with specific reasons.

---

### Deliverable 2: Brief-to-Draft Pipeline Run

Run one complete article through the brief-to-draft pipeline using the Lab 4 business.

Document each step:

**Step 1: Brief** — completed seven-field brief for one Phase 1 article from Lab 4. All fields filled.

**Step 2: Draft generation** — paste the Article Generator Project output. Note the time taken.

**Step 3: Four-pass editing** — document each pass with the specific changes made.
- AQCE pass: what was changed and why
- Information gain pass: the three claims added that were not in the generated draft
- Human writing pass: which killer phrases removed, which structural patterns corrected
- FAQ quality pass: which FAQs revised and why

**Step 4: Article Checker audit** — run the edited draft through the Article Checker Project. Paste the scored report. Note what score was achieved and what the top three improvement recommendations were.

**Step 5: Final article** — the publish-ready version after all four passes.

*Standard:* The final article passes the Voice Test, contains three documented information gain claims, has no killer phrases, and has a FAQ section where all answers pass the standalone test.

---

### Deliverable 3: Monitoring Setup

Set up the monthly citation audit tracking sheet for the Lab 4 business.

The sheet must contain:
- Twenty target queries as rows
- Four platform columns (ChatGPT, Perplexity, Google AIO, Gemini)
- Current month baseline filled in from Lab 4 Section 1 data
- AI SOV formula calculated from baseline data
- Refresh date column for every published article
- Monthly action items section

Run the monitoring prompt from Module 9 for two of the Lab 4 business's target queries. Document the output and note what the prompt revealed about gaps the standard audit did not surface.

*Standard:* Sheet is fully set up and usable for monthly updates without rebuilding. Baseline month is filled in. AI SOV is calculated.

---

### Deliverable 4: Time Comparison

Document the time taken for each automation step versus the estimated manual time.

| Task | Manual time estimate | Automated time | Time saved |
|---|---|---|---|
| FANMAP generation | | | |
| Article brief completion | | | |
| Article draft (first version) | | | |
| FAQ generation (30 candidates) | | | |
| Article audit (scored report) | | | |
| Schema generation | | | |
| Monthly citation audit | | | |

*Standard:* Times are based on actual measurements from this lab, not estimates. Manual time is an honest estimate of how long the task would take without the automation.

---

### Capstone Completion Standard

A student who completes both labs has demonstrated:

- The ability to produce a professional AEO audit that could be delivered to a paying client
- A working automation stack that reduces per-article execution time by at least 40%
- A monitoring setup that will catch citation changes before they become losses
- The judgment to know when automation output meets standard and when it needs editing

These are the practitioner capabilities that distinguish a student who has read the course from a practitioner who can execute it.

---

## A Final Note

The course gave you the system. The labs give you the evidence that you can run it.

Most people complete courses and never use them. The practitioners who apply this material — who build the FANMAP, write the briefs, set up the Claude Projects, run the audits, and maintain the monitoring — build something that compounds.

Citations in two weeks. Authority in six months. A competitive position that is very difficult to close in twelve.

Start with Lab 4. Use a real business if possible. The closer the work is to real conditions, the more useful it is when you face real conditions with a paying client.

---

*AEO Course 2.0 — Capstone Labs | Ali Sheikh | rankarrow.com*
*youtube.com/@AliSheikhSEO | rankarrow.com/aeo-automation*
