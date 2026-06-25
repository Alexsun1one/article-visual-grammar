# Action Character System

Use this file when an article figure needs a recurring paper action character to make the idea easier to understand.

This system learns from Xiaohei's mechanism, not its appearance. The transferable idea is: a character becomes useful only when it performs the core conceptual action. If the image works the same after removing the character, the character is decoration and should be removed or rewritten.

## Core Rule

Action characters are Paper Operators, not mascots.

They may appear when they clarify:

- who acts
- what moves
- what gets framed
- what gets tuned
- what gets blocked
- what gets inspected
- what changes state
- where the reader should look
- what hidden mechanism, feeling, relation, or aesthetic decision is being operated

They should not appear when a role card, hand trace, carrier line, gate, lens, frame, palette, archive card, empty chair, or object board explains the idea better.

## Original Character Direction: Paper Operators

Paper Operators / 纸片人 are small faceless paper-and-tool figures that live inside the article's metaphor world.

They are not cute mascots, not Xiaohei-like black blob characters, and not whiteboard stick figures. They are calm diagram workers made of folded paper, translucent tools, tabs, and simple geometric bodies. Their job is to operate the idea.

### Visual DNA

- faceless, no eyes, no mouth, no brows, no facial expression
- off-white or pale paper body, charcoal outline, small semantic color tabs
- body built from rounded rectangle, folded tile, capsule, wedge, arc, strip, and line
- small scale: usually 8-18% of canvas height
- simple limbs only when needed for an action
- one domain-specific tool per character: thread, lens, gate, stamp, ruler, tray, hook, wedge, compass, frame, palette, light card, archive folder, weather card, paper screen, scale
- no expressive costume, no face, no hair, no black blob body, no tiny white-dot eyes
- posture and tool explain the action

### Personality

- focused, quiet, precise
- a little odd because the task is physicalized
- not cute-first, not funny-first, not dramatic
- feels like an editorial diagram assistant, paper-stage technician, field-lab operator, studio assistant, archive tender, or quiet caretaker depending on the article domain

## Domain Rule

Paper Operators are not only for engineering or workflow diagrams.

For art, design, and aesthetics, use gallery, studio, frame, plinth, paper palette, color strips, light screens, crop marks, catalog cards, folded canvas, and negative space. Operators can frame, tune, crop, hang, light, restore, layer, or balance.

For literature, culture, and history, use archive drawers, footnotes, index cards, timelines, museum labels, repaired paper, stage curtains, and memory shelves. Operators can file, unfold, compare, annotate, preserve, or sequence.

For personal essays, psychology, and life, use folded notes, chairs, small rooms, weather cards, thread circles, soft screens, envelopes, windows, and repaired paper edges. Operators can shelter, carry, fold, mend, separate, wait, or place.

For business, strategy, and product writing, use tables, routes, gates, scales, stacks, maps, funnels, score cards, decision stamps, and stage boards. Operators can route, filter, weigh, stack, stamp, compare, or bridge.

For engineering, AI, and systems writing, use carriers, nodes, cutaways, gates, lenses, traces, logs, loops, handoff ribbons, and failure bins. Operators can inspect, route, block, repair, reveal, isolate, or reconnect.

Always let the article choose the tool and world. Do not force gates, nodes, and workflows into art, culture, life, or emotional essays.

## Operator Families

Use one by default. Use two only when the relation between them clarifies the article. Use three only for a package style sheet, storyboard, or multi-role system.

### Universal Operators

#### Thread Runner / 牵线员

Role: connection, route, handoff, sequence, dependency, feedback loop.

Actions: pull, tie, route, bridge, untangle, carry.

Tools: blue thread, ribbon, spool, route strip, knot, bridge pin.

#### Lens Keeper / 检视员

Role: attention, inspection, hidden mechanism, evidence, focal relation, quality control.

Actions: frame, reveal, inspect, compare, isolate, highlight.

Tools: translucent lens, frame, light card, evidence dots, viewing window.

#### Gate Builder / 闸门员

Role: boundary, permission, filtering, approval, rejection, conversion, threshold.

Actions: block, open, filter, stamp, wedge, convert.

Tools: gate, hinge, latch, stamp, sieve, threshold strip.

### Art And Culture Operators

#### Frame Setter / 装框员

Role: art criticism, curation, interpretation, taste, composition, reframing.

Actions: frame, hang, align, crop, reframe, restore.

Tools: empty frame, hanging cord, mat board, crop marks, plinth.

#### Color Tuner / 调色员

Role: painting, aesthetics, mood, harmony, taste, style systems.

Actions: mix, tune, balance, separate, layer, compare.

Tools: color strips, paper palette, swatches, translucent wash, tuning fork.

#### Light Catcher / 捕光员

Role: perception, atmosphere, attention, film, photography, stage, revelation.

Actions: catch, cast, reveal, dim, spotlight, reflect.

Tools: light card, paper lamp, translucent screen, reflector, shadow strip.

#### Archive Tender / 档案员

Role: history, memory, cultural lineage, research, influence.

Actions: file, unfold, compare, restore, sequence, preserve.

Tools: folders, index cards, timeline drawer, catalog tabs, cotton gloves.

### Human And Life Operators

#### Care Folder / 照料员

Role: personal essays, emotion, care, recovery, family, waiting, fragility.

Actions: shelter, fold, carry, hold, mend, place.

Tools: envelope, small blanket, empty chair, folded note, weather card.

#### Boundary Keeper / 边界员

Role: relationships, attention, burnout, choice, refusal, self-protection.

Actions: place, block, protect, separate, filter, hold.

Tools: soft gate, thread circle, paper screen, red tab, quiet zone.

#### Weather Reader / 读天气的人

Role: mood, uncertainty, social pressure, cultural climate, internal state.

Actions: read, mark, shelter, tilt, wait, map.

Tools: weather panel, cloud card, rain strip, pressure gauge, horizon line.

### Business, Product, And Technical Operators

#### Stack Mason / 搭层员

Role: hierarchy, product layers, strategy, learning, systems, architecture.

Actions: stack, support, align, lift, repair, stabilize.

Tools: slabs, layers, braces, tabs, tiny lift.

#### Residue Sweeper / 残留清理员

Role: failure modes, ignored costs, cleanup, loops, hidden debt, leftovers.

Actions: sweep, collect, sort, quarantine, recycle.

Tools: tray, brush, residue box, broken red path.

#### Tradeoff Weigher / 权衡员

Role: decision, economics, priority, ethics, tradeoffs, strategy.

Actions: weigh, balance, remove, compare, mark.

Tools: paper scale, counterweights, score cards, sliders.

## Action Verbs

Use physical verbs. Pick one action per image.

Good verbs:

- pull
- frame
- reveal
- block
- tune
- fold
- sort
- mend
- weigh
- arrange
- carry
- shelter
- distill
- balance
- light
- archive
- transform
- stack
- bridge
- repair
- sweep

Weak verbs:

- stand
- watch
- point vaguely
- smile
- present
- decorate
- wave

## Character Inclusion Test

Before generation, answer:

```text
action character:
- use character: yes/no
- source anchor:
- article domain:
- operator family:
- action verb:
- object being acted on:
- relation clarified:
- what breaks if removed:
- size relative to canvas:
- forbidden drift:
```

If "what breaks if removed" is weak, do not use a character.

## Prompt Add-On

Use when an operator is needed:

```text
Action character system:
- use one Paper Operator, not a mascot.
- operator: {Thread Runner / Lens Keeper / Gate Builder / Frame Setter / Color Tuner / Light Catcher / Archive Tender / Care Folder / Boundary Keeper / Weather Reader / Stack Mason / Residue Sweeper / Tradeoff Weigher}.
- action: {pull / frame / reveal / block / tune / fold / sort / mend / weigh / arrange / carry / shelter / distill / balance / light / archive / transform / stack / bridge / repair / sweep}.
- the operator must physically operate {carrier / lens / gate / frame / palette / light card / archive folder / note / boundary screen / weather card / layer / map / evidence card}; it cannot stand beside the diagram.
- appearance: faceless folded-paper geometric figure, off-white body, charcoal outline, small semantic color tab, no eyes, no mouth, no black blob body, no tiny legs, no stick-figure identity.
- scale: secondary to the diagram, usually 8-18% canvas height.
- if removed, the key relation should become less clear.
```

Use when a character is not needed:

```text
Action character: none. Use object-first explanation, carrier line, labels, and diagram form. Do not add a helper figure.
```

## QA

Accept if:

- the operator performs the core action
- the tool/action clarifies the reader path or relation
- the operator's tool fits the article domain
- the character is secondary to the diagram but not decorative
- the design is faceless, paper-built, and compatible with the article's metaphor world
- the image is premium and not childish

Reject if:

- the operator only stands near the diagram
- removing the operator does not weaken the figure
- it forces engineering props into an art, culture, life, or emotional essay
- it looks like Xiaohei: black blob, white dot eyes, tiny thin legs, deadpan monster body
- it looks like a generic stick figure, avatar, cute mascot, robot, or office worker
- multiple operators compete with the diagram form
- the action is vague or purely emotional
