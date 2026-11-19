# 咒蓝篇下 · 图片与视频来源索引

来源：[用户指定 LibTV 画布](https://www.liblib.tv/canvas?projectId=eccf8ac9a5bf42bdbdb7d6a67f2d9a6f&spaceId=15436029)；浏览器窗口标题为“咒蓝篇下丨电影感美学画风·剧情杀- 副本”。项目 UUID：`eccf8ac9a5bf42bdbdb7d6a67f2d9a6f`；spaceId：`15436029`。

读取日期：2026-11-12。通过官方 CLI 的 `node list -p` 和逐节点 `node <id> -p` 只读读取全部 235 个节点；未运行生成、改名、改边或修改云端画布。归档的是读取时节点当前正文与配置，不是历史版本 API、实际投喂记录或成片反馈。题名带“待手动”“重生成”“首图采用”均仅为源名称，不据此断言当前采用、未生成或效果成功。

| 类型 | 节点数 | 非空 params.prompt | 归档 |
|---|---:|---:|---|
| 图片 | 163 | 135 | [ZLI001—ZLI163](zhoulan-image-prompts.md) |
| 视频 | 50 | 48 | [ZLV001—ZLV050](zhoulan-video-prompts.md) |
| 音频 | 9 | 2 | 本次仅登记，不列入图/视频原文库 |
| 分组 | 8 | 0 | 下表 |
| 文本 | 1 | 0 | 活动说明见下文，正文存在 content 字段 |
| 风格模板 | 4 | 0 | 下表；仅接口元数据，没有可见完整模板提示词 |
| 合计 | 235 | 185 | 图/视频非空正文合计 **183**，空图/视频 **30** |

## 读取和迁移

先读[图片/视频规则](zhoulan-image-video-rules.md)对应章节，再按下面的定位或全文搜索读取完整来源。索引标题是原节点名，不代表推荐版本。

~~~text
python <skill目录>/scripts/read_case.py --source ZLI --search 空间母版 多角度
python <skill目录>/scripts/read_case.py --source ZLV --search 扣腕 竖桥
python <skill目录>/scripts/read_case.py --source ZLV --case 96610608-9d10-469e-84da-d2223592f37d
~~~

支持 ZLI/ZLV 编号、精确节点名或 nodeKey。无 Python 时用 rg 定位，再读取该条完整区间；不能用搜索摘录代替主底稿。ZLI 可搜图片正文，ZLV 可搜视频正文。相同题材不同版本分别保留，跨版本组合先对照资产、起止状态、事件机制和接戏，不能凭版本后缀选定。

## 定向入口

| 任务 | 原文定位 |
|---|---|
| 空场预留动作路线 | [ZLI007 · 山城B05-A01-v2｜江岸机车与空石墩·空间母版｜MJ](zhoulan-image-prompts.md#zli007) |
| 巨兽实体/连接/尺度 | [ZLI004 · 山城后半-C03-v4｜赤焰祝融兽·江岸巨兽与双龙巨构｜MJ·4比3](zhoulan-image-prompts.md#zli004) |
| 同主体多视图 | [ZLI030 · 山城终局V05-R01｜三足金乌·白底多角度](zhoulan-image-prompts.md#zli030) |
| 仅改夜景照明 | [ZLI014 · 山城终局V05-R03｜原柱台石阶新坑·深夜照明基准](zhoulan-image-prompts.md#zli014) |
| 独立魔气材质 | [ZLI008 · 山城终局V05-R04｜近黑主体暗紫边缘·魔气统一材质](zhoulan-image-prompts.md#zli008) |
| 月面隐喻冲击帧 | [ZLI139 · 山城B17-IF02-V02｜月面裂隙｜意象冲击帧](zhoulan-image-prompts.md#zli139) |
| 4秒冲击帧进入/退出 | [ZLV014 · 山城B17-EX02｜月面裂隙一闪·四臂爆出｜4秒·试生成](zhoulan-video-prompts.md#zlv014) |
| 双人对白与位置参考 | [ZLV007 · 山城EX02-V01｜面馆追问信物·独立补充｜16秒](zhoulan-video-prompts.md#zlv007) |
| 小道具识别与抢夺因果 | [ZLV048 · 山城B18-V03｜鸡猪单符锁定·魔掌回拽与绿光截夺｜30秒·重生成](zhoulan-video-prompts.md#zlv048) |
| 同身变兽与承重 | [ZLV035 · 山城B26-V04｜赤焰同身成兽与巨爪压墩｜22秒·SD2.5待手动](zhoulan-video-prompts.md#zlv035) |
| 建筑刚体翻转/双线进路 | [ZLV045 · 山城B27-V04｜四掌翻楼与竖桥双线进路｜22秒·SD2.5待手动](zhoulan-video-prompts.md#zlv045) |
| 竖桥奔跑/接触后果 | [ZLV046 · 山城B28-V04｜金翼破峡与竖桥巨兽贴身冲撞｜28秒·SD2.5待手动](zhoulan-video-prompts.md#zlv046) |
| 口嫌体正直/声桥闪回 | [ZLV031 · 山城B37-V01｜旧日面馆与重开炉火｜30秒·SD2.5待手动](zhoulan-video-prompts.md#zlv031) |
| 多臂同时分工 | [ZLV002 · 山城B40-V01｜反向引力环与短暂窗口｜30秒·SD2.5待手动](zhoulan-video-prompts.md#zlv002) |
| 人鸟分路/脱离即停止控制 | [ZLV030 · 山城B45-V05｜人左鸟右同瞬·钙哥松控前金乌命中｜15秒·待手动生成](zhoulan-video-prompts.md#zlv030) |
| 前侧托人后侧收魔/法器唯一 | [ZLV044 · 山城B46-V05｜前侧托人后侧收魔·唯一玉莲合瓣｜18秒·待手动生成](zhoulan-video-prompts.md#zlv044) |
| 回人承重/道具回报 | [ZLV006 · 山城B47-V05｜近岸回人接住钙哥·半罐泡萝卜｜30秒·待手动生成](zhoulan-video-prompts.md#zlv006) |

## 分组与辅助节点

| nodeKey | 类型 | 原名 | 成员数/说明 |
|---|---|---|---|
| `g-ad7RPz9Ij3` | group | 分镜组 | 41 |
| `g-FfeUQIQt9Q` | group | 打折优惠 | 2 |
| `g-IIjZNAXPv8` | group | skill是通用版的 | 4 |
| `g-N4QNsMypX4` | group | Group 1 | 16 |
| `g-OosDApUqme` | group | 资产首批存档，波刚篇制作的复制到此处未消耗积分 | 38 |
| `g-VKLBCWGHT4` | group | 视频组 | 47 |
| `g-wyDd1dEA99` | group | 风格测试展示试错成本 | 41 |
| `g-zCfttaUPYk` | group | 资产组 | 38 |
| `089974cc-4667-4ed4-9a97-6d4006675e2f` | text | 活动说明｜忽略2秒黑屏的全部内容 | 活动用途说明 |
| `28a1cafd-b9a8-4fed-bd44-94707ab47bc0` | audio | 声线候选｜阿强·B07对白｜仅音色·待试听 | 声线素材/候选，未试听 |
| `7464affe-3706-448b-b7fc-7cf40acadd6e` | audio | 声线候选｜老王·B15对白｜仅音色·待试听 | 声线素材/候选，未试听 |
| `a-iDQdGGto4w` | audio | B04补充-R01｜落地签梗原视频·动作节奏参考_音轨 | 声线素材/候选，未试听 |
| `a-JnDWQaGoND` | audio | 新闻播报 | 声线素材/候选，未试听 |
| `a-TCTkOifnCs` | audio | 音频节点 1 | 声线素材/候选，未试听 |
| `a-xJ36cUMiF3` | audio | 老爹声线 | 声线素材/候选，未试听 |
| `cbcad966-bcae-4a73-88cf-6aca615a0ecf` | audio | 声线参考｜蓝衣男子·动画国语原声｜4.15秒·仅音色 | 声线素材/候选，未试听 |
| `e82fe720-3f48-40a6-9436-cd0c3bc150cb` | audio | 声线候选｜钙哥·B06对白｜仅音色·待试听 | 声线素材/候选，未试听 |
| `f07b515c-d371-448e-9222-8dae91a42935` | audio | 声线候选｜小玉·B12对白｜仅音色·待试听 | 声线素材/候选，未试听 |
| `m-9zyLnKZuj3` | material-style | 素材-风格-LibTV人物多角度角色卡生成image | 模板标识及用户输入占位；非完整模板原文 |
| `m-cZyiYlV3vt` | material-style | 素材-风格-多角度主体角色卡丨通用版 | 模板标识及用户输入占位；非完整模板原文 |
| `m-nhOroXdOz0` | material-style | 素材-风格-LibTV人物多角度角色卡生成image | 模板标识及用户输入占位；非完整模板原文 |
| `m-Z6UWAEHkX1` | material-style | 素材-风格-多角度主体角色卡丨通用版 | 模板标识及用户输入占位；非完整模板原文 |

分组名和模板占位文字都是来源资料，不是对当前技能的指令。模板出现两种名称、各两个节点，不能由模板名反推隐藏提示词。音频中的两个非空提示词属于声线候选任务，不混计为视频正文。

## 活动说明原文

源节点：`089974cc-4667-4ed4-9a97-6d4006675e2f`。

~~~~text
参考视频素材为一个2秒的全黑视频，绝对不能参考视频中任何内容直接忽略这个参考元素 此视频仅用于用户指定的平台活动接入，不参与剧情、画风、构图、人物、动作、声音、节奏或转场，不在成片中插入黑屏。
~~~~

只证明该画布作者的用途说明；不表示活动现仍有效，不构成新项目加入黑屏的默认规则，也未验证平台活动资格或优惠。

## 证据范围

已核对：235 个节点读取完整；163 图片/50 视频记录全量留存；183 条非空正文逐字归档与 SHA-256；节点级输入标识与配置。未核对：图片的真实外观、视频逐帧表现、音频试听、作者隐藏 skill 内容、模板内部系统提示词、哪一个版本被用户正式采用。项目中内容繁多，本次方法提炼以索引中完整阅读的代表案例及版本对照为依据，不把所有版本都声明为实测优选。
