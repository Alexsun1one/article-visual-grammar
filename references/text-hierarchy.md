# Text Hierarchy

Text is part of the image system. It should guide reading, not explain the whole article.

## Default Text Budget

- Total labels: determined by diagram form and cognitive load, not by an old model-text limit.
- Single-object metaphor: 1-4 labels.
- Simple diagram: 4-8 labels.
- Matrix, map, service blueprint, evidence table, field atlas, or technical plate: 6-12 labels if the layout is built for scanning.
- Total Chinese characters: usually 20-90 for article body diagrams; more only for long infographics or quote posters.
- No paragraphs inside the image.
- No full sentence unless it is the article's central quote and the user requests it.

## Text Levels

### L1: Focal Label

Purpose: name the central object, state, or result.

Length: usually 2-14 Chinese characters.

Placement: on the main object, under the main object, or as a sign attached to it.

Use at most one.

### L2: Object Labels

Purpose: identify key parts.

Length: usually 2-10 Chinese characters.

Placement: tray label, tag, signpost, sticky note, caption under mini-panel, small callout line.

Use 2-5.

### L3: State Marks

Purpose: show status, warning, pass/fail, version, direction.

Length: usually 1-6 Chinese characters.

Placement: stamp, seal, badge, checkmark, warning mark, route tag.

Use 1-3.

## Where Text May Appear

Allowed:

- object tag
- label on container
- signpost
- stamp or seal
- mini-panel caption
- callout line
- margin note
- route label

Avoid:

- floating explanatory sentences
- top-left title by default
- paragraph blocks
- labels on every object
- text that crosses important line art

## Font Feeling

For model-generated draft labels:

- clean, legible Chinese sans-serif or editorial label feeling
- medium weight
- not casual handwriting by default
- not calligraphy
- not decorative brush
- not childish
- not chaotic

For publish-ready overlays:

- use a real Chinese font after image generation when exact wording matters
- recommended feeling: `PingFang SC`, `Noto Sans CJK SC`, `Source Han Sans SC`, or a clean handwritten font if available
- use two weights at most
- keep tracking normal
- avoid vertical text unless the composition requires a signboard or scroll
- prefer label boxes, captions, axis labels, tags, and legend blocks over doodle annotations

See `typography-token-system.md` for the fuller typography token system, including overlay mode, type scale, font family choices, and text container rules.

## Text Strategy

### Model-Rendered Label Mode

Let the model render concise Chinese labels directly when the text is integrated into signs, stamps, route tags, panels, maps, technical plates, or editorial diagrams. Use exact label text and normal editorial font feeling. This is acceptable for many current image models.

### Publish Mode

Ask the model to draw blank tags, signs, trays, seals, or caption spaces. Overlay final Chinese text afterwards. Use this when the image is for public posting, thumbnails, covers, or paid/presentation use.

Prompt token:

```text
Draw blank label areas and signs where text should go, but do not render Chinese text. Leave clean white space inside each label area for later typography overlay.
```

## Text Plan Template

```text
text mode: model-rendered labels | blank labels for overlay
font family feeling:
L1 focal label:
L2 object labels:
L3 state marks:
font feeling:
placements:
text-free zones:
```
