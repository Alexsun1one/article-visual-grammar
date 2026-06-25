# Auto Shot Planner

Use this file when the user gives an article but does not say where images are needed.

The planner decides what to illustrate, what to skip, how many images to make, and which role each image should play in the article. It prevents the common failure where every section becomes a decorative diagram.

## Planning Principle

An article image is justified only when it does at least one of these jobs:

- prevents a concrete misunderstanding
- makes a hidden mechanism visible
- compresses a complex relationship into a readable structure
- gives the reader a memorable anchor for the thesis
- changes the reading rhythm after dense prose
- helps the reader compare choices, levels, evidence, or consequences

If the paragraph is already vivid, quotable, or emotionally precise, text may be stronger than an image.

## Step 1: Segment The Article

Split the article into editorial units:

- title and promise
- opening hook
- thesis
- context / problem
- mechanism
- evidence
- turn or contradiction
- cases / examples
- implications
- conclusion

For each unit, note:

```text
unit:
- source anchor:
- article job:
- visual potential: 0-5
- reason:
- likely form family:
- skip reason if not illustrated:
```

Visual potential scoring:

- 5: must illustrate; a diagram will materially improve understanding
- 4: strong candidate; image likely improves memory or clarity
- 3: optional; good if the article needs rhythm
- 2: mostly decorative; avoid unless package is sparse
- 1: text is better
- 0: do not illustrate

## Step 2: Build A Coverage Set

Choose 3-6 images for most long articles.

Default package roles:

1. Thesis anchor: one image that makes the core claim memorable.
2. Mechanism explainer: one image that shows how the system works.
3. Tension or failure: one image that shows where the problem appears.
4. Evidence or comparison: one image that makes proof, options, or tradeoffs legible.
5. Human / consequence: optional image that shows what changes for a person, team, or workflow.
6. Summary map: optional final image only when the article is long and systemic.

Do not fill all six roles by default. Pick the roles the article actually earns.

## Step 3: Assign Image Types

Use a balanced package instead of repeating one form.

Recommended package patterns:

| Article type | Good package pattern |
| --- | --- |
| product / method essay | thesis object + flow/cutaway + matrix/scorecard + room/workspace |
| technical explainer | cutaway + flow + failure bottleneck + evidence shelf |
| business / strategy analysis | map/value chain + matrix + causal model + scorecard |
| cultural commentary | contrast + storyboard + spectrum + ecosystem |
| personal essay | object metaphor + room/stage + timeline + quiet final image |
| work/life system | room diagram + calendar/timeline + service blueprint + object board |
| AI / agent system | service blueprint + causal model + boundary/gate + evidence table |
| research / trend note | data relationship + small multiples + map/territory + implication scale |

Package balance rules:

- use at most one complex spatial image unless the article is explicitly spatial or systemic
- use at most one dense evidence/table image
- use at least one simple image when the package has 4+ images
- avoid two consecutive images with the same reader path
- vary scale: object, process, system, consequence

## Step 4: Decide Placement

Good placements:

- after the thesis, to anchor the promise
- after the first dense mechanism explanation
- before a major turn, to prepare the reader
- after evidence, to summarize the proof
- near the end, to show implication or final model

Bad placements:

- before the reader knows the article's problem
- after every subheading by habit
- inside a paragraph that already has a strong example
- where the image would interrupt a tightly written emotional passage

## Step 5: Write Rejection Notes

For every skipped high-level section, state why.

Good skip reasons:

- "quote is stronger than diagram"
- "same job already handled by shot 2"
- "would require fake data"
- "would create causal certainty the article does not support"
- "would be a decorative scene, not a thinking tool"

## Step 6: Convert To Figure Specs

Only after the package is chosen, write a full figure spec for each image using `figure-spec-schema.md`.

Every image must have:

- source anchor
- reader takeaway
- simplest sufficient rung
- diagram form
- visual token plan
- typography plan
- accuracy risk
- beauty gate

## Planner Output Template

```text
article segmentation:
1. source anchor:
   article job:
   visual potential:
   candidate form:
   decision: illustrate / skip
   reason:

package plan:
- number of images:
- package rhythm:
- repeated tokens:
- forms intentionally varied:
- sections intentionally not illustrated:

shots:
1. placement:
   package role:
   source anchor:
   reader takeaway:
   figure spec: see full spec
```

