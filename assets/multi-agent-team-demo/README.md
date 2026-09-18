# 多 Agent 团队 Demo（统一角色池 + 可插拔引擎）

基于 **统一角色池**（四库合并去重，335 个唯一角色 / 23 个领域）+ **轻量多智能体引擎** 的可运行多 Agent 团队示例。
核心特点：**按领域小组组织、团队组成完全可配置**——每个领域至少 2 名专家，项目需要哪些 Agent 就列哪些。

## 目录
- `team_config.py` —— **你只改这一个文件**：在 `TEAM` 里增删 Agent（`domain` / `source` / `role` / `goal` / `backstory`）；`ENGINE` 选择引擎。每条须带 `domain`（领域）与 `source`（角色池 slug），且**每领域至少 2 人**。
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
`team_config.py` 里的 `TEAM` 是一个列表，**每个字典 = 一个 Agent**，必须带 `domain` + `source`：
- 想加"产品经理"：复制一个字典，填 `domain`（如 `product`）、`source`（池内 slug，或库外新建用 `new:<自定 slug>`）、`role/goal/backstory`。
- **每个领域至少 2 人**组成领域小组；不足 2 人时从相近领域（如 `academic` / `specialized`）补齐。
- 角色人设从**统一角色池**取：`references/统一角色池.md`，按 `<领域>/<slug>`（例如 `engineering/engineering-code-reviewer`）。
- 讨论阶段（小组讨论 / 团队讨论）从**不去重**的全量清单招募：`references/agent-全量清单.md`（608 条）。

运行时会先打印**领域小组**分组与人数校验（不足会告警），再按列表顺序让各 Agent 接力完成职责。

## 安全须知
- **密钥只在 `.env` 中**，绝不要写进代码或提交到仓库。
- 本 demo 默认在**本机**让 LLM 生成内容（不执行代码），相对安全；若后续接入会跑代码的 Agent，请用沙箱。
- 输入会发往你配置的 LLM 服务商，**不要喂入密钥或隐私数据**。
- 费用：每次真实运行都会消耗 token，请用便宜的入门模型先试。

## 与 多智能体团队搭建 的关系
本 demo 是「多智能体团队搭建」技能落地时的**标准脚手架**：触发「多Agent」/「多Agent团队」/
「帮我新建一个多Agent团队」后，技能会据此模板，结合你的真实项目，从统一角色池
挑选/组合角色（按领域组成 ≥2 人的小组），先跑 `--dry-run` 校验，再真实运行。
