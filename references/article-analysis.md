# Article Analysis

The first job is to decide what deserves an image. Most article paragraphs do not.

## Extract These From The Article

### Thesis

The sentence the article is trying to make unforgettable.

Good image job: one strong metaphor or contrast.

### Cognitive Turn

The moment where the reader should change their mind.

Good image job: before/after, boundary crossing, scale, inversion.

### Mechanism

How something actually works.

Good image job: pipeline, assembly path, exploded view, feedback loop.

### Tension

Two forces pulling against each other.

Good image job: tradeoff scale, forked route, tug, pressure system.

### Failure Mode

Where things silently break.

Good image job: bottleneck, leak, paper jam, missing part, blocked gate.

### Evidence

What makes the claim credible.

Good image job: stack, archive, repeated objects, small multiples.

### Human State

How the reader/user/founder/operator feels.

Good image job: comic beat, mini-world, object theater.

## Shot Selection Rules

Prefer shots that:

- reduce a hard idea to one visible relation
- help the reader remember the argument
- make a hidden mechanism visible
- clarify a tradeoff
- turn a vague claim into a physical scene

Reject shots that:

- only decorate a section
- duplicate another shot's job
- require more than 8 labels to understand
- are just "AI doing X" with a robot or brain
- are beautiful but do not sharpen the article

## Automatic Article Planning

When the user pastes a full article and does not specify images, do not ask them where diagrams belong. Use `auto-shot-planner.md`.

The planning order is:

1. segment the article into editorial units
2. score each unit's visual potential from 0 to 5
3. choose a small package of images with distinct roles
4. name sections that should not be illustrated
5. convert selected images into figure specs

Good package roles:

- thesis anchor
- mechanism explainer
- tension or failure
- evidence or comparison
- human consequence
- summary map

Do not treat every heading as an image request.

## Article-To-Shot Matrix

For each candidate, fill this before prompting:

```text
paragraph/section:
reader takeaway:
article job: thesis | cognitive turn | mechanism | tension | failure mode | evidence | human state
visual structure:
connection grammar:
metaphor world:
visual potential:
package role:
decision: illustrate | skip
skip reason:
must-show objects:
must-not-show cliches:
```
