# Comic And Picture-Book Forms

Use comic/picture-book language for clarity and charm, not for manga/anime aesthetics. Do not copy any named artist or existing IP.

## Best Default: Clear-Line Picture-Book Explainer

Use for: most article body illustrations.

Why it works:

- child-readable before text
- clear object silhouettes
- flat colors
- low shading
- strong separation between foreground and background
- simple scenes with one visible relation

Tokens:

- clean consistent outlines
- flat color planes
- one focal object or pair of objects
- no hatching
- no texture clutter
- simple background props only when they clarify context
- labels in designed strips or captions, not scribbles

Prompt language:

```text
clear-line picture-book explainer, flat colors, clean object silhouettes, no hatching, no sketchy doodle texture, child-readable composition, one visible relationship
```

## 2x2 Yonkoma Explainer

Use for: before/after, failure-to-insight, user pain, product transformation, a small narrative turn.

Structure:

1. setup
2. development
3. turn
4. result

Rules:

- four equal panels
- same camera angle if possible
- one changed variable per panel
- minimal dialogue
- captions outside or below panels
- no manga screen-tone clutter
- no exaggerated anime expressions unless the article is playful

Prompt language:

```text
2x2 four-panel explainer comic, setup-development-turn-result, same simple scene repeated, one variable changes per panel, flat colors, clear captions, no anime detail
```

## Picture-Book Spread

Use for: emotional or conceptual essays where a single big scene should carry the meaning.

Rules:

- one large simple scene
- text area planned before drawing
- strong eye path
- fewer objects than adult editorial illustration
- emotional color palette
- one surprise detail

Prompt language:

```text
children's picture-book style spread for adults, simple shapes, clear eye path, planned blank text area, warm but not childish, one memorable object
```

## Diagram Comic

Use for: technical or product content that needs both clarity and warmth.

Rules:

- diagram structure remains visible
- objects are lightly personified only when useful
- arrows become physical paths
- captions and labels are disciplined
- humor appears as one small visual twist, not many jokes

Prompt language:

```text
diagram-comic hybrid, clear structural diagram with simple picture-book objects, one small visual joke, disciplined labels, flat colors
```

## Human Presence Control

Use `human-presence-and-charm-system.md` before adding people.

Good defaults:

- H1 human trace for subtle warmth
- H2 role token for teams, users, operators, or stakeholders
- H3 faceless abstract figure for posture/action
- H4 storybook actor only when the emotional scene is the point

Do not use generic stick figures by habit. If a simple figure is needed, make it a faceless paper-cut or clear-line actor whose posture clarifies the article's meaning.

## Avoid As Default

- anime / manga character style
- shoujo decorative panels
- action manga speed lines
- chibi mascots
- over-expressive faces
- generic stick-figure identity
- recurring cute helper
- dense speech bubbles
- black-and-white manga screentones
- casual whiteboard doodles

## Selection Rule

Choose by article job:

- mechanism -> clear-line picture-book explainer or diagram comic
- transformation -> 2x2 yonkoma explainer
- emotional thesis -> picture-book spread
- comparison -> small multiples or 2x2 comic
- technical clarity -> diagram comic / technical plate
