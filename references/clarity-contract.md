# Clarity Contract

Use this contract before planning or generating non-trivial article illustrations. It prevents attractive but unreadable AI clutter.

## Contract Output

For an article package, fill this compact structure:

```text
output language:
article structure:
- thesis:
- cognitive turn:
- mechanism:
- tension:
- failure mode:
- evidence:
- human state:

article package plan:
- segmentation:
- selected image count:
- package rhythm:
- package roles:
- skipped sections and why:
- intentional variety: object / process / system / evidence / human / summary

visualizable moments:
1. section/paragraph:
   source anchor:
   reader takeaway:
   why image helps:
   reject if:

form selection strategy:
- reader misunderstandings to prevent:
- simplest sufficient rungs:
- forms likely useful:
- forms likely harmful:
- spatial forms allowed only if:
- package complexity budget:

style decision:
- direction:
- metaphor world:
- why this style fits:
- anti-copy boundary:
- symbol system:

diagram form strategy:
- dominant form families:
- coverage matrix check:
- spatial modes allowed:
- forms to avoid for this article:
- why these forms fit the article's thinking path:

visual token strategy:
- color roles:
- line roles:
- line patterns:
- shape roles:
- label containers:
- emphasis rule:
- spatial token rules:

typography strategy:
- mode: draft labels / publish overlay
- Chinese font feeling:
- English font feeling if needed:
- type levels:
- label container plan:
- text-free zones:

human presence and charm strategy:
- human presence level: H0 / H1 / H2 / H3 / H4 / H5
- charm level: C0 / C1 / C2 / C3 / C4 / C5
- chosen form: none / human trace / role token / abstract faceless figure / storybook actor / explicit mascot
- why this clarifies the article:
- why not a simpler human trace:
- why not a full character:
- forbidden character traits:

visual harness strategy:
- output families likely useful:
- output families to avoid:
- form family:
- spatial mode:
- style lineage:
- abstraction level:
- material:
- line behavior:
- color system:
- composition engine:
- human presence:
- typography mode:
- why this lineage helps comprehension:
- anti-copy boundary:

image quality harness strategy:
- quality target:
- material family:
- default composition presets:
- grid and margins:
- focal hierarchy:
- palette discipline:
- typography / overlay plan:
- texture and depth rule:
- negative space contract:
- anti-default-AI constraints:
- default-generation smoke target:

package symbol legend:
- shared primitive geometry:
- shared shape meanings:
- shared color meanings:
- shared label containers:
- recurring marks:
- inheritance rule:
```

For each image, fill:

```text
shot:
placement:
package role:
source anchor:
article job:
reader takeaway:
misunderstanding prevented:
selection:
- reader misunderstanding prevented:
- simplest sufficient rung:
- chosen form:
- why this form:
- why not simpler:
- why not more complex:
- accuracy risk:
- complexity budget:
visual structure:
diagram form:
- family:
- specific form:
- why this form fits the article:
- coverage family:
- layout skeleton:
- spatial mode: flat / isometric / cutaway / room / terrain / tabletop / orbit
- what must be visible in three seconds:
- rejected alternatives:
- beauty move:
- optional guide object:
visual tokens:
- color roles:
- line roles:
- line patterns:
- shape roles:
- label containers:
- emphasis rule:
- spatial tokens:
metaphor world:
focal action:
reader path:
key objects:
line / relation grammar:
chart / diagram form:
symbol system:
- system name:
- primitive geometry:
- symbol classes:
- semantic shape map:
- carrier glyph:
- label containers:
- color roles:
- layout skeleton:
- micro chart form:
- forbidden items:
hierarchy:
- L0 carrier:
- L1 anchor nodes:
- L2 embedded forms:
- L3 text marks:
text plan:
- typography mode:
- L1 focal label:
- L2 object labels:
- L3 state marks:
- text zones:
- font feeling:
- recommended font family feeling:
- render text now or leave blank:
human presence and charm:
- human presence level:
- charm level:
- human form:
- what it clarifies:
- forbidden character traits:
visual harness:
- output family:
- form family:
- spatial mode:
- style lineage:
- abstraction level:
- material:
- line behavior:
- color system:
- composition engine:
- human presence:
- typography mode:
- why this lineage helps comprehension:
- anti-copy boundary:
image quality harness:
- quality target:
- material family:
- grid and margins:
- focal hierarchy:
- palette discipline:
- typography / overlay plan:
- texture and depth rule:
- negative space contract:
- anti-default-AI constraints:
- default-generation smoke target:
composition stability preset:
- preset:
- fixed layout:
- max anchors:
- max labels:
- focal module:
- reader path in seven words or fewer:
- quiet zones:
- forbidden drift:
clarity risk:
beauty gate:
- target score:
- what makes it accurate:
- what makes it understandable:
- what makes it visually desirable:
- what was removed to keep it simple:
- one focal surprise:
- remaining risk:
compact figure spec:
- source anchor:
- reader takeaway:
- form:
- complexity budget:
- visual tokens:
- typography:
- reader path:
- accuracy risk:
- must not show:
prompt notes:
```

## Hard Rules

- One image, one claim or mechanism.
- Read path must be left-to-right, top-to-bottom, outside-to-inside, center-to-parts, or clockwise.
- Every object must either represent a concept, show a relationship, or carry a label.
- Labels attach to objects, containers, paths, panels, or states. Avoid floating explanations.
- Same shape means same semantic role inside one image.
- If quantity matters, use repeated same-scale objects instead of one enlarged object.
- If sequence matters, split into frames or anchor nodes. One frame changes one variable.
- If causality matters, show the local cause and local result, not a symbolic cloud of effects.
- If comparison matters, use small multiples, a scale, two trays, or repeated cards.
- If the image needs more than 8 labels, split it into multiple images.
- If a simpler rung preserves the idea, use the simpler rung.
- If the visual is more interesting than true, reject it.

## Text And Typography Contract

Use the smallest text budget that keeps the diagram clear, but do not cap Chinese labels by habit.

- L1 focal label: usually 2-14 Chinese characters, one per image.
- L2 object labels: usually 2-10 Chinese characters, two to seven per image.
- L3 state marks: usually 1-6 Chinese characters, one to four per image.
- Total Chinese characters: usually 20-90 for article body diagrams.
- Evidence tables, maps, service blueprints, field atlases, and technical plates may use 6-12 labels when the layout is designed for scanning.

Font feeling:

- clean editorial sans-serif for most article work
- technical manual label for mechanism work
- field atlas caption for research or trend notes
- picture-book caption for emotional or narrative work

For publish-ready Chinese, choose model-rendered labels or overlay based on the job. Let the model render concise Chinese when integrated text improves the scene. Use blank label zones and overlay real text later when wording is dense, legally/financially sensitive, client-facing, or must remain editable. Use `typography-token-system.md` to choose the mode. Good font feelings are PingFang SC, Noto Sans CJK SC, Source Han Sans SC, or a restrained clean handwritten font only when the article mood supports it.

## Line / Relation Contract

Choose one main relation grammar:

- path: route, thread, conveyor, river, timeline
- transformation: filter, press, oven, lens, patch, repair bench
- boundary: gate, membrane, threshold, customs desk, lock
- containment: shelf, drawer, jar, folder, box
- weight: scale, counterweight, pressure, sinking platform
- repetition: repeated panels, repeated icons, repeated cards
- causality: lever, domino, fuse, root, chain reaction

Line treatment must be visible but secondary:

- primary carrier line: strongest line or ribbon
- secondary connectors: thin ticks or short callouts
- chart/grid lines: faint and disciplined
- no decorative arrow soup

Use `visual-token-system.md` for line weights and patterns. The contract must say which line is Carrier, which lines are secondary, and whether dashed/dotted/broken/wavy/glow lines carry meaning.

## Chart / Diagram Contract

Use charts only when they clarify the relation.

- mini table: before/after, pro/con, two criteria
- small multiples: compare states, roles, versions, options
- micro chart: trend, accumulation, drop, threshold
- cutaway: hidden components or layered mechanism
- map: route, migration, learning path
- scale: tradeoff or priority
- no chart: single physical metaphor is enough

Use `diagram-form-catalog.md` to choose named forms for every non-trivial shot. Do not write only "flowchart" or "infographic". Specify the family, the exact form, why it fits, what alternatives were rejected, and the beauty move that prevents a stiff PPT look.

Use `diagram-coverage-matrix.md` after the catalog to confirm the chosen form covers the right meaning family: sequence, transformation, hierarchy, choice, territory, system, evidence, quantity, overlap, human situation, work/life system, hidden mechanism, constraint, accumulation, identity, or taxonomy.

Examples:

- workflow article: `flow / curved path / one ribbon with 4 physical stations / rejected swimlane because roles are not central`
- hierarchy article: `pyramid / soft layered foundation stack / base supports top / rejected matrix because sequence is not the point`
- decision article: `matrix / risk-value field / one highlighted quadrant / rejected funnel because no filtering happens`
- work/life article: `room diagram / clean cutaway workspace / zones show attention, duties, and recovery`
- complex system article: `spatial stack / isometric 3D hierarchy / edge labels show levels and access path`
- emotional article: `storyboard / 3-beat clear-line strip / one emotional variable changes / rejected process flow because it would flatten the feeling`

Diagram form must shape the composition:

- flow forms need a carrier
- pyramid forms need support and level labels
- matrix forms need semantic axes
- map forms need landmarks and territory
- loop forms need a return path and residue
- funnel forms need input, constraint, output, and loss
- cutaway forms need one opened object and attached callouts
- scorecard forms need criteria and direct evidence marks
- tree forms need parent-child nesting
- Venn/Euler forms need a meaningful overlap
- Sankey/alluvial forms need true quantity if width varies
- service blueprint forms need route plus lanes
- causal forms need evidence for causality and one main path
- value-chain forms need semantic axes
- storyboard forms need repeated framing and short captions
- spatial forms need depth, occlusion, layer edges, or room/terrain/tabletop relationships that clarify meaning

## Form Selection Contract

Use `form-selection-engine.md` before the diagram catalog.

Every shot must name:

- the reader misunderstanding the image prevents
- the simplest sufficient rung: no image / single object / two-state contrast / simple diagram / spatial model / package system
- why it is not simpler
- why it is not more complex
- the complexity budget: stages, labels, objects, colors, and forms
- the accuracy risk

Default to the simpler rung when uncertain.

## Visual Token Contract

Use `visual-token-system.md` to regulate the image.

Every non-trivial shot must define:

- color roles: Ink, Paper, Quiet, Passage, Evidence, Risk, Growth, Human, Focus as needed
- line roles: Hairline, Standard, Carrier, Boundary, Emphasis
- line patterns: solid, dashed, dotted, double, wavy, broken, glow
- shape roles: module, evidence mark, state, pressure, grouping, layer, contour, lens, thread
- label containers: strip, route tag, state stamp, callout flag, side note, panel caption, floor/zone label, edge tab
- emphasis rule: the single focal object/path/layer/quadrant/boundary/failure/result
- spatial token rules if used: what foreground, height, depth, occlusion, floor zones, or contour density mean

Hard rules:

- One dominant accent only.
- Maximum 3 accent roles per image.
- Main carrier must be visually stronger than secondary connectors.
- Labels live in containers and attach to objects, surfaces, zones, edges, or paths.
- Perspective must encode meaning, not spectacle.
- Guide objects clarify structure; they do not become characters.

## Aesthetic Quality Contract

Use `aesthetic-quality-bar.md` before delivery.
Use `image-quality-harness.md` before the final generation prompt.

Every final image should target score 4 or 5.

The beauty gate must answer:

- what makes it accurate
- what makes it understandable
- what makes it visually desirable
- what was removed to keep it simple
- the one focal surprise
- remaining risk

Do not deliver a score 3 image as final unless the user explicitly wants draft exploration.

## Figure Spec Contract

Use `figure-spec-schema.md` before prompting.

Every non-trivial image must have a checkable figure spec. The spec is allowed to be compact, but it must include:

- source anchor
- reader takeaway
- misunderstanding prevented
- simplest sufficient rung
- exact diagram family and specific form
- complexity budget
- visual token plan
- typography mode and font feeling
- human presence level and charm level
- visual harness and anti-copy boundary
- image quality harness: material family, grid/margins, focal hierarchy, palette discipline, typography/overlay plan, negative space contract, and anti-default-AI constraints
- composition stability preset: exactly one preset, fixed layout, max anchors, max labels, focal module, quiet zones, and forbidden drift
- reader path
- accuracy risk
- must-not-show constraints

If these fields are missing, repair the plan before generating.

## Symbol System Contract

Use `PrismGrid / Anchor Glyph System` when the image needs a consistent non-character identity.

For multi-image packages, define a package symbol legend before individual shots. The legend decides which marks stay stable across the article.

Package legend must include:

- shared primitive geometry
- shared shape meanings
- shared color meanings
- shared label containers
- recurring marks
- inheritance rule: what every image must reuse, and what each image may vary

Every symbol-system image must define:

- primitive geometry: rounded rectangle, circle/dot, arc, wedge, line/polyline
- symbol classes: anchor node, carrier, boundary, container, evidence, tension, transformation, state, or human-stake
- semantic shape map: which shape means which concept
- carrier glyph: ribbon, rail, shelf, route, spine, river, or frame
- label containers: strip, tray label, route tag, state stamp, side note, callout flag, or panel caption
- color roles: passage, evidence, risk, growth, quiet, or ink
- layout skeleton: spine map, shelf sequence, gate transfer, atlas spread, cutaway block, pressure scale, or loop with residue
- micro chart form: bar, dot, step, quadrant, or none
- forbidden items: the specific things not allowed in this image, such as faces, limbs, mascot behavior, generic robot, decorative arrows, or floating labels

Do not invent a mascot to create consistency. Create consistency through repeated marks, stable meanings, line rules, label containers, and color roles.

Treat the package symbol legend as an internal consistency contract. Do not draw a large visible legend box unless the user explicitly asks for a map key. Avoid courseware habits: checkmarks under every step, bottom principle bars, long explanatory footers, sterile rows of equal cards, and head-and-shoulders user icons.

## Optional Guide Object Contract

If the package needs a stronger visual identity, use a guide object, not a mascot.

Allowed guide objects:

- Prism Lantern: reveals structure with light paths
- Folded Compass: points to the reader path
- Index Lens: frames the focal relation
- Signal Thread: moves through each diagram as the carrier
- Anchor Tile: small recurring package mark

Rules:

- optional and secondary
- no face, eyes, limbs, or mascot behavior
- must clarify the chosen diagram form
- may recur across an article package
- must not replace the diagram form or become the main subject

## Style Difference From Xiaohei

Do not use:

- black blob character
- white dot eyes
- tiny mascot worker
- pure white doodle identity as the whole style
- casual handwritten labels everywhere
- Xiaohei action library or known compositions

Prefer one of these original directions:

- **PrismGrid / Anchor Glyph System**: reusable semantic marks, carrier paths, label containers, primitive geometry, and color roles; no character identity.
- **Zukan / Field Atlas**: specimen cards, numbers, side notes, measured objects, calm annotation.
- **Instruction Manual**: ruled steps, part labels, wrong/right marks, hand-free object assembly.
- **Explanation Engineering**: clear line diagram, object metaphors, small charts, visible reasoning path.
- **Clear-Line Picture Book**: simple outlines, flat color, one relation, adult editorial restraint.
- **Editorial Grid-Collage**: paper modules, label zones, chart-object hybrids, strong negative space.

The transferable lesson from Xiaohei is not the character. It is the product discipline: one idea, short labels, consistent defaults, examples, QA, and fast installation.
