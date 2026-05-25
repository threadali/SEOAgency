# SaaS SEO Course
## Module 3 — SaaS Site Architecture

**Prerequisite:** Module 1 (Product Intelligence Document complete) and Module 2 (Keyword Architecture Spreadsheet complete)
**Module outcome:** A complete SaaS CMap — every structural page defined with URL, page type, funnel layer, crawl depth, and internal link flow — before any content brief is written.

---

## Why SaaS Architecture Fails Differently

SaaS sites have a structural problem that e-commerce and publisher sites do not.

A SaaS site serves three fundamentally different audiences at the same time: buyers who have never heard of the product, buyers who are evaluating it, and users who already pay for it. Each audience needs different content, different CTAs, and different page structures. Most SaaS sites try to serve all three from the same architectural layer and succeed at none of them.

The blog posts that educate buyers at Layer 1 compete for authority with the product landing pages that convert buyers at Layer 3. The help documentation that serves existing users bleeds topical authority off the main domain onto a subdomain that Google treats as a separate site. The pricing page has no SEO consideration because the product team owns it.

This module builds the architecture that separates these three audiences while keeping their authority signals unified under one domain.

---

## Lesson 3.1 — The SaaS Site Structure Problem

A standard SaaS site has five sections that work against each other when left unarchitected.

**The five sections and their conflict points:**

| Section | Owns | Conflicts with | Common mistake |
|---|---|---|---|
| Marketing / homepage | Brand messaging | Blog content | Competes for category head terms |
| Product / feature pages | Conversion | Blog guides | Blog guides outrank feature pages |
| Blog / resources | Traffic acquisition | Feature pages, landing pages | Layer 1 content cannibalises Layer 3 |
| Help / docs / knowledge base | User retention | Blog | Deployed on subdomain, loses authority |
| Pricing page | Transaction | Nothing ranks for branded pricing queries | No SEO consideration applied |

The architecture fix is not complicated. It requires assigning each section a clear macro context, a URL home, a funnel layer it owns, and a rule for how it links to the other sections. That is what this module builds.

---

**The app subdomain problem**

Most SaaS products live at app.product.com. The marketing site lives at product.com. The knowledge base lives at help.product.com or on a third-party tool like Zendesk. The blog may live at blog.product.com.

Google treats subdomains as semi-independent entities. Subdirectories share domain authority fully. A blog at blog.product.com starts SEO from scratch, separately from the main domain. A blog at product.com/blog shares all domain authority with every product and landing page on the main site.

The rule: SEO-critical content lives on the main domain under subdirectories. The product application (app.product.com) is the only justified subdomain for most SaaS companies.

---

**Common Mistake: Building the architecture for the product team, not the buyer**

Most SaaS site structures reflect the product team's mental model: home, product, pricing, about, blog. This structure does not map to how buyers move through a purchase journey. A buyer does not go from "home" to "product" to "pricing." They go from a problem-aware search to a category-aware comparison to a product-aware evaluation. The architecture must map to the buyer's path, not the internal org chart.

---

**Summary**

- Five SaaS sections conflict when left unarchitected. Assign each a clear macro context and funnel layer.
- SEO-critical content lives on subdirectories, not subdomains. The app subdomain is the only exception.
- Build the architecture for the buyer's path, not the product team's mental model.

*Next: URL architecture is the first structural decision. Get it wrong and every page that builds on top of it inherits the mistake.*

---

## Lesson 3.2 — URL Architecture for SaaS

SaaS sites have more URL types than standard content sites. Each page type needs a URL home that signals its function clearly to both Google and the buyer.

**The SaaS URL hierarchy**

```
domain.com/                          → Homepage
domain.com/features/                 → Feature overview
domain.com/features/[feature-name]/  → Individual feature page
domain.com/solutions/                → Solutions / use cases hub
domain.com/solutions/[use-case]/     → Individual use-case page
domain.com/solutions/[industry]/     → Industry-specific page
domain.com/integrations/             → Integrations hub
domain.com/integrations/[tool]/      → Individual integration page
domain.com/pricing/                  → Pricing page
domain.com/compare/                  → Comparison hub
domain.com/compare/[product]-vs-[competitor]/  → Vs page
domain.com/alternatives/             → Alternatives hub
domain.com/alternatives/[competitor]-alternatives/ → Alternative page
domain.com/blog/                     → Blog hub
domain.com/blog/[article-slug]/      → Individual blog post
domain.com/resources/                → Resource hub (optional)
domain.com/customers/                → Case studies hub
domain.com/customers/[customer-name]/ → Individual case study
domain.com/docs/ or /help/           → Knowledge base (keep on main domain)
domain.com/templates/                → Template library (if applicable)
domain.com/about/                    → About page
domain.com/pricing/                  → Pricing
```

**Five URL rules for SaaS**

1. **One macro context per URL.** A page at /solutions/crm-for-healthcare/ owns one context: CRM software for the healthcare industry. It does not also target "healthcare data management" or "healthcare workflow automation." Those get separate pages.

2. **No term duplication across URL levels.** /features/feature-overview/ has "feature" twice. Correct: /features/[feature-name]/.

3. **Functional areas get their own directories.** Comparison pages live under /compare/. Alternative pages live under /alternatives/. Integration pages live under /integrations/. Mixing these into /blog/ dilutes the macro context of each page type.

4. **Layer 3 pages (pricing, trial, demo) live at root level or one level deep.** /pricing/, /free-trial/, /demo/. Not /resources/getting-started/free-trial/. Conversion pages must be crawled frequently and discovered easily.

5. **The blog lives at /blog/, not at the root.** Content posts under the root domain (domain.com/post-slug/) create URL structure conflicts with product pages and are harder to architect correctly as the site grows.

---

**The /solutions/ vs /use-cases/ vs /for/ debate**

Three common patterns for vertical and use-case pages:

| Pattern | Example | Best for |
|---|---|---|
| /solutions/[use-case]/ | /solutions/project-management/ | Functional use cases (what the product does) |
| /for/[audience]/ | /for/marketing-teams/ | Audience-specific positioning (who it is for) |
| /industries/[industry]/ | /industries/healthcare/ | Vertical-specific pages (which sector) |

Use all three if the product has distinct functional use cases, distinct audience segments, AND distinct industry verticals. Do not use all three for the same page. A healthcare-focused project management page lives at either /solutions/project-management-for-healthcare/ or /industries/healthcare/project-management/ — not both.

---

**Common Mistake: Putting comparison and alternative pages in /blog/**

Comparison and alternative pages at /blog/best-competitor-alternatives/ inherit the blog's macro context. They rank as blog posts, not as product evaluation pages. They lose the structured page type signal that /alternatives/competitor-alternatives/ would send. Build a dedicated /compare/ and /alternatives/ directory.

---

**Summary**

- SaaS sites need more URL types than standard sites. Map every page type to its directory before building.
- Five URL rules: one macro context per URL, no term duplication, functional areas get dedicated directories, Layer 3 pages at root level, blog under /blog/.
- Comparison and alternative pages belong in dedicated directories, not in /blog/.

*Next: The landing page hierarchy determines which pages capture which buyer stages and how they connect.*

---

## Lesson 3.3 — The Landing Page Hierarchy

SaaS landing pages are not a single category. They divide into four types, each serving a different buyer intent and requiring a different content structure.

**The four landing page types**

**Type 1: Feature pages**

Feature pages sit at /features/[feature-name]/. They target Layer 2 and Layer 3 buyers who are evaluating whether the product does what they need it to do.

A feature page is not a feature description. It is a conversion page built around the job the feature accomplishes. The structure:

- H1: The outcome the feature delivers, not the feature name.
  Bad: "Time Tracking"
  Good: "Track billable hours automatically — no manual timers"
- Problem section: The pain without this feature.
- Feature description: What it does, with screenshots or demo.
- Use case section: Three to five specific workflows this feature enables.
- Social proof: One customer quote specific to this feature's value.
- CTA: Start trial or book demo.

**Type 2: Use-case and industry pages**

Use-case pages sit at /solutions/[use-case]/ or /for/[audience]/. They target buyers who search "[category] for [specific context]": "scheduling software for restaurants," "CRM for marketing agencies."

These pages rank for vertical-specific Layer 2 keywords and convert buyers who see their context reflected. The structure mirrors a feature page but substitutes the vertical or use case for the feature. The language adapts to the industry — a healthcare page uses healthcare terminology, a restaurant page uses hospitality language.

ClickUp structured their template pages by use case and then user type, building 5,000+ programmatic pages from this pattern. The key: each page uses the industry's own vocabulary, not the product team's category label.

**Type 3: Comparison and alternative pages**

Covered in depth in Module 2. They live at /compare/ and /alternatives/. They target Layer 2 buyers in active evaluation.

**Type 4: Location pages**

For SaaS with geographic relevance (local software, regional pricing, local compliance requirements), location pages sit at /[city]/ or /[country]/. These serve geographically qualified buyers and are particularly relevant for SaaS that sells to specific markets or has region-specific features.

---

**The pillar page problem in SaaS**

Standard content SEO uses pillar pages as broad topic hubs. In SaaS, the pillar page concept requires adjustment because a SaaS site already has structural hubs: /features/, /solutions/, /integrations/.

The blog pillar page model works for Layer 1 content. "The Ultimate Guide to Employee Scheduling" is a legitimate pillar at /blog/employee-scheduling-guide/. It covers the broad topic, links out to more specific articles, and internally links to the /features/ and /solutions/ pages.

Do not build pillar pages for Layer 3 content. Layer 3 pages are conversion pages. A "complete guide to pricing" page that also tries to convert buyers creates a macro context conflict. Keep Layer 1 pillars in /blog/. Keep Layer 3 conversion pages in their own directories.

---

**Common Mistake: Feature pages that describe instead of sell**

A feature page that lists what the feature does without addressing the buyer's job-to-be-done fails at both SEO and conversion. It does not match the search query (buyers search for outcomes, not feature descriptions) and it does not convert (buyers need to see the value, not the mechanic). Every feature page must answer "what job does this feature get me hired to do?" before describing how the feature works.

---

**Summary**

- Four SaaS landing page types: feature pages, use-case/industry pages, comparison/alternative pages, location pages. Each requires a different structure.
- Feature pages must lead with the outcome the feature delivers, not the feature name.
- Blog pillar pages serve Layer 1 content. Do not build pillar pages for Layer 3 conversion content.

*Next: Programmatic SEO is where SaaS architecture scales — but only for page types where it is structurally justified.*

---

## Lesson 3.4 — Programmatic SEO for SaaS

Programmatic SEO means creating large numbers of pages from a template plus variable data. For SaaS, it works for specific page types and destroys authority for others.

**When programmatic SEO works in SaaS**

Programmatic SEO works when three conditions hold simultaneously:

1. A genuine, unique dataset exists that makes each page distinct.
2. A repeatable intent pattern maps each page to a real user query.
3. Each page delivers genuine utility to the searcher, not just template text with swapped variables.

The Canva template library is the clearest example. Every design use case — "Instagram post templates," "presentation templates," "resume templates" — gets a dedicated page. Each page embeds real, usable templates the user can open and edit immediately. The data is the product itself. The page earns its ranking by delivering what the user came for before they even click through to the editor.

**Five programmatic page types justified for SaaS**

| Page type | Template pattern | Data source | Example |
|---|---|---|---|
| Integration pages | "[Product] + [Tool] integration" | Product's own integration data | /integrations/slack/ |
| Comparison pages | "[Product] vs [Competitor]" | Competitor feature/pricing data | /compare/product-vs-competitor/ |
| Alternative pages | "Best [Competitor] alternatives" | Category data + competitor weaknesses | /alternatives/competitor-alternatives/ |
| Template library | "[Use case] template" | Product's own template data | /templates/project-plan-template/ |
| Use-case/industry pages | "[Category] for [Industry]" | Industry-specific language and workflows | /solutions/crm-for-healthcare/ |

**What makes each template valid versus thin:**

A valid programmatic page has unique content per variable. The integration page for Slack includes Slack-specific workflows, Slack-specific setup steps, and Slack-specific use cases. The integration page for HubSpot includes HubSpot-specific workflows, HubSpot-specific setup steps, and HubSpot-specific use cases. The template is the same. The content is not.

A thin programmatic page swaps the variable name and leaves everything else identical. "Connect Product to Slack. Connect Product to HubSpot. Connect Product to Salesforce." — three sentences, three pages, three 404s waiting to happen.

---

**The Google Scaled Content Abuse line**

Google's March 2024 Scaled Content Abuse policy applies directly to programmatic SEO. The test: does this page exist to serve a genuine user need, or does it exist to occupy a search position?

Pages that pass: integration pages with real workflow examples, comparison pages with real feature and pricing data, template pages with actual templates.

Pages that fail: location pages with "[City] + [Category]" and no city-specific content, use-case pages that swap the industry name but keep identical body copy, comparison pages that repeat the same generic competitor weaknesses for every competitor.

The minimum viable programmatic page contains: a distinct primary keyword, at least three pieces of content that are unique to the variable being swapped, and a CTA that is relevant to the specific use case.

---

**The ClickUp model: use-case by user-type matrix**

ClickUp built 5,000+ programmatic pages by structuring templates by use case and then by user type. The pattern: /templates/[use-case]/[user-type]/. A project plan template page for project managers. A project plan template page for product teams. A project plan template page for construction companies.

The variable is the user type. The template format is consistent. But the content differs because project managers, product teams, and construction companies have different workflows, different terminology, and different priorities when choosing a template.

This two-dimensional matrix (use case × user type) multiplies the number of valid, distinct pages a single template type can generate. It is not thin because each page genuinely serves a different buyer with a different context.

---

**Common Mistake: Building programmatic pages before the template is validated**

A validated template has been proven to rank and convert for at least three to five manually built instances before being automated to hundreds. Teams that launch 500 pages on an unvalidated template — then discover the template does not rank — have created 500 pages to audit, fix, or remove. Build five manually. Rank them. Validate the template. Then scale.

---

**Summary**

- Programmatic SEO works for five SaaS page types: integrations, comparisons, alternatives, template libraries, and use-case/industry pages.
- The Google Scaled Content Abuse test: does each page genuinely serve a distinct user need with genuinely unique content? Generic variable swaps fail this test.
- Validate the template manually (three to five instances ranking) before scaling to hundreds.

*Next: Integration pages are a programmatic category worth dedicated treatment because they produce some of the highest-converting traffic in SaaS.*

---

## Lesson 3.5 — Integration Pages

Integration pages deserve a separate lesson because they are the most commonly under-built high-value page type in SaaS.

Most SaaS companies build one page per integration partner and stop. That one page says "We integrate with Salesforce." It does not rank. It does not convert. It is a disclosure, not an SEO asset.

**The three-tier integration page structure**

**Tier 1: Integration hub** — /integrations/

Lists all integrations by category. Targets "[product] integrations" and "tools that work with [product]." Links to all individual integration pages.

**Tier 2: Individual integration page** — /integrations/[tool]/

Targets "[product] + [tool] integration" and "how to connect [product] to [tool]." This page requires:

1. What the integration does (one sentence, in buyer language).
2. Three to five specific workflows the integration enables (named and detailed).
3. Step-by-step setup instructions (actual steps, not "go to settings and connect").
4. What data passes between the two systems.
5. Which plan includes this integration.
6. CTA: Start the integration or start a trial.

Zapier's integration pages include specific workflow examples, step-by-step setup instructions, popular automation templates, and user testimonials for that specific integration. This depth ensures each page provides genuine value.

**Tier 3: Workflow pages** — /integrations/[tool]/[workflow]/

Optional. Only build these when a specific workflow has its own search demand: "automate invoicing with [product] and QuickBooks," "sync [product] contacts with Salesforce." These target ultra-specific long-tail queries with high purchase intent.

---

**Integration page SEO considerations**

Integration pages target multiple intent types simultaneously:

- The buyer researching whether the product fits their stack (Layer 2, commercial intent).
- The existing user setting up the integration (Layer 4, navigational intent).
- The prospect validating the integration exists before signing up (Layer 3, near-transactional).

The page must serve all three. The structure above does this: the workflow examples serve the Layer 2 buyer, the setup instructions serve the Layer 4 user, and the plan information and CTA serve the Layer 3 prospect.

---

**Common Mistake: Building integration pages on a third-party marketplace**

Many SaaS companies build their integration directory on a third-party platform (Zapier, Make, or their own app marketplace) instead of on the main domain. All the search authority from integration queries goes to the third party. Build integration pages on the main domain. Link to the third-party marketplace from the page, but keep the primary content on your own domain.

---

**Summary**

- Three-tier integration structure: hub, individual page, workflow page. Only build Tier 3 when specific workflows have their own search demand.
- Each integration page must include workflows, setup steps, data mapping, and a plan-specific CTA. "We integrate with X" is not an integration page.
- Build integration pages on the main domain. Third-party marketplaces capture the authority if you rely on them for the primary content.

*Next: Internal linking is the system that connects all these page types and moves buyers from Layer 1 to Layer 3.*

---

## Lesson 3.6 — Internal Linking Strategy for SaaS

SaaS internal linking has one strategic goal: move buyers from Layer 1 content (high-volume, low-conversion) to Layer 3 pages (low-volume, high-conversion) without forcing them.

The internal link is the conversion mechanism inside the article. The blog post ranks for the Layer 1 query. The internal link delivers the buyer to a Layer 2 or Layer 3 page when they are ready to act.

**The mandatory link rule**

Every Layer 1 blog post must contain at least one contextual internal link to a Layer 2 or Layer 3 page. Not a sidebar link. Not a footer link. A contextual link inside the body copy, in a section where the buyer's attention is already on a relevant topic.

An article on "how to manage employee scheduling in Excel" contextually links to:
- Layer 2: "best employee scheduling software" comparison page.
- Layer 3: The trial page with anchor text "start a free trial."

The link appears where the article solves the problem the buyer came for and naturally extends toward a better solution.

---

**Link direction rules by page type**

| Source page | Links to | Anchor text type |
|---|---|---|
| Layer 1 blog post | Layer 2 comparison / use case + Layer 3 trial / feature page | Problem-solution phrase ("employee scheduling software") |
| Layer 2 comparison page | Layer 3 trial / demo / pricing | CTA phrase ("start free trial", "see pricing") |
| Layer 3 feature page | Other feature pages + Layer 2 use-case pages | Feature outcome phrase |
| Integration page | Feature page + trial page + related integrations | Integration outcome phrase |
| Comparison page | Alternative page + trial page | Evaluation phrase |

---

**Crawl depth: the three-click rule**

Critical pages — pricing, trial, feature pages, comparison pages — must be reachable within three clicks from the homepage. Pages buried more than four clicks deep are crawled infrequently and accumulate authority slowly.

Navigation placement is the highest-value crawl depth lever. Every page in the main navigation header is at crawl depth two. Feature pages, solutions, pricing, and the blog hub belong in the main navigation. Comparison and alternative pages belong in a secondary navigation or the footer at minimum.

SaaS platforms should prioritise keeping essential content within three clicks, ensuring accessibility across site structures.

---

**The blog-to-product internal link audit**

Most SaaS blogs have strong Layer 1 content with no internal links to product pages. The fix is systematic:

1. Pull all blog posts with the most organic traffic from Search Console.
2. For each post, identify the Layer 2 or Layer 3 page it is most relevant to.
3. Add a contextual internal link within the first 500 words where the buyer's attention is highest.
4. Add a second contextual link in the section where the product is the natural solution.
5. Add a CTA at the end with a direct link to the trial or feature page.

This audit on an existing blog with 50 posts typically produces measurable trial signup increases within 60-90 days without publishing a single new article.

---

**Common Mistake: Using sidebar and widget links as the only path to product pages**

Sidebar links and "related posts" widgets are low-authority navigation elements. Google treats them as secondary navigation, not editorial endorsements. Contextual links within the body text carry more weight and produce more click-throughs because they are placed at the point of highest reader attention. Never rely on sidebar or widget links as the primary internal link path from blog to product.

---

**Summary**

- Every Layer 1 blog post needs at least one contextual internal link to a Layer 2 or Layer 3 page. This is the conversion mechanism inside the article.
- Critical pages must be within three clicks of the homepage. Navigation placement is the most powerful crawl depth lever.
- The blog-to-product internal link audit produces signup increases from existing content without new articles.

*Next: Crawl path optimisation — making sure Google discovers your highest-converting pages before your lowest-converting ones.*

---

## Lesson 3.7 — Crawl Path Optimisation

Crawl path in SaaS requires specific attention because SaaS sites accumulate page types quickly. The product app, the marketing site, the blog, the help centre, and the legal pages are all crawled by the same Googlebot with the same crawl budget.

Googlebot must spend its crawl budget on the pages that matter most. Left unconfigured, it will crawl the legal pages, the pagination from the blog archive, and the duplicate product pages before it finds the integration pages and comparison pages.

**Crawl depth by priority tier**

| Priority | Pages | Correct depth | Method |
|---|---|---|---|
| Must crawl frequently | Pricing, trial, feature pages, comparison pages | 2-3 clicks | Main navigation + homepage links |
| Crawl regularly | Blog posts, integration pages, use-case pages | 3-4 clicks | Category pages + blog hub |
| Crawl periodically | Historical blog content, edge-case use-case pages | 4-5 clicks | Sitemap + category pagination |
| Minimal crawl | Help articles, terms pages, legal | Sitemap only, low priority | XML sitemap with lastmod |

**Five crawl configuration decisions**

1. **Block the app subdomain in robots.txt.** app.product.com should be blocked from crawling. It is not SEO content. Every crawl budget wasted on the app interface is a crawl budget not spent on the /compare/ pages.

2. **Block paginated blog archive pages.** /blog/page/2/ through /blog/page/N/ consume crawl budget without adding rankable content. Use rel=canonical or noindex on paginated pages beyond the first.

3. **Use a clear XML sitemap.** Include only canonical, indexable pages. Exclude paginated pages, app pages, admin pages, and duplicate content. Submit the sitemap to Search Console.

4. **Set lastmod dates accurately in the sitemap.** When a page is updated — pricing changes, new feature added, comparison page refreshed — update the lastmod date. This signals to Googlebot that the page has new content worth recrawling.

5. **Ensure the /integrations/, /compare/, and /alternatives/ directories are in the sitemap.** These are the highest-converting page types in the SaaS architecture. If they are missing from the sitemap, their indexing depends entirely on link discovery.

---

**The product app vs marketing site structure**

The product application at app.product.com must stay separate from the marketing site at product.com. The application requires authentication. Googlebot cannot crawl authenticated pages. If the app and the marketing site are on the same domain without proper segmentation, Googlebot wastes crawl budget following links into authenticated pages it cannot access.

Canonical configuration: every page that the app and marketing site share (pricing, signup, login) must have a clear canonical pointing to the marketing site version. The app's signup page at app.product.com/signup should canonicalise to product.com/pricing/ or product.com/free-trial/.

---

**Common Mistake: Submitting a sitemap that includes every URL on the site**

A sitemap that includes 10,000 URLs for a site with 200 quality pages trains Googlebot to expect 10,000 crawlable pages — and wastes crawl budget on the 9,800 that do not need frequent recrawling. A clean sitemap includes only canonical, indexable, content-quality pages. Every other page is either blocked in robots.txt or managed with noindex.

---

**Summary**

- Four crawl priority tiers: must crawl frequently, crawl regularly, crawl periodically, minimal crawl. Configure navigation and robots.txt accordingly.
- Five crawl decisions: block the app, block paginated archives, maintain a clean XML sitemap, set accurate lastmod dates, and include /integrations/, /compare/, /alternatives/ in the sitemap.
- A sitemap with 10,000 URLs for a 200-page quality site wastes crawl budget. Include only canonical, indexable, content-quality pages.

---

## Module 3 Summary

Three principles govern every SaaS architecture decision:

- **Authority stays on the main domain.** Blog, help docs, resources, integrations, comparisons — all on the main domain under subdirectories. The only justified subdomain is the product app itself.
- **Every page type has one home.** Integration pages live under /integrations/. Comparison pages live under /compare/. Alternative pages live under /alternatives/. Blog posts live under /blog/. Mixing these destroys the macro context signals that make each type rank well.
- **Internal links are the conversion mechanism.** Every Layer 1 article links contextually to at least one Layer 2 or Layer 3 page. No blog post earns its production cost if it does not move buyers toward a product page.

---

## Module 3 Deliverable: SaaS CMap

Complete this before building the Topical Map or writing any briefs.

---

```
SAAS CMAP
==========
Client:
Domain:
Date completed:
Reviewed by:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 1 — DOMAIN STRUCTURE DECISIONS

App subdomain: app.[domain].com
  [ ] Confirmed blocked in robots.txt
  [ ] Canonical tags on shared pages (signup, pricing) pointing to main domain

Knowledge base / help:
  [ ] On main domain (/docs/ or /help/) — recommended
  [ ] On subdomain (help.[domain].com) — document the authority loss risk

Blog:
  [ ] On main domain (/blog/) — recommended
  [ ] On subdomain (blog.[domain].com) — document the authority loss risk

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 2 — URL DIRECTORY STRUCTURE

Complete the following for each directory:

| Directory | Purpose | Page count | Funnel layer | Priority |
|---|---|---|---|---|
| /features/ | Feature conversion | | Layer 2-3 | High |
| /solutions/ or /for/ | Use-case / audience | | Layer 2-3 | High |
| /industries/ | Vertical pages | | Layer 2-3 | Medium |
| /integrations/ | Integration pages | | Layer 2-4 | High |
| /compare/ | Vs pages | | Layer 2-3 | High |
| /alternatives/ | Alternative pages | | Layer 2-3 | High |
| /pricing/ | Pricing page | | Layer 3 | High |
| /free-trial/ or /demo/ | Trial / demo | | Layer 3 | High |
| /blog/ | Content / Layer 1 | | Layer 1 | High |
| /customers/ | Case studies | | Layer 2-3 | Medium |
| /templates/ | Template library | | Layer 1-3 | Medium |
| /docs/ or /help/ | Knowledge base | | Layer 4 | Medium |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3 — PAGE INVENTORY

(One row per page. Complete for all Tier 1 pages before brief writing begins.)

Column A: Page ID
Column B: Page type [Feature / Use-case / Industry / Integration / Comparison /
                      Alternative / Pricing / Trial / Blog pillar / Case study /
                      Template / Help / Structural]
Column C: Page name / topic
Column D: Target URL (full path)
Column E: H1 (final — not working title)
Column F: Meta description (150-160 chars)
Column G: Primary target keyword
Column H: Funnel layer [1 / 2 / 3 / 4]
Column I: Programmatic? [Y / N]
          If Y: template validated? [Y / N]
Column J: Parent page (which URL links to this page from one level up)
Column K: Crawl depth (clicks from homepage)
Column L: Navigation placement [Main nav / Secondary / Footer / None]
Column M: Priority [High / Medium / Low]
Column N: Status [Planned / In progress / Live]
Column O: Notes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 4 — INTERNAL LINK FLOW MAP

For each Layer 1 blog pillar, document the mandatory internal links:

Page: [Blog post title + URL]
  Mandatory link 1:
    Target page: [URL]
    Anchor text: [approved anchor]
    Placement: [which section — first 500 words / solution section / CTA end]
  Mandatory link 2:
    Target page: [URL]
    Anchor text: [approved anchor]
    Placement: [section]

[Repeat for all Layer 1 blog posts]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 5 — CRAWL CONFIGURATION

[ ] App subdomain blocked in robots.txt
[ ] Paginated archive pages blocked or noindexed beyond page 1
[ ] XML sitemap includes only canonical, indexable content-quality pages
[ ] XML sitemap submitted to Search Console
[ ] /integrations/, /compare/, /alternatives/ directories in sitemap
[ ] lastmod dates set accurately in sitemap
[ ] All Layer 3 pages (pricing, trial, feature) within 3 clicks of homepage
[ ] Navigation includes links to: Feature hub, Solutions hub, Pricing, Blog hub

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 6 — PROGRAMMATIC PAGE VALIDATION

For each programmatic page type planned:

Page type: [e.g. Integration pages]
  Template URL pattern: /integrations/[tool]/
  Validation pages built manually: [list 3-5 URLs]
  Ranking status of validation pages: [not indexed / indexed / ranking / converting]
  Template validated: [ ] Yes  [ ] No
  Scale approved: [ ] Yes  [ ] No (do not scale until Yes on both above)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SIGN-OFF

Architecture reviewed by: _________________ Date: _________
Topical Map build begins: [ ] Approved
```

---

*Module 4 covers TOFU Content: building Layer 1 content that attracts problem-aware buyers and moves them toward the product — without the content becoming general information with a SaaS logo on it.*
