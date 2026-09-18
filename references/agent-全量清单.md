# Agent 全量清单（四库完整登记 - 不去重）

> 用途：**小组讨论环节的成员池**。小组讨论需要比较不同 agent 的思路，
> 因此本清单**刻意不去重、不合并、不省略**：跨库重复或同库多次出现的条目一律逐条保留，并标注所属库、路径与职责。
>
> 与 `统一角色池.md` 的关系：角色池是「去重后的**组队**视图」；本清单是「不去重的**讨论**视图」。
> 组队用角色池（避免重复占位），讨论用本清单（保留不同视角）。
>
> **文件在哪**：四库内容已发布为独立仓库 **`https://github.com/zhangruilin158/agent-role-libraries`**。
> 本清单的「所属库」对应仓库目录：通用角色库→`general-role-library/`、中文角色库→`chinese-role-library/`、
> 工程专家人设库→`engineering-personas/`、评审专家人设库→`review-personas/`（4 个 agent）与 `workflow-skills/`（25 个工作流技能）。
> 表内「文件路径」为**库内相对路径**，前面拼上对应目录即为仓库内路径（例：`general-role-library/engineering/engineering-code-reviewer.md`）。
> 原始许可与版权声明在仓库 `LICENSES/`。

## 一、统计

| 所属库 | 登记条目 | 其中 agent | 其中工作流技能 |
|--------|----------|-----------|----------------|
| 通用角色库（英文总库） | 280 | 280 | 0 |
| 中文角色库 | 278 | 278 | 0 |
| 工程专家人设库 | 21 | 21 | 0 |
| 评审专家人设库 | 29 | 4 | 25 |
| **合计** | **608** | **583** | **25** |

- 登记总数：**608** 条（agent 583 条 + 工作流技能 25 条）
- 重复出现（同一相对路径出现在多个库）的条目：**454** 条，涉及 **227** 个路径
- 识别口径：含 YAML frontmatter 且同时具备 `name:` 与 `description:` 即登记；遍历仓库**全部目录**（含子目录，不限于顶层角色目录）。
- 重复判定：以**库内相对路径**为键（同一角色在两库路径一致），避免同名文件误判。
- 说明：`评审专家人设库/skills/` 下的 25 条是**工作流技能**（非 agent），已按用户要求一并登记，在仓库中对应 `workflow-skills/`；`agents/` 下 4 条才是该库的 agent，对应 `review-personas/`。

## 二、重复出现索引

| 相对路径 | 出现次数 | 出现于 |
|----------|----------|--------|
| `academic/academic-anthropologist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `academic/academic-geographer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `academic/academic-historian.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `academic/academic-narratologist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `academic/academic-psychologist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `design/design-brand-guardian.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `design/design-image-prompt-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `design/design-inclusive-visuals-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `design/design-persona-walkthrough.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `design/design-ui-designer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `design/design-ux-architect.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `design/design-ux-researcher.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `design/design-visual-storyteller.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `design/design-whimsy-injector.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-ai-data-remediation-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-ai-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-autonomous-optimization-architect.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-backend-architect.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-cms-developer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-code-reviewer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-codebase-onboarding-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-data-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-database-optimizer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-devops-automator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-drupal-shopping-cart.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-email-intelligence-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-embedded-firmware-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-feishu-integration-developer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-filament-optimization-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-frontend-developer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-git-workflow-master.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-incident-response-commander.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-it-service-manager.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-minimal-change-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-mobile-app-builder.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-multi-agent-systems-architect.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-orgscript-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-prompt-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-rapid-prototyper.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-senior-developer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-software-architect.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-solidity-smart-contract-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-sre.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-technical-writer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-voice-ai-integration-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-wechat-mini-program-developer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `engineering/engineering-wordpress-shopping-cart.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `finance/finance-bookkeeper-controller.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `finance/finance-financial-analyst.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `finance/finance-fpa-analyst.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `finance/finance-investment-researcher.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `finance/finance-tax-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/blender/blender-addon-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/game-audio-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/game-designer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/godot/godot-gameplay-scripter.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/godot/godot-multiplayer-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/godot/godot-shader-developer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/level-designer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/narrative-designer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/roblox-studio/roblox-avatar-creator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/roblox-studio/roblox-experience-designer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/roblox-studio/roblox-systems-scripter.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/technical-artist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/unity/unity-architect.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/unity/unity-editor-tool-developer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/unity/unity-multiplayer-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/unity/unity-shader-graph-artist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/unreal-engine/unreal-multiplayer-architect.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/unreal-engine/unreal-systems-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/unreal-engine/unreal-technical-artist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `game-development/unreal-engine/unreal-world-builder.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `gis/gis-3d-scene-developer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `gis/gis-analyst.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `gis/gis-bim-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `gis/gis-cartography-designer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `gis/gis-drone-reality-mapping.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `gis/gis-geoai-ml-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `gis/gis-geoprocessing-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `gis/gis-qa-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `gis/gis-solution-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `gis/gis-spatial-data-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `gis/gis-spatial-data-scientist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `gis/gis-technical-consultant.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `gis/gis-web-gis-developer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `integrations/mcp-memory/backend-architect-with-memory.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-aeo-foundations.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-agentic-search-optimizer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-ai-citation-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-app-store-optimizer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-baidu-seo-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-book-co-author.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-carousel-growth-engine.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-china-ecommerce-operator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-china-market-localization-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-content-creator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-cross-border-ecommerce.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-douyin-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-email-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-global-podcast-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-growth-hacker.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-instagram-curator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-kuaishou-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-linkedin-content-creator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-livestream-commerce-coach.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-multi-platform-publisher.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-podcast-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-pr-communications-manager.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-private-domain-operator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-reddit-community-builder.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-seo-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-short-video-editing-coach.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-social-media-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-tiktok-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-twitter-engager.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-video-optimization-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-wechat-official-account.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-weibo-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-x-twitter-intelligence-analyst.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-xiaohongshu-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `marketing/marketing-zhihu-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `paid-media/paid-media-auditor.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `paid-media/paid-media-creative-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `paid-media/paid-media-paid-social-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `paid-media/paid-media-ppc-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `paid-media/paid-media-programmatic-buyer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `paid-media/paid-media-search-query-analyst.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `paid-media/paid-media-tracking-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `product/product-behavioral-nudge-engine.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `product/product-feedback-synthesizer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `product/product-manager.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `product/product-sprint-prioritizer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `product/product-trend-researcher.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `project-management/project-management-experiment-tracker.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `project-management/project-management-jira-workflow-steward.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `project-management/project-management-meeting-notes-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `project-management/project-management-project-shepherd.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `project-management/project-management-studio-operations.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `project-management/project-management-studio-producer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `project-management/project-manager-senior.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `sales/sales-account-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `sales/sales-coach.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `sales/sales-deal-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `sales/sales-discovery-coach.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `sales/sales-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `sales/sales-offer-lead-gen-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `sales/sales-outbound-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `sales/sales-pipeline-analyst.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `sales/sales-proposal-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `security/security-appsec-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `security/security-architect.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `security/security-blockchain-security-auditor.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `security/security-cloud-security-architect.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `security/security-compliance-auditor.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `security/security-incident-responder.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `security/security-penetration-tester.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `security/security-senior-secops.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `security/security-threat-detection-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `security/security-threat-intelligence-analyst.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `spatial-computing/macos-spatial-metal-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `spatial-computing/terminal-integration-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `spatial-computing/visionos-spatial-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `spatial-computing/xr-cockpit-interaction-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `spatial-computing/xr-immersive-developer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `spatial-computing/xr-interface-architect.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/accounts-payable-agent.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/agentic-identity-trust.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/agents-orchestrator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/automation-governance-architect.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/business-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/change-management-consultant.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/corporate-training-designer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/customer-success-manager.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/data-consolidation-agent.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/data-privacy-officer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/esg-sustainability-officer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/government-digital-presales-consultant.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/grant-writer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/healthcare-customer-service.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/healthcare-marketing-compliance.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/hospitality-guest-services.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/hr-onboarding.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/identity-graph-operator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/language-translator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/legal-billing-time-tracking.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/legal-client-intake.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/legal-document-review.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/loan-officer-assistant.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/lsp-index-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/ma-integration-manager.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/medical-billing-coding-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/operations-manager.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/organizational-psychologist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/personal-growth-mentor.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/real-estate-buyer-seller.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/recruitment-specialist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/report-distribution-agent.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/retail-customer-returns.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/sales-data-extraction-agent.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/specialized-civil-engineer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/specialized-cultural-intelligence-strategist.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/specialized-developer-advocate.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/specialized-document-generator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/specialized-french-consulting-market.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/specialized-korean-business-navigator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/specialized-mcp-builder.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/specialized-model-qa.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/specialized-pricing-analyst.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/specialized-salesforce-architect.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/specialized-strategy-duel-agent.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/specialized-workflow-architect.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/study-abroad-advisor.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `specialized/zk-steward.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `support/support-analytics-reporter.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `support/support-executive-summary-generator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `support/support-finance-tracker.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `support/support-infrastructure-maintainer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `support/support-legal-compliance-checker.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `support/support-support-responder.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `testing/testing-accessibility-auditor.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `testing/testing-api-tester.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `testing/testing-evidence-collector.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `testing/testing-performance-benchmarker.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `testing/testing-reality-checker.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `testing/testing-test-results-analyzer.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `testing/testing-tool-evaluator.md` | 2 | 中文角色库、通用角色库（英文总库） |
| `testing/testing-workflow-optimizer.md` | 2 | 中文角色库、通用角色库（英文总库） |

## 三、全量清单（逐条登记）

| # | 名称 | 类型 | 所属库 | 文件路径 | 核心职责 | 重复 | 重复来源 |
|---|------|------|--------|----------|----------|------|----------|
| 1 | Anthropologist | agent | 通用角色库（英文总库） | `academic/academic-anthropologist.md` | Cultural anthropologist specializing in social organization, belief systems, and... | 是 | 中文角色库 |
| 2 | Geographer | agent | 通用角色库（英文总库） | `academic/academic-geographer.md` | Physical and human geographer specializing in climate systems, geomorphology, re... | 是 | 中文角色库 |
| 3 | Historian | agent | 通用角色库（英文总库） | `academic/academic-historian.md` | Research historian with expertise across periods from antiquity to the modern er... | 是 | 中文角色库 |
| 4 | Narratologist | agent | 通用角色库（英文总库） | `academic/academic-narratologist.md` | Senior narrative theorist and story structure analyst | 是 | 中文角色库 |
| 5 | Psychologist | agent | 通用角色库（英文总库） | `academic/academic-psychologist.md` | Clinical and research psychologist specializing in personality, motivation, trau... | 是 | 中文角色库 |
| 6 | Statistician | agent | 通用角色库（英文总库） | `academic/academic-statistician.md` | Research methodologist and applied statistician specializing in study design, ca... | 否 | - |
| 7 | Brand Guardian | agent | 通用角色库（英文总库） | `design/design-brand-guardian.md` | Brand strategy and identity guardian specialist | 是 | 中文角色库 |
| 8 | Image Prompt Engineer | agent | 通用角色库（英文总库） | `design/design-image-prompt-engineer.md` | Photography prompt engineering specialist for AI image generation | 是 | 中文角色库 |
| 9 | Inclusive Visuals Specialist | agent | 通用角色库（英文总库） | `design/design-inclusive-visuals-specialist.md` | You are a rigorous prompt engineer specializing exclusively in authentic human r... | 是 | 中文角色库 |
| 10 | Persona Walkthrough Specialist | agent | 通用角色库（英文总库） | `design/design-persona-walkthrough.md` | Persona Walkthrough Specialist | 是 | 中文角色库 |
| 11 | UI Designer | agent | 通用角色库（英文总库） | `design/design-ui-designer.md` | Visual design systems and interface creation specialist | 是 | 中文角色库 |
| 12 | UI Finish-Gate Reviewer | agent | 通用角色库（英文总库） | `design/design-ui-finish-gate-reviewer.md` | Product-specific interface critic and pre-ship finish-gate owner | 否 | - |
| 13 | UX Architect | agent | 通用角色库（英文总库） | `design/design-ux-architect.md` | Technical architecture and UX foundation specialist | 是 | 中文角色库 |
| 14 | UX Researcher | agent | 通用角色库（英文总库） | `design/design-ux-researcher.md` | User behavior analysis and research methodology specialist | 是 | 中文角色库 |
| 15 | Visual Storyteller | agent | 通用角色库（英文总库） | `design/design-visual-storyteller.md` | Visual communication and storytelling specialist | 是 | 中文角色库 |
| 16 | Whimsy Injector | agent | 通用角色库（英文总库） | `design/design-whimsy-injector.md` | Brand personality and delightful interaction specialist | 是 | 中文角色库 |
| 17 | AI Data Remediation Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-ai-data-remediation-engineer.md` | AI Data Remediation Specialist | 是 | 中文角色库 |
| 18 | AI Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-ai-engineer.md` | AI/ML engineer and intelligent systems architect | 是 | 中文角色库 |
| 19 | API Platform Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-api-platform-engineer.md` | API platform and developer-experience engineer for public, partner, and internal... | 否 | - |
| 20 | ATS Validator Architect | agent | 通用角色库（英文总库） | `engineering/engineering-ats-validator-architect.md` | ATS compliance auditor, parser diagnostic specialist, information retrieval (IR)... | 否 | - |
| 21 | Autonomous Optimization Architect | agent | 通用角色库（英文总库） | `engineering/engineering-autonomous-optimization-architect.md` | You are the governor of self-improving software. Your mandate is to enable auton... | 是 | 中文角色库 |
| 22 | Backend Architect | agent | 通用角色库（英文总库） | `engineering/engineering-backend-architect.md` | System architecture and server-side development specialist | 是 | 中文角色库 |
| 23 | China Network Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-china-network-engineer.md` | Network engineering specialist for Huawei, H3C, Ruijie, and Hillstone environmen... | 否 | - |
| 24 | CMS Developer | agent | 通用角色库（英文总库） | `engineering/engineering-cms-developer.md` | 🧱 CMS Developer | 是 | 中文角色库 |
| 25 | Code Reviewer | agent | 通用角色库（英文总库） | `engineering/engineering-code-reviewer.md` | Code review and quality assurance specialist | 是 | 中文角色库 |
| 26 | Codebase Onboarding Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-codebase-onboarding-engineer.md` | Repository exploration, execution tracing, and developer onboarding specialist | 是 | 中文角色库 |
| 27 | Data Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-data-engineer.md` | Data pipeline architect and data platform engineer | 是 | 中文角色库 |
| 28 | Data Visualization Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-data-visualization-engineer.md` | Data visualization and charting specialist — encoding design, perceptual accurac... | 否 | - |
| 29 | Database Optimizer | agent | 通用角色库（英文总库） | `engineering/engineering-database-optimizer.md` | 🗄️ Database Optimizer | 是 | 中文角色库 |
| 30 | Database Reliability Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-database-reliability-engineer.md` | Database reliability and operations specialist — availability, durability, repli... | 否 | - |
| 31 | Desktop App Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-desktop-app-engineer.md` | Electron and Tauri application specialist covering architecture, security, packa... | 否 | - |
| 32 | Developer Tooling Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-developer-tooling-engineer.md` | Developer-experience and command-line tooling specialist — CLIs, internal dev pl... | 否 | - |
| 33 | DevOps Automator | agent | 通用角色库（英文总库） | `engineering/engineering-devops-automator.md` | Infrastructure automation and deployment pipeline specialist | 是 | 中文角色库 |
| 34 | Drupal Performance Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-drupal-performance.md` | ⚡ Drupal Performance Engineer | 否 | - |
| 35 | Drupal Shopping Cart Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-drupal-shopping-cart.md` | 🛒 Drupal Shopping Cart Engineer | 是 | 中文角色库 |
| 36 | Email Intelligence Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-email-intelligence-engineer.md` | Email data pipeline architect and context engineering specialist | 是 | 中文角色库 |
| 37 | Embedded Firmware Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-embedded-firmware-engineer.md` | Design and implement production-grade firmware for resource-constrained embedded... | 是 | 中文角色库 |
| 38 | Feishu Integration Developer | agent | 通用角色库（英文总库） | `engineering/engineering-feishu-integration-developer.md` | Full-stack integration engineer for the Feishu Open Platform | 是 | 中文角色库 |
| 39 | Filament Optimization Specialist | agent | 通用角色库（英文总库） | `engineering/engineering-filament-optimization-specialist.md` | Structurally redesign Filament resources, forms, tables, and navigation for maxi... | 是 | 中文角色库 |
| 40 | FinOps Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-finops-engineer.md` | Cloud financial-operations engineer bridging engineering, finance, and product a... | 否 | - |
| 41 | Frontend Developer | agent | 通用角色库（英文总库） | `engineering/engineering-frontend-developer.md` | Modern web application and UI implementation specialist | 是 | 中文角色库 |
| 42 | GaussDB Expert Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-gaussdb-expert.md` | 🗄️ GaussDB OLTP Expert | 否 | - |
| 43 | Git Workflow Master | agent | 通用角色库（英文总库） | `engineering/engineering-git-workflow-master.md` | Git workflow and version control specialist | 是 | 中文角色库 |
| 44 | Internationalization Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-i18n-engineer.md` | Internationalization and localization-engineering specialist for web, mobile, an... | 否 | - |
| 45 | Identity & Access Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-identity-access-engineer.md` | Authentication, SSO, and authorization systems specialist across consumer login,... | 否 | - |
| 46 | Incident Response Commander | agent | 通用角色库（英文总库） | `engineering/engineering-incident-response-commander.md` | Production incident commander, post-mortem facilitator, and on-call process arch... | 是 | 中文角色库 |
| 47 | IoT Fleet Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-iot-fleet-engineer.md` | IoT and edge fleet operations specialist — provisioning, connectivity, OTA, and ... | 否 | - |
| 48 | IT Service Manager | agent | 通用角色库（英文总库） | `engineering/engineering-it-service-manager.md` | 🖧 IT Service Manager | 是 | 中文角色库 |
| 49 | Knowledge Graph Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-knowledge-graph-engineer.md` | Knowledge graph engineer — you structure information into interconnected entity-... | 否 | - |
| 50 | LLM Post-Training Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-llm-post-training-engineer.md` | Evidence-driven owner for post-training experiments and release gates. | 否 | - |
| 51 | Minimal Change Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-minimal-change-engineer.md` | Surgical implementation specialist whose value is measured in lines NOT written | 是 | 中文角色库 |
| 52 | Mobile App Builder | agent | 通用角色库（英文总库） | `engineering/engineering-mobile-app-builder.md` | Native and cross-platform mobile application specialist | 是 | 中文角色库 |
| 53 | Mobile Release Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-mobile-release-engineer.md` | Mobile release, code-signing, and store-distribution specialist for iOS and Andr... | 否 | - |
| 54 | Multi-Agent Systems Architect | agent | 通用角色库（英文总库） | `engineering/engineering-multi-agent-systems-architect.md` | Multi-agent systems architect specializing in topology selection, context archit... | 是 | 中文角色库 |
| 55 | Network Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-network-engineer.md` | Senior network engineer specializing in enterprise routing, switching, firewall ... | 否 | - |
| 56 | OrgScript Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-orgscript-engineer.md` | Core Developer and Architect for OrgScript & Process Modeling Specialist | 是 | 中文角色库 |
| 57 | Payments & Billing Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-payments-billing-engineer.md` | Payment systems and subscription billing specialist across Stripe, Adyen, Braint... | 否 | - |
| 58 | PDF Engine Architect | agent | 通用角色库（英文总库） | `engineering/engineering-pdf-engine-architect.md` | Deterministic PDF engine architect, Playwright browser context pool designer, do... | 否 | - |
| 59 | Platform Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-platform-engineer.md` | Internal developer platform engineer, IDP architect, DevEx multiplier | 否 | - |
| 60 | Privacy Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-privacy-engineer.md` | Privacy engineering specialist — implementing data protection, consent, and subj... | 否 | - |
| 61 | Prompt Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-prompt-engineer.md` | Prompt design and LLM behavior specialist | 是 | 中文角色库 |
| 62 | RAG Pipeline Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-rag-pipeline-engineer.md` | RAG architect and retrieval quality engineer | 否 | - |
| 63 | Rapid Prototyper | agent | 通用角色库（英文总库） | `engineering/engineering-rapid-prototyper.md` | Ultra-fast prototype and MVP development specialist | 是 | 中文角色库 |
| 64 | Realtime Collaboration Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-realtime-collaboration-engineer.md` | Realtime infrastructure and collaborative-state specialist for web and mobile ap... | 否 | - |
| 65 | Rust Refactoring Specialist | agent | 通用角色库（英文总库） | `engineering/engineering-rust-refactoring-specialist.md` | Repository-scale Rust refactoring specialist who joins compiler rigor with archi... | 否 | - |
| 66 | Search Relevance Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-search-relevance-engineer.md` | Search infrastructure and relevance-tuning specialist for Elasticsearch, OpenSea... | 否 | - |
| 67 | Section 508 Accessibility Specialist | agent | 通用角色库（英文总库） | `engineering/engineering-section-508-specialist.md` | ♿ Section 508 Accessibility Specialist | 否 | - |
| 68 | Senior Developer | agent | 通用角色库（英文总库） | `engineering/engineering-senior-developer.md` | Implement premium web experiences using Laravel/Livewire/FluxUI | 是 | 中文角色库 |
| 69 | Software Architect | agent | 通用角色库（英文总库） | `engineering/engineering-software-architect.md` | Software architecture and system design specialist | 是 | 中文角色库 |
| 70 | Solidity Smart Contract Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-solidity-smart-contract-engineer.md` | Senior Solidity developer and smart contract architect for EVM-compatible chains | 是 | 中文角色库 |
| 71 | SRE (Site Reliability Engineer) | agent | 通用角色库（英文总库） | `engineering/engineering-sre.md` | Site reliability engineering and production systems specialist | 是 | 中文角色库 |
| 72 | Technical Writer | agent | 通用角色库（英文总库） | `engineering/engineering-technical-writer.md` | Developer documentation architect and content engineer | 是 | 中文角色库 |
| 73 | Universal Document Compiler | agent | 通用角色库（英文总库） | `engineering/engineering-universal-document-compiler.md` | Principal Document AST Architect, Typographical Layout Inference Specialist, and... | 否 | - |
| 74 | USWDS Developer | agent | 通用角色库（英文总库） | `engineering/engineering-uswds-developer.md` | 🏛️ USWDS Developer | 否 | - |
| 75 | Video Streaming Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-video-streaming-engineer.md` | Video encoding, packaging, and adaptive-streaming delivery specialist | 否 | - |
| 76 | Voice AI Integration Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-voice-ai-integration-engineer.md` | Speech transcription architect and voice AI pipeline engineer | 是 | 中文角色库 |
| 77 | WebAssembly Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-webassembly-engineer.md` | WebAssembly and Wasm-runtime specialist across browser (Emscripten/wasm-bindgen)... | 否 | - |
| 78 | WeChat Mini Program Developer | agent | 通用角色库（英文总库） | `engineering/engineering-wechat-mini-program-developer.md` | WeChat Mini Program architecture, development, and ecosystem integration special... | 是 | 中文角色库 |
| 79 | WordPress Performance Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-wordpress-performance.md` | ⚡ WordPress Performance Engineer | 否 | - |
| 80 | WordPress Shopping Cart Engineer | agent | 通用角色库（英文总库） | `engineering/engineering-wordpress-shopping-cart.md` | 🛍️ WordPress Shopping Cart Engineer | 是 | 中文角色库 |
| 81 | Bookkeeper & Controller | agent | 通用角色库（英文总库） | `finance/finance-bookkeeper-controller.md` | 📒 Bookkeeper & Controller Agent | 是 | 中文角色库 |
| 82 | Financial Analyst | agent | 通用角色库（英文总库） | `finance/finance-financial-analyst.md` | 📊 Financial Analyst Agent | 是 | 中文角色库 |
| 83 | FP&A Analyst | agent | 通用角色库（英文总库） | `finance/finance-fpa-analyst.md` | 📈 FP&A Analyst Agent | 是 | 中文角色库 |
| 84 | Investment Researcher | agent | 通用角色库（英文总库） | `finance/finance-investment-researcher.md` | 🔍 Investment Researcher Agent | 是 | 中文角色库 |
| 85 | Tax Strategist | agent | 通用角色库（英文总库） | `finance/finance-tax-strategist.md` | 🏛️ Tax Strategist Agent | 是 | 中文角色库 |
| 86 | Economy Designer | agent | 通用角色库（英文总库） | `game-development/economy-designer.md` | Design, model, and tune in-game economies — currencies, resources, markets, prog... | 否 | - |
| 87 | Game Audio Engineer | agent | 通用角色库（英文总库） | `game-development/game-audio-engineer.md` | Design and implement interactive audio systems — SFX, music, voice, spatial audi... | 是 | 中文角色库 |
| 88 | Game Designer | agent | 通用角色库（英文总库） | `game-development/game-designer.md` | Design gameplay systems, mechanics, economies, and player progressions — then do... | 是 | 中文角色库 |
| 89 | Level Designer | agent | 通用角色库（英文总库） | `game-development/level-designer.md` | Design, document, and iterate on game levels with precise control over pacing, f... | 是 | 中文角色库 |
| 90 | Narrative Designer | agent | 通用角色库（英文总库） | `game-development/narrative-designer.md` | Design and implement narrative systems — dialogue, branching story, lore, enviro... | 是 | 中文角色库 |
| 91 | Technical Artist | agent | 通用角色库（英文总库） | `game-development/technical-artist.md` | Bridge art and engineering — build shaders, VFX, asset pipelines, and performanc... | 是 | 中文角色库 |
| 92 | Blender Add-on Engineer | agent | 通用角色库（英文总库） | `game-development/blender/blender-addon-engineer.md` | Build Blender-native tooling with Python and `bpy` — custom operators, panels, v... | 是 | 中文角色库 |
| 93 | Godot Gameplay Scripter | agent | 通用角色库（英文总库） | `game-development/godot/godot-gameplay-scripter.md` | Design and implement clean, type-safe gameplay systems in Godot 4 using GDScript... | 是 | 中文角色库 |
| 94 | Godot Multiplayer Engineer | agent | 通用角色库（英文总库） | `game-development/godot/godot-multiplayer-engineer.md` | Design and implement multiplayer systems in Godot 4 using MultiplayerAPI, Multip... | 是 | 中文角色库 |
| 95 | Godot Shader Developer | agent | 通用角色库（英文总库） | `game-development/godot/godot-shader-developer.md` | Author and optimize shaders for Godot 4 across 2D (CanvasItem) and 3D (Spatial) ... | 是 | 中文角色库 |
| 96 | Roblox Avatar Creator | agent | 通用角色库（英文总库） | `game-development/roblox-studio/roblox-avatar-creator.md` | Design, rig, and pipeline Roblox avatar items — accessories, clothing, bundle co... | 是 | 中文角色库 |
| 97 | Roblox Experience Designer | agent | 通用角色库（英文总库） | `game-development/roblox-studio/roblox-experience-designer.md` | Design and implement player-facing systems for Roblox experiences — progression,... | 是 | 中文角色库 |
| 98 | Roblox Systems Scripter | agent | 通用角色库（英文总库） | `game-development/roblox-studio/roblox-systems-scripter.md` | Design and implement core systems for Roblox experiences — game logic, client-se... | 是 | 中文角色库 |
| 99 | Unity Architect | agent | 通用角色库（英文总库） | `game-development/unity/unity-architect.md` | Architect scalable, data-driven Unity systems using ScriptableObjects and compos... | 是 | 中文角色库 |
| 100 | Unity Editor Tool Developer | agent | 通用角色库（英文总库） | `game-development/unity/unity-editor-tool-developer.md` | Build Unity Editor tools — windows, property drawers, asset processors, validato... | 是 | 中文角色库 |
| 101 | Unity Multiplayer Engineer | agent | 通用角色库（英文总库） | `game-development/unity/unity-multiplayer-engineer.md` | Design and implement Unity multiplayer systems using Netcode for GameObjects (NG... | 是 | 中文角色库 |
| 102 | Unity Shader Graph Artist | agent | 通用角色库（英文总库） | `game-development/unity/unity-shader-graph-artist.md` | Author, optimize, and maintain Unity's shader library using Shader Graph for art... | 是 | 中文角色库 |
| 103 | Unreal Multiplayer Architect | agent | 通用角色库（英文总库） | `game-development/unreal-engine/unreal-multiplayer-architect.md` | Design and implement UE5 multiplayer systems — actor replication, authority mode... | 是 | 中文角色库 |
| 104 | Unreal Systems Engineer | agent | 通用角色库（英文总库） | `game-development/unreal-engine/unreal-systems-engineer.md` | Design and implement high-performance, modular Unreal Engine 5 systems using C++... | 是 | 中文角色库 |
| 105 | Unreal Technical Artist | agent | 通用角色库（英文总库） | `game-development/unreal-engine/unreal-technical-artist.md` | Own UE5's visual pipeline — Material Editor, Niagara, PCG, LOD systems, and rend... | 是 | 中文角色库 |
| 106 | Unreal World Builder | agent | 通用角色库（英文总库） | `game-development/unreal-engine/unreal-world-builder.md` | Design and implement open-world environments using UE5 World Partition, Landscap... | 是 | 中文角色库 |
| 107 | 3D & Scene Developer | agent | 通用角色库（英文总库） | `gis/gis-3d-scene-developer.md` | 3D web visualization — scenes, terrain, point clouds, Cesium, ArcGIS Scene Viewe... | 是 | 中文角色库 |
| 108 | GIS Analyst | agent | 通用角色库（英文总库） | `gis/gis-analyst.md` | Day-to-day GIS operations — map creation, data management, spatial queries, laye... | 是 | 中文角色库 |
| 109 | BIM/GIS Specialist | agent | 通用角色库（英文总库） | `gis/gis-bim-specialist.md` | BIM-to-GIS integration — Revit/IFC data conversion, indoor mapping, digital twin... | 是 | 中文角色库 |
| 110 | Cartography Designer | agent | 通用角色库（英文总库） | `gis/gis-cartography-designer.md` | Map design and aesthetics — color theory, typography, label hierarchy, basemap s... | 是 | 中文角色库 |
| 111 | Drone/Reality Mapping Specialist | agent | 通用角色库（英文总库） | `gis/gis-drone-reality-mapping.md` | Drone-based reality capture — flight planning, photogrammetric processing, point... | 是 | 中文角色库 |
| 112 | GeoAI/ML Engineer | agent | 通用角色库（英文总库） | `gis/gis-geoai-ml-engineer.md` | Geospatial AI/ML model development — feature extraction, object detection, seman... | 是 | 中文角色库 |
| 113 | Geoprocessing Specialist | agent | 通用角色库（英文总库） | `gis/gis-geoprocessing-specialist.md` | Geoprocessing automation — Python Toolbox (.pyt), Model Builder, ArcPy scripting... | 是 | 中文角色库 |
| 114 | GIS QA Engineer | agent | 通用角色库（英文总库） | `gis/gis-qa-engineer.md` | GISQAEngineer Agent Personality | 是 | 中文角色库 |
| 115 | Solution Engineer | agent | 通用角色库（英文总库） | `gis/gis-solution-engineer.md` | Pre-sales and PoC engineer — build working demos, validate feasibility, estimate... | 是 | 中文角色库 |
| 116 | Spatial Data Engineer | agent | 通用角色库（英文总库） | `gis/gis-spatial-data-engineer.md` | Geospatial ETL specialist — data ingestion, cleaning, transformation, validation... | 是 | 中文角色库 |
| 117 | Spatial Data Scientist | agent | 通用角色库（英文总库） | `gis/gis-spatial-data-scientist.md` | Advanced spatial statistics and predictive modeling — spatial clustering, regres... | 是 | 中文角色库 |
| 118 | Technical Consultant | agent | 通用角色库（英文总库） | `gis/gis-technical-consultant.md` | Strategic GIS advisor — gap analysis, technology selection, ROI modeling, digita... | 是 | 中文角色库 |
| 119 | Web GIS Developer | agent | 通用角色库（英文总库） | `gis/gis-web-gis-developer.md` | Web GIS application development — mapping libraries, REST APIs, dashboards, real... | 是 | 中文角色库 |
| 120 | Clinical Evidence Agent | agent | 通用角色库（英文总库） | `healthcare/healthcare-clinical-evidence-agent.md` | Clinical Evidence Agent | 否 | - |
| 121 | Healthcare Innovation Strategist | agent | 通用角色库（英文总库） | `healthcare/healthcare-innovation-strategist.md` | Healthcare Innovation Strategist | 否 | - |
| 122 | Sovereign Health Systems Agent | agent | 通用角色库（英文总库） | `healthcare/healthcare-sovereign-health-systems-agent.md` | Sovereign Health Systems Agent | 否 | - |
| 123 | Backend Architect | agent | 通用角色库（英文总库） | `integrations/mcp-memory/backend-architect-with-memory.md` | System architecture and server-side development specialist | 是 | 中文角色库 |
| 124 | AEO Foundations Architect | agent | 通用角色库（英文总库） | `marketing/marketing-aeo-foundations.md` | AEO Foundations Architect | 是 | 中文角色库 |
| 125 | Agentic Search Optimizer | agent | 通用角色库（英文总库） | `marketing/marketing-agentic-search-optimizer.md` | Agentic Search Optimizer | 是 | 中文角色库 |
| 126 | AI Citation Strategist | agent | 通用角色库（英文总库） | `marketing/marketing-ai-citation-strategist.md` | AI Citation Strategist | 是 | 中文角色库 |
| 127 | App Store Optimizer | agent | 通用角色库（英文总库） | `marketing/marketing-app-store-optimizer.md` | App Store Optimization and mobile marketing specialist | 是 | 中文角色库 |
| 128 | Baidu SEO Specialist | agent | 通用角色库（英文总库） | `marketing/marketing-baidu-seo-specialist.md` | Baidu search ecosystem optimization and China-market SEO specialist | 是 | 中文角色库 |
| 129 | Bilibili Content Strategist | agent | 通用角色库（英文总库） | `marketing/marketing-bilibili-content-strategist.md` | Bilibili platform content strategy and UP主 growth specialist | 否 | - |
| 130 | Book Co-Author | agent | 通用角色库（英文总库） | `marketing/marketing-book-co-author.md` | Strategic co-author, ghostwriter, and narrative architect for thought-leadership... | 是 | 中文角色库 |
| 131 | Carousel Growth Engine | agent | 通用角色库（英文总库） | `marketing/marketing-carousel-growth-engine.md` | Marketing Carousel Growth Engine | 是 | 中文角色库 |
| 132 | China E-Commerce Operator | agent | 通用角色库（英文总库） | `marketing/marketing-china-ecommerce-operator.md` | China e-commerce multi-platform operations and campaign strategy specialist | 是 | 中文角色库 |
| 133 | China Market Localization Strategist | agent | 通用角色库（英文总库） | `marketing/marketing-china-market-localization-strategist.md` | Full-stack China market localization and trend-to-action strategist | 是 | 中文角色库 |
| 134 | Content Creator | agent | 通用角色库（英文总库） | `marketing/marketing-content-creator.md` | Marketing Content Creator Agent | 是 | 中文角色库 |
| 135 | Cross-Border E-Commerce Specialist | agent | 通用角色库（英文总库） | `marketing/marketing-cross-border-ecommerce.md` | Cross-border e-commerce multi-platform operations and brand globalization strate... | 是 | 中文角色库 |
| 136 | Douyin Strategist | agent | 通用角色库（英文总库） | `marketing/marketing-douyin-strategist.md` | Douyin (China's TikTok) short-video marketing and livestream commerce strategy s... | 是 | 中文角色库 |
| 137 | Email Marketing Strategist | agent | 通用角色库（英文总库） | `marketing/marketing-email-strategist.md` | Expert email marketing strategist who bridges CRM data and ESP execution. You de... | 是 | 中文角色库 |
| 138 | Global Podcast Strategist | agent | 通用角色库（英文总库） | `marketing/marketing-global-podcast-strategist.md` | Marketing Global Podcast Strategist | 是 | 中文角色库 |
| 139 | Growth Hacker | agent | 通用角色库（英文总库） | `marketing/marketing-growth-hacker.md` | Marketing Growth Hacker Agent | 是 | 中文角色库 |
| 140 | Instagram Curator | agent | 通用角色库（英文总库） | `marketing/marketing-instagram-curator.md` | Marketing Instagram Curator | 是 | 中文角色库 |
| 141 | Kuaishou Strategist | agent | 通用角色库（英文总库） | `marketing/marketing-kuaishou-strategist.md` | Kuaishou platform strategy, live commerce, and grassroots community growth speci... | 是 | 中文角色库 |
| 142 | LinkedIn Content Creator | agent | 通用角色库（英文总库） | `marketing/marketing-linkedin-content-creator.md` | LinkedIn content strategist and personal brand architect specializing in thought... | 是 | 中文角色库 |
| 143 | Livestream Commerce Coach | agent | 通用角色库（英文总库） | `marketing/marketing-livestream-commerce-coach.md` | Livestream e-commerce host trainer and full-scope live room operations coach | 是 | 中文角色库 |
| 144 | Multi-Platform Publisher | agent | 通用角色库（英文总库） | `marketing/marketing-multi-platform-publisher.md` | A multi-platform publishing orchestrator specialized in Chinese content distribu... | 是 | 中文角色库 |
| 145 | Podcast Strategist | agent | 通用角色库（英文总库） | `marketing/marketing-podcast-strategist.md` | Chinese podcast content strategy and full-funnel operations specialist | 是 | 中文角色库 |
| 146 | PR & Communications Manager | agent | 通用角色库（英文总库） | `marketing/marketing-pr-communications-manager.md` | 📣 PR & Communications Manager | 是 | 中文角色库 |
| 147 | Private Domain Operator | agent | 通用角色库（英文总库） | `marketing/marketing-private-domain-operator.md` | Enterprise WeChat (WeCom) private domain operations and user lifecycle managemen... | 是 | 中文角色库 |
| 148 | Reddit Community Builder | agent | 通用角色库（英文总库） | `marketing/marketing-reddit-community-builder.md` | Marketing Reddit Community Builder | 是 | 中文角色库 |
| 149 | SEO Specialist | agent | 通用角色库（英文总库） | `marketing/marketing-seo-specialist.md` | Marketing SEO Specialist | 是 | 中文角色库 |
| 150 | Short-Video Editing Coach | agent | 通用角色库（英文总库） | `marketing/marketing-short-video-editing-coach.md` | Short-video editing technical coach and full post-production workflow specialist | 是 | 中文角色库 |
| 151 | Social Media Strategist | agent | 通用角色库（英文总库） | `marketing/marketing-social-media-strategist.md` | Social Media Strategist Agent | 是 | 中文角色库 |
| 152 | TikTok Strategist | agent | 通用角色库（英文总库） | `marketing/marketing-tiktok-strategist.md` | Marketing TikTok Strategist | 是 | 中文角色库 |
| 153 | Twitter Engager | agent | 通用角色库（英文总库） | `marketing/marketing-twitter-engager.md` | Marketing Twitter Engager | 是 | 中文角色库 |
| 154 | Video Optimization Specialist | agent | 通用角色库（英文总库） | `marketing/marketing-video-optimization-specialist.md` | Audience growth and retention optimization expert for video platforms | 是 | 中文角色库 |
| 155 | WeChat Official Account Manager | agent | 通用角色库（英文总库） | `marketing/marketing-wechat-official-account.md` | Marketing WeChat Official Account Manager | 是 | 中文角色库 |
| 156 | Weibo Strategist | agent | 通用角色库（英文总库） | `marketing/marketing-weibo-strategist.md` | Weibo (China's leading microblogging platform) full-spectrum operations and bran... | 是 | 中文角色库 |
| 157 | X/Twitter Intelligence Analyst | agent | 通用角色库（英文总库） | `marketing/marketing-x-twitter-intelligence-analyst.md` | Marketing X/Twitter Intelligence Analyst | 是 | 中文角色库 |
| 158 | Xiaohongshu Specialist | agent | 通用角色库（英文总库） | `marketing/marketing-xiaohongshu-specialist.md` | Marketing Xiaohongshu Specialist | 是 | 中文角色库 |
| 159 | Zhihu Strategist | agent | 通用角色库（英文总库） | `marketing/marketing-zhihu-strategist.md` | Marketing Zhihu Strategist | 是 | 中文角色库 |
| 160 | Paid Media Auditor | agent | 通用角色库（英文总库） | `paid-media/paid-media-auditor.md` | Paid Media Auditor Agent | 是 | 中文角色库 |
| 161 | Ad Creative Strategist | agent | 通用角色库（英文总库） | `paid-media/paid-media-creative-strategist.md` | Paid Media Ad Creative Strategist Agent | 是 | 中文角色库 |
| 162 | Paid Social Strategist | agent | 通用角色库（英文总库） | `paid-media/paid-media-paid-social-strategist.md` | Paid Media Paid Social Strategist Agent | 是 | 中文角色库 |
| 163 | PPC Campaign Strategist | agent | 通用角色库（英文总库） | `paid-media/paid-media-ppc-strategist.md` | Paid Media PPC Campaign Strategist Agent | 是 | 中文角色库 |
| 164 | Programmatic & Display Buyer | agent | 通用角色库（英文总库） | `paid-media/paid-media-programmatic-buyer.md` | Paid Media Programmatic & Display Buyer Agent | 是 | 中文角色库 |
| 165 | Search Query Analyst | agent | 通用角色库（英文总库） | `paid-media/paid-media-search-query-analyst.md` | Paid Media Search Query Analyst Agent | 是 | 中文角色库 |
| 166 | Tracking & Measurement Specialist | agent | 通用角色库（英文总库） | `paid-media/paid-media-tracking-specialist.md` | Paid Media Tracking & Measurement Specialist Agent | 是 | 中文角色库 |
| 167 | Behavioral Nudge Engine | agent | 通用角色库（英文总库） | `product/product-behavioral-nudge-engine.md` | You are a proactive coaching intelligence grounded in behavioral psychology and ... | 是 | 中文角色库 |
| 168 | Feedback Synthesizer | agent | 通用角色库（英文总库） | `product/product-feedback-synthesizer.md` | Product Feedback Synthesizer Agent | 是 | 中文角色库 |
| 169 | Product Manager | agent | 通用角色库（英文总库） | `product/product-manager.md` | 🧭 Product Manager Agent | 是 | 中文角色库 |
| 170 | Sprint Prioritizer | agent | 通用角色库（英文总库） | `product/product-sprint-prioritizer.md` | Product Sprint Prioritizer Agent | 是 | 中文角色库 |
| 171 | Trend Researcher | agent | 通用角色库（英文总库） | `product/product-trend-researcher.md` | Product Trend Researcher Agent | 是 | 中文角色库 |
| 172 | Experiment Tracker | agent | 通用角色库（英文总库） | `project-management/project-management-experiment-tracker.md` | Scientific experimentation and data-driven decision making specialist | 是 | 中文角色库 |
| 173 | Jira Workflow Steward | agent | 通用角色库（英文总库） | `project-management/project-management-jira-workflow-steward.md` | Delivery traceability lead, Git workflow governor, and Jira hygiene specialist | 是 | 中文角色库 |
| 174 | Meeting Notes Specialist | agent | 通用角色库（英文总库） | `project-management/project-management-meeting-notes-specialist.md` | Meeting Notes Specialist | 是 | 中文角色库 |
| 175 | Project Shepherd | agent | 通用角色库（英文总库） | `project-management/project-management-project-shepherd.md` | Cross-functional project orchestrator and stakeholder alignment specialist | 是 | 中文角色库 |
| 176 | Studio Operations | agent | 通用角色库（英文总库） | `project-management/project-management-studio-operations.md` | Operational excellence and process optimization specialist | 是 | 中文角色库 |
| 177 | Studio Producer | agent | 通用角色库（英文总库） | `project-management/project-management-studio-producer.md` | Executive creative strategist and portfolio orchestrator | 是 | 中文角色库 |
| 178 | Senior Project Manager | agent | 通用角色库（英文总库） | `project-management/project-manager-senior.md` | Convert specifications into structured task lists for development teams | 是 | 中文角色库 |
| 179 | Research Synthesist | agent | 通用角色库（英文总库） | `research/research-synthesist.md` | Literature reviewer and evidence synthesist specializing in systematic search, s... | 否 | - |
| 180 | Account Strategist | agent | 通用角色库（英文总库） | `sales/sales-account-strategist.md` | Post-sale expansion strategist and account development architect | 是 | 中文角色库 |
| 181 | Sales Coach | agent | 通用角色库（英文总库） | `sales/sales-coach.md` | Sales rep developer, pipeline review facilitator, deal strategist, forecast disc... | 是 | 中文角色库 |
| 182 | Deal Strategist | agent | 通用角色库（英文总库） | `sales/sales-deal-strategist.md` | Deal Strategist Agent | 是 | 中文角色库 |
| 183 | Discovery Coach | agent | 通用角色库（英文总库） | `sales/sales-discovery-coach.md` | Discovery methodology coach and call structure architect | 是 | 中文角色库 |
| 184 | Sales Engineer | agent | 通用角色库（英文总库） | `sales/sales-engineer.md` | Sales Engineer Agent | 是 | 中文角色库 |
| 185 | Offer & Lead Gen Strategist | agent | 通用角色库（英文总库） | `sales/sales-offer-lead-gen-strategist.md` | Top-of-funnel strategist — offer architect, lead magnet designer, channel planne... | 是 | 中文角色库 |
| 186 | Outbound Strategist | agent | 通用角色库（英文总库） | `sales/sales-outbound-strategist.md` | Signal-based outbound strategist and sequence architect | 是 | 中文角色库 |
| 187 | Pipeline Analyst | agent | 通用角色库（英文总库） | `sales/sales-pipeline-analyst.md` | Pipeline health diagnostician and revenue forecasting analyst | 是 | 中文角色库 |
| 188 | Proposal Strategist | agent | 通用角色库（英文总库） | `sales/sales-proposal-strategist.md` | Proposal strategist and win theme architect | 是 | 中文角色库 |
| 189 | AI-Generated Code Security Auditor | agent | 通用角色库（英文总库） | `security/security-ai-generated-code-auditor.md` | Application security reviewer specializing in AI-generated and AI-assisted code ... | 否 | - |
| 190 | Application Security Engineer | agent | 通用角色库（英文总库） | `security/security-appsec-engineer.md` | Senior application security engineer specializing in secure SDLC, threat modelin... | 是 | 中文角色库 |
| 191 | Security Architect | agent | 通用角色库（英文总库） | `security/security-architect.md` | Security architect, threat-modeling lead, and adversarial systems thinker | 是 | 中文角色库 |
| 192 | Blockchain Security Auditor | agent | 通用角色库（英文总库） | `security/security-blockchain-security-auditor.md` | Senior smart contract security auditor and vulnerability researcher | 是 | 中文角色库 |
| 193 | Cloud Security Architect | agent | 通用角色库（英文总库） | `security/security-cloud-security-architect.md` | Senior cloud security architect specializing in multi-cloud security design, ide... | 是 | 中文角色库 |
| 194 | Compliance Auditor | agent | 通用角色库（英文总库） | `security/security-compliance-auditor.md` | Technical compliance auditor and controls assessor | 是 | 中文角色库 |
| 195 | Incident Responder | agent | 通用角色库（英文总库） | `security/security-incident-responder.md` | Senior incident responder and digital forensics analyst specializing in breach i... | 是 | 中文角色库 |
| 196 | Penetration Tester | agent | 通用角色库（英文总库） | `security/security-penetration-tester.md` | Senior penetration tester and red team operator specializing in network, web app... | 是 | 中文角色库 |
| 197 | Secrets & Credential Hygiene Engineer | agent | 通用角色库（英文总库） | `security/security-secrets-credential-engineer.md` | Secrets and credential lifecycle engineer — detection and prevention, vaulting a... | 否 | - |
| 198 | Senior SecOps Engineer | agent | 通用角色库（英文总库） | `security/security-senior-secops.md` | Defensive application security engineer and guardian of the organization's Secur... | 是 | 中文角色库 |
| 199 | Threat Detection Engineer | agent | 通用角色库（英文总库） | `security/security-threat-detection-engineer.md` | Detection engineer, threat hunter, and security operations specialist | 是 | 中文角色库 |
| 200 | Threat Intelligence Analyst | agent | 通用角色库（英文总库） | `security/security-threat-intelligence-analyst.md` | Senior cyber threat intelligence analyst specializing in adversary tracking, cam... | 是 | 中文角色库 |
| 201 | macOS Spatial/Metal Engineer | agent | 通用角色库（英文总库） | `spatial-computing/macos-spatial-metal-engineer.md` | Swift + Metal rendering specialist with visionOS spatial computing expertise | 是 | 中文角色库 |
| 202 | Terminal Integration Specialist | agent | 通用角色库（英文总库） | `spatial-computing/terminal-integration-specialist.md` | Terminal Integration Specialist | 是 | 中文角色库 |
| 203 | visionOS Spatial Engineer | agent | 通用角色库（英文总库） | `spatial-computing/visionos-spatial-engineer.md` | visionOS Spatial Engineer | 是 | 中文角色库 |
| 204 | XR Cockpit Interaction Specialist | agent | 通用角色库（英文总库） | `spatial-computing/xr-cockpit-interaction-specialist.md` | Spatial cockpit design expert for XR simulation and vehicular interfaces | 是 | 中文角色库 |
| 205 | XR Immersive Developer | agent | 通用角色库（英文总库） | `spatial-computing/xr-immersive-developer.md` | Full-stack WebXR engineer with experience in A-Frame, Three.js, Babylon.js, and ... | 是 | 中文角色库 |
| 206 | XR Interface Architect | agent | 通用角色库（英文总库） | `spatial-computing/xr-interface-architect.md` | Spatial UI/UX designer for AR/VR/XR interfaces | 是 | 中文角色库 |
| 207 | Accounts Payable Agent | agent | 通用角色库（英文总库） | `specialized/accounts-payable-agent.md` | Payment processing, accounts payable, financial operations | 是 | 中文角色库 |
| 208 | Agentic Identity & Trust Architect | agent | 通用角色库（英文总库） | `specialized/agentic-identity-trust.md` | Identity systems architect for autonomous AI agents | 是 | 中文角色库 |
| 209 | Agents Orchestrator | agent | 通用角色库（英文总库） | `specialized/agents-orchestrator.md` | Autonomous workflow pipeline manager and quality orchestrator | 是 | 中文角色库 |
| 210 | Automation Governance Architect | agent | 通用角色库（英文总库） | `specialized/automation-governance-architect.md` | Automation Governance Architect | 是 | 中文角色库 |
| 211 | Business Strategist | agent | 通用角色库（英文总库） | `specialized/business-strategist.md` | ♟️ Business Strategist | 是 | 中文角色库 |
| 212 | Change Management Consultant | agent | 通用角色库（英文总库） | `specialized/change-management-consultant.md` | 🔄 Change Management Consultant | 是 | 中文角色库 |
| 213 | Chief Financial Officer | agent | 通用角色库（英文总库） | `specialized/chief-financial-officer.md` | Strategic finance executive governing financial planning and analysis, treasury ... | 否 | - |
| 214 | Corporate Training Designer | agent | 通用角色库（英文总库） | `specialized/corporate-training-designer.md` | Enterprise training system architect and curriculum development expert | 是 | 中文角色库 |
| 215 | Customer Service | agent | 通用角色库（英文总库） | `specialized/customer-service.md` | 🎧 Customer Service Agent | 否 | - |
| 216 | Customer Success Manager | agent | 通用角色库（英文总库） | `specialized/customer-success-manager.md` | 🌟 Customer Success Manager | 是 | 中文角色库 |
| 217 | Data Consolidation Agent | agent | 通用角色库（英文总库） | `specialized/data-consolidation-agent.md` | Data Consolidation Agent | 是 | 中文角色库 |
| 218 | Data Privacy Officer | agent | 通用角色库（英文总库） | `specialized/data-privacy-officer.md` | Corporate Data Protection Officer specializing in privacy program governance, da... | 是 | 中文角色库 |
| 219 | ESG & Sustainability Officer | agent | 通用角色库（英文总库） | `specialized/esg-sustainability-officer.md` | Corporate sustainability strategist and ESG disclosure specialist focused on mat... | 是 | 中文角色库 |
| 220 | Government Digital Presales Consultant | agent | 通用角色库（英文总库） | `specialized/government-digital-presales-consultant.md` | Full-lifecycle presales expert for ToG (government) projects, combining technica... | 是 | 中文角色库 |
| 221 | Grant Writer | agent | 通用角色库（英文总库） | `specialized/grant-writer.md` | 📝 Grant Writer | 是 | 中文角色库 |
| 222 | Aging Parent Care Companion | agent | 通用角色库（英文总库） | `specialized/healthcare-aging-parent-care-companion.md` | 🧡 Aging Parent Care Companion | 否 | - |
| 223 | Healthcare Customer Service | agent | 通用角色库（英文总库） | `specialized/healthcare-customer-service.md` | 🏥 Healthcare Customer Service Agent | 是 | 中文角色库 |
| 224 | Healthcare Marketing Compliance Specialist | agent | 通用角色库（英文总库） | `specialized/healthcare-marketing-compliance.md` | Full-lifecycle healthcare marketing compliance expert, combining regulatory dept... | 是 | 中文角色库 |
| 225 | Hospitality Guest Services | agent | 通用角色库（英文总库） | `specialized/hospitality-guest-services.md` | 🏨 Hospitality Guest Services Agent | 是 | 中文角色库 |
| 226 | HR Onboarding | agent | 通用角色库（英文总库） | `specialized/hr-onboarding.md` | 🤝 HR Onboarding Agent | 是 | 中文角色库 |
| 227 | Identity Graph Operator | agent | 通用角色库（英文总库） | `specialized/identity-graph-operator.md` | Identity resolution specialist for multi-agent systems | 是 | 中文角色库 |
| 228 | Language Translator | agent | 通用角色库（英文总库） | `specialized/language-translator.md` | 🌐 Language Translator | 是 | 中文角色库 |
| 229 | Legal Billing & Time Tracking | agent | 通用角色库（英文总库） | `specialized/legal-billing-time-tracking.md` | ⏱️ Legal Billing & Time Tracking Agent | 是 | 中文角色库 |
| 230 | Legal Client Intake | agent | 通用角色库（英文总库） | `specialized/legal-client-intake.md` | 📋 Legal Client Intake Agent | 是 | 中文角色库 |
| 231 | Legal Document Review | agent | 通用角色库（英文总库） | `specialized/legal-document-review.md` | ⚖️ Legal Document Review Agent | 是 | 中文角色库 |
| 232 | Loan Officer Assistant | agent | 通用角色库（英文总库） | `specialized/loan-officer-assistant.md` | 🏦 Loan Officer Assistant Agent | 是 | 中文角色库 |
| 233 | LSP/Index Engineer | agent | 通用角色库（英文总库） | `specialized/lsp-index-engineer.md` | LSP client orchestration and semantic index engineering specialist | 是 | 中文角色库 |
| 234 | M&A Integration Manager | agent | 通用角色库（英文总库） | `specialized/ma-integration-manager.md` | Post-merger integration manager specializing in integration strategy, Day 1 read... | 是 | 中文角色库 |
| 235 | Medical Billing & Coding Specialist | agent | 通用角色库（英文总库） | `specialized/medical-billing-coding-specialist.md` | 🏥 Medical Billing & Coding Specialist | 是 | 中文角色库 |
| 236 | Operations Manager | agent | 通用角色库（英文总库） | `specialized/operations-manager.md` | Business operations specialist focused on process mapping and improvement, Lean ... | 是 | 中文角色库 |
| 237 | Organizational Psychologist | agent | 通用角色库（英文总库） | `specialized/organizational-psychologist.md` | Applied organizational psychologist specializing in psychological safety, team e... | 是 | 中文角色库 |
| 238 | Personal Growth Mentor | agent | 通用角色库（英文总库） | `specialized/personal-growth-mentor.md` | You are a cross-domain personal development mentor, strategic coach, and account... | 是 | 中文角色库 |
| 239 | Real Estate Buyer & Seller | agent | 通用角色库（英文总库） | `specialized/real-estate-buyer-seller.md` | 🏠 Real Estate Buyer & Seller Agent | 是 | 中文角色库 |
| 240 | Recruitment Specialist | agent | 通用角色库（英文总库） | `specialized/recruitment-specialist.md` | Recruitment operations, talent acquisition, and HR compliance expert | 是 | 中文角色库 |
| 241 | Report Distribution Agent | agent | 通用角色库（英文总库） | `specialized/report-distribution-agent.md` | Report Distribution Agent | 是 | 中文角色库 |
| 242 | Resume Tailor | agent | 通用角色库（英文总库） | `specialized/resume-tailor.md` | Resume optimization, job description analysis, ATS keyword alignment, and career... | 否 | - |
| 243 | Retail Customer Returns | agent | 通用角色库（英文总库） | `specialized/retail-customer-returns.md` | 🛒 Retail Customer Returns Agent | 是 | 中文角色库 |
| 244 | Sales Data Extraction Agent | agent | 通用角色库（英文总库） | `specialized/sales-data-extraction-agent.md` | Sales Data Extraction Agent | 是 | 中文角色库 |
| 245 | Sales Outreach | agent | 通用角色库（英文总库） | `specialized/sales-outreach.md` | 🎯 Sales Outreach Agent | 否 | - |
| 246 | Chief of Staff | agent | 通用角色库（英文总库） | `specialized/specialized-chief-of-staff.md` | 🧭 Chief of Staff | 否 | - |
| 247 | Civil Engineer | agent | 通用角色库（英文总库） | `specialized/specialized-civil-engineer.md` | Senior structural and civil engineer with international project experience | 是 | 中文角色库 |
| 248 | Codebase Archaeologist | agent | 通用角色库（英文总库） | `specialized/specialized-codebase-archaeologist.md` | Multi-session/multi-tool codebase drift auditor | 否 | - |
| 249 | Cultural Intelligence Strategist | agent | 通用角色库（英文总库） | `specialized/specialized-cultural-intelligence-strategist.md` | You are an Architectural Empathy Engine. Your job is to detect "invisible exclus... | 是 | 中文角色库 |
| 250 | Developer Advocate | agent | 通用角色库（英文总库） | `specialized/specialized-developer-advocate.md` | Developer relations engineer, community champion, and DX architect | 是 | 中文角色库 |
| 251 | Document Generator | agent | 通用角色库（英文总库） | `specialized/specialized-document-generator.md` | Programmatic document creation specialist | 是 | 中文角色库 |
| 252 | FedRAMP & RMF Compliance Engineer | agent | 通用角色库（英文总库） | `specialized/specialized-fedramp-rmf-compliance.md` | 🛡️ FedRAMP & RMF Compliance Engineer | 否 | - |
| 253 | Focus Music Architect | agent | 通用角色库（英文总库） | `specialized/specialized-focus-music-architect.md` | Architect of instrumental focus music, neuroacoustic soundscapes, and production... | 否 | - |
| 254 | French Consulting Market Navigator | agent | 通用角色库（英文总库） | `specialized/specialized-french-consulting-market.md` | French Consulting Market Navigator | 是 | 中文角色库 |
| 255 | Korean Business Navigator | agent | 通用角色库（英文总库） | `specialized/specialized-korean-business-navigator.md` | 🧠 Your Identity & Memory | 是 | 中文角色库 |
| 256 | Master Plan Architect | agent | 通用角色库（英文总库） | `specialized/specialized-master-plan-architect.md` | Master Planning Architect, Technical Educator, and Red Teaming Implementation Cr... | 否 | - |
| 257 | MCP Builder | agent | 通用角色库（英文总库） | `specialized/specialized-mcp-builder.md` | MCP server development specialist — you design, build, test, and deploy MCP serv... | 是 | 中文角色库 |
| 258 | Model QA Specialist | agent | 通用角色库（英文总库） | `specialized/specialized-model-qa.md` | Independent model auditor - you review models built by others, never your own | 是 | 中文角色库 |
| 259 | Pricing Analyst | agent | 通用角色库（英文总库） | `specialized/specialized-pricing-analyst.md` | Specialized pricing analyst and margin optimization specialist | 是 | 中文角色库 |
| 260 | Salesforce Architect | agent | 通用角色库（英文总库） | `specialized/specialized-salesforce-architect.md` | Salesforce Architect | 是 | 中文角色库 |
| 261 | Strategy Duel Agent | agent | 通用角色库（英文总库） | `specialized/specialized-strategy-duel-agent.md` | Strategic orchestrator and duel master | 是 | 中文角色库 |
| 262 | Workflow Architect | agent | 通用角色库（英文总库） | `specialized/specialized-workflow-architect.md` | Workflow design, discovery, and system flow specification specialist | 是 | 中文角色库 |
| 263 | Study Abroad Advisor | agent | 通用角色库（英文总库） | `specialized/study-abroad-advisor.md` | Multi-country, multi-degree-level study abroad application planning expert | 是 | 中文角色库 |
| 264 | Supply Chain Strategist | agent | 通用角色库（英文总库） | `specialized/supply-chain-strategist.md` | Supply chain management, strategic sourcing, and supplier relationship expert | 否 | - |
| 265 | ZK Steward | agent | 通用角色库（英文总库） | `specialized/zk-steward.md` | Niklas Luhmann for the AI age—turning complex tasks into **organic parts of a kn... | 是 | 中文角色库 |
| 266 | Analytics Reporter | agent | 通用角色库（英文总库） | `support/support-analytics-reporter.md` | Data analysis, visualization, and business intelligence specialist | 是 | 中文角色库 |
| 267 | Executive Summary Generator | agent | 通用角色库（英文总库） | `support/support-executive-summary-generator.md` | Senior strategy consultant and executive communication specialist | 是 | 中文角色库 |
| 268 | Finance Tracker | agent | 通用角色库（英文总库） | `support/support-finance-tracker.md` | Financial planning, analysis, and business performance specialist | 是 | 中文角色库 |
| 269 | Infrastructure Maintainer | agent | 通用角色库（英文总库） | `support/support-infrastructure-maintainer.md` | System reliability, infrastructure optimization, and operations specialist | 是 | 中文角色库 |
| 270 | Legal Compliance Checker | agent | 通用角色库（英文总库） | `support/support-legal-compliance-checker.md` | Legal compliance, risk assessment, and regulatory adherence specialist | 是 | 中文角色库 |
| 271 | Support Responder | agent | 通用角色库（英文总库） | `support/support-support-responder.md` | Customer service excellence, issue resolution, and user experience specialist | 是 | 中文角色库 |
| 272 | Accessibility Auditor | agent | 通用角色库（英文总库） | `testing/testing-accessibility-auditor.md` | Accessibility auditing, assistive technology testing, and inclusive design verif... | 是 | 中文角色库 |
| 273 | API Tester | agent | 通用角色库（英文总库） | `testing/testing-api-tester.md` | API testing and validation specialist with security focus | 是 | 中文角色库 |
| 274 | Evidence Collector | agent | 通用角色库（英文总库） | `testing/testing-evidence-collector.md` | Quality assurance specialist focused on visual evidence and reality checking | 是 | 中文角色库 |
| 275 | Performance Benchmarker | agent | 通用角色库（英文总库） | `testing/testing-performance-benchmarker.md` | Performance engineering and optimization specialist with data-driven approach | 是 | 中文角色库 |
| 276 | Reality Checker | agent | 通用角色库（英文总库） | `testing/testing-reality-checker.md` | Final integration testing and realistic deployment readiness assessment | 是 | 中文角色库 |
| 277 | Test Automation Engineer | agent | 通用角色库（英文总库） | `testing/testing-test-automation-engineer.md` | End-to-end test automation specialist for Playwright and Cypress suites and the ... | 否 | - |
| 278 | Test Results Analyzer | agent | 通用角色库（英文总库） | `testing/testing-test-results-analyzer.md` | Test data analysis and quality intelligence specialist with statistical expertis... | 是 | 中文角色库 |
| 279 | Tool Evaluator | agent | 通用角色库（英文总库） | `testing/testing-tool-evaluator.md` | Technology assessment and strategic tool adoption specialist with ROI focus | 是 | 中文角色库 |
| 280 | Workflow Optimizer | agent | 通用角色库（英文总库） | `testing/testing-workflow-optimizer.md` | Process improvement and automation specialist with systems thinking approach | 是 | 中文角色库 |
| 281 | 人类学家 | agent | 中文角色库 | `academic/academic-anthropologist.md` | 文化人类学家，专精社会组织、信仰系统和物质文化 | 是 | 通用角色库（英文总库） |
| 282 | 地理学家 | agent | 中文角色库 | `academic/academic-geographer.md` | 自然与人文地理学家，专精气候系统、地貌学、资源分布和空间分析 | 是 | 通用角色库（英文总库） |
| 283 | 历史学家 | agent | 中文角色库 | `academic/academic-historian.md` | 研究型历史学者，专业领域涵盖从古代到现代的各个时期 | 是 | 通用角色库（英文总库） |
| 284 | 叙事学家 | agent | 中文角色库 | `academic/academic-narratologist.md` | 资深叙事理论家和故事结构分析师 | 是 | 通用角色库（英文总库） |
| 285 | 心理学家 | agent | 中文角色库 | `academic/academic-psychologist.md` | 临床与研究心理学家，专精人格、动机、创伤和群体动力学 | 是 | 通用角色库（英文总库） |
| 286 | 学习规划师 | agent | 中文角色库 | `academic/academic-study-planner.md` | 学习者的备考战略顾问和执行教练，兼具方法论功底和实战经验 | 否 | - |
| 287 | 首席执行官（CEO） | agent | 中文角色库 | `company/chief-executive-officer.md` | 企业最高决策者，掌管战略取舍、年度与季度优先级、高管团队分工、重大资源配置、关键对外关系（投资人/核心客户/合作伙伴）与危机时刻的最终拍板。 | 否 | - |
| 288 | 首席财务官（CFO） | agent | 中文角色库 | `company/chief-financial-officer.md` | 战略财务高管，掌管财务规划与分析（FP&A）、资金管理与资本结构、资本配置、并购财务、投资者关系、董事会与审计委员会汇报、税务策略，以及财务内控。 | 否 | - |
| 289 | 首席营销官（CMO） | agent | 中文角色库 | `company/chief-marketing-officer.md` | 营销最高负责人，掌管市场定位与信息体系（messaging）、渠道组合与预算分配、品牌资产管理、增长实验体系、公关与危机口径、营销团队与代理商管理。 | 否 | - |
| 290 | 幕僚长（Chief of Staff） | agent | 中文角色库 | `company/chief-of-staff.md` | 幕僚长 | 否 | - |
| 291 | 首席运营官（COO） | agent | 中文角色库 | `company/chief-operating-officer.md` | 运营最高负责人，掌管目标拆解与执行追踪、核心业务流程设计、跨部门协调与冲突仲裁、供应商与外部协作管理、运营指标体系、产能与成本控制。 | 否 | - |
| 292 | 首席产品官（CPO） | agent | 中文角色库 | `company/chief-product-officer.md` | 产品最高负责人，掌管产品愿景与战略、路线图与优先级裁决、产品线取舍（含下线决策）、定价与打包策略、产品组织与 PM 培养、用户洞察体系。 | 否 | - |
| 293 | 首席技术官（CTO） | agent | 中文角色库 | `company/chief-technology-officer.md` | 技术最高负责人，掌管技术路线图、架构与选型决策、研发团队组织与招聘标准、技术债务管理、安全与稳定性底线、研发预算与买/建决策。 | 否 | - |
| 294 | 品牌守护者 | agent | 中文角色库 | `design/design-brand-guardian.md` | 品牌策略与形象守护专家 | 是 | 通用角色库（英文总库） |
| 295 | 图像提示词工程师 | agent | 中文角色库 | `design/design-image-prompt-engineer.md` | AI 图像生成的摄影提示词专家 | 是 | 通用角色库（英文总库） |
| 296 | 包容性视觉专家 | agent | 中文角色库 | `design/design-inclusive-visuals-specialist.md` | 你是一位严谨的 Prompt 工程师，专攻 AI 生成内容中的真实人物表现。你的战场是那些深植于基础图像和视频模型中的系统性偏见。 | 是 | 通用角色库（英文总库） |
| 297 | Persona 走查专家 | agent | 中文角色库 | `design/design-persona-walkthrough.md` | Persona 走查专家 | 是 | 通用角色库（英文总库） |
| 298 | UI 设计师 | agent | 中文角色库 | `design/design-ui-designer.md` | 视觉设计系统与界面创建专家 | 是 | 通用角色库（英文总库） |
| 299 | UX 架构师 | agent | 中文角色库 | `design/design-ux-architect.md` | 技术架构与 UX 基础设施专家 | 是 | 通用角色库（英文总库） |
| 300 | UX 研究员 | agent | 中文角色库 | `design/design-ux-researcher.md` | 用户行为分析与研究方法论专家 | 是 | 通用角色库（英文总库） |
| 301 | 视频提示词工程师 | agent | 中文角色库 | `design/design-video-prompt-engineer.md` | 文生视频提示词的作者与把关人，负责题材判断、5 段式结构落笔、负面提示词、多镜一致性规划，以及在出片前把可预见的翻车点写进提示词里。 | 否 | - |
| 302 | 视觉叙事师 | agent | 中文角色库 | `design/design-visual-storyteller.md` | 视觉传达与叙事专家 | 是 | 通用角色库（英文总库） |
| 303 | 趣味注入师 | agent | 中文角色库 | `design/design-whimsy-injector.md` | 品牌个性与趣味交互专家 | 是 | 通用角色库（英文总库） |
| 304 | AI 数据修复工程师 | agent | 中文角色库 | `engineering/engineering-ai-data-remediation-engineer.md` | AI 数据修复专家 | 是 | 通用角色库（英文总库） |
| 305 | AI 工程师 | agent | 中文角色库 | `engineering/engineering-ai-engineer.md` | 机器学习工程师与 AI 系统架构师 | 是 | 通用角色库（英文总库） |
| 306 | 自主优化架构师 | agent | 中文角色库 | `engineering/engineering-autonomous-optimization-architect.md` | 你是自演进软件系统的治理者。你的使命是让系统自主进化（找到更快、更便宜、更聪明的方式执行任务），同时用数学手段保证系统不会把自己烧穿，也不会陷入恶意循环。 | 是 | 通用角色库（英文总库） |
| 307 | 后端架构师 | agent | 中文角色库 | `engineering/engineering-backend-architect.md` | 系统架构和服务端开发专家 | 是 | 通用角色库（英文总库） |
| 308 | CMS 开发者 | agent | 中文角色库 | `engineering/engineering-cms-developer.md` | CMS 开发者 | 是 | 通用角色库（英文总库） |
| 309 | 代码审查员 | agent | 中文角色库 | `engineering/engineering-code-reviewer.md` | 代码审查与质量保障专家 | 是 | 通用角色库（英文总库） |
| 310 | 代码库入职引导工程师 | agent | 中文角色库 | `engineering/engineering-codebase-onboarding-engineer.md` | 代码库探索、执行追踪与开发者入职引导专家 | 是 | 通用角色库（英文总库） |
| 311 | 数据工程师 | agent | 中文角色库 | `engineering/engineering-data-engineer.md` | 数据管线架构师与数据平台工程师 | 是 | 通用角色库（英文总库） |
| 312 | 数据库优化师 | agent | 中文角色库 | `engineering/engineering-database-optimizer.md` | 🗄️ 数据库优化师 | 是 | 通用角色库（英文总库） |
| 313 | DevOps 自动化师 | agent | 中文角色库 | `engineering/engineering-devops-automator.md` | 基础设施自动化与部署流水线专家 | 是 | 通用角色库（英文总库） |
| 314 | 钉钉集成开发工程师 | agent | 中文角色库 | `engineering/engineering-dingtalk-integration-developer.md` | 钉钉开放平台全栈集成工程师 | 否 | - |
| 315 | Drupal 购物车工程师 | agent | 中文角色库 | `engineering/engineering-drupal-shopping-cart.md` | 🛒 Drupal 购物车工程师 | 是 | 通用角色库（英文总库） |
| 316 | 邮件智能工程师 | agent | 中文角色库 | `engineering/engineering-email-intelligence-engineer.md` | 邮件数据管线架构师与上下文工程专家 | 是 | 通用角色库（英文总库） |
| 317 | 嵌入式固件工程师 | agent | 中文角色库 | `engineering/engineering-embedded-firmware-engineer.md` | 为资源受限的嵌入式系统设计和实现生产级固件 | 是 | 通用角色库（英文总库） |
| 318 | 嵌入式 Linux 驱动工程师 | agent | 中文角色库 | `engineering/engineering-embedded-linux-driver-engineer.md` | 为嵌入式 Linux 系统设计和实现生产级内核驱动与板级支持包（BSP） | 否 | - |
| 319 | 飞书集成开发工程师 | agent | 中文角色库 | `engineering/engineering-feishu-integration-developer.md` | 飞书开放平台全栈集成工程师 | 是 | 通用角色库（英文总库） |
| 320 | Filament 优化专家 | agent | 中文角色库 | `engineering/engineering-filament-optimization-specialist.md` | 从结构层面重新设计 Filament 资源、表单、表格和导航，最大化用户体验 | 是 | 通用角色库（英文总库） |
| 321 | FPGA/ASIC 数字设计工程师 | agent | 中文角色库 | `engineering/engineering-fpga-digital-design-engineer.md` | 为嵌入式系统和高性能计算场景设计和实现可综合的数字逻辑 | 否 | - |
| 322 | 前端开发者 | agent | 中文角色库 | `engineering/engineering-frontend-developer.md` | 现代 Web 应用和 UI 实现专家 | 是 | 通用角色库（英文总库） |
| 323 | Git 工作流大师 | agent | 中文角色库 | `engineering/engineering-git-workflow-master.md` | Git 工作流和版本控制专家 | 是 | 通用角色库（英文总库） |
| 324 | 故障响应指挥官 | agent | 中文角色库 | `engineering/engineering-incident-response-commander.md` | 生产故障指挥官、事后复盘主持人、on-call 流程架构师 | 是 | 通用角色库（英文总库） |
| 325 | IoT 方案架构师 | agent | 中文角色库 | `engineering/engineering-iot-solution-architect.md` | 设计从传感器到云端的完整物联网方案架构，打通硬件、固件、边缘和云的全链路 | 否 | - |
| 326 | IT 服务经理 | agent | 中文角色库 | `engineering/engineering-it-service-manager.md` | 🖧 IT 服务经理 | 是 | 通用角色库（英文总库） |
| 327 | 机械设计工程师 | agent | 中文角色库 | `engineering/engineering-mechanical-design-engineer.md` | 为工业装备、自动化产线、检测仪器、消费类机械产品提供从方案到出图的全流程机械设计 | 否 | - |
| 328 | 最小变更工程师 | agent | 中文角色库 | `engineering/engineering-minimal-change-engineer.md` | 精准实现专家，价值以"没写的代码行数"来衡量 | 是 | 通用角色库（英文总库） |
| 329 | 移动应用开发者 | agent | 中文角色库 | `engineering/engineering-mobile-app-builder.md` | 原生和跨平台移动应用专家 | 是 | 通用角色库（英文总库） |
| 330 | 多智能体系统架构师 | agent | 中文角色库 | `engineering/engineering-multi-agent-systems-architect.md` | 多智能体系统架构师，专精于拓扑选型、上下文架构、故障模式工程、信任与权限划分、human-in-the-loop 门控，以及面向生产级智能体流水线的可观测性。 | 是 | 通用角色库（英文总库） |
| 331 | 国内网络工程师 | agent | 中文角色库 | `engineering/engineering-network-engineer-china.md` | 面向国产设备（华为/华三/锐捷）的企业网络设计与运维工程师 | 否 | - |
| 332 | OrgScript 工程师 | agent | 中文角色库 | `engineering/engineering-orgscript-engineer.md` | OrgScript 核心开发者兼架构师，以及流程建模专家 | 是 | 通用角色库（英文总库） |
| 333 | 上位机工程师 | agent | 中文角色库 | `engineering/engineering-pc-host-engineer.md` | 为工业自动化、检测设备、IoT 网关、实验室仪器构建生产级桌面上位机软件 | 否 | - |
| 334 | Prompt 工程师 | agent | 中文角色库 | `engineering/engineering-prompt-engineer.md` | prompt 设计与 LLM 行为专家 | 是 | 通用角色库（英文总库） |
| 335 | 快速原型师 | agent | 中文角色库 | `engineering/engineering-rapid-prototyper.md` | 超快速原型和 MVP 开发专家 | 是 | 通用角色库（英文总库） |
| 336 | 安全工程师 | agent | 中文角色库 | `engineering/engineering-security-engineer.md` | 应用安全工程师、安全架构师、对抗性思维者 | 否 | - |
| 337 | 高级开发者 | agent | 中文角色库 | `engineering/engineering-senior-developer.md` | 用 Laravel/Livewire/FluxUI 打造高端 Web 体验 | 是 | 通用角色库（英文总库） |
| 338 | 软件架构师 | agent | 中文角色库 | `engineering/engineering-software-architect.md` | 软件架构与系统设计专家 | 是 | 通用角色库（英文总库） |
| 339 | Solidity 智能合约工程师 | agent | 中文角色库 | `engineering/engineering-solidity-smart-contract-engineer.md` | 资深 Solidity 开发者与智能合约架构师，服务于所有 EVM 兼容链 | 是 | 通用角色库（英文总库） |
| 340 | SRE (站点可靠性工程师) | agent | 中文角色库 | `engineering/engineering-sre.md` | 站点可靠性工程与生产系统专家 | 是 | 通用角色库（英文总库） |
| 341 | 技术文档工程师 | agent | 中文角色库 | `engineering/engineering-technical-writer.md` | 开发者文档架构师和内容工程师 | 是 | 通用角色库（英文总库） |
| 342 | 威胁检测工程师（工程侧） | agent | 中文角色库 | `engineering/engineering-threat-detection-engineer.md` | 检测工程师、威胁猎手、安全运营专家 | 否 | - |
| 343 | 语音 AI 集成工程师 | agent | 中文角色库 | `engineering/engineering-voice-ai-integration-engineer.md` | 语音转录架构师与语音 AI 流水线工程师 | 是 | 通用角色库（英文总库） |
| 344 | 微信小程序开发者 | agent | 中文角色库 | `engineering/engineering-wechat-mini-program-developer.md` | 微信小程序全栈开发工程师 | 是 | 通用角色库（英文总库） |
| 345 | WordPress 购物车工程师 | agent | 中文角色库 | `engineering/engineering-wordpress-shopping-cart.md` | 🛍️ WordPress 购物车工程师 | 是 | 通用角色库（英文总库） |
| 346 | 簿记与财务总监 | agent | 中文角色库 | `finance/finance-bookkeeper-controller.md` | 簿记与财务总监 | 是 | 通用角色库（英文总库） |
| 347 | 财务分析师 | agent | 中文角色库 | `finance/finance-financial-analyst.md` | 财务分析师 | 是 | 通用角色库（英文总库） |
| 348 | 财务预测分析师 | agent | 中文角色库 | `finance/finance-financial-forecaster.md` | 企业财务预测、场景建模与融资策略专家 | 否 | - |
| 349 | FP&A 分析师 | agent | 中文角色库 | `finance/finance-fpa-analyst.md` | FP&A 分析师 | 是 | 通用角色库（英文总库） |
| 350 | 金融风控分析师 | agent | 中文角色库 | `finance/finance-fraud-detector.md` | 交易欺诈检测、风险监控与合规管理专家 | 否 | - |
| 351 | 香港股市合规审查专家 | agent | 中文角色库 | `finance/finance-hk-stock-compliance-reviewer.md` | 香港股市合规审查专家 | 否 | - |
| 352 | 投资研究员 | agent | 中文角色库 | `finance/finance-investment-researcher.md` | 投资研究员 | 是 | 通用角色库（英文总库） |
| 353 | 发票管理专家 | agent | 中文角色库 | `finance/finance-invoice-manager.md` | 企业发票全生命周期管理与税务合规专家 | 否 | - |
| 354 | 税务策略师 | agent | 中文角色库 | `finance/finance-tax-strategist.md` | 税务策略师 | 是 | 通用角色库（英文总库） |
| 355 | 游戏音频工程师 | agent | 中文角色库 | `game-development/game-audio-engineer.md` | 设计和实现交互式音频系统——音效、音乐、语音、空间音频——通过 FMOD、Wwise 或引擎原生音频集成 | 是 | 通用角色库（英文总库） |
| 356 | 游戏设计师 | agent | 中文角色库 | `game-development/game-designer.md` | 设计游戏系统、机制、经济和玩家成长体系——然后严谨地文档化 | 是 | 通用角色库（英文总库） |
| 357 | 关卡设计师 | agent | 中文角色库 | `game-development/level-designer.md` | 设计、文档化和迭代游戏关卡，精确控制节奏、流线、遭遇战设计和环境叙事 | 是 | 通用角色库（英文总库） |
| 358 | 叙事设计师 | agent | 中文角色库 | `game-development/narrative-designer.md` | 设计和实现叙事系统——对话、分支故事、世界观、环境叙事和角色声音——与游戏玩法无缝融合 | 是 | 通用角色库（英文总库） |
| 359 | 技术美术 | agent | 中文角色库 | `game-development/technical-artist.md` | 连接美术与工程——搭建 shader、VFX、资源管线和性能标准，在运行时预算内保持视觉品质 | 是 | 通用角色库（英文总库） |
| 360 | Blender 插件工程师 | agent | 中文角色库 | `game-development/blender/blender-addon-engineer.md` | 使用 Python 和 `bpy` 构建 Blender 原生工具——自定义 Operator、Panel、验证器、导入/导出自动化，以及面向美术、技术美术和游... | 是 | 通用角色库（英文总库） |
| 361 | Godot 游戏脚本开发者 | agent | 中文角色库 | `game-development/godot/godot-gameplay-scripter.md` | 在 Godot 4 中设计和实现干净、类型安全的游戏系统，使用 GDScript 2.0，必要时引入 C# | 是 | 通用角色库（英文总库） |
| 362 | Godot 多人游戏工程师 | agent | 中文角色库 | `game-development/godot/godot-multiplayer-engineer.md` | 使用 MultiplayerAPI、MultiplayerSpawner、MultiplayerSynchronizer 和 RPC 在 Godot 4 中设计... | 是 | 通用角色库（英文总库） |
| 363 | Godot Shader 开发者 | agent | 中文角色库 | `game-development/godot/godot-shader-developer.md` | 使用 Godot 着色语言和 VisualShader 编辑器，为 Godot 4 的 2D（CanvasItem）和 3D（Spatial）场景编写和优化 s... | 是 | 通用角色库（英文总库） |
| 364 | Roblox 虚拟形象创作者 | agent | 中文角色库 | `game-development/roblox-studio/roblox-avatar-creator.md` | 设计、绑定和管线化 Roblox 虚拟形象物品——配件、服装、套装组件——用于体验内使用和 Creator Marketplace 发布 | 是 | 通用角色库（英文总库） |
| 365 | Roblox 体验设计师 | agent | 中文角色库 | `game-development/roblox-studio/roblox-experience-designer.md` | 为 Roblox 体验设计和实现面向玩家的系统——进度、变现、社交循环和新手引导——使用 Roblox 原生工具和最佳实践 | 是 | 通用角色库（英文总库） |
| 366 | Roblox 系统脚本工程师 | agent | 中文角色库 | `game-development/roblox-studio/roblox-systems-scripter.md` | 为 Roblox 体验设计和实现核心系统——游戏逻辑、客户端-服务端通信、DataStore 持久化和模块架构，使用 Luau | 是 | 通用角色库（英文总库） |
| 367 | Unity 架构师 | agent | 中文角色库 | `game-development/unity/unity-architect.md` | 使用 ScriptableObject 和组合模式架构可扩展、数据驱动的 Unity 系统 | 是 | 通用角色库（英文总库） |
| 368 | Unity 编辑器工具开发者 | agent | 中文角色库 | `game-development/unity/unity-editor-tool-developer.md` | 构建 Unity 编辑器工具——窗口、属性绘制器、资源处理器、验证器和管线自动化——减少手动工作并提前捕获错误 | 是 | 通用角色库（英文总库） |
| 369 | Unity 多人游戏工程师 | agent | 中文角色库 | `game-development/unity/unity-multiplayer-engineer.md` | 使用 Netcode for GameObjects（NGO）、Unity Gaming Services（UGS）和网络最佳实践设计和实现 Unity 多人系... | 是 | 通用角色库（英文总库） |
| 370 | Unity Shader Graph 美术师 | agent | 中文角色库 | `game-development/unity/unity-shader-graph-artist.md` | 使用 Shader Graph 保障美术可操作性，使用 HLSL 应对性能关键场景，编写、优化和维护 Unity 的 Shader 库 | 是 | 通用角色库（英文总库） |
| 371 | Unreal 多人游戏架构师 | agent | 中文角色库 | `game-development/unreal-engine/unreal-multiplayer-architect.md` | 设计和实现 UE5 多人系统——Actor 复制、权威模型、网络预测、GameState/GameMode 架构和专用服务器配置 | 是 | 通用角色库（英文总库） |
| 372 | Unreal 系统工程师 | agent | 中文角色库 | `game-development/unreal-engine/unreal-systems-engineer.md` | 使用 C++ 配合 Blueprint 暴露，设计和实现高性能、模块化的 Unreal Engine 5 系统 | 是 | 通用角色库（英文总库） |
| 373 | Unreal 技术美术 | agent | 中文角色库 | `game-development/unreal-engine/unreal-technical-artist.md` | 掌管 UE5 的视觉管线——材质编辑器、Niagara、PCG、LOD 系统和渲染优化，交付出货级画质 | 是 | 通用角色库（英文总库） |
| 374 | Unreal 世界构建师 | agent | 中文角色库 | `game-development/unreal-engine/unreal-world-builder.md` | 使用 UE5 World Partition、Landscape、PCG 和 HLOD 系统设计和实现产品级开放世界环境 | 是 | 通用角色库（英文总库） |
| 375 | 三维场景开发者 | agent | 中文角色库 | `gis/gis-3d-scene-developer.md` | Web 三维可视化——场景、地形、点云、Cesium、ArcGIS Scene Viewer、3D Tiles | 是 | 通用角色库（英文总库） |
| 376 | GIS 分析师 | agent | 中文角色库 | `gis/gis-analyst.md` | 日常 GIS 运营——制图、数据管理、空间查询、图层维护 | 是 | 通用角色库（英文总库） |
| 377 | BIM/GIS 专家 | agent | 中文角色库 | `gis/gis-bim-specialist.md` | BIM 到 GIS 的整合——Revit/IFC 数据转换、室内地图、数字孪生架构、空间管理 | 是 | 通用角色库（英文总库） |
| 378 | 地图制图设计师 | agent | 中文角色库 | `gis/gis-cartography-designer.md` | 地图设计与美学——配色理论、字体排印、标注层级、底图选择、视觉风格规范 | 是 | 通用角色库（英文总库） |
| 379 | 无人机实景测绘专家 | agent | 中文角色库 | `gis/gis-drone-reality-mapping.md` | 基于无人机的实景采集——航线规划、photogrammetry（摄影测量）处理、point cloud（点云）分类、ortho/dem/mesh 成果生产 | 是 | 通用角色库（英文总库） |
| 380 | GeoAI/ML 工程师 | agent | 中文角色库 | `gis/gis-geoai-ml-engineer.md` | 地理空间 AI/ML 模型开发——特征提取、目标检测、语义分割（semantic segmentation）、模型部署 | 是 | 通用角色库（英文总库） |
| 381 | 地理处理专家 | agent | 中文角色库 | `gis/gis-geoprocessing-specialist.md` | 地理处理自动化——Python 工具箱（.pyt）、Model Builder、ArcPy 脚本、批量处理 | 是 | 通用角色库（英文总库） |
| 382 | GIS 质检工程师 | agent | 中文角色库 | `gis/gis-qa-engineer.md` | GIS 质量保证与质量控制专家——空间数据校验、元数据审计、合规验证 | 是 | 通用角色库（英文总库） |
| 383 | 解决方案工程师 | agent | 中文角色库 | `gis/gis-solution-engineer.md` | 售前与 PoC 工程师——搭建可运行的演示、验证可行性、估算工作量 | 是 | 通用角色库（英文总库） |
| 384 | 空间数据工程师 | agent | 中文角色库 | `gis/gis-spatial-data-engineer.md` | 地理空间 ETL 专家——数据摄取、清洗、转换、校验，以及自动化管线设计 | 是 | 通用角色库（英文总库） |
| 385 | 空间数据科学家 | agent | 中文角色库 | `gis/gis-spatial-data-scientist.md` | 高级空间统计与预测建模——空间聚类、回归、插值、点模式分析 | 是 | 通用角色库（英文总库） |
| 386 | 技术顾问 | agent | 中文角色库 | `gis/gis-technical-consultant.md` | 战略型 GIS 顾问——差距分析、技术选型、ROI 建模、数字化转型路线图 | 是 | 通用角色库（英文总库） |
| 387 | Web GIS 开发工程师 | agent | 中文角色库 | `gis/gis-web-gis-developer.md` | Web GIS 应用开发——地图库、REST API、仪表盘、实时数据、响应式设计 | 是 | 通用角色库（英文总库） |
| 388 | 绩效管理专家 | agent | 中文角色库 | `hr/hr-performance-reviewer.md` | 企业绩效管理体系设计与运营专家 | 否 | - |
| 389 | 招聘专家（HR 全流程） | agent | 中文角色库 | `hr/hr-recruiter.md` | 企业人才获取与招聘全流程管理专家 | 否 | - |
| 390 | Backend Architect | agent | 中文角色库 | `integrations/mcp-memory/backend-architect-with-memory.md` | System architecture and server-side development specialist | 是 | 通用角色库（英文总库） |
| 391 | 合同审查专家 | agent | 中文角色库 | `legal/legal-contract-reviewer.md` | 企业合同风险管理与法律审查专家 | 否 | - |
| 392 | 制度文件撰写专家 | agent | 中文角色库 | `legal/legal-policy-writer.md` | 企业合规制度体系设计与法律文书撰写专家 | 否 | - |
| 393 | AEO 基础架构师 | agent | 中文角色库 | `marketing/marketing-aeo-foundations.md` | AEO 基础架构师 | 是 | 通用角色库（英文总库） |
| 394 | 智能搜索优化师 | agent | 中文角色库 | `marketing/marketing-agentic-search-optimizer.md` | 智能搜索优化师 | 是 | 通用角色库（英文总库） |
| 395 | AI 搜索可见性与 GEO 策略师 | agent | 中文角色库 | `marketing/marketing-ai-citation-strategist.md` | AI 搜索可见性与 GEO 策略师 v2 | 是 | 通用角色库（英文总库） |
| 396 | 应用商店优化师 | agent | 中文角色库 | `marketing/marketing-app-store-optimizer.md` | 应用商店优化和移动营销专家 | 是 | 通用角色库（英文总库） |
| 397 | 百度 SEO 专家 | agent | 中文角色库 | `marketing/marketing-baidu-seo-specialist.md` | 百度搜索优化与中文搜索营销策略专家 | 是 | 通用角色库（英文总库） |
| 398 | B站内容策略师 | agent | 中文角色库 | `marketing/marketing-bilibili-strategist.md` | B站中长视频内容策略与UP主运营专家 | 否 | - |
| 399 | 图书联合作者 | agent | 中文角色库 | `marketing/marketing-book-co-author.md` | 思想领袖力图书的战略联合作者、代笔人和叙事架构师 | 是 | 通用角色库（英文总库） |
| 400 | 轮播图增长引擎 | agent | 中文角色库 | `marketing/marketing-carousel-growth-engine.md` | 轮播图增长引擎 | 是 | 通用角色库（英文总库） |
| 401 | 中国电商运营专家 | agent | 中文角色库 | `marketing/marketing-china-ecommerce-operator.md` | 中国多平台电商运营与大促策略专家 | 是 | 通用角色库（英文总库） |
| 402 | 中国市场本地化策略师 | agent | 中文角色库 | `marketing/marketing-china-market-localization-strategist.md` | 全栈中国市场本地化与趋势转化策略师 | 是 | 通用角色库（英文总库） |
| 403 | 内容创作者 | agent | 中文角色库 | `marketing/marketing-content-creator.md` | 内容策略师与多平台创作者 | 是 | 通用角色库（英文总库） |
| 404 | 跨境电商运营专家 | agent | 中文角色库 | `marketing/marketing-cross-border-ecommerce.md` | 跨境电商全平台运营与品牌出海战略专家 | 是 | 通用角色库（英文总库） |
| 405 | 新闻情报官 | agent | 中文角色库 | `marketing/marketing-daily-news-briefing.md` | 新闻采集员与信息筛选专家，内容生产线的第一环 | 否 | - |
| 406 | 抖音策略师 | agent | 中文角色库 | `marketing/marketing-douyin-strategist.md` | 抖音短视频营销与直播电商策略专家 | 是 | 通用角色库（英文总库） |
| 407 | 电商运营师 | agent | 中文角色库 | `marketing/marketing-ecommerce-operator.md` | 中国电商全平台运营与大促策划专家 | 否 | - |
| 408 | 邮件营销策略师 | agent | 中文角色库 | `marketing/marketing-email-strategist.md` | 资深邮件营销策略师，打通 CRM 数据与 ESP（邮件服务商）执行。你设计数据架构（属性、列表、segment 分群）、生命周期流程（从欢迎到转介绍），以及衡量... | 是 | 通用角色库（英文总库） |
| 409 | 全球播客策略师 | agent | 中文角色库 | `marketing/marketing-global-podcast-strategist.md` | 全球播客策略师 | 是 | 通用角色库（英文总库） |
| 410 | 增长黑客 | agent | 中文角色库 | `marketing/marketing-growth-hacker.md` | 增长策略师与实验驱动者 | 是 | 通用角色库（英文总库） |
| 411 | Instagram 策展师 | agent | 中文角色库 | `marketing/marketing-instagram-curator.md` | 视觉叙事者 + 品牌美学构建者 | 是 | 通用角色库（英文总库） |
| 412 | 知识付费产品策划师 | agent | 中文角色库 | `marketing/marketing-knowledge-commerce-strategist.md` | 知识付费产品全链路策划与商业化专家 | 否 | - |
| 413 | 快手策略师 | agent | 中文角色库 | `marketing/marketing-kuaishou-strategist.md` | 快手短视频运营与直播电商策略专家 | 是 | 通用角色库（英文总库） |
| 414 | LinkedIn 内容创作专家 | agent | 中文角色库 | `marketing/marketing-linkedin-content-creator.md` | LinkedIn 内容策略师与个人品牌架构师 | 是 | 通用角色库（英文总库） |
| 415 | 直播电商主播教练 | agent | 中文角色库 | `marketing/marketing-livestream-commerce-coach.md` | 直播电商主播培训与直播间全盘运营教练 | 是 | 通用角色库（英文总库） |
| 416 | 多平台发布编排官 | agent | 中文角色库 | `marketing/marketing-multi-platform-publisher.md` | 专攻中文内容分发的多平台发布编排官。你把一篇源文章转换成各平台原生的草稿,并编排它们投递到 知乎 / 小红书 / CSDN / B 站 / 公众号 / 掘金 /... | 是 | 通用角色库（英文总库） |
| 417 | 播客内容策略师 | agent | 中文角色库 | `marketing/marketing-podcast-strategist.md` | 中文播客内容策略与全链路运营专家 | 是 | 通用角色库（英文总库） |
| 418 | PR 与传播经理 | agent | 中文角色库 | `marketing/marketing-pr-communications-manager.md` | 📣 PR 与传播经理 | 是 | 通用角色库（英文总库） |
| 419 | 私域流量运营师 | agent | 中文角色库 | `marketing/marketing-private-domain-operator.md` | 企业微信私域运营与用户生命周期管理专家 | 是 | 通用角色库（英文总库） |
| 420 | Reddit 社区运营 | agent | 中文角色库 | `marketing/marketing-reddit-community-builder.md` | 社区融入者 + 品牌口碑建设者 | 是 | 通用角色库（英文总库） |
| 421 | 搜索增长编排器 | agent | 中文角色库 | `marketing/marketing-search-growth-orchestrator.md` | 搜索增长编排器（Organic + AI Search） | 否 | - |
| 422 | SEO 与自然搜索增长专家 | agent | 中文角色库 | `marketing/marketing-seo-specialist.md` | SEO 与自然搜索增长专家 v2 | 是 | 通用角色库（英文总库） |
| 423 | 短视频剪辑指导师 | agent | 中文角色库 | `marketing/marketing-short-video-editing-coach.md` | 短视频剪辑技术教练与后期制作全流程指导专家 | 是 | 通用角色库（英文总库） |
| 424 | 社交媒体策略师 | agent | 中文角色库 | `marketing/marketing-social-media-strategist.md` | 社交媒体策略师 | 是 | 通用角色库（英文总库） |
| 425 | TikTok 策略师 | agent | 中文角色库 | `marketing/marketing-tiktok-strategist.md` | 病毒内容工程师 + TikTok 生态玩家 | 是 | 通用角色库（英文总库） |
| 426 | Twitter 互动官 | agent | 中文角色库 | `marketing/marketing-twitter-engager.md` | 实时互动专家 + 品牌对话操盘手 | 是 | 通用角色库（英文总库） |
| 427 | 视频优化专家 | agent | 中文角色库 | `marketing/marketing-video-optimization-specialist.md` | 视频平台的观众增长与留存优化专家 | 是 | 通用角色库（英文总库） |
| 428 | 微信公众号管理 | agent | 中文角色库 | `marketing/marketing-wechat-official-account.md` | 订阅关系架构师 + 私域运营专家 | 是 | 通用角色库（英文总库） |
| 429 | 微信公众号运营 | agent | 中文角色库 | `marketing/marketing-wechat-operator.md` | 微信生态内容运营与私域流量增长专家 | 否 | - |
| 430 | 微博运营策略师 | agent | 中文角色库 | `marketing/marketing-weibo-strategist.md` | 微博全域运营与品牌传播策略专家 | 是 | 通用角色库（英文总库） |
| 431 | 微信视频号运营策略师 | agent | 中文角色库 | `marketing/marketing-weixin-channels-strategist.md` | 微信视频号生态全链路运营策略师 | 否 | - |
| 432 | X/Twitter 情报分析师 | agent | 中文角色库 | `marketing/marketing-x-twitter-intelligence-analyst.md` | X/Twitter 情报分析师 | 是 | 通用角色库（英文总库） |
| 433 | 小红书运营专家 | agent | 中文角色库 | `marketing/marketing-xiaohongshu-operator.md` | 小红书内容运营与品牌种草策略专家 | 否 | - |
| 434 | 小红书专家 | agent | 中文角色库 | `marketing/marketing-xiaohongshu-specialist.md` | 生活方式内容操盘手 + 趋势捕手 | 是 | 通用角色库（英文总库） |
| 435 | 知乎策略师 | agent | 中文角色库 | `marketing/marketing-zhihu-strategist.md` | 权威建设师 + 知识型品牌运营者 | 是 | 通用角色库（英文总库） |
| 436 | 付费媒体审计师 | agent | 中文角色库 | `paid-media/paid-media-auditor.md` | 付费媒体审计专家 | 是 | 通用角色库（英文总库） |
| 437 | 广告创意策略师 | agent | 中文角色库 | `paid-media/paid-media-creative-strategist.md` | 效果导向的创意策略师 | 是 | 通用角色库（英文总库） |
| 438 | 社交广告策略师 | agent | 中文角色库 | `paid-media/paid-media-paid-social-strategist.md` | 全链路社交广告策略师 | 是 | 通用角色库（英文总库） |
| 439 | PPC 竞价策略师 | agent | 中文角色库 | `paid-media/paid-media-ppc-strategist.md` | 资深竞价策略架构师 | 是 | 通用角色库（英文总库） |
| 440 | 程序化广告采买专家 | agent | 中文角色库 | `paid-media/paid-media-programmatic-buyer.md` | 程序化媒介采买策略师 | 是 | 通用角色库（英文总库） |
| 441 | 搜索词分析师 | agent | 中文角色库 | `paid-media/paid-media-search-query-analyst.md` | 搜索词深度分析专家 | 是 | 通用角色库（英文总库） |
| 442 | 追踪与归因专家 | agent | 中文角色库 | `paid-media/paid-media-tracking-specialist.md` | 精准追踪工程师 | 是 | 通用角色库（英文总库） |
| 443 | 行为助推引擎 | agent | 中文角色库 | `product/product-behavioral-nudge-engine.md` | 你是一个基于行为心理学和习惯养成理论的主动式教练智能体。你把被动的软件仪表盘变成主动的、个性化的效率搭档。 | 是 | 通用角色库（英文总库） |
| 444 | 反馈分析师 | agent | 中文角色库 | `product/product-feedback-synthesizer.md` | 用户声音翻译官与产品洞察分析师 | 是 | 通用角色库（英文总库） |
| 445 | 产品经理（PM） | agent | 中文角色库 | `product/product-manager.md` | 🧭 产品经理智能体 | 是 | 通用角色库（英文总库） |
| 446 | Sprint 排序师 | agent | 中文角色库 | `product/product-sprint-prioritizer.md` | 产品优先级决策者与 Sprint 规划师 | 是 | 通用角色库（英文总库） |
| 447 | 趋势研究员 | agent | 中文角色库 | `product/product-trend-researcher.md` | 行业分析师与技术趋势研究员 | 是 | 通用角色库（英文总库） |
| 448 | 实验追踪员 | agent | 中文角色库 | `project-management/project-management-experiment-tracker.md` | 科学实验与数据驱动决策专家 | 是 | 通用角色库（英文总库） |
| 449 | Jira工作流管家 | agent | 中文角色库 | `project-management/project-management-jira-workflow-steward.md` | 交付可追溯性负责人、Git工作流管理者、Jira卫生专家 | 是 | 通用角色库（英文总库） |
| 450 | 会议纪要专家 | agent | 中文角色库 | `project-management/project-management-meeting-notes-specialist.md` | 会议纪要专家 | 是 | 通用角色库（英文总库） |
| 451 | 项目牧羊人 | agent | 中文角色库 | `project-management/project-management-project-shepherd.md` | 跨部门项目协调者和利益方对齐专家 | 是 | 通用角色库（英文总库） |
| 452 | 工作室运营 | agent | 中文角色库 | `project-management/project-management-studio-operations.md` | 运营效率和流程优化专家 | 是 | 通用角色库（英文总库） |
| 453 | 工作室制片人 | agent | 中文角色库 | `project-management/project-management-studio-producer.md` | 高管级创意策略师和项目组合统筹者 | 是 | 通用角色库（英文总库） |
| 454 | 高级项目经理 | agent | 中文角色库 | `project-management/project-manager-senior.md` | 把规格说明书转化成结构化任务清单，交给开发团队执行 | 是 | 通用角色库（英文总库） |
| 455 | 客户拓展策略师 | agent | 中文角色库 | `sales/sales-account-strategist.md` | 售后客户拓展策略师与客户发展架构师 | 是 | 通用角色库（英文总库） |
| 456 | 销售教练 | agent | 中文角色库 | `sales/sales-coach.md` | 销售能力开发者、Pipeline Review 主持人、单子策略师、Forecast 纪律守护者 | 是 | 通用角色库（英文总库） |
| 457 | 赢单策略师 | agent | 中文角色库 | `sales/sales-deal-strategist.md` | 赢单策略师 | 是 | 通用角色库（英文总库） |
| 458 | Discovery 教练 | agent | 中文角色库 | `sales/sales-discovery-coach.md` | Discovery 方法论教练与通话架构师 | 是 | 通用角色库（英文总库） |
| 459 | 售前工程师 | agent | 中文角色库 | `sales/sales-engineer.md` | 售前工程师 | 是 | 通用角色库（英文总库） |
| 460 | Offer 与 Lead Gen 策略师 | agent | 中文角色库 | `sales/sales-offer-lead-gen-strategist.md` | 漏斗顶端策略师——offer 架构师、lead magnet 设计师、渠道规划者、触达放大器 | 是 | 通用角色库（英文总库） |
| 461 | Outbound 策略师 | agent | 中文角色库 | `sales/sales-outbound-strategist.md` | 信号驱动的 Outbound 策略师与序列架构师 | 是 | 通用角色库（英文总库） |
| 462 | Pipeline 分析师 | agent | 中文角色库 | `sales/sales-pipeline-analyst.md` | Pipeline 健康诊断师与营收预测分析师 | 是 | 通用角色库（英文总库） |
| 463 | 投标策略师 | agent | 中文角色库 | `sales/sales-proposal-strategist.md` | 投标策略师与赢标主题架构师 | 是 | 通用角色库（英文总库） |
| 464 | 应用安全工程师 | agent | 中文角色库 | `security/security-appsec-engineer.md` | 资深应用安全工程师，专注于安全 SDLC（软件开发生命周期）、威胁建模、代码审查、漏洞管理以及开发者安全赋能 | 是 | 通用角色库（英文总库） |
| 465 | 安全架构师 | agent | 中文角色库 | `security/security-architect.md` | 安全架构师、威胁建模负责人、对抗式系统思考者 | 是 | 通用角色库（英文总库） |
| 466 | 区块链安全审计师 | agent | 中文角色库 | `security/security-blockchain-security-auditor.md` | 资深智能合约安全审计师与漏洞研究员 | 是 | 通用角色库（英文总库） |
| 467 | 云安全架构师 | agent | 中文角色库 | `security/security-cloud-security-architect.md` | 资深云安全架构师，专精多云安全设计、身份与访问管理（IAM）、基础设施即代码安全，以及合规自动化 | 是 | 通用角色库（英文总库） |
| 468 | 合规审计师 | agent | 中文角色库 | `security/security-compliance-auditor.md` | 技术合规审计师与控制措施评估者 | 是 | 通用角色库（英文总库） |
| 469 | 事件响应专家 | agent | 中文角色库 | `security/security-incident-responder.md` | 资深事件响应专家与数字取证（forensics）分析师，专精数据泄露调查、威胁遏制与危机协调 | 是 | 通用角色库（英文总库） |
| 470 | 渗透测试员 | agent | 中文角色库 | `security/security-penetration-tester.md` | 资深渗透测试员兼红队操盘手，专注于网络、Web 应用与云基础设施的安全评估 | 是 | 通用角色库（英文总库） |
| 471 | 高级安全运营工程师 | agent | 中文角色库 | `security/security-senior-secops.md` | 防御型应用安全工程师，组织安全标准的守护者。你站在开发与安全的交汇点——两种语言你都说得流利，并且拒绝让其中一方牺牲另一方 | 是 | 通用角色库（英文总库） |
| 472 | 威胁检测工程师（安全运营） | agent | 中文角色库 | `security/security-threat-detection-engineer.md` | 检测工程师、威胁猎手、安全运营专家 | 是 | 通用角色库（英文总库） |
| 473 | 威胁情报分析师 | agent | 中文角色库 | `security/security-threat-intelligence-analyst.md` | 高级网络威胁情报分析师，专长在于对手追踪、攻击活动分析、检测工程，以及战略情报产出 | 是 | 通用角色库（英文总库） |
| 474 | macOS Metal 空间工程师 | agent | 中文角色库 | `spatial-computing/macos-spatial-metal-engineer.md` | Swift + Metal 渲染专家，同时精通 visionOS 空间计算 | 是 | 通用角色库（英文总库） |
| 475 | 终端集成专家 | agent | 中文角色库 | `spatial-computing/terminal-integration-specialist.md` | 终端模拟与文本渲染工程师，SwiftTerm 集成专家 | 是 | 通用角色库（英文总库） |
| 476 | visionOS 空间工程师 | agent | 中文角色库 | `spatial-computing/visionos-spatial-engineer.md` | Apple 空间计算平台的原生应用工程师 | 是 | 通用角色库（英文总库） |
| 477 | XR 座舱交互专家 | agent | 中文角色库 | `spatial-computing/xr-cockpit-interaction-specialist.md` | XR 模拟和载具界面的空间座舱设计专家 | 是 | 通用角色库（英文总库） |
| 478 | XR 沉浸式开发者 | agent | 中文角色库 | `spatial-computing/xr-immersive-developer.md` | 全栈 WebXR 工程师，有 A-Frame、Three.js、Babylon.js 和 WebXR Device API 的实战经验 | 是 | 通用角色库（英文总库） |
| 479 | XR 界面架构师 | agent | 中文角色库 | `spatial-computing/xr-interface-architect.md` | AR/VR/XR 界面的空间 UI/UX 设计师 | 是 | 通用角色库（英文总库） |
| 480 | 应付账款智能体 | agent | 中文角色库 | `specialized/accounts-payable-agent.md` | 支付处理、应付账款管理、财务运营 | 是 | 通用角色库（英文总库） |
| 481 | 身份信任架构师 | agent | 中文角色库 | `specialized/agentic-identity-trust.md` | 自主 AI 智能体的身份系统架构师 | 是 | 通用角色库（英文总库） |
| 482 | 智能体编排者 | agent | 中文角色库 | `specialized/agents-orchestrator.md` | 自主工作流流水线管理者和质量编排者 | 是 | 通用角色库（英文总库） |
| 483 | 鉴定评估师 | agent | 中文角色库 | `specialized/authenticity-appraiser.md` | 真伪鉴别要点讲解（奢侈品箱包/腕表/球鞋/文玩）、行情估值框架、成色分级标准、买卖渠道与话术避坑、送检渠道指引。 | 否 | - |
| 484 | 自动化治理架构师 | agent | 中文角色库 | `specialized/automation-governance-architect.md` | 自动化治理架构师 | 是 | 通用角色库（英文总库） |
| 485 | 商业战略家 | agent | 中文角色库 | `specialized/business-strategist.md` | ♟️ 商业战略家 | 是 | 通用角色库（英文总库） |
| 486 | 变革管理顾问 | agent | 中文角色库 | `specialized/change-management-consultant.md` | 🔄 变革管理顾问 | 是 | 通用角色库（英文总库） |
| 487 | 企业培训课程设计师 | agent | 中文角色库 | `specialized/corporate-training-designer.md` | 企业培训体系架构师与课程开发专家 | 是 | 通用角色库（英文总库） |
| 488 | 客户成功经理 | agent | 中文角色库 | `specialized/customer-success-manager.md` | 🌟 客户成功经理 | 是 | 通用角色库（英文总库） |
| 489 | 数据整合师 | agent | 中文角色库 | `specialized/data-consolidation-agent.md` | 实时销售数据整合与仪表盘构建专家 | 是 | 通用角色库（英文总库） |
| 490 | 数据隐私官 | agent | 中文角色库 | `specialized/data-privacy-officer.md` | 企业数据保护官，专长于隐私合规治理、数据测绘与 Article 30 处理记录、DPIA、同意与合法性基础（lawful basis）、数据主体权利、泄露响应、... | 是 | 通用角色库（英文总库） |
| 491 | ESG 与可持续发展官 | agent | 中文角色库 | `specialized/esg-sustainability-officer.md` | 企业可持续发展战略专家与 ESG 信息披露专员，专注于 materiality（重要性）评估、多框架报告、decarbonization 与气候战略、社会影响与... | 是 | 通用角色库（英文总库） |
| 492 | 高考志愿填报顾问 | agent | 中文角色库 | `specialized/gaokao-college-advisor.md` | 中国高考志愿填报全流程策略专家 | 否 | - |
| 493 | 政务数字化售前顾问 | agent | 中文角色库 | `specialized/government-digital-presales-consultant.md` | ToG 项目售前全流程专家，兼具技术深度和商务敏感度 | 是 | 通用角色库（英文总库） |
| 494 | 资助申请撰稿人 | agent | 中文角色库 | `specialized/grant-writer.md` | 📝 资助申请撰稿人 | 是 | 通用角色库（英文总库） |
| 495 | 医疗客服专家 | agent | 中文角色库 | `specialized/healthcare-customer-service.md` | 医疗客服专家 | 是 | 通用角色库（英文总库） |
| 496 | 医疗健康营销合规师 | agent | 中文角色库 | `specialized/healthcare-marketing-compliance.md` | 医疗健康营销合规全流程专家，兼具法规深度和营销实战经验 | 是 | 通用角色库（英文总库） |
| 497 | 酒店宾客服务专家 | agent | 中文角色库 | `specialized/hospitality-guest-services.md` | 酒店宾客服务专家 | 是 | 通用角色库（英文总库） |
| 498 | HR 入职管理专家 | agent | 中文角色库 | `specialized/hr-onboarding.md` | HR 入职管理专家 | 是 | 通用角色库（英文总库） |
| 499 | 身份图谱操作员 | agent | 中文角色库 | `specialized/identity-graph-operator.md` | 多智能体系统的身份解析专家 | 是 | 通用角色库（英文总库） |
| 500 | 语言翻译专家 | agent | 中文角色库 | `specialized/language-translator.md` | 语言翻译专家 | 是 | 通用角色库（英文总库） |
| 501 | 律所计费与工时专家 | agent | 中文角色库 | `specialized/legal-billing-time-tracking.md` | 律所计费与工时专家 | 是 | 通用角色库（英文总库） |
| 502 | 律所客户接案专家 | agent | 中文角色库 | `specialized/legal-client-intake.md` | 律所客户接案专家 | 是 | 通用角色库（英文总库） |
| 503 | 法律文书审查专家 | agent | 中文角色库 | `specialized/legal-document-review.md` | 法律文书审查专家 | 是 | 通用角色库（英文总库） |
| 504 | 养殖档案核对员 | agent | 中文角色库 | `specialized/livestock-archive-auditor.md` | 养殖档案数据核对员、生产日报交叉校验员、批号 FIFO 复核员 | 否 | - |
| 505 | 信贷经理助手 | agent | 中文角色库 | `specialized/loan-officer-assistant.md` | 信贷经理助手 | 是 | 通用角色库（英文总库） |
| 506 | LSP 索引工程师 | agent | 中文角色库 | `specialized/lsp-index-engineer.md` | LSP 客户端编排和语义索引工程专家 | 是 | 通用角色库（英文总库） |
| 507 | M&A 整合经理 | agent | 中文角色库 | `specialized/ma-integration-manager.md` | 并购后整合经理，专精于整合战略、Day 1 就绪、百日计划、synergy 追踪、职能工作流协调、文化整合，以及过渡服务协议(Transition Servic... | 是 | 通用角色库（英文总库） |
| 508 | 医疗账单与编码专员 | agent | 中文角色库 | `specialized/medical-billing-coding-specialist.md` | 🏥 医疗账单与编码专员 | 是 | 通用角色库（英文总库） |
| 509 | 运营经理 | agent | 中文角色库 | `specialized/operations-manager.md` | 业务运营专家，专注于流程（process）梳理与改进、Lean 与 Six Sigma 落地、产能规划、KPI 治理、供应商管理、SOP（标准作业程序）开发、业... | 是 | 通用角色库（英文总库） |
| 510 | 组织心理学家 | agent | 中文角色库 | `specialized/organizational-psychologist.md` | 应用型组织心理学家，专注于 psychological safety、团队效能、burnout 诊断与预防、culture 评估、动机与 engagement（... | 是 | 通用角色库（英文总库） |
| 511 | 个人成长导师 | agent | 中文角色库 | `specialized/personal-growth-mentor.md` | 你是一位跨领域的个人发展导师、战略教练，也是责任督促（accountability）伙伴。你帮助用户改进生活中的各类系统——职业、学习、健康习惯、财务、生产力、... | 是 | 通用角色库（英文总库） |
| 512 | 提示词工程师 | agent | 中文角色库 | `specialized/prompt-engineer.md` | 大语言模型提示词架构师与优化专家 | 否 | - |
| 513 | 房地产经纪助手 | agent | 中文角色库 | `specialized/real-estate-buyer-seller.md` | 房地产经纪助手 | 是 | 通用角色库（英文总库） |
| 514 | 人才获取专家 | agent | 中文角色库 | `specialized/recruitment-specialist.md` | Recruitment operations, talent acquisition, and HR compliance expert | 是 | 通用角色库（英文总库） |
| 515 | 报告分发师 | agent | 中文角色库 | `specialized/report-distribution-agent.md` | 自动化报告分发与邮件投递专家 | 是 | 通用角色库（英文总库） |
| 516 | 零售退货专家 | agent | 中文角色库 | `specialized/retail-customer-returns.md` | 零售退货专家 | 是 | 通用角色库（英文总库） |
| 517 | 销售数据提取师 | agent | 中文角色库 | `specialized/sales-data-extraction-agent.md` | 销售数据提取师 | 是 | 通用角色库（英文总库） |
| 518 | AI 治理政策专家 | agent | 中文角色库 | `specialized/specialized-ai-policy-writer.md` | 企业 AI 合规治理体系的总架构师，兼具技术理解力和法规解读能力 | 否 | - |
| 519 | 土木工程师 | agent | 中文角色库 | `specialized/specialized-civil-engineer.md` | 具有国际项目经验的资深结构与土木工程师 | 是 | 通用角色库（英文总库） |
| 520 | 文化智能策略师 | agent | 中文角色库 | `specialized/specialized-cultural-intelligence-strategist.md` | 你是一台架构级共情引擎。你的工作是在软件上线之前，检测 UI 流程、文案和视觉素材中的"隐性排斥"。 | 是 | 通用角色库（英文总库） |
| 521 | 开发者布道师 | agent | 中文角色库 | `specialized/specialized-developer-advocate.md` | 开发者关系工程师、社区领袖、DX 架构师 | 是 | 通用角色库（英文总库） |
| 522 | 文档生成器 | agent | 中文角色库 | `specialized/specialized-document-generator.md` | 程序化文档创建专家 | 是 | 通用角色库（英文总库） |
| 523 | 法国咨询市场专家 | agent | 中文角色库 | `specialized/specialized-french-consulting-market.md` | 🧠 你的身份与记忆 | 是 | 通用角色库（英文总库） |
| 524 | 韩国商务专家 | agent | 中文角色库 | `specialized/specialized-korean-business-navigator.md` | 🧠 你的身份与记忆 | 是 | 通用角色库（英文总库） |
| 525 | MCP 构建器 | agent | 中文角色库 | `specialized/specialized-mcp-builder.md` | MCP 服务器开发专家 | 是 | 通用角色库（英文总库） |
| 526 | 会议效率专家 | agent | 中文角色库 | `specialized/specialized-meeting-assistant.md` | 企业会议效率体系的设计者和实施教练，兼具流程设计能力和工具运用功底 | 否 | - |
| 527 | 模型 QA 专家 | agent | 中文角色库 | `specialized/specialized-model-qa.md` | 独立模型审计师——你审查别人构建的模型，绝不审查自己的 | 是 | 通用角色库（英文总库） |
| 528 | 定价分析师 | agent | 中文角色库 | `specialized/specialized-pricing-analyst.md` | 专精定价分析师，margin（利润率）优化专家 | 是 | 通用角色库（英文总库） |
| 529 | 动态定价策略师 | agent | 中文角色库 | `specialized/specialized-pricing-optimizer.md` | 电商动态定价与促销策略专家 | 否 | - |
| 530 | 企业风险评估师 | agent | 中文角色库 | `specialized/specialized-risk-assessor.md` | 企业全面风险管理体系的设计师和实施顾问，兼具宏观视角和落地能力 | 否 | - |
| 531 | Salesforce 架构师 | agent | 中文角色库 | `specialized/specialized-salesforce-architect.md` | 🧠 你的身份与记忆 | 是 | 通用角色库（英文总库） |
| 532 | 策略对决推演师 | agent | 中文角色库 | `specialized/specialized-strategy-duel-agent.md` | 策略编排者与对决主裁 | 是 | 通用角色库（英文总库） |
| 533 | 工作流架构师 | agent | 中文角色库 | `specialized/specialized-workflow-architect.md` | 工作流设计、发现与系统流程规格说明专家 | 是 | 通用角色库（英文总库） |
| 534 | 留学规划顾问 | agent | 中文角色库 | `specialized/study-abroad-advisor.md` | 多国别、多学位层次的留学申请全流程规划专家 | 是 | 通用角色库（英文总库） |
| 535 | 技术翻译专家 | agent | 中文角色库 | `specialized/technical-translator-agent.md` | 技术文档翻译专家、术语管理顾问 | 否 | - |
| 536 | 旅行规划师 | agent | 中文角色库 | `specialized/travel-planner.md` | 行程设计专家，覆盖国内游与出境游的路线编排、交通与住宿组合、签证/证件与出行文件、预算分配、亲子/老人/蜜月等不同客群的节奏适配、旺季与突发状况预案。 | 否 | - |
| 537 | ZK 管家 | agent | 中文角色库 | `specialized/zk-steward.md` | AI 时代的 Niklas Luhmann——把复杂任务转化为**知识网络的有机组成部分**，而非一次性答案。 | 是 | 通用角色库（英文总库） |
| 538 | 服装工厂规划工程师 | agent | 中文角色库 | `supply-chain/supply-chain-garment-factory-planning-engineer.md` | 服装工厂规划工程师. | 否 | - |
| 539 | 库存预测专家 | agent | 中文角色库 | `supply-chain/supply-chain-inventory-forecaster.md` | 供应链库存预测与补货策略专家 | 否 | - |
| 540 | 物流路线优化师 | agent | 中文角色库 | `supply-chain/supply-chain-route-optimizer.md` | 物流路线规划与配送网络优化专家 | 否 | - |
| 541 | 供应链采购策略师 | agent | 中文角色库 | `supply-chain/supply-chain-strategist.md` | 供应链管理、战略采购与供应商关系专家 | 否 | - |
| 542 | 供应商评估专家 | agent | 中文角色库 | `supply-chain/supply-chain-vendor-evaluator.md` | 供应商评估与采购决策策略专家 | 否 | - |
| 543 | 数据分析师 | agent | 中文角色库 | `support/support-analytics-reporter.md` | 数据分析、可视化和商业智能专家 | 是 | 通用角色库（英文总库） |
| 544 | 高管摘要师 | agent | 中文角色库 | `support/support-executive-summary-generator.md` | 资深战略顾问与高管沟通专家 | 是 | 通用角色库（英文总库） |
| 545 | 财务追踪员 | agent | 中文角色库 | `support/support-finance-tracker.md` | 财务规划、分析与经营绩效专家 | 是 | 通用角色库（英文总库） |
| 546 | 基础设施运维师 | agent | 中文角色库 | `support/support-infrastructure-maintainer.md` | 系统可靠性、基础设施优化与运营专家 | 是 | 通用角色库（英文总库） |
| 547 | 法务合规员 | agent | 中文角色库 | `support/support-legal-compliance-checker.md` | 法律合规、风险评估和监管合规专家 | 是 | 通用角色库（英文总库） |
| 548 | 招聘运营专家 | agent | 中文角色库 | `support/support-recruitment-specialist.md` | 招聘运营、人才获取与HR合规专家 | 否 | - |
| 549 | 客服响应者 | agent | 中文角色库 | `support/support-support-responder.md` | 客户服务卓越、问题解决和用户体验专家 | 是 | 通用角色库（英文总库） |
| 550 | 无障碍审核员 | agent | 中文角色库 | `testing/testing-accessibility-auditor.md` | 无障碍审核、辅助技术测试、包容性设计验证专家 | 是 | 通用角色库（英文总库） |
| 551 | API 测试员 | agent | 中文角色库 | `testing/testing-api-tester.md` | 具有安全关注的 API 测试和验证专家 | 是 | 通用角色库（英文总库） |
| 552 | 嵌入式测试工程师 | agent | 中文角色库 | `testing/testing-embedded-qa-engineer.md` | 确保嵌入式系统从固件到硬件的全链路质量，覆盖开发测试到量产测试 | 否 | - |
| 553 | 证据收集者 | agent | 中文角色库 | `testing/testing-evidence-collector.md` | 测试证据工程师与质量审计员 | 是 | 通用角色库（英文总库） |
| 554 | 性能基准师 | agent | 中文角色库 | `testing/testing-performance-benchmarker.md` | 性能测试工程师与容量规划师 | 是 | 通用角色库（英文总库） |
| 555 | 现实检验者 | agent | 中文角色库 | `testing/testing-reality-checker.md` | 最终集成测试和现实部署就绪性评估 | 是 | 通用角色库（英文总库） |
| 556 | 测试结果分析师 | agent | 中文角色库 | `testing/testing-test-results-analyzer.md` | 测试数据分析与质量情报专家，擅长统计分析 | 是 | 通用角色库（英文总库） |
| 557 | 工具评估师 | agent | 中文角色库 | `testing/testing-tool-evaluator.md` | 技术评估与工具选型专家，关注投入产出比 | 是 | 通用角色库（英文总库） |
| 558 | 工作流优化师 | agent | 中文角色库 | `testing/testing-workflow-optimizer.md` | 流程改进与自动化专家，有系统思维 | 是 | 通用角色库（英文总库） |
| 559 | accessibility | agent | 工程专家人设库 | `personas/accessibility.md` | Inclusive Design & WCAG Compliance Specialist | 否 | - |
| 560 | ai-engineer | agent | 工程专家人设库 | `personas/ai-engineer.md` | Machine Learning & AI Systems Specialist | 否 | - |
| 561 | analyzer | agent | 工程专家人设库 | `personas/analyzer.md` | Root Cause Analysis & Investigation Specialist | 否 | - |
| 562 | architect | agent | 工程专家人设库 | `personas/architect.md` | Systems Design Specialist | 否 | - |
| 563 | backend | agent | 工程专家人设库 | `personas/backend.md` | Server-Side Development Specialist | 否 | - |
| 564 | code-reviewer | agent | 工程专家人设库 | `personas/code-reviewer.md` | Code Reviewer Persona | 否 | - |
| 565 | devops | agent | 工程专家人设库 | `personas/devops.md` | Infrastructure Automation & Deployment Specialist | 否 | - |
| 566 | documentation | agent | 工程专家人设库 | `personas/documentation.md` | Technical Writing & Knowledge Management Specialist | 否 | - |
| 567 | frontend | agent | 工程专家人设库 | `personas/frontend.md` | UI/UX Development Specialist | 否 | - |
| 568 | mentor | agent | 工程专家人设库 | `personas/mentor.md` | Educational Guidance & Knowledge Transfer Specialist | 否 | - |
| 569 | mobile | agent | 工程专家人设库 | `personas/mobile.md` | iOS/Android Development Expert | 否 | - |
| 570 | performance | agent | 工程专家人设库 | `personas/performance.md` | Optimization & Efficiency Specialist | 否 | - |
| 571 | persona-architect | agent | 工程专家人设库 | `personas/persona-architect.md` | AI Agent Persona Design & Optimization Specialist | 否 | - |
| 572 | prompt-engineer | agent | 工程专家人设库 | `personas/prompt-engineer.md` | Advanced LLM Optimization & Prompt Design Specialist | 否 | - |
| 573 | qa | agent | 工程专家人设库 | `personas/qa.md` | Quality Assurance & Testing Specialist | 否 | - |
| 574 | refactor | agent | 工程专家人设库 | `personas/refactor.md` | Code Quality & Technical Debt Management Specialist | 否 | - |
| 575 | security | agent | 工程专家人设库 | `personas/security.md` | Cybersecurity & Threat Modeling Specialist | 否 | - |
| 576 | sre | agent | 工程专家人设库 | `personas/sre.md` | Site Reliability Engineering Specialist | 否 | - |
| 577 | technical-program-manager | agent | 工程专家人设库 | `personas/technical-pm.md` | Cross-Functional Coordination Specialist | 否 | - |
| 578 | ui-designer | agent | 工程专家人设库 | `personas/ui-designer.md` | Visual Design Systems & Interface Aesthetics Specialist | 否 | - |
| 579 | ux-researcher | agent | 工程专家人设库 | `personas/ux-researcher.md` | User Experience Research & Analytics Specialist | 否 | - |
| 580 | code-reviewer | agent | 评审专家人设库 | `agents/code-reviewer.md` | Senior Code Reviewer | 否 | - |
| 581 | security-auditor | agent | 评审专家人设库 | `agents/security-auditor.md` | Security Auditor | 否 | - |
| 582 | test-engineer | agent | 评审专家人设库 | `agents/test-engineer.md` | Test Engineer | 否 | - |
| 583 | web-performance-auditor | agent | 评审专家人设库 | `agents/web-performance-auditor.md` | Web Performance Auditor | 否 | - |
| 584 | api-and-interface-design | 工作流技能 | 评审专家人设库 | `skills/api-and-interface-design/SKILL.md` | API and Interface Design | 否 | - |
| 585 | browser-testing-with-devtools | 工作流技能 | 评审专家人设库 | `skills/browser-testing-with-devtools/SKILL.md` | Browser Testing with DevTools | 否 | - |
| 586 | ci-cd-and-automation | 工作流技能 | 评审专家人设库 | `skills/ci-cd-and-automation/SKILL.md` | CI/CD and Automation | 否 | - |
| 587 | code-review-and-quality | 工作流技能 | 评审专家人设库 | `skills/code-review-and-quality/SKILL.md` | Code Review and Quality | 否 | - |
| 588 | code-simplification | 工作流技能 | 评审专家人设库 | `skills/code-simplification/SKILL.md` | Code Simplification | 否 | - |
| 589 | constraint-driven-development | 工作流技能 | 评审专家人设库 | `skills/constraint-driven-development/SKILL.md` | Constraint-Driven Development | 否 | - |
| 590 | context-engineering | 工作流技能 | 评审专家人设库 | `skills/context-engineering/SKILL.md` | Context Engineering | 否 | - |
| 591 | debugging-and-error-recovery | 工作流技能 | 评审专家人设库 | `skills/debugging-and-error-recovery/SKILL.md` | Debugging and Error Recovery | 否 | - |
| 592 | deprecation-and-migration | 工作流技能 | 评审专家人设库 | `skills/deprecation-and-migration/SKILL.md` | Deprecation and Migration | 否 | - |
| 593 | documentation-and-adrs | 工作流技能 | 评审专家人设库 | `skills/documentation-and-adrs/SKILL.md` | Documentation and ADRs | 否 | - |
| 594 | doubt-driven-development | 工作流技能 | 评审专家人设库 | `skills/doubt-driven-development/SKILL.md` | Doubt-Driven Development | 否 | - |
| 595 | frontend-ui-engineering | 工作流技能 | 评审专家人设库 | `skills/frontend-ui-engineering/SKILL.md` | Frontend UI Engineering | 否 | - |
| 596 | git-workflow-and-versioning | 工作流技能 | 评审专家人设库 | `skills/git-workflow-and-versioning/SKILL.md` | Git Workflow and Versioning | 否 | - |
| 597 | idea-refine | 工作流技能 | 评审专家人设库 | `skills/idea-refine/SKILL.md` | Idea Refine | 否 | - |
| 598 | incremental-implementation | 工作流技能 | 评审专家人设库 | `skills/incremental-implementation/SKILL.md` | Incremental Implementation | 否 | - |
| 599 | interview-me | 工作流技能 | 评审专家人设库 | `skills/interview-me/SKILL.md` | Interview Me | 否 | - |
| 600 | observability-and-instrumentation | 工作流技能 | 评审专家人设库 | `skills/observability-and-instrumentation/SKILL.md` | Observability and Instrumentation | 否 | - |
| 601 | performance-optimization | 工作流技能 | 评审专家人设库 | `skills/performance-optimization/SKILL.md` | Performance Optimization | 否 | - |
| 602 | planning-and-task-breakdown | 工作流技能 | 评审专家人设库 | `skills/planning-and-task-breakdown/SKILL.md` | Planning and Task Breakdown | 否 | - |
| 603 | security-and-hardening | 工作流技能 | 评审专家人设库 | `skills/security-and-hardening/SKILL.md` | Security and Hardening | 否 | - |
| 604 | shipping-and-launch | 工作流技能 | 评审专家人设库 | `skills/shipping-and-launch/SKILL.md` | Shipping and Launch | 否 | - |
| 605 | source-driven-development | 工作流技能 | 评审专家人设库 | `skills/source-driven-development/SKILL.md` | Source-Driven Development | 否 | - |
| 606 | spec-driven-development | 工作流技能 | 评审专家人设库 | `skills/spec-driven-development/SKILL.md` | Spec-Driven Development | 否 | - |
| 607 | test-driven-development | 工作流技能 | 评审专家人设库 | `skills/test-driven-development/SKILL.md` | Test-Driven Development | 否 | - |
| 608 | using-agent-skills | 工作流技能 | 评审专家人设库 | `skills/using-agent-skills/SKILL.md` | Using Agent Skills | 否 | - |
