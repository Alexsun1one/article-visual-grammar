# Image Quality Harness

Use this file when the image must look publish-grade by default, not merely follow a correct plan.

The skill is not a model fine-tune. It only becomes world-class when the final prompt, generated image, and repair loop all carry strong art direction. Abstract terms like "premium", "beautiful", "PrismGrid", or "editorial" are not enough. Translate them into visible constraints.

## Quality Ladder

Every generated image should pass these four gates.

### Q1: Editorial Reason

- The image is tied to a source anchor.
- It prevents one named reader misunderstanding.
- It has one reader takeaway.
- It uses the simplest sufficient form.

Reject decorative images even if they look good.

### Q2: Art Direction

The prompt must specify concrete visual direction:

- canvas: 16:9 article body figure unless another placement is chosen
- grid: 6-column or 8-column invisible editorial grid
- margins: generous outer margins and clear gutters
- material: one material family only
- line: named line hierarchy and line behavior
- color: semantic palette with one focus accent
- shape: semantic shape map, not stock icons
- labels: attached label containers, no floating text
- typography: model-rendered concise labels or blank overlay containers by decision
- texture: light and controlled, never busy behind text
- depth: only if it encodes hierarchy, containment, route, or distance

Reject prompts that say only "nice", "premium", "modern", "clean", or "world-class".

### Q3: Generated Image Smoke

After generation, inspect the image as an image, not as a prompt:

- Does the first glance reveal the form?
- Does the eye know where to start?
- Is there a visible focal action?
- Are the quiet zones actually quiet?
- Do colors mean the roles they were assigned?
- Are labels readable or clearly reserved for overlay?
- Does it avoid PPT, stock icon, courseware, and generic AI-art habits?
- Would it still look intentional if cropped into an article column?

Only call it final if the image is a 4 or 5 on `aesthetic-quality-bar.md`.

### Q4: Repair Loop

Repair the single largest failure first. Do not rewrite the whole image unless the meaning is wrong.

Common first repairs:

- no focal structure -> add one continuous carrier and one larger anchor node
- PPT feel -> replace boxes/arrows with tactile modules, object board, cutaway, route, shelf, terrain, or field-atlas plate
- visual mud -> remove 30-50% of objects and labels
- weak style -> pick one stronger material family and one style lineage
- bad text -> switch to blank label containers and overlay
- too cute -> remove figures; make charm come from shapes, spacing, and one truthful detail
- too cold -> add H1/H2 human trace or role token, not a mascot

## Default World-Class Prompt Stack

When the user asks to generate directly, compile each figure through this stack:

```text
1. Figure Spec: source anchor, reader takeaway, misunderstanding prevented, form, risk, must-not-show.
2. Diagram Engine: exact form, layout skeleton, reader path, carrier, focal action.
3. Visual Token System: colors, line weights, line patterns, shapes, labels, emphasis.
4. Typography Plan: render exact concise labels or leave blank overlay containers.
5. Composition Stability Preset: exactly one preset, fixed layout, max anchors, max labels, focal module, quiet zones, forbidden drift.
6. Art Direction Harness: grid, margins, material, color taste, line behavior, texture, whitespace, focal surprise.
7. Negative Space Contract: what stays empty, what is deliberately not shown, what complexity was removed.
8. Anti-Default-AI Constraints: no PPT, no stock icons, no robot/brain/rocket/lightbulb by habit, no mascot identity, no decorative arrows, no fake data.
9. Smoke Target: "must read in three seconds and score 4+ on the beauty gate."
```

If the final prompt is too long, do not delete the art direction. Delete secondary concepts, extra labels, and style adjectives first.

## Material Families

Choose one.

### Editorial Paper Model

Best for essays, business analysis, culture commentary, personal reflection.

- warm off-white Paper
- charcoal Ink
- paper-layer modules with subtle fiber
- soft shadow under only major layers
- cut tabs, stamps, shelf labels, route tags
- no glossy render, no photo realism

### Field Atlas Plate

Best for classifications, mechanisms, technical explanation, evidence, taxonomy.

- pale neutral field sheet
- precise ink outlines
- specimen cards, edge labels, small measurement marks
- micro charts embedded as evidence marks
- restrained color chips
- no decorative scenery

### Soft Diagram Infographic

Best for workflows, product concepts, operating systems, strategy.

- flat vector slabs with tactile corners
- one strong carrier color
- quiet grid or lanes
- chart-object hybrids
- large focal module plus secondary modules
- no equal-weight card wall

### Spatial Editorial Model

Best for hierarchy, territory, containment, work/life systems, complex systems.

- isometric or gentle three-quarter view
- shallow depth
- labels on surfaces, floor zones, or layer edges
- soft shadows only for separation
- no cinematic lighting or game-like realism

### Clear-Line Picturebook Explainer

Best for human consequence, emotion, care, learning, social situations.

- clean contour lines
- flat color areas
- faceless abstract figures only when needed
- few props, generous stage space
- warmth through posture, distance, and scale, not cute mascot behavior

## Palette Discipline

Use semantic roles, then choose taste.

Default tasteful palette:

- Paper: warm white `#F8F5EE`
- Ink: charcoal `#243036`
- Quiet: blue-gray `#D8E1E7`
- Passage: clear blue `#2F80ED`
- Evidence: muted amber `#E2A93B`
- Risk: coral `#E85D5A`
- Growth: calm mint `#4BAE85`
- Human: muted plum `#8A6FA8`
- Focus: one of Passage, Evidence, Risk, Growth, or Human, not an extra rainbow color

Rules:

- Use 3-5 visible colors, not all roles.
- Do not put saturated color behind small text.
- Use Risk only for actual constraint, failure, loss, or warning.
- Use Focus only once.
- Avoid all-blue enterprise palettes, purple-gradient dominance, beige-only diagrams, and neon rainbow diagrams.

## Typography And Overlay Defaults

Use model-rendered labels when:

- labels are short and integrated into signs, stamps, tabs, maps, shelves, surfaces, or UI-like panels
- wording can tolerate minor imperfections
- the image benefits from natural in-scene text

Use publish overlay when:

- Chinese text must be exact
- labels are dense
- the image is public-facing, legal, financial, client-facing, or presentation-critical
- the user may need to edit labels later

Overlay containers must be drawn as real design elements: tabs, strips, flags, stamps, floor labels, surface plates, or side notes. Do not leave random empty rectangles.

## Anti-Default-AI List

For default article diagrams, forbid these unless the article specifically asks for them:

- robot, brain, rocket, lightbulb, floating circuit head
- generic dashboard UI cards
- generic people avatars or head-and-shoulder icons
- checkmark under every step
- bottom moral/principle bar
- equal-sized process cards in a row
- stock isometric office scene
- glassmorphism blobs or decorative gradient spheres
- dense arrows with no semantic line hierarchy
- title-heavy poster layout for a body figure
- fake small text texture
- pseudo-Chinese text when exact labels matter

## Prompt Compiler Pattern

Use this compact block inside final prompts:

```text
Image quality harness:
- quality target: publish-grade article body figure, beauty score 4+.
- material family: {editorial paper model / field atlas plate / soft diagram infographic / spatial editorial model / clear-line picturebook explainer}.
- composition stability preset: {Hero Object With State Marks / Carrier Through Gate / Two-State Contrast / Shelf Matrix / Field Atlas Plate / Cutaway Mechanism / Route Map With One Obstacle / Spatial Stack / Three-Beat Storyboard}; obey one fixed layout only.
- composition: 6/8-column invisible grid, generous margins, one large focal module, clear gutters, quiet zones.
- focal hierarchy: {largest object / strongest carrier / isolated module / one accent / cutaway reveal / guide-object light}.
- palette: semantic roles only; Paper, Ink, Quiet, Passage, Evidence, Risk, Growth, Human, Focus as needed; 3-5 visible colors.
- typography: {model-rendered concise labels / blank overlay containers}; labels attached to objects, paths, surfaces, zones, or tabs.
- texture and depth: one controlled texture/material; depth only if it encodes meaning.
- negative space: leave {specific zones} quiet; remove {specific complexity}.
- anti-default-AI: no PPT, no stock icons, no robot/brain/rocket/lightbulb, no mascot identity, no fake dense text, no decorative arrows.
```

## Forward-Test Requirement

After a substantial change to this skill, run at least one default-generation smoke when feasible:

1. Give the skill a real article or real concept.
2. Let it choose the figure spec.
3. Generate one image with no extra manual art direction beyond the skill.
4. Score the image with this harness and `qa-checklist.md`.
5. Patch the skill if the image looks like generic AI output, PPT, stock icons, or a pretty but unclear poster.

Do not call a visual skill world-class until its default path produces at least one strong sample without the author rescuing it by hand.
