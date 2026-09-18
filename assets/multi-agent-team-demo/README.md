# 多 Agent 团队 Demo（角色库 + 引擎）

基于 **通用角色库** + **轻量多智能体引擎** 的可运行多 Agent 团队示例。
核心特点：**团队组成完全可配置**，项目需要哪些 Agent 就列哪些，不限于 3 个角色。

## 目录
- `team_config.py` —— **你只改这一个文件**：在 `TEAM` 里增删 Agent（role / goal / backstory）；`ENGINE` 选择引擎。
- `build_team.py` —— 读取配置，按所选引擎组建团队并运行（引擎可插拔）。
- `engines/` —— **引擎插件层**：统一接口 `BaseEngine` + `lightweight`（默认）与 `mock`（零依赖）两个适配器，可自由扩展。
- `requirements.txt` —— 默认引擎依赖（轻量多智能体引擎所需的库 + python-dotenv）；用 mock 引擎可不装。
- `.env.example` —— 密钥模板（复制为 `.env` 后填值）。

## 快速开始
```bash
# 1) 安装依赖（已自动装进 .venv 则跳过）
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt

# 2) 配置密钥
copy .env.example .env      # 然后编辑 .env 填入 API Key

# 3) 先预览团队（不花一分钱、不调用模型，且不依赖任何引擎）
.venv\Scripts\python build_team.py --dry-run

# 4) 真实运行
.venv\Scripts\python build_team.py --topic "你的具体主题"
```

## 引擎可插拔（可选）
团队"用哪套引擎真正跑起来"是可替换的，主流程不写死任何框架：
- `team_config.py` 里的 `ENGINE`（或环境变量 `TEAM_ENGINE`、或命令行 `--engine`）决定用哪套。
- 已内置两套适配器：`lightweight`（默认，需装依赖+配密钥）与 `mock`（零依赖，只演示不调模型）。
- 想接别的多智能体框架：在 `engines/` 里照 `BaseEngine` 写一个新适配器类，到 `engines/factory.py` 的字典里登记即可，业务代码一行都不用改。

```bash
# 不装任何依赖也能零依赖演示
.venv\Scripts\python build_team.py --engine mock --topic "你的主题"
```

## 如何扩展团队（重点）
`team_config.py` 里的 `TEAM` 是一个列表，**每个字典 = 一个 Agent**：
- 想加"产品经理"：复制一个字典改 `role/goal/backstory`。
- 想加"安全专家""技术作家"：同理，文件里已留了示例注释。
- 角色人设可直接从通用角色库搬：
  `ai-agent-frameworks/通用角色库/<部门>/<角色>.md`
  （例如 `engineering/engineering-code-reviewer.md` 的 frontmatter 可直接用作 backstory）。

运行时会按列表**顺序**让各 Agent 接力完成各自职责，最后汇总产出。

## 安全须知
- **密钥只在 `.env` 中**，绝不要写进代码或提交到仓库。
- 本 demo 默认在**本机**让 LLM 生成内容（不执行代码），相对安全；若后续接入会跑代码的 Agent，请用沙箱。
- 输入会发往你配置的 LLM 服务商，**不要喂入密钥或隐私数据**。
- 费用：每次真实运行都会消耗 token，请用便宜的入门模型先试。

## 与 多智能体团队搭建 的关系
本 demo 是「多智能体团队搭建」技能落地时的**标准脚手架**：触发「多Agent」/「多Agent团队」/
「帮我新建一个多Agent团队」后，技能会据此模板，结合你的真实项目，从通用角色库
挑选/组合角色，生成可运行的团队。
