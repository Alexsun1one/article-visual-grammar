# Article Visual Grammar / 文章配图语法

> 把长文里的判断、转折、机制和关系，先拆成可审查的图像 brief，再生成清楚、好看、能读懂的中文正文配图。

这是今天这批视觉 skill 里最底层的“图解语法引擎”：它不急着生图，而是先读文章、找出真正值得画的句子，再决定用路线图、剖面图、货架矩阵、故事板、纸片舞台还是别的形式来表达。适合公众号长文、产品文章、AI/工程复盘、商业分析、知识科普。

## 示例图

<p><img src="examples/images/06-72h-ai-town-visual-harness-preview.png" alt="AI 小镇系统图" width="100%"><br><sub>AI 小镇系统图</sub></p>
<p><img src="examples/images/08-composition-stability-presets-smoke.png" alt="稳定母版示例" width="100%"><br><sub>稳定母版示例</sub></p>
<p><img src="examples/images/09-prism-operators-character-system.png" alt="动作角色系统" width="100%"><br><sub>动作角色系统</sub></p>

## 它能做什么

- 从文章中提取 source anchor：一句判断、一个冲突、一个机制或一个认知转折。
- 自动规划一篇文章要配几张图，哪些段落值得画，哪些段落不必硬配。
- 选择图式：路线图、剖面图、矩阵、飞轮、漏斗、时间线、系统地图、纸片小镇等。
- 规划中文字层级、标签位置、线条关系、颜色语义和统一符号系统。
- 用 QA 约束“读者三秒能不能看懂”，避免只漂亮但空泛的 AI 图。

## 安装

把这个仓库克隆到本机 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Alexsun1one/article-visual-grammar.git ~/.codex/skills/article-visual-grammar
```

如果你的 Agent 使用其它 skills 目录，也可以把包含 `SKILL.md` 的这个仓库复制过去。

## 怎么用

示例请求：

```text
用 article-visual-grammar 读这篇中文长文。先输出 3 张正文配图的 figure specs，再生成配图提示词。要求中文标签可读、每张图绑定原文锚点、整组风格统一。
```

Skill 入口是 [`SKILL.md`](SKILL.md)。细则在 [`references/`](references/)；如果这个仓库带脚本，脚本在 [`scripts/`](scripts/)。

## 质量要求

- 先服务内容，再服务风格；图必须解释一个具体想法。
- 中文默认要可读，标题、caption、标签不能只当装饰纹理。
- 同一组图要风格统一，但每张图要贴合自己的段落/用途。
- 示例图是工作流参考，不是唯一模板。

## 公众号

更完整的拆解、提示词、案例复盘、AI 写作和产品实践，我会继续写在公众号里。下面是我的真实公众号二维码/搜一搜卡片，不是仿造的装饰二维码。

<p align="center">
  <img src="assets/wechat-official-account.png" alt="微信搜一搜：正在逐渐AI化" width="720">
</p>

## 开源协议

MIT。见 [`LICENSE`](LICENSE)。

## 声明

这是 Sun Wuyuan / Alexsun1one 的原创开源 Skill 包。它不隶属于 OpenAI、GitHub、微信或任何被提及的平台。请不要用它去复制受保护 IP、仿冒在世艺术家，或暗示不存在的品牌背书。
