# Visual Token System

This file defines the shared visual language across different diagram forms. The goal is not to make every image look identical. The goal is to make every image feel designed, regulated, beautiful, and semantically accurate.

Use these tokens for article packages, complex diagrams, spatial diagrams, and any generated image that must feel like part of this skill.

## Principle

Different forms, same grammar:

- a pyramid may use layers
- a map may use territory
- a matrix may use fields
- a room may use zones
- an orbit may use distance

But they should share the same semantic line roles, color roles, label containers, emphasis rules, and spacing discipline.

## Color Roles

Use 1 base palette plus 1-3 semantic accents. Do not use color as decoration only.

| Role | Default feeling | Use for | Avoid |
| --- | --- | --- | --- |
| Ink | charcoal / deep slate | primary outlines, main labels, axes | pure black everywhere |
| Paper | warm white / pale tint | background and quiet surfaces | dirty beige overuse |
| Quiet | light gray / mist | secondary grid, inactive objects, distant planes | low-contrast unreadable text |
| Passage | blue / cyan | path, timeline, flow, route, carrier | making every object blue |
| Evidence | yellow / amber | proof dots, receipts, data marks, citations | confusing with warning |
| Risk | red / coral | failure, blocked state, loss, danger, exception | red-green only contrast |
| Growth | green / mint | improvement, recovery, accepted state, output | generic success checkmarks |
| Human | violet / rose | emotion, user state, social pressure | avatar/profile icons |
| Focus | single chosen accent | one focal node or key layer | multiple competing accents |

Default palette recipe:

- background: Paper
- outlines and text: Ink
- secondary scaffolding: Quiet
- carrier path: Passage
- proof or data: Evidence
- problem or constraint: Risk
- desired output: Growth
- one focal emphasis: Focus, chosen from Passage/Risk/Growth/Human depending on article

For one image:

- maximum 3 accent roles
- one dominant accent only
- same color must mean the same semantic role
- if a color marks a state, add a shape or label too

## Line Roles

Line width should communicate hierarchy.

| Role | Width | Use for | Prompt language |
| --- | --- | --- | --- |
| Hairline | 1px | grid, measurement, distant guide, subtle axes | `thin quiet guide lines` |
| Standard | 2px | object outline, ordinary connector, label leader | `clean standard outline` |
| Carrier | 4px | main path, spine, ribbon edge, route, orbit | `strong visible carrier line` |
| Boundary | 3px plus shape | gate, membrane, threshold, container edge | `firm boundary line` |
| Emphasis | 5px or filled band | selected layer, decisive relation, focal route | `single bold emphasis stroke` |

Rules:

- every multi-part image needs one Carrier or equivalent visual spine
- secondary connectors must be weaker than the Carrier
- grid lines must be Hairline and Quiet
- do not use more than one Emphasis stroke unless comparing two states
- line corners may be gently rounded unless technical rigidity is the point

## Line Patterns

| Pattern | Meaning | Use |
| --- | --- | --- |
| Solid | real relation, stable path, current state | default connectors and carriers |
| Dashed | possible path, uncertainty, planned future | future route, hypothesis, tentative link |
| Dotted | evidence trail, sampled data, weak signal | citations, observation, trace |
| Double line | boundary or protected channel | permissions, gates, safety, contracts |
| Wavy line | instability, pressure, emotion, noise | human stress, volatile market, interference |
| Broken line | failure, interruption, dropped handoff | bug, leak, missing step |
| Glow line | guide object light, attention path | optional Prism Lantern / Index Lens reveal |

Never use line patterns as decoration. Name their semantic role in the prompt.

## Shape Roles

Keep shapes stable inside a package.

| Shape | Meaning |
| --- | --- |
| Rounded rectangle | concept, module, step, container |
| Circle / dot | data point, evidence mark, personless actor, sample |
| Capsule | process state, label tag, transient status |
| Arc | feedback, return, orbit, partial relation |
| Wedge | pressure, conflict, risk, decision force |
| Bracket | grouping, boundary, excerpt, scope |
| Layer slab | hierarchy, foundation, system level |
| Terrain contour | uncertainty, difficulty, pressure field |
| Lens | focus, inspection, framing |
| Thread / cord | continuity, journey, handoff |

If using PrismGrid, limit primitive geometry to rounded rectangle, circle/dot, arc, wedge, and line/polyline. Spatial diagrams may extrude these primitives into slabs, shelves, rooms, or terrain.

## Label Containers

Text should live in containers, not float.

| Container | Use |
| --- | --- |
| Strip label | layer, shelf, timeline, matrix axis |
| Route tag | map, flow, carrier path |
| State stamp | pass/fail/risk/done/status |
| Callout flag | cutaway, anatomy, object detail |
| Side note | field atlas, evidence, caveat |
| Panel caption | storyboard, small multiples |
| Floor/zone label | room, stage, workspace, territory |
| Edge tab | spatial stack, 3D layer, folded object |
| Badge dot | tiny evidence or severity mark |

Rules:

- L1 label is the largest and closest to the focal node
- L2 labels attach to objects or zones
- L3 labels are stamps, badges, tiny state marks
- labels must not cross the main carrier unless that crossing means conflict
- no long explanatory footer by default

## Emphasis Rules

Every image needs one focus decision:

- focus object
- focus path
- focus layer
- focus quadrant
- focus boundary
- focus failure
- focus result

Emphasis tools, in priority order:

1. position on reader path
2. scale
3. color role
4. line weight
5. isolation / whitespace
6. small guide object or glow

Do not use all emphasis tools at once.

## Spatial Tokens

Use these when using isometric, cutaway, room, terrain, tabletop, or orbit forms.

| Spatial token | Meaning |
| --- | --- |
| Foreground | current action, reader entry |
| Middle ground | active mechanism or comparison |
| Background | context or consequence |
| Vertical height | hierarchy, maturity, support, priority |
| Depth distance | influence strength, dependency distance, uncertainty |
| Occlusion | hidden cost, blocked relation, unseen mechanism |
| Cutaway edge | revealed interior, not decoration |
| Shadow | separation of layers, not drama |
| Floor zone | role, responsibility, habit area |
| Contour density | pressure, complexity, difficulty |

Spatial rules:

- perspective must encode meaning
- labels attach to layer edges, floors, surfaces, or callout flags
- keep camera gentle: isometric, three-quarter, top-down, or dollhouse cutaway
- avoid cinematic realism; this is editorial information design

## Diagram Form Token Pairings

| Form | Carrier | Accent | Label container | Spatial option |
| --- | --- | --- | --- | --- |
| Flow | ribbon / rail / cord | Passage | route tag | tabletop conveyor |
| Pyramid | layer edge / vertical support | Focus on target layer | strip label / edge tab | isometric stack |
| Matrix | axes / field boundary | Focus quadrant | axis strips | tilted field board |
| Map | route / contour | Passage + Risk obstacle | route tag | terrain model |
| Timeline | shelf / tick rail | Focus turning point | milestone tag | calendar wall |
| Loop | ring / return path | Passage + Evidence residue | state stamp | orbit ring |
| Funnel | narrowing channel | Risk at constraint | tray label | physical sieve |
| Cutaway | callout spine | Evidence on hidden part | callout flag | cutaway object |
| Ecosystem | orbit / cluster path | Focus node | cluster label | depth network |
| Scorecard | grid rail | Evidence + Focus row | row tab | evidence shelf |
| Part-to-whole | container edge | Focus segment | direct segment label | nested box |
| Tree | branch / root / nested edge | Focus branch | branch label / edge tab | root shelf |
| Venn / overlap | field boundary | Focus intersection | field label | shared room zone |
| Sankey / alluvial | weighted ribbon | Passage + Evidence | flow label | braided stream |
| Service blueprint | lane rail | Human curve or Focus lane | lane label / journey tag | room lanes |
| Causal model | causal chain / feedback cord | Risk cause or Growth leverage | variable tag | pressure system |
| Value chain | strategic path | Focus capability | axis strip / map tag | strategic terrain |
| Storyboard | panel rhythm | Human or Risk | panel caption | paper stage |
| Room | floor path | Human / Passage | floor zone label | dollhouse cutaway |
| Terrain | route / contour | Risk pressure | map tag | miniature landscape |
| Object board | thread / connector | Focus object | edge tab / side note | tabletop model |

## Prompt Add-On

Use this block in generation prompts when consistency matters:

```text
Visual token system:
- color roles: Ink outlines and labels, Paper background, Quiet scaffolding, Passage carrier, Evidence marks, Risk constraint, Growth result, one Focus accent only
- line roles: Hairline quiet grid, Standard object outlines, Carrier main path, Boundary gate/container, one Emphasis stroke
- line patterns: solid for real relation, dashed for possible/future, dotted for evidence trail, broken for failure, wavy for pressure
- shape roles: rounded rectangles for modules, dots for evidence, arcs for loops, wedges for pressure, brackets for grouping, layer slabs for hierarchy
- label containers: strip labels, route tags, state stamps, callout flags, side notes, panel captions, edge tabs
- spatial tokens if used: perspective encodes hierarchy, distance, containment, or route; labels attach to surfaces and edges
```

## QA

Reject or regenerate if:

- colors do not have semantic roles
- every element has the same line weight
- the main carrier is not visually dominant
- labels float without containers
- spatial depth is decorative
- multiple accent colors compete
- red means both risk and focus in the same image
- guide object becomes a mascot
- the image looks regulated but lifeless because it has no focal surprise
