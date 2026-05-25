# Claude Skill Builder — Project Instructions

Add these instructions to your Claude Project so every skill you generate follows the official Anthropic format perfectly.

---

## Core Rules (Always Apply)

When I ask you to create a skill, always follow these rules without exception:

1. **Output a single SKILL.md file** — nothing else unless I ask for supporting files
2. **Start with YAML frontmatter** — the file must open with `---`
3. **Only two frontmatter fields are valid**: `name` and `description`
4. **No extra frontmatter fields** — do not add `triggers`, `tags`, `version`, `author`, or anything else
5. **Keep SKILL.md under 500 lines**
6. **Write in Markdown** after the frontmatter block

---

## Frontmatter Rules

```yaml
---
name: verb-ing-skill-name
description: "Third-person description of what the skill does and exactly when to use it."
---
```

### `name` field
- Use **gerund form** (verb + -ing): `cleaning-human-writing`, `generating-reports`, `reviewing-contracts`
- Lowercase letters, numbers, and hyphens only — no spaces, no uppercase
- Keep it short and descriptive

### `description` field
- Always write in **third person** ("Generates...", "Cleans...", "Reviews...") — never "Use this when I..." or "This skill..."
- Include **what the skill does** AND **when to use it** in the same field
- Be **explicit about triggers** — list the user phrases that should activate this skill
- Be slightly **"pushy"** — Claude tends to undertrigger skills, so the description should proactively say when to load it, even if the user doesn't use exact words
- Wrap the entire value in **double quotes**

**Good example:**
```yaml
description: "Generates SEO-optimized blog post outlines. Use whenever the user asks to plan a blog post, create a content outline, structure an article, or brainstorm post sections — even if they don't explicitly say 'SEO' or 'outline'."
```

**Bad example:**
```yaml
description: "Use this skill to help with blog posts."
```

---

## SKILL.md Body Structure

After the frontmatter, write the skill instructions in Markdown. Use this structure:

```
# Skill Name (Title Case, human-readable)

## Purpose
One or two sentences. What does this skill do and why does it exist.

## Instructions / Steps / Rules
The core logic. Use numbered steps for procedures, bullet points for rules, tables for mappings.

## Output Format
What exactly should Claude return. Be specific:
- What to include
- What to omit
- Any special formatting (e.g. "return only the result, no preamble")

## Examples
At least one Before/After or Input/Output example.

## Notes (optional)
Edge cases, caveats, things to preserve or avoid.
```

---

## Writing Good Instructions

- **Use numbered steps** for procedures — Claude follows sequences more reliably than unstructured prose
- **Use tables** for find/replace rules or mappings
- **Set explicit boundaries**: "Do not modify X", "Only return Y", "Never add Z"
- **Include at least one example** — concrete examples improve output quality significantly
- **Be specific about output format** — vague instructions produce vague outputs
- **Do not repeat** information already in the description

---

## What NOT to Include

- ❌ `triggers:` field in frontmatter — not a valid field
- ❌ `version:`, `author:`, `tags:` — not valid fields
- ❌ First-person language in description ("I will...", "Use me when...")
- ❌ Unnecessary preamble in skill body ("This skill is designed to help you...")
- ❌ More than 500 lines total
- ❌ Vague descriptions that don't mention when to trigger

---

## Optional: Supporting Files

For complex skills, you can reference supporting files. Place them in subfolders and reference them explicitly in SKILL.md:

```
skill-name/
├── SKILL.md              ← required
├── references/           ← documentation Claude loads on demand
│   └── reference.md
├── scripts/              ← executable code
│   └── process.py
└── assets/               ← templates, icons, fonts
    └── template.txt
```

Reference them in SKILL.md like:
> "For detailed rules, see `references/reference.md`."

Claude will only load these files when needed, keeping context efficient.

---

## Skill Invocation Control (Optional Frontmatter)

These two optional fields control who can invoke the skill:

```yaml
disable-model-invocation: true   # Only the user can invoke (good for /deploy, /commit)
user-invocable: false            # Only Claude invokes it automatically (good for background knowledge)
```

Use `disable-model-invocation: true` for skills with side effects (sending messages, deploying code) where you don't want Claude deciding when to run them.

---

## Upload to Claude.ai

1. Create a folder named after the skill (e.g. `cleaning-human-writing/`)
2. Put `SKILL.md` inside it
3. Zip the folder
4. Go to **Settings → Customize → Skills** → upload the zip

---

## Quick Reference Card

| Rule | Value |
|---|---|
| Frontmatter fields | `name` and `description` only |
| Name format | gerund-form, lowercase, hyphens |
| Description voice | Third person |
| Description style | Pushy — explicit about when to trigger |
| Max file length | 500 lines |
| Min examples | 1 Before/After |
| Output instruction | Always specify exactly what to return |

---

## Example: Minimal Valid Skill

```markdown
---
name: summarizing-articles
description: "Summarizes articles, blog posts, and long-form content into concise key points. Use whenever the user pastes an article and asks for a summary, TL;DR, key takeaways, or asks what something is about — even if the word 'summarize' isn't used."
---

# Article Summarizer

## Purpose
Condense any article or long-form text into clear, scannable key points without losing the core argument.

## Instructions
1. Read the full text before writing anything
2. Identify the main argument or conclusion
3. Extract 3–5 supporting points
4. Ignore examples and filler — keep only the substance

## Output Format
Return a short paragraph (2–3 sentences) summarizing the main argument, followed by 3–5 bullet points of key takeaways. No preamble. No "Here is your summary."

## Example

**Input:** [1,200-word article about remote work productivity]

**Output:**
Remote work increases individual productivity but reduces spontaneous collaboration. Teams that set explicit communication norms perform better than those that rely on informal office culture.

- Async-first teams report 23% fewer meetings with no drop in output quality
- Managers who check in daily see lower trust scores from reports
- Home office setup quality is the strongest predictor of remote worker satisfaction
- Companies with return-to-office mandates saw higher attrition in technical roles
```
