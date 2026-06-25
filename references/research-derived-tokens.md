# Research-Derived Tokens

This file records the visual systems abstracted into this skill. Do not copy any source style directly; extract reusable structure.

## ISOTYPE / Pictogram Systems

Useful abstraction:

- Standardize symbols.
- Repeat same-scale units instead of resizing them for emphasis.
- Use image + keyword, not paragraph text.
- Put symbols on a clear grid so relationships are easy to scan.

Skill token:

- `repeated same-scale objects`
- `keyword labels`
- `grid or row comparison`
- `object count as meaning`

## Assembly Manuals

Useful abstraction:

- Show how parts connect.
- Make the sequence physically understandable.
- Use warnings only where mistakes matter.
- Let the image do most of the explaining.

Skill token:

- `part label`
- `step path`
- `before/after part position`
- `wrong/correct mark`
- `object physically transforms`

## Patent / Technical Line Drawings

Useful abstraction:

- Isolate the mechanism.
- Use clear black line work.
- Use callouts only when needed.
- Show enough views to reveal hidden function.

Skill token:

- `exploded view`
- `callout line`
- `single mechanism focus`
- `hidden part revealed`
- `clean black line`

## Small Multiples

Useful abstraction:

- Repeat one frame to compare variables.
- Keep scale and layout consistent.
- Change only one thing per panel.

Skill token:

- `same frame repeated`
- `one variable changed`
- `2-4 panels`
- `caption under each state`

## IKEA / Assembly Manuals

Useful abstraction:

- Reduce cognitive load by showing only the next necessary action.
- Use part labels, callouts, warnings, and wrong/right marks sparingly.
- Make sequence visible without long explanatory text.
- Keep the camera and symbol system stable so the reader does not relearn the drawing each step.

Skill token:

- `one action per step`
- `stable camera`
- `wrong/right mini mark`
- `part relationship`
- `minimal language`

## Explorable Explanation / Reasoning Path

Useful abstraction:

- Treat text and image as a thinking environment, not decoration.
- Let the reader see the assumption, mechanism, and consequence together.
- Put conclusion near the process that produced it.

Skill token:

- `visible reasoning path`
- `assumption card`
- `local consequence`
- `reader can trace why`

## Thing Explainer / Plain Language

Useful abstraction:

- Simple language can make complex mechanisms less intimidating.
- Physical objects and everyday verbs often explain better than abstract nouns.

Skill token:

- `plain noun labels`
- `short verb labels`
- `everyday object metaphor`
- `no jargon unless article requires it`

## Zukan / Illustrated Catalogs

Useful abstraction:

- Organize visual facts as specimen cards, side notes, labels, numbers, and comparison rows.
- Calm order can be more memorable than dramatic metaphor.

Skill token:

- `specimen card`
- `numbered label`
- `side note`
- `comparison row`
- `legend box`

## Ten Transferable Clarity Principles

- One image explains one claim or mechanism.
- Reader path moves in one clear direction.
- Same shape means the same semantic role.
- Quantity uses repetition, not arbitrary scale.
- Sequence uses steps or frames, one changed variable each.
- Labels attach to objects and use plain words.
- Objects come first; arrows, boundaries, containers, and layers explain relationships.
- A conclusion should sit near process, evidence, or contrast.
- Use the minimum effective difference and remove decorative noise.
- Use catalog-like rows, cards, or small multiples when comparison matters.

## Final Principle

The reusable asset is not a mascot. It is a grammar:

```text
article idea -> visual structure -> connection grammar -> metaphor world -> style tokens -> prompt -> QA
```

## 2026 Deep Research Additions

### Visual Vocabulary / Relationship-First Selection

Useful abstraction:

- Choose forms by the relationship that matters first: change, ranking, distribution, correlation, part-to-whole, flow, geography, hierarchy.
- A chart or diagram is not a neutral container; it asserts which relation deserves attention.

Skill token:

- `reader misunderstanding prevented`
- `relationship-first form choice`
- `why not simpler / why not more complex`

### Data-To-Viz / Decision Tree And Caveats

Useful abstraction:

- Pick forms from input structure and intent.
- A good selector includes caveats, not just suggestions.
- The same data can support several forms; choose by story and risk.

Skill token:

- `simplest sufficient rung`
- `accuracy risk`
- `rejected alternatives`
- `complexity budget`

### NN/g / Visual Hierarchy And Cognitive Load

Useful abstraction:

- Clear hierarchy guides attention to what matters.
- Cognitive load drops when structure, clarity, transparency, and support are visible.
- Proximity and common regions make relationships easier to parse.

Skill token:

- `one focal module`
- `quiet zone`
- `labels attach to objects`
- `single reader path`
- `remove small frictions`

### Gestalt Principles

Useful abstraction:

- Proximity groups related elements.
- Similarity creates semantic families.
- Enclosure is a powerful grouping signal.
- Continuity makes the eye follow smooth paths.
- Connection is stronger than mere closeness.

Skill token:

- `same shape means same role`
- `carrier line creates continuity`
- `container creates grouping`
- `spacing separates unrelated ideas`

### Tufte / Signal Over Noise

Useful abstraction:

- Remove chart junk.
- Use the smallest effective difference.
- Do not let decoration distort data or importance.

Skill token:

- `visual token must carry information`
- `no decorative 3D`
- `one dominant accent`
- `remove what does not prevent misunderstanding`

### Spatial Diagrams

Useful abstraction:

- Spatial depth is powerful only when height, distance, occlusion, zone, or terrain carry meaning.
- 3D can make hierarchy and hidden mechanisms memorable, but it can also hide labels and distort quantities.

Skill token:

- `spatial gate`
- `perspective encodes meaning`
- `edge labels`
- `dollhouse cutaway`
- `miniature terrain`

### Premium Simplicity

Useful abstraction:

- A simple object can outperform a complex diagram when the article has one strong sentence.
- Simplicity feels premium when whitespace, material coherence, and focal surprise are deliberate.

Skill token:

- `single object metaphor`
- `two-state contrast`
- `3-step carrier`
- `one focal surprise`
- `beauty score`

### Service Blueprint / Frontstage-Backstage Thinking

Useful abstraction:

- Some article systems have visible user actions and hidden operational work.
- A layered journey prevents "simple timeline" diagrams from hiding backstage complexity.
- Evidence, emotion, and system response can be separate lanes.

Skill token:

- `service blueprint lanes`
- `frontstage / backstage`
- `evidence lane`
- `emotion curve`
- `lane count budget`

### Typography As Information Architecture

Useful abstraction:

- Text hierarchy is a diagram layer, not an afterthought.
- Real Chinese fonts are safer than model-rendered Chinese for publish-ready assets.
- Labels should sit in designed containers and follow the reader path.

Skill token:

- `typography mode`
- `publish overlay`
- `L1 / L2 / L3 type levels`
- `blank label containers`
- `font family feeling`

### Package Planning

Useful abstraction:

- Long articles need visual rhythm, not image-per-heading automation.
- A strong package varies scale: thesis, mechanism, failure, evidence, human consequence.
- Skipping a section can be a quality decision.

Skill token:

- `article segmentation`
- `visual potential score`
- `package role`
- `skipped section reason`
- `intentional variety`

### Communication, Not Decoration

Useful abstraction:

- Images that do not carry relevant information become visual noise.
- Icons, figures, and characters must first communicate an object, action, role, or idea.
- Illustration systems add value when they explain workflow, context, or emotional state, not when they merely "jazz up" the page.
- Decorative images should be treated as optional atmosphere, not as article figures.

Skill token:

- `human presence level`
- `charm level`

### Art And Design Lineages As Harness Tokens

Useful abstraction:

- Famous art/design movements are useful as visual control systems, not as imitation targets.
- Bauhaus contributes construction logic, simple geometry, and function-first layout.
- De Stijl contributes orthogonal grids, primary accents, and whitespace as structure.
- Constructivist poster logic contributes diagonal pressure and urgency when the article is about risk or force.
- Cubist faceting contributes multiple viewpoints, but can harm quantitative precision.
- Matisse cutout logic contributes warm simplified shape, economy, and lively but controlled color.
- Ukiyo-e and Hokusai-informed composition contribute flat color planes, bold contour, cropped perspective, and force/route rhythm without copying a famous wave.
- Kandinsky and Klee contribute abstract rhythm, symbolic micro-worlds, and gentle complexity when labels remain disciplined.
- Albers contributes color interaction for comparison and nested states.
- Calder contributes balance, dependency, and mobile-like equilibrium.
- Swiss typography contributes grid discipline and label hierarchy.
- Art Nouveau, Art Deco, and risograph contribute organic continuity, premium poster structure, or approachable print texture only when those qualities serve the article.

Skill token:

- `visual harness`
- `output family`
- `style lineage`
- `lineage improves comprehension`
- `anti-copy boundary`
- `style does not override form`
- `composition / line / color / material / rhythm, not artist imitation`
- `what the human element clarifies`
- `minimum useful human presence`
- `reject decorative character`

### Human Presence Without Mascot Drift

Useful abstraction:

- Human context can be shown through traces and roles before full characters.
- A hand, empty chair, role card, or decision desk often explains human consequence better than a generic avatar.
- Stick figures are legible but often lower perceived quality if used as a default identity.

Skill token:

- `H0 no human`
- `H1 human trace`
- `H2 role token`
- `H3 abstract faceless figure`
- `H4 paper theater actor`
- `H5 explicit mascot only`
- `C0-C5 charm scale`
