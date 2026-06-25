# Typography Token System

Use this file when images need text, Chinese labels, English labels, or optional blank label zones for later overlay.

Typography is not decoration. In article diagrams, text is a structural layer: it names the focal claim, anchors objects, and prevents metaphor drift.

## Default Typography Decision

Choose one of three modes:

### Model-Rendered Label Mode

Use when the image benefits from integrated Chinese text as part of the scene: signs, stamps, tabs, labels, panels, route markers, packaging, maps, dashboards, or editorial diagram modules.

- model may render concise Chinese labels directly
- labels must be containerized, attached, and readable
- use exact label strings in the prompt
- keep line breaks deliberate; avoid tiny text
- accept direct model text for previews and many article figures when it reads cleanly

### Publish Overlay Mode

Use when exact wording, later editing, legal/financial wording, dense copy, client handoff, thumbnails, covers, or presentation typography matters more than integrated rendering.

- ask the image model to draw blank label containers
- overlay final text using real fonts afterwards
- keep label zones clean, wide, and attached to objects

Default for Chinese article figures: Model-Rendered Label Mode for concise labels; Publish Overlay Mode for dense or mission-critical text. Do not assume model-rendered Chinese is bad; judge by the current model and by the figure's text burden.

## Font Families

### Chinese

Preferred real overlay fonts:

- PingFang SC: clean native macOS editorial sans
- Noto Sans CJK SC: cross-platform clean sans
- Source Han Sans SC: polished open-source Chinese sans
- LXGW WenKai: warm handwritten feeling, only for gentle essays and picture-book captions

Avoid:

- chaotic handwriting
- brush calligraphy unless the article is explicitly about calligraphy or tradition
- childish cartoon fonts
- fake 3D text
- condensed Chinese labels that hurt legibility

### English

Preferred feeling:

- Inter / SF Pro / Helvetica-like sans for clean editorial labels
- IBM Plex Sans / Source Sans for technical explainers
- Source Serif / editorial serif only for article title overlays, not tiny object labels

Use at most two font personalities in one image.

## Type Scale

For a 16:9 article image:

| Level | Use | Chinese length | Relative size | Weight |
| --- | --- | --- | --- | --- |
| L1 | focal label | 2-14 characters | largest | 600-700 |
| L2 | object / zone label | 2-10 characters | medium | 500-600 |
| L3 | state mark / badge | 1-6 characters | small | 600 |
| L4 | optional side note | 4-18 characters | smallest | 400-500 |

Rules:

- use L1 once
- use L2 two to seven times if the diagram needs them
- use L3 one to four times
- avoid L4 unless the image is an evidence/table figure
- never use paragraph text inside the image

## Text Containers

Text should live inside a designed container.

| Container | Best for | Font feeling |
| --- | --- | --- |
| strip label | layers, shelves, axes | clean editorial sans |
| route tag | paths, maps, flows | medium sans |
| state stamp | risk, pass, done, waiting | compact bold sans |
| callout flag | cutaway, mechanism | technical label |
| side note | caveat, proof | small editorial caption |
| panel caption | storyboard, small multiples | picture-book or editorial caption |
| floor/zone label | room, workspace, map | medium sans on surface |
| edge tab | spatial layer, folded object | compact sans |
| axis strip | matrix, scale, value chain | crisp sans |

Labels should attach to:

- surfaces
- edge tabs
- paths
- panels
- objects
- zones
- state marks

Avoid floating labels.

## Chinese Label Constraints

Good Chinese labels:

- use article vocabulary
- use nouns and short verb-object phrases
- avoid abstract filler such as "价值", "能力", "效率" unless the article uses it as a named concept
- keep labels parallel when comparing
- use punctuation sparingly

Bad Chinese labels:

- full slogans in tiny labels
- overlong explanations
- AI-generated pseudo-Chinese
- mixed simplified/traditional unless requested
- English labels mixed in for style only

## Layout Rules

- keep text on calm surfaces, not texture
- reserve padding around each label
- align labels to the grid, path, layer edge, or object edge
- make label reading order match the visual reader path
- never let labels cross the carrier line unless the crossing means conflict
- keep line leaders short and thin
- keep labels away from image edges

## Text Budget

The budget is based on cognitive load, not old model limitations.

- single-object metaphor: 1-4 labels
- simple diagram: 4-8 labels
- matrix, map, service blueprint, field atlas, evidence table: 6-12 labels if the layout is designed for scanning
- cover/social image: 1-5 labels
- avoid paragraphs unless the user explicitly requests a quote poster or long infographic
- split the image if text becomes the main content instead of a diagram layer

## Prompt Tokens

Model-rendered labels:

```text
Render concise Chinese labels directly in the image using a clean editorial Chinese sans-serif feeling, medium weight, normal tracking, attached to objects through label containers. Use the exact provided label text. Keep labels readable, containerized, and aligned to the diagram path. No floating paragraphs.
```

Publish overlay:

```text
Do not render final Chinese text. Draw blank but clearly designed label containers: one L1 focal label zone, 2-5 L2 object label zones, and 1-3 L3 state stamp zones. Make them wide enough for PingFang SC / Noto Sans CJK SC overlay, with clean quiet surfaces and internal padding.
```

Font specificity:

```text
Typography feeling: clean editorial sans-serif, similar to PingFang SC or Noto Sans CJK SC, normal tracking, two weights maximum, label text attached to tags, tabs, route labels, state stamps, and callout flags.
```
