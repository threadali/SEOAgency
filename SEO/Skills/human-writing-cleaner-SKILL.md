---
name: human-writing-cleaner
description: "Use this skill when the user asks to clean this up, make this sound human, remove AI fluff, remove em dashes, make this more direct, rewrite naturally, fix the AI writing, or any variation of removing robotic, corporate, or over-polished language."
triggers:
  - "clean this up"
  - "make this sound human"
  - "remove AI fluff"
  - "remove em dashes"
  - "make this more direct"
  - "rewrite naturally"
  - "fix the AI writing"
---

# Human Writing Cleaner Skill

## Purpose
Clean AI-generated or AI-inflected writing to sound direct, human, and clear. Remove filler, corporate language, and structural bloat without changing the meaning or reordering content.

---

## Cleaning Rules

### Remove or Replace These Phrases

| Remove | Replace with |
|---|---|
| Em dashes (—) | Rewrite using comma or period |
| "It's worth noting that" | Cut — state the point directly |
| "It's important to note" | Cut — state the point directly |
| "In today's landscape / world / environment" | Cut the opener, start with the actual claim |
| "Leverage" | "use" |
| "Utilize" | "use" |
| "Ensure" | "make sure" or restructure |
| "Furthermore", "Moreover", "Additionally" as sentence starters | Restructure — join to prior sentence or cut |
| "In conclusion" / "To summarize" | Cut entirely |
| "This means that" | Cut — state the consequence directly |
| "Feel free to" / "Don't hesitate to" / "I hope this helps" | Cut entirely |
| "Game-changer", "revolutionary", "cutting-edge" | Describe the actual benefit instead |
| "Seamless", "robust", "holistic" | Replace with specific description or cut |
| "Simply" / "just" (used to minimize difficulty) | Cut the word; keep the instruction |
| Rhetorical questions as section openers | Rewrite as a statement |
| "Sort of", "kind of", "in a way", "somewhat" | Cut — commit to the claim or qualify precisely |
| Stacked synonyms: "key and critical", "important and essential" | Pick one word |
| Sentences starting with "This" + vague noun | Name the subject directly |

### Structural Rules
- Paragraphs over 4 lines → tighten or break into two
- Every sentence must earn its place. If removing it loses no meaning, remove it
- Do not reorder content unless something is genuinely misplaced
- Keep precise technical terms — do not simplify accurate language
- Do not add explanations that weren't in the original

### Tone Rules
- No enthusiasm injection
- No empathy performance
- No softening of direct statements
- Add reasoning only where its absence makes the point unclear
- Do not editorialize

---

## Output Format
Return **only** the cleaned content.
- No preamble ("Here's the cleaned version…")
- No sign-off ("I hope this helps!")
- No explanation of changes **unless** the user explicitly asks for a changelog

If the user asks for a changelog, list changes as brief bullet points after a `---` separator below the cleaned content.

---

## Before / After Example

**Before:**
"It's important to note that leveraging the right SEO strategy can be a game-changer for your business. In today's competitive landscape, ensuring your website is optimized is crucial — it directly impacts visibility and, moreover, revenue."

**After:**
"The right SEO strategy affects search visibility and revenue. An unoptimized site loses ground to competitors who have done the work."

---

## Notes
- Preserve the author's voice where it exists — don't flatten personality, only remove bloat
- When in doubt, cut. Shorter is almost always better
- Never add words to sound warmer or more complete
