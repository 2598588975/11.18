---
name: film-acting
description: Write only the acting and performance block for a user-approved scene or shot from project files or uploaded materials when the router selects stage 07-acting.
---

# 表演阶段

读取 `references/source.md` 作为方法来源。

输入可以是项目角色、剧本和资产文件，也可以是用户本轮明确指定的场景、镜头、角色卡、资产参考或表演目标。允许直接进入 ACTING，不要求全流程前序齐全。只有 `00_project/reference-memory.md` 中已经确认、状态为“启用”、使用范围为“表演（07）”或“全流程（01-08）”的方法可以作为可选补充；没有适用参考时不得主动检索。

输出仅限：`04_performance/<场次ID>-acting-vNNN.md`。文件内只处理当前场次，输出表演目标、阻力、策略、节拍变化、潜台词和可执行行为。修改一场表演时只标记引用该场次与版本的镜头和提示词过期，不连带重做其他场次。

禁止：输出摄影机、光学镜头、完整 Seedance 提示词、图像提示词；不得未经用户授权重写剧本和角色圣经。发现上游问题时交回总控切换阶段。

完成后标记版本和“待人工确认”，更新 `00_project/artifact-registry.md` 的当前草稿并停止；用户确认后才登记为最新确认 ACTING 版本。

## 压力测试的表演交接

若输入含用户采纳的结构诊断，读取 [结构到表演的术语映射](../film-scene-audit/references/acting-handoff.md)。结构 Goal 是故事因果目标，表演目标是每个人此刻向特定搭档索取什么；结构 Tactic 是有限信息下的情节尝试，表演 tactics 是逐刻施压、安抚或拖延等行动。把观众重估人物的节点落实为可见节拍，不移植未确认修复。

源材料“写状态而非过程”主要用于通过反复转换才能抵达的目标状态，不能据此删除剧情必须看见的连续行为或道具变化；这些过程仍须按已定动作与时长呈现。
