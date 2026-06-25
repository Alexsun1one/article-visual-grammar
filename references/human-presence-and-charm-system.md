# Human Presence And Charm System

Use this file when an image needs more visual warmth, cuteness, human context, or story energy.

The goal is not to add characters everywhere. The goal is to choose the minimum human presence that improves clarity, empathy, memory, or reading pleasure.

## Research Basis

This system abstracts from:

- usability research: decorative images are ignored when they do not carry relevant information
- icon usability: symbols must communicate a recognizable object, action, or idea before they add personality
- product illustration systems: illustration can guide tasks, explain workflows, and reflect user context or emotional state
- accessibility guidance: decorative images add no information; meaningful images should communicate content

## Default Decision

Default to no character.

Add human presence only when at least one is true:

- the article is about a person, team, role, habit, emotion, decision, or social situation
- the reader needs to understand who acts, waits, chooses, or is affected
- a mechanism is otherwise too cold or abstract
- the image's package role is human consequence, storyboard, room/stage, service blueprint, or work/life system
- the article's emotional temperature matters to comprehension
- a small operator physically performing the action would make the diagram relation clearer than labels alone

Do not add human presence when:

- the article is primarily about data, architecture, evidence, taxonomy, or hidden mechanism
- a character would simply stand beside a diagram
- the figure would be a mascot, logo, or recurring IP by accident
- a stick figure or avatar would weaken the premium feel

If a recurring action figure is needed, use `action-character-system.md`. Prefer a Paper Operator over a generic stick figure or mascot.

## Human Presence Scale

Choose one level per image.

| Level | Name | Use when | Allowed forms | Avoid |
| --- | --- | --- | --- | --- |
| H0 | No human | mechanism/data/system clarity is enough | objects, carriers, labels, guide object | fake empathy |
| H1 | Human trace | a person is implied but not central | empty chair, hand, footprint, coffee ring, cursor, calendar mark, worn path | avatar icons |
| H2 | Role token | roles matter but faces do not | role tab, name card, badge, audience slice, decision desk, seat marker | head-and-shoulders pictograms |
| H3 | Abstract figure | action or posture clarifies the point | faceless paper-cut figure, rounded silhouette from behind, simple hand-only actor, tiny operator shape | dot eyes, limbs as mascot identity, stick figures |
| H4 | Scene actor | a human situation is the point | paper theater, room/stage figure, storyboard actor, clear-line picture-book character | over-expressive faces, manga/anime, cute worker IP |
| H5 | Mascot / recurring character | only if user explicitly asks for a brand character | custom character bible, explicit consent, separate IP design | default article diagrams |

Default package mix:

- analytical/technical article: H0-H1
- product/workflow article: H1-H2, sometimes H3
- personal/culture/life essay: H2-H4
- cover/social image: H2-H4 if emotional hook matters

## Cuteness / Charm Scale

Charm is a control, not a style default.

| Level | Name | Visual behavior |
| --- | --- | --- |
| C0 | austere | technical plate, no softness beyond spacing |
| C1 | warm | rounded modules, soft color, friendly labels |
| C2 | playful | one charming object, soft irregular shapes, mild visual wit |
| C3 | storybook | clear-line picture-book scene, warm props, simple emotional beat |
| C4 | characterful | abstract figures with posture, room/stage storytelling |
| C5 | mascot-led | only by explicit request; separate brand/IP work |

Default: C1-C2 for article body diagrams. Use C3-C4 only when the article needs human feeling or narrative.

## Stick Figure Decision

Do not use generic stick figures as the default.

Why:

- they often look like cheap whiteboard training diagrams
- they make the system feel less premium
- they become a weak recurring character without enough originality
- they can imply "people" when the article only means roles, users, or states

Allowed stick-like forms only when:

- the article explicitly needs simple human motion or posture
- the style is a controlled service blueprint, storyboard, or instruction manual
- the figure is not the identity anchor
- the body is abstract, geometric, faceless, and secondary

Better alternatives:

- empty chair for absence or burden
- hand moving an object for agency
- role card or badge for team/user/operator
- audience slice card for groups
- decision desk for judgment
- paper theater figure for narrative
- faceless rounded silhouette from behind for attention or stance
- cut-paper hand, cursor, footprint, shadow, or path for human trace

Important: do not default to a hand. A hand is useful only when physical agency, permission, judgment, care, or intervention is the point. If the article is about a system, hidden mechanism, security boundary, data flow, taxonomy, or market structure, prefer objects, boundaries, doors, locks, ledgers, paths, diagrams, and role tokens before using any visible body part.

## Character Forms

### Human Trace

Best for: subtle warmth, premium diagrams, technical articles that need a human consequence.

Tokens:

- small hand
- empty seat
- route worn into paper
- coffee ring
- calendar pressure mark
- cursor / pointer
- object with use marks

### Role Tokens

Best for: teams, users, operators, stakeholders, service blueprints.

Tokens:

- role tab
- seat marker
- badge without face
- nameplate
- audience slice
- permission card
- decision desk

### Abstract Figures

Best for: posture, attention, waiting, choosing, carrying, passing, blocked action.

Rules:

- faceless
- minimal body detail
- no white-dot eyes
- no expressive face
- no recurring costume as IP
- small relative to the diagram form
- posture must clarify the article's meaning

Good prompt language:

```text
secondary faceless paper-cut human figure, simple rounded silhouette, no eyes, no facial features, posture clarifies the decision, not a mascot
```

### Paper Operators

Best for: action-led diagrams where a figure must operate the relation.

Use `action-character-system.md` for:

- universal/system: Thread Runner, Lens Keeper, Gate Builder.
- art/design: Frame Setter, Color Tuner, Light Catcher.
- culture/history: Archive Tender.
- personal/life: Care Folder, Boundary Keeper, Weather Reader.
- business/product/technical: Stack Mason, Residue Sweeper, Tradeoff Weigher.

Rules:

- one operator by default
- action verb must be visible
- the operator must act on a concrete object from the article domain: carrier, lens, gate, frame, palette, light card, archive folder, note, boundary screen, weather card, layer, map, evidence card
- no eyes, no face, no black blob body, no tiny-worker identity
- if removing the operator does not weaken the diagram, remove it
- do not force engineering props into art, culture, personal, life, or emotional essays

### Storybook / Paper Theater Actors

Best for: personal essays, culture commentary, emotional turn, user pain, life/work situations.

Rules:

- use 1-2 actors max
- keep props and diagram overlay more important than the character
- use captions, not speech bubble clutter
- same camera and simple staging
- emotion comes from posture, distance, color, and object state

## Human Representation By Diagram Form

| Diagram form | Best human presence |
| --- | --- |
| flow / process | H1 handoff marks, H2 role tabs, H3 small operators |
| service blueprint | H2 role tokens plus emotional curve; H3 only for frontstage action |
| room / workspace | H1 empty seats, H2 zone labels, H3 faceless actors if roles matter |
| storyboard | H3-H4 actors, but one changed variable per panel |
| matrix / scorecard | H2 role cards or audience slices, no figures needed |
| cutaway / mechanism | H1 human trace near consequence, not inside every part |
| ecosystem / network | H2 stakeholder tokens, no profile heads |
| map / journey | H1 footprints/path, H2 traveler token, H3 figure only if journey is personal |
| technical plate | H0-H1 only |
| personal essay | H1-H4 depending on emotional centrality |

## Charm Tokens

Use one or two:

- rounded imperfect modules
- tiny physical tabs
- one oversized focal object
- soft shadow under paper layers
- warm accent color
- small truthful visual joke
- object with use marks
- gentle contour line
- folded corner
- tactile label stamp

Avoid:

- emoji-like symbols
- kawaii faces
- random animals
- mascot helper
- repeated tiny workers
- hearts/sparkles as generic cuteness
- decorative confetti
- over-soft pastel palette with no semantic color

## Prompt Add-On

Use when warmth is needed:

```text
Human presence and charm:
- human presence level: H{0-5}
- charm level: C{0-5}
- use {human trace / role token / abstract faceless figure / paper theater actor}
- explain what the human element clarifies
- no mascot, no dot eyes, no stick-figure identity, no head-and-shoulders avatar, no character standing beside the diagram
```

Use when characters are not needed:

```text
Human presence: H0-H1 only. Do not draw people or mascots. If human consequence is needed, show it through an empty chair, hand trace, role card, or used object.
```

## QA

Accept if:

- the human element explains who acts, decides, waits, suffers, benefits, or learns
- a Paper Operator, if used, performs the core action, clarifies a relation, and uses tools that fit the article domain
- the human element is smaller than the diagram idea
- the article supports the emotion or role shown
- the cuteness comes from proportion, material, spacing, or one truthful detail
- the figure is not becoming the package identity unless explicitly requested

Reject if:

- the character is only decorative
- the character repeats across images as an accidental mascot
- the figure has dot eyes, expressive face, or tiny-worker behavior
- the operator stands beside the diagram instead of operating it
- the image would be clearer as a role card, hand, empty chair, or object trace
- charm makes the article feel childish, unserious, or less accurate
