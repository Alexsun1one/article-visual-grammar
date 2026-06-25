# Form Selection Engine

Use this engine before `diagram-form-catalog.md`. It decides whether the image should be simple, structured, spatial, data-like, narrative, or not generated at all.

The goal is coverage without bloat: avoid missing important forms, but do not make every idea into a complex diagram.

## Research Basis

This engine abstracts from:

- Financial Times Visual Vocabulary: choose charts by the relationship the reader must understand first.
- Data-to-Viz: use a decision tree from input structure to possible visualization types and include caveats.
- Data Visualisation Catalogue / Data Viz Project: maintain broad form coverage, including less common forms.
- NN/g visual hierarchy and cognitive-load guidance: guide attention, reduce clutter, build on mental models.
- Gestalt principles: proximity, similarity, enclosure, continuity, and connection determine how readers group information.
- ISOTYPE: repeat same-scale symbols and keep meanings stable.
- IKEA-style assembly manuals: show one action per step and minimize text burden.
- Tufte-style restraint: remove visual noise unless it carries information.

## The First Question

Ask:

```text
What would the reader misunderstand if there were no image?
```

If the answer is vague, do not generate yet. Rewrite the shot or skip it.

## Selection Ladder

Choose the simplest rung that preserves the article's meaning.

### Rung 0: No Image

Use when:

- the paragraph is pure voice, transition, or rhetoric
- the visual would repeat the sentence literally
- the idea needs a quote pull, not a diagram

Output: `skip: text is stronger`.

### Rung 1: Single Object Metaphor

Use when:

- one claim or feeling is enough
- no sequence, hierarchy, or comparison is needed
- the article needs a memorable pause

Forms: one object, one label, one state mark, one small visual twist.

### Rung 2: Two-State Contrast

Use when:

- the point is before/after, old/new, false/true, surface/depth
- the reader needs one changed variable

Forms: two panels, split object, wrong/right pair, threshold gate.

### Rung 3: Simple Diagram

Use when:

- the idea has 3-5 parts
- a clear path, layer, matrix, map, scale, or loop explains it

Forms: flow, pyramid, matrix, map, timeline, loop, funnel, cutaway, scorecard.

### Rung 4: Spatial Model

Use when:

- flat layout hides the point
- depth, height, occlusion, rooms, terrain, or distance carry meaning
- the article discusses systems, nested roles, territory, hidden cost, or work/life environments

Forms: spatial stack, room cutaway, terrain model, orbit network, tabletop model.

### Rung 5: Package System

Use when:

- a long article needs 3-6 images
- repeated visual language will improve memory
- multiple forms must feel like one family

Use a package symbol legend, visual token system, and optional guide object.

If uncertain between two rungs, choose the simpler one.

## Article Signal To Form

| Article signal | Recommended form families | Simpler fallback |
| --- | --- | --- |
| "how it works" | cutaway, flow, exploded view, object board | single object metaphor |
| "why it fails" | bottleneck, broken carrier, cutaway, risk boundary | two-state contrast |
| "levels / maturity" | pyramid, ladder, spatial stack | layered shelf |
| "choice / strategy" | matrix, scorecard, scale | two-column contrast |
| "journey / learning" | route map, timeline, terrain | stepping stones |
| "relationships / ecosystem" | cluster map, orbit, room/workspace | hub and spokes |
| "evidence / proof" | scorecard, evidence shelf, mini table | annotated receipt |
| "resource split" | nested container, proportional shelf, waffle | stacked bar |
| "human tension" | storyboard, room/stage, paper theater | single scene |
| "framework / method" | canvas, modular board, spatial workspace | 4-card board |
| "uncertainty / pressure" | terrain, weather field, pressure scale | gradient scale |
| "compounding" | loop, spiral, flywheel with residue | before/after plus residue |
| "data relationship" | FT-style data form by relation | direct label + small chart |
| "workflow across roles" | swimlane, room zones, service blueprint | curved path |
| "from many to few" | funnel, sieve, filter, queue | local bottleneck |

## Data Relationship Gate

If the shot uses real data, choose by relationship before metaphor:

- change over time: line, timeline, slope, milestone shelf
- ranking: ordered bar, lollipop, dot strip, ranked slips
- distribution: histogram, strip plot, density field, specimen row
- correlation: scatter, quadrant, field map
- part-to-whole: stacked bar, waffle, nested container
- flow quantity: Sankey, alluvial, weighted route
- geography or territory: map, choropleth-like field, route map
- hierarchy: tree, icicle, treemap, nested shelf

Never use 3D perspective for quantitative comparison unless spatial position is the actual subject.

## Spatial Gate

Use spatial forms only if at least one is true:

- vertical height means priority, level, maturity, or support
- depth distance means influence, dependency, uncertainty, or time horizon
- occlusion means hidden cost, unseen mechanism, blocked relation, or risk
- room/floor zones mean responsibility, role, habit, or work/life area
- terrain means difficulty, pressure, or navigational choice
- tabletop placement means grouping, assembly, sorting, or physical model logic

Reject spatial forms when:

- the 3D view only makes the image prettier
- labels become smaller or harder to attach
- perspective makes the reader path ambiguous
- the same point would be clearer as a flat contrast, matrix, or flow

## Simplicity Gate

Before prompting, answer:

```text
Can this be a single object, two-state contrast, or 3-step path?
```

If yes, prefer that simpler form unless the article explicitly needs a system view.

Hard limits:

- 1 claim per image
- 1 dominant form per image
- 1 focal action
- 1 carrier or reader path
- label budget chosen by diagram form and cognitive load
- 5-9 objects
- 3-5 stages, layers, landmarks, or panels
- 1 dominant accent color

Break a shot into multiple images if it needs:

- more than 8 labels
- more than 6 stages
- more than 2 axes
- more than 3 clusters
- more than 1 metaphor world
- both a detailed human story and a detailed mechanism

## Coverage Backstop

When planning a full article package, check whether any of these form families should appear:

- object metaphor
- before/after
- flow/process
- hierarchy/layer
- matrix/decision
- map/territory
- timeline/time
- loop/feedback
- funnel/bottleneck
- cutaway/anatomy
- ecosystem/network
- scorecard/evidence
- part-to-whole
- storyboard/human state
- spatial model

Do not force all families into one package. Use this only to prevent blind spots.

## Accuracy Gate

A visual is accurate only if:

- the source anchor is explicit
- the takeaway matches the source, not the artist's invention
- quantity, order, and causality are not exaggerated
- metaphor preserves the article's direction of meaning
- data-like marks do not imply fake precision
- labels use the article's vocabulary
- the rejected alternatives are named when the form choice is non-obvious

Reject if the visual is more interesting than true.

## Form Decision Output

Every shot should include:

```text
selection:
- reader misunderstanding prevented:
- simplest sufficient rung:
- chosen form:
- why this form:
- why not simpler:
- why not more complex:
- accuracy risk:
- complexity budget:
```
