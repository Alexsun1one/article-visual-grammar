# Composition Stability Presets

Use this file when the user cares about beauty, first-glance clarity, and generation stability.

The goal is to reduce random composition drift. Do not ask the image model to invent a layout from scratch. Choose one preset, lock counts, and make the prompt obey that preset.

## Stability Rule

One image = one preset + one claim + one focal hierarchy + one material family.

Do not combine multiple presets unless building a deliberate multi-image package. If the idea seems to need two presets, split it into two figures.

## Preset Fields

Every figure must choose:

```text
composition preset:
- preset:
- why this preset:
- fixed layout:
- max anchors:
- max labels:
- focal module:
- reader path:
- quiet zones:
- allowed depth:
- forbidden drift:
```

## Preset A: Hero Object With State Marks

Best for a strong thesis, concept definition, or emotional turn.

Fixed layout:

- one large central object
- 2-4 state marks attached around it
- no process row
- no background scene
- one generous quiet field around the object

Use when:

- the article has one memorable sentence
- a single object can carry the metaphor
- exact labels matter

Max anchors: 1 focal object + 4 marks.  
Max labels: 1 L1 + 4 L2.  
Focal module: the object silhouette.  
Reader path: object first, then marks clockwise or left-to-right.  
Quiet zones: all corners.  
Allowed depth: flat or shallow paper relief.  
Forbidden drift: do not add a scene, characters, a long process, or many callouts.

## Preset B: Carrier Through Gate

Best for transformation, permission, filter, quality control, audit, approval, constraint, or before/after.

Fixed layout:

- left input
- central gate/filter/boundary
- right output
- one carrier line or ribbon passes through
- optional rejected branch drops below

Use when:

- the article says something must pass a threshold
- the key idea is "not everything gets through"
- the reader needs to see causality without a full flowchart

Max anchors: input, gate, output, optional rejected branch.  
Max labels: 3-5.  
Focal module: the gate.  
Reader path: left -> gate -> right; failed branch down.  
Quiet zones: top and outer margins.  
Allowed depth: tabletop or soft diagram.  
Forbidden drift: do not turn into a 7-step process or a dashboard.

## Preset C: Two-State Contrast

Best for before/after, misconception/reframe, old way/new way, weak/strong comparison.

Fixed layout:

- two unequal panels or two objects
- center boundary, hinge, or transformation marker
- one shared baseline
- one visual variable changes

Use when:

- a contrast is clearer than a process
- the article corrects a misconception
- the reader needs instant comparison

Max anchors: 2 focal states + 1 transition mark.  
Max labels: 2 L1 + 2-4 L2.  
Focal module: the changed variable.  
Reader path: left misconception -> right reframe.  
Quiet zones: top center and bottom margins.  
Allowed depth: flat, paper relief, or small tabletop.  
Forbidden drift: do not add a third state, long arrows, or extra examples.

## Preset D: Shelf Matrix

Best for taxonomy, criteria, scorecard, evidence comparison, or decision framework.

Fixed layout:

- 2x2, 3x2, or 4-row shelf
- rows or cells have stable size
- one highlighted cell/row only
- small evidence dots or chips inside cells

Use when:

- the article compares categories
- the reader needs an organized scan
- evidence matters more than metaphor

Max anchors: 4-8 cells.  
Max labels: 4-8 cell labels + 1 highlight label.  
Focal module: one highlighted cell/row.  
Reader path: axes/rows first, then highlight.  
Quiet zones: outer margins and one side note area.  
Allowed depth: flat field atlas or shallow shelf.  
Forbidden drift: do not create a cluttered dashboard, many icons, or arbitrary chart decorations.

## Preset E: Field Atlas Plate

Best for explaining parts, categories, components, failure modes, or repeated patterns.

Fixed layout:

- one plate with specimen cards
- edge labels and small measurement marks
- 3-6 specimens arranged on a grid
- one small legend strip or evidence mark group

Use when:

- the idea is a classification or anatomy
- the article needs a precise, collectible, high-taste explainer
- many things are related but not a sequence

Max anchors: 3-6 specimens.  
Max labels: 3-8.  
Focal module: the specimen with the key difference.  
Reader path: title strip or focal specimen, then supporting cards.  
Quiet zones: plate margins.  
Allowed depth: flat, paper relief, precise linework.  
Forbidden drift: do not turn it into scenery, a poster, or a random icon set.

## Preset F: Cutaway Mechanism

Best for hidden mechanism, root cause, layered system, bottleneck, or "what is really happening inside".

Fixed layout:

- one opened object/system
- 3-5 internal layers or components
- one highlighted hidden cause
- labels on layer edges or callout tabs

Use when:

- the article reveals a hidden structure
- the external symptom differs from the internal cause
- the reader needs depth but not a network

Max anchors: one shell + 3-5 internals.  
Max labels: 4-7.  
Focal module: highlighted hidden cause.  
Reader path: outside -> cut edge -> hidden cause -> consequence.  
Quiet zones: background around the cutaway.  
Allowed depth: cutaway or isometric stack.  
Forbidden drift: do not add many floating parts or a full exploded diagram unless needed.

## Preset G: Route Map With One Obstacle

Best for journey, strategy, product path, learning path, decision path, or tradeoff.

Fixed layout:

- one route line from start to result
- 3-5 landmarks
- one obstacle/pressure field
- optional detour or residue mark

Use when:

- the article is about navigating uncertainty
- sequence and territory both matter
- the result depends on route choice

Max anchors: start, 2-3 landmarks, obstacle, result.  
Max labels: 4-6.  
Focal module: obstacle or detour.  
Reader path: start -> obstacle -> result.  
Quiet zones: open map areas.  
Allowed depth: flat map, terrain, tabletop map.  
Forbidden drift: do not add a full city, many roads, or decorative landscape.

## Preset H: Spatial Stack

Best for hierarchy, maturity levels, system layers, dependencies, capability stack.

Fixed layout:

- 3-5 stacked layers
- labels on front edges
- one carrier or highlight moving upward/downward
- no floating unrelated panels

Use when:

- the article explains levels, dependencies, or maturity
- vertical position carries meaning
- readers need "what supports what"

Max anchors: 3-5 layers.  
Max labels: one per layer + 1 focus label.  
Focal module: layer where change happens.  
Reader path: base -> focal layer -> result/top.  
Quiet zones: background around stack and top air.  
Allowed depth: isometric shallow stack.  
Forbidden drift: do not make it a mountain, game map, or cinematic 3D scene.

## Preset I: Three-Beat Storyboard

Best for human consequence, behavior change, small narrative, or before/action/after.

Fixed layout:

- three equal or rhythmically varied panels
- repeated framing
- one variable changes across panels
- labels are panel captions, not floating notes

Use when:

- the article needs human time and consequence
- posture, distance, waiting, or social tension clarifies the claim
- a single diagram would feel too cold

Max anchors: 3 panels.  
Max labels: 3 captions + 1 small state mark.  
Focal module: changed variable across panels.  
Reader path: panel 1 -> panel 2 -> panel 3.  
Quiet zones: panel gutters and outer margins.  
Allowed depth: flat picturebook or paper theater.  
Forbidden drift: do not use expressive mascot acting, comic clutter, speech bubbles everywhere, or manga styling.

## First-Glance Test

Before generation, ask:

- Can the preset be named from the prompt?
- Can the focal module be seen without reading labels?
- Can the reader path be described in seven words or fewer?
- Are there fewer than 7 anchors unless the preset explicitly allows more?
- Is there one large quiet area?

If not, simplify before generating.

## Stability Prompt Add-On

Use this in final prompts:

```text
Composition stability preset:
- use exactly one preset: {A/B/C/D/E/F/G/H/I}.
- obey the fixed layout; do not invent a new layout.
- max anchors: {number}; max labels: {number}.
- focal module: {one thing}; make it largest/clearest.
- reader path: {seven words or fewer}.
- quiet zones: {where empty space must remain}.
- forbidden drift: {what the model must not add}.
```
