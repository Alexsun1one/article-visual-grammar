# Article Visual Grammar

> A Chinese-first visual grammar skill for turning long-form ideas into clear article figures.

Article Visual Grammar is the big system layer behind the visual skills: article analysis, shot planning, figure specs, diagram form selection, clarity rules, typography, visual tokens, and QA. Use it when the article needs more than decoration: it needs a readable visual argument.

## Examples

<p><img src="examples/images/06-72h-ai-town-visual-harness-preview.png" alt="72h AI town visual harness" width="100%"><br><sub>72h AI town visual harness</sub></p>
<p><img src="examples/images/08-composition-stability-presets-smoke.png" alt="Composition stability preset" width="100%"><br><sub>Composition stability preset</sub></p>
<p><img src="examples/images/09-prism-operators-character-system.png" alt="Action character system" width="100%"><br><sub>Action character system</sub></p>

## What It Does

- Extract visualizable moments from an article before prompting an image model.
- Choose figure forms such as route maps, cutaways, shelf matrices, field atlases, storyboards, and carrier-through-gate diagrams.
- Plan text hierarchy, line grammar, labels, visual tokens, and clarity checks for Chinese article illustrations.
- Produce multi-image packages with a shared symbol legend and consistent visual language.

## Install

Clone this repository into your local Codex skills folder:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Alexsun1one/article-visual-grammar.git ~/.codex/skills/article-visual-grammar
```

If your agent expects a nested skill directory instead of a direct clone, copy the folder that contains `SKILL.md` into its skills directory.

## Use

Example request:

```text
Use article-visual-grammar on this Chinese article. First produce figure specs, then generate 3 body illustrations with readable Chinese labels and a shared symbol legend.
```

The skill entry point is [`SKILL.md`](SKILL.md). Supporting rules live in [`references/`](references/) when this repo includes them; helper scripts live in [`scripts/`](scripts/) when available.

## Quality Bar

- The image must explain a concrete idea, not merely decorate the page.
- Chinese text should be readable at the actual publishing size.
- The output should keep a stable style system across a set while letting each image fit its topic.
- Generated examples are prompts and visual references, not fixed templates.

## WeChat

More writeups, examples, and AI workflow notes are published on my WeChat official account. This is the real QR/search card used for the account, included as a normal bitmap asset rather than a stylized fake code.

<p align="center">
  <img src="assets/wechat-official-account.png" alt="微信搜一搜：正在逐渐AI化" width="720">
</p>

## License

MIT. See [`LICENSE`](LICENSE).

## Notice

This is an original open-source skill package by Sun Wuyuan / Alexsun1one. It is not affiliated with OpenAI, GitHub, WeChat, or any referenced platform. Avoid using it to imitate protected characters, living artists, or third-party brand assets without permission.
