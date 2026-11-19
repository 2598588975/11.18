# 洋子方法库 · 本机正文补全版

首次补充日期：2026-10-28。来源是用户本机已安装的洋子电影工作流适配版，不冒充未经修改的原厂V3完整发行包。

本次补入10个核心模块及其直接引用的3个支持模块，共235份文件。原C库91份目录、说明与模板保留；其中旧自动索引记录的是补全前状态。当前可用文件以本文及`local-supplement-manifest.json`为准。

## 读取方式

晓之意志仍是唯一入口。根据当前任务在下表选择一项，只读取对应的ENTRYPOINT和它点名的必要参考文件，不整库通读，也不从头重跑已完成阶段。

原独立技能的SKILL.md在本库保存为ENTRYPOINT.md，避免与本机独立洋子技能重复注册。正文保留；指向同批模块的相对SKILL.md链接相应改成ENTRYPOINT.md，变化逐文件记入清单。

| 模块 | 用途 | 入口 | 文件数 |
|---|---|---|---:|
| ai-film-router | 弹性总控与项目接管 | [正文入口](01-Codex完整工程版/skills/ai-film-router/ENTRYPOINT.md) | 18 |
| film-synopsis | 概念锚定 | [正文入口](01-Codex完整工程版/skills/film-synopsis/ENTRYPOINT.md) | 2 |
| film-characters | 角色圣经 | [正文入口](01-Codex完整工程版/skills/film-characters/ENTRYPOINT.md) | 2 |
| film-worldbuilding | 世界观 | [正文入口](01-Codex完整工程版/skills/film-worldbuilding/ENTRYPOINT.md) | 2 |
| film-treatment | 分场大纲 | [正文入口](01-Codex完整工程版/skills/film-treatment/ENTRYPOINT.md) | 2 |
| film-screenplay | 正式剧本 | [正文入口](01-Codex完整工程版/skills/film-screenplay/ENTRYPOINT.md) | 2 |
| film-lira-assets | 图像资产 | [正文入口](01-Codex完整工程版/skills/film-lira-assets/ENTRYPOINT.md) | 3 |
| film-acting | 表演 | [正文入口](01-Codex完整工程版/skills/film-acting/ENTRYPOINT.md) | 2 |
| film-cinedance | 镜头规划与视频提示词 | [正文入口](01-Codex完整工程版/skills/film-cinedance/ENTRYPOINT.md) | 9 |
| film-knowledge-bridge | 可选本地知识桥 | [正文入口](01-Codex完整工程版/skills/film-knowledge-bridge/ENTRYPOINT.md) | 12 |
| film-expert-bridge | 可选专家资料桥 | [正文入口](01-Codex完整工程版/skills/film-expert-bridge/ENTRYPOINT.md) | 173 |
| film-scene-audit | 剧本压力测试 | [正文入口](01-Codex完整工程版/skills/film-scene-audit/ENTRYPOINT.md) | 4 |
| film-staging | 走位与空间规划 | [正文入口](01-Codex完整工程版/skills/film-staging/ENTRYPOINT.md) | 6 |

2026-11-04 增补 · 现合计 236 份本机方法文件。P3/08 情绪选镜及旧提示词诊断见[情绪选镜与改稿四查](01-Codex完整工程版/skills/film-cinedance/references/camera-emotion.md)。本次按飞书可读正文适配，网盘文件名标 v1.3，未核验压缩包正文。

2026-11-11 增补 · 现合计 237 份本机方法文件。同步[五项视觉前缀](01-Codex完整工程版/skills/film-cinedance/references/global-visual-prefix.md)、08入口、2.5模板与总控路由，重点补齐可执行光影色彩；规则按项目适配，不固定为古风暖调。

## 原先缺失的核心参考正文

- [Seedance 2.0适配原文](01-Codex完整工程版/skills/film-cinedance/references/source.md)
- [跨镜连续性编译](01-Codex完整工程版/skills/film-cinedance/references/continuity-compiler.md)
- [H3格式适配](01-Codex完整工程版/skills/film-cinedance/references/h3-prompt-format.md)
- [镜头规划与时长](01-Codex完整工程版/skills/film-cinedance/references/shot-planning.md)
- [Seedance 2.5适配](01-Codex完整工程版/skills/film-cinedance/references/seedance-25-prompt-format.md)
- [图像连续性质检](01-Codex完整工程版/skills/film-cinedance/references/visual-continuity-audit.md)

## 与晓之意志及项目文件的关系

1. 用户本轮明确要求、已经给出的授权和最新确认项目文件优先。补充库只补方法，不覆盖项目剧情、台词、参数、导演方案或既有目录；不反复询问已有答案。
2. 总体路由继续采用晓之意志。C库负责具体电影阶段的执行细则；A/B/D库按当前缺口补充。普通文字分镜修订可以只做当前阶段，不因图像或模型参数尚未选择而强迫重跑立项。
3. 本库不是另一个项目总控开关。仅按任务使用指定模块；维护技能时不弹创作菜单。专家增强只在用户点名或选择后读取正文；复制文件不等于启用专家增强或检索知识库。
4. `references/09E`保留了上游旧项目的示例路径、模型锁和世界观口径。它们不作为本项目默认值；本机正文读取路径以本文为准。
5. 私人`knowledge-base.json`、缓存和agents界面配置未复制。知识桥工具已随方法正文保留，但配置和实际数据库仍须在用户明确启用时单独定位；本次未读取剧本数据库、未执行索引维护或知识库配置。
6. 原C库的02通用版、课程安装器及旧工程模板保留原状，本次没有声称补齐该发行包的全部适配器。新增的是本机Codex方法正文；课程安装器不用于安装ENTRYPOINT快照。
7. 专家资料中的旧包名称、历史SKILL路径和平台说明可能是引用或示例；当前专家执行入口是film-expert-bridge及其modules，不把历史引用自动变成新的安装依赖。
8. 本地方法文件的模型规格是该适配版的记录，具体生产仍按用户目标平台和当前实际能力核对。脚本复制不代表已执行或已经配置运行环境。

## 来源与回退

源文件目录：`C:/Users/codex/.codex/skills/`下上述13个独立模块。首次补全从这 13 个模块取源；后续增补同步更新受影响的独立模块与本库快照。

`local-supplement-manifest.json`记录每个源文件与补入文件的SHA256，以及仅为ENTRYPOINT改名所需的相对引用修改数。补全前完整备份另存于本次交付目录。补入文件不含任何当前影片的剧情或制作资产。
