---
name: article-visual-grammar
description: Plan, prompt, generate, and repair expressive article illustrations for Chinese or English essays, blogs, newsletters, social posts, product writing, technical writing, business analysis, culture commentary, personal essays, and educational explainers. Use when the user asks for article illustration strategy, shot lists, visual metaphors, diagram-like editorial illustrations, consistent illustration style, clearer image prompts, generated article figures, or edits that make an image more beautiful, readable, and idea-dense.
---

# Article Visual Grammar

## Core

Create article illustrations by separating **meaning structure**, **diagram form**, **visual tokens**, **connection grammar**, and **style tokens**.

Do not lock every article into one IP, mascot, scene, or domain. A security article, founder essay, product teardown, education note, and culture commentary may share the same visual grammar while using different metaphor worlds.

Default output: 16:9 horizontal article illustration, strong focal structure, readable connection grammar, controlled typography zones, and no mascot-first hand-drawn look. The default style is not "cool AI art"; it is a clear visual explanation that a reader can understand in three seconds.

The core promise: extract the article first, then decide what diagram form to use, what visual tokens regulate it, what to draw, where text appears, what the text says, how lines/relations/charts/spatial depth create hierarchy, which style system makes the idea easiest to read, and how the final prompt avoids generic AI/PPT output.

For public galleries, README examples, or demo images, do not let the skill look like an engineering workflow generator. Include non-engineering subjects where possible: culture, history, art, education, food, place, memory, psychology, or personal essays. The same clarity contract applies, but the metaphor world must come from the article domain instead of gates, nodes, dashboards, or software props.

World-class default path: do not assume the image model will infer taste from abstract words. Translate beauty into visible art direction: grid, margins, material family, semantic palette, line hierarchy, label containers, typography mode, negative space, focal surprise, and anti-default-AI constraints.

Use the user's language for strategy output, labels, and delivery notes unless they request otherwise. When the source is an article, bind each shot to a concrete section, paragraph, heading, or quote fragment so the image has an editorial reason to exist.

## Read References As Needed

- `references/visual-structures.md`: choose the right conceptual structure.
- `references/auto-shot-planner.md`: decide where images are needed when the user gives a full article.
- `references/form-selection-engine.md`: decide whether to skip, simplify, use a standard diagram, use spatial form, or build a package system.
- `references/diagram-coverage-matrix.md`: prevent blind spots across work, life, systems, strategy, data, emotion, and spatial relations.
- `references/diagram-form-catalog.md`: choose the concrete diagram, chart, map, pyramid, matrix, spatial, storyboard, or infographic form.
- `references/visual-token-system.md`: define semantic colors, line weights, line patterns, shapes, labels, emphasis, and spatial tokens.
- `references/typography-token-system.md`: define Chinese/English font feeling, label modes, type scale, and overlay-ready text containers.
- `references/human-presence-and-charm-system.md`: choose whether to use no people, human traces, role tokens, abstract figures, or storybook actors, and regulate cuteness.
- `references/action-character-system.md`: use Paper Operator action characters only when they physically clarify the article idea, with tools adapted to the article domain.
- `references/visual-harness-and-style-atlas.md`: expand supported visual styles and art/design lineages without copying artists.
- `references/figure-spec-schema.md`: turn each planned image into a checkable spec before prompting.
- `references/image-quality-harness.md`: compile publish-grade art direction, anti-default-AI constraints, smoke-test criteria, and repair loops.
- `references/composition-stability-presets.md`: choose one stable composition preset to improve beauty, first-glance clarity, and generation repeatability.
- `references/aesthetic-quality-bar.md`: enforce publish-grade beauty, simplicity, focal surprise, and repair decisions.
- `references/article-analysis.md`: extract what deserves illustration from an article.
- `references/clarity-contract.md`: mandatory output contract for non-trivial article illustration work.
- `references/symbol-system.md`: PrismGrid, the original non-character visual symbol system and reusable visual identity rules.
- `references/connection-grammar.md`: connect elements so the idea is legible.
- `references/continuous-carrier-grammar.md`: build hierarchy with one continuous visual spine and embedded information forms.
- `references/style-token-bank.md`: choose surface style tokens and metaphor worlds.
- `references/comic-picturebook-forms.md`: choose simple comic/picture-book forms that stay clear and non-plagiaristic.
- `references/text-hierarchy.md`: decide where text appears, how much text, and what font feeling.
- `references/research-derived-tokens.md`: background abstractions from mature visual systems.
- `references/prompt-builder.md`: assemble robust image prompts.
- `references/beauty-expression-rules.md`: make images clearer and more attractive.
- `references/clarity-rules.md`: prevent over-metaphorical AI clutter.
- `references/qa-checklist.md`: evaluate generated images and decide edits/regeneration.

## Workflow

### 1. Extract The Article Jobs

Read the article, draft, outline, screenshot, or concept. Identify:

- main thesis
- cognitive turn
- tension or conflict
- process or mechanism
- before/after state
- hidden cost, risk, or failure mode
- decision point
- emotional temperature

Only illustrate moments that help a reader understand, remember, or feel the article. Do not decorate every section.

For non-trivial articles, use `references/article-analysis.md` before building the shot list.

### 2. Plan The Article Package

If the user gives a full article and does not specify images, use `auto-shot-planner.md`.

First segment the article, score visual potential, decide which sections to skip, then choose a compact package of 3-6 images by default. A package should vary scale and role: thesis anchor, mechanism, tension or failure, evidence or comparison, human consequence, or summary map. Do not illustrate every section.

For every planned image, name its package role and source anchor before choosing style.

### 3. Lock The Clarity Contract

For non-trivial article packages, output or internally complete the contract in `references/clarity-contract.md` before prompting an image model.

The contract must decide:

- article structure summary
- visualizable paragraph-to-shot mapping with concrete section, paragraph, heading, or quote anchors
- package plan: selected images, skipped sections, package rhythm, and intentional variety
- form selection: reader misunderstanding prevented, simplest sufficient rung, chosen form, why not simpler, why not more complex
- output family: article body figure, diagram/infographic, editorial/social, or technical/product
- reader path
- text zones, typography mode, font feeling, and overlay plan
- human presence level and charm level: H0-H5 and C0-C5
- action character decision: none or one Paper Operator; operator family; article domain; action verb; what breaks if removed
- line / relation grammar
- chart or diagram form, including spatial mode if useful
- visual token plan: color roles, line roles, line patterns, shape roles, label containers, emphasis, and spatial tokens
- hierarchy anchors from L0 to L3
- style direction and anti-copy boundaries
- visual harness: output family, form family, spatial mode, style lineage, abstraction, material, line behavior, color system, composition engine, human presence, typography mode, why the lineage helps comprehension, and anti-copy boundary
- image quality harness: material family, grid/margins, palette discipline, typography/overlay choice, negative space contract, focal hierarchy, texture/depth rule, and anti-default-AI constraints
- composition stability preset: one locked preset, fixed layout, max anchors, max labels, focal module, reader path, quiet zones, and forbidden drift
- symbol system: primitive geometry, semantic shapes, carrier, label containers, color roles, micro chart form, and forbidden marks
- package symbol legend: shared shape meanings, color meanings, label containers, and recurring marks across the article package
- beauty gate: score target, what was removed to keep it simple, focal surprise, remaining risk
- figure spec: a compact or full spec from `figure-spec-schema.md`

If the user asks for strategy, show the contract in compact form. If the user asks to generate directly, still use the contract to build each prompt.

### 4. Select Complexity Before Form

Use `form-selection-engine.md` before choosing a form.

For each candidate shot, decide the simplest sufficient rung:

- no image
- single object metaphor
- two-state contrast
- simple diagram
- spatial model
- package system

Prefer the simpler rung when it preserves the article's point. Complexity must earn its place by improving accuracy, comprehension, memory, or emotional truth.

### 5. Pick A Diagram Form Before Style

For each candidate shot, choose one conceptual structure from `visual-structures.md`, then choose one concrete form from `diagram-form-catalog.md` before choosing objects, characters, or surface style.

Use the form catalog for any request involving flowcharts, diagrams, charts, frameworks, pyramids, matrices, work/life systems, spatial relations, hierarchy, or "make it beautiful". Because generated images can render complex scenes, you may choose flat, isometric, cutaway, room, terrain, tabletop, or orbit spatial modes.

Structure examples:

- contrast
- pipeline
- stack
- boundary
- map
- small multiples
- feedback loop
- exploded view
- tradeoff scale

Diagram form examples:

- flow / process / swimlane
- pyramid / layered hierarchy
- matrix / quadrant
- map / territory / route
- timeline / calendar
- loop / flywheel
- funnel / filter / bottleneck
- anatomy / cutaway
- ecosystem / network
- comparison / small multiples
- evidence / table / scorecard
- proportion / part-to-whole
- spectrum / ladder / scale
- tree / nested hierarchy
- set / overlap / Venn
- flow quantity / Sankey / alluvial
- service blueprint / journey layers
- causal / systems model
- value chain / strategic position
- storyboard / comic diagram
- canvas / framework board
- spatial stack / 3D hierarchy
- room / stage / workspace diagram
- terrain / landscape model
- orbit / depth network
- object board / physical model

After choosing a form, run `diagram-coverage-matrix.md` as a backstop. This does not mean adding more forms. It means checking whether the article is actually about sequence, transformation, hierarchy, choice, territory, system, evidence, quantity, overlap, human situation, work/life system, hidden mechanism, constraint, accumulation, or taxonomy.

If the structure or form is unclear, do not generate yet; rewrite the shot idea. If the image needs two unrelated forms, split it into two images.

### 6. Choose A Metaphor World

Choose a metaphor world that fits the article's subject and mood, not a fixed default:

- grid / editorial layout
- paper collage / cutout objects
- modular blocks / tiles
- chart-object hybrid
- instruction manual / technical plate
- archive / index cards
- map / route / territory
- calendar / timeline
- lab / samples
- market / exchange
- city / transit
- garden / growth
- weather / pressure
- theater / roles
- machine / assembly

Use the chosen world consistently within one image, and usually across an article package.

Before surface style, define visual tokens from `visual-token-system.md`:

- color roles: Ink, Paper, Quiet, Passage, Evidence, Risk, Growth, Human, Focus
- line roles: Hairline, Standard, Carrier, Boundary, Emphasis
- line patterns: solid, dashed, dotted, double, wavy, broken, glow
- shape roles: rounded rectangle, dot, capsule, arc, wedge, bracket, layer slab, contour, lens, thread
- label containers: strip label, route tag, state stamp, callout flag, side note, panel caption, floor/zone label, edge tab
- spatial tokens if used: foreground, middle ground, background, vertical height, depth distance, occlusion, cutaway edge, shadow, floor zone, contour density

Colors and lines must mean something. Same color and same line pattern must carry the same semantic role inside one image and usually across an article package.

Choose a style direction that is not Xiaohei-like. Good defaults:

- PrismGrid / Anchor Glyph System
- structured editorial grid-collage
- clear-line picture-book explainer
- instruction-manual diagram
- field atlas / zukan card
- data-object hybrid
- diagram comic

When the user asks for a broader harness or famous artist-inspired visuality, use `visual-harness-and-style-atlas.md`. First choose the supported output family: article body figure, diagram/infographic, editorial/social, or technical/product. Then choose the specific diagram form and only then choose a style lineage as a set of visual parameters, not as direct imitation. Good lineages include Bauhaus constructive workshop, De Stijl grid, constructivist poster logic, suprematist geometry, cubist faceting, Matisse cutout logic, ukiyo-e-informed composition, Kandinsky musical geometry, Klee symbolic micro-world, Albers color interaction, Calder mobile balance, Swiss typographic clarity, Art Nouveau organic line, Art Deco streamlined geometry, and risograph editorial print.

Do not prompt "in the style of" a living artist or contemporary copyrighted illustrator. For historical artists, extract composition, line, color, material, and spatial principles instead of copying signature works.

### 7. Lock Typography And Figure Specs

Before building prompts, choose the typography mode from `typography-token-system.md`:

- `draft labels` for exploration
- `publish overlay` for public Chinese, exact text, thumbnails, covers, presentations, or paid work

Modern image models can render concise Chinese labels well. For publish-ready Chinese, choose between `model-rendered labels` and `publish overlay` based on accuracy needs, label density, and downstream editability. Use model-rendered labels when the image needs integrated signs, stamps, packaging, UI-like panels, or natural in-scene Chinese text. Use blank label containers and later overlay only when exact text is mission-critical, text is dense, legal/financial/public-facing, or the user will need editable typography.

Then write a compact or full spec from `figure-spec-schema.md`. Do not generate a non-trivial image until the spec includes source anchor, reader takeaway, misunderstanding prevented, selected form, visual tokens, typography mode, accuracy risk, and must-not-show constraints.

### 8. Compile The Image Quality Harness

Before the final image prompt, use `image-quality-harness.md`.
For generated images, also use `composition-stability-presets.md`. Pick exactly one preset before writing the final prompt.

Translate the abstract style decision into concrete visible rules:

- material family: editorial paper model, field atlas plate, soft diagram infographic, spatial editorial model, or clear-line picturebook explainer
- composition: 6-column or 8-column invisible grid, generous margins, one large focal module, clear gutters, and quiet zones
- focal hierarchy: largest object, strongest carrier, isolated module, one accent, cutaway reveal, or guide-object light
- palette: semantic roles only, usually 3-5 visible colors
- typography: model-rendered concise labels or blank overlay containers
- composition preset: Hero Object With State Marks, Carrier Through Gate, Two-State Contrast, Shelf Matrix, Field Atlas Plate, Cutaway Mechanism, Route Map With One Obstacle, Spatial Stack, or Three-Beat Storyboard
- stability limits: max anchors, max labels, focal module, seven-word reader path, quiet zones, and forbidden drift
- negative space: what stays empty and what complexity was removed
- anti-default-AI: no PPT, no stock icons, no robot/brain/rocket/lightbulb by habit, no mascot identity, no fake dense text, no decorative arrows

Do not generate from a prompt that only says "beautiful", "premium", "modern", "clean", or "world-class". If the prompt does not contain concrete art direction, repair the prompt first.

### 9. Build The Shot List

If the user asks for planning, output 3-6 shots by default. For each shot include:

- placement
- package role
- source anchor: section, paragraph, heading, or quote fragment
- reader takeaway
- selection: reader misunderstanding prevented, simplest sufficient rung, why not simpler, why not more complex, accuracy risk, complexity budget
- structure
- diagram form: family, specific form, layout skeleton, spatial mode, rejected alternatives, beauty move, optional guide object
- coverage check: meaning family and why the form covers it
- visual harness: output family, form family, spatial mode, style lineage, abstraction level, material, line behavior, color system, composition engine, why it helps comprehension, and anti-copy boundary
- image quality harness: material family, focal hierarchy, grid/margins, palette, typography mode, negative space, anti-default-AI constraints
- composition stability preset: preset, fixed layout, max anchors, max labels, focal module, reader path, quiet zones, forbidden drift
- action character: none or one Paper Operator; operator family, domain, action verb, object acted on, relation clarified, what breaks if removed
- human presence and charm: H0-H5 level, C0-C5 level, and why a person/trace/role token is or is not needed
- metaphor world
- visual tokens: color roles, line roles, line patterns, shape roles, label containers, emphasis rule, spatial tokens if any
- key objects
- connection grammar
- line / relation plan
- chart or diagram form
- hierarchy anchors
- symbol system choices: PrismGrid primitive geometry, anchor glyphs, carrier glyph, label containers, color roles, micro chart form, forbidden items
- text zones and font feeling
- typography mode: draft labels or publish overlay, with font family feeling
- label words
- beauty gate: target score, focal surprise, what is intentionally removed, remaining risk
- default-generation smoke notes when generating directly: what must be visible on first glance, what would trigger regeneration, and how to repair if the image looks generic
- compact figure spec
- generation prompt notes

Short posts may need 1-2 shots. Long essays rarely need more than 8 unless the user asks for a visual essay.

### 10. Generate Or Edit

When generating, use `references/prompt-builder.md`. Each prompt must specify:

- article context and target idea
- form selection: simplest sufficient rung, why not simpler, why not more complex
- chosen structure
- diagram form catalog choice: family, specific form, layout skeleton, spatial mode, rejected alternatives, beauty move
- visual token system: semantic colors, line weights, line patterns, shape roles, label containers, emphasis rule, spatial tokens
- typography token system: draft vs overlay, font feeling, L1/L2/L3 labels, and exact label zones
- human presence and charm system: H0-H5, C0-C5, allowed human form, and what it clarifies
- action character system: if used, one Paper Operator that physically operates a domain-specific object such as a carrier, lens, gate, frame, palette, light card, archive folder, note, boundary screen, weather card, layer, map, or evidence object
- visual harness and style atlas: output family, form family, spatial mode, style lineage, abstraction level, material, line behavior, color system, composition engine, why it helps comprehension, and anti-copy boundary
- image quality harness: quality target, material family, grid/margins, focal hierarchy, palette discipline, typography/overlay plan, texture/depth rule, negative space contract, and anti-default-AI list
- composition stability preset: one preset, fixed layout, max anchors, max labels, focal module, reader path, quiet zones, forbidden drift
- figure spec: the checkable compact spec for this image
- metaphor world
- 5-9 visual tokens
- connection grammar
- continuous carrier: the main line/ribbon/path that creates hierarchy
- line grammar: connector type, weight, direction, and label attachment
- chart form: none / mini table / small multiples / micro chart / cutaway / map / scale / pyramid / matrix / timeline / loop / funnel / ecosystem / scorecard / part-to-whole / tree / Venn / Sankey / service blueprint / causal model / value chain / storyboard / canvas / spatial stack / room / terrain / orbit / object board
- symbol fields: primitive geometry, symbol classes, semantic shape map, carrier glyph, label containers, color roles, layout skeleton, micro chart form, forbidden items
- hierarchy layers: L0 carrier, L1 anchor nodes, L2 embedded information forms, L3 text marks
- focal action
- text plan: label hierarchy, placement, and font feeling
- beauty gate: target score, whitespace plan, focal surprise, simplification decision
- smoke target: the generated image must read in three seconds, avoid generic AI output, avoid PPT/courseware/stock-icon habits, and score 4+ on the beauty gate
- style tokens
- negative constraints

When editing, preserve what works and change only the failure: wrong text, weak focal action, messy composition, too much PPT, no carrier line, poor hierarchy, poor metaphor, or ugly spacing.

For publish-ready Chinese images, do not over-constrain text by habit. Let the model render concise Chinese when it improves integration and the prompt can specify exact labels clearly. Prefer blank label spaces and overlay only when exact wording, dense copy, or editability matters.

After substantial revisions to this skill, run a default-generation smoke when feasible: give the skill a real article or concept, let it choose the figure spec, generate one image without extra manual rescue art direction, score it with `image-quality-harness.md` and `qa-checklist.md`, then patch the skill if it falls back to generic AI output.

## Originality Boundary

Do not imitate Ian Xiaohei Illustrations. Do not use black blob mascots, white-dot eyes, tiny thin legs, casual whiteboard doodle identity, or a recurring little worker as the main style anchor. Learn from the product method, not the IP: simple workflow, strong examples, one idea per image, short labels, clear QA, and a memorable visual grammar.

Characters are not forbidden, but they are controlled. Default to no character or subtle human trace. Use `human-presence-and-charm-system.md` before adding people, stick-like figures, cute actors, or storybook scenes. Use `action-character-system.md` when the diagram needs a recurring operator to perform the core conceptual action. Generic stick figures are not the default because they often look like cheap whiteboard training diagrams; prefer human traces, role tokens, faceless paper-cut figures, Paper Operators, or paper-theater actors when human context is truly needed.

If using a Paper Operator, it must not be a mascot. It must physically perform the article action: pulling a carrier, framing a composition, tuning color, catching light, filing an archive, sheltering a note, operating a boundary, weighing a tradeoff, stacking layers, or sweeping residue. If removing the operator does not weaken the figure, remove or rewrite it. For art, culture, personal essays, and life topics, adapt the operator's tool and metaphor world to the domain instead of forcing engineering gates or workflow nodes.

## Output

For strategy: give a compact article structure summary, clarity contract, and shot list.

For generated images: report what was generated, intended use, saved path if applicable, and which images need regeneration.
