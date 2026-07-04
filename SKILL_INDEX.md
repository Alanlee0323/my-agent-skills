# Skill Index

> **此檔案由 `tools/generate_skill_index.py` 自動生成**，
> 請勿手動編輯；修改 skill frontmatter 後重新執行腳本（CI 會驗證同步）。

共 **50** 個 skill。

## Shared（跨領域共用）（4）

| Skill | Version | Description |
|---|---|---|
| [`creating-skills-from-knowledge-folder`](skills/shared/creating-skills-from-knowledge-folder/SKILL.md) | — | Creates new agent skills from a user-specified knowledge folder. Use when the user asks to convert notes, docs, templates, or domain references into reusable SKILL.md packages. |
| [`researching-deeply`](skills/shared/researching-deeply/SKILL.md) | 1.0.0 | Systematic deep-investigation methodology for auditing codebases, evaluating systems, and researching complex questions. Enforces breadth-first mapping, claim-evidence disciplin... |
| [`using-minimax`](skills/shared/using-minimax/SKILL.md) | 2.0.0 | 以 Minimax 作為主力執行者處理絕大多數任務（草稿、實作、分析初版）， Copilot / Codex 僅擔任 Review Gate——審查 Minimax 輸出、標記偏差、 執行最終糾錯——以最小高階 token 消耗確保品質。 |
| [`writing-technical-docs`](skills/shared/writing-technical-docs/SKILL.md) | — | Use this skill when creating, rewriting, structuring, or reviewing technical documentation in Chinese. Suitable for 技術文件, 文件撰寫, 教學文件, 操作指南, 架構說明, API 文件, README 重構, and troubles... |

## Meta（技能開發與治理）（3）

| Skill | Version | Description |
|---|---|---|
| [`creating-agent-skills`](skills/meta/creating-agent-skills/SKILL.md) | — | Expert system for generating Agent Skills compatible with any LLM agent (Copilot, Gemini, Codex, Claude, etc.). Enforces folder structure, YAML standards, and best practices. |
| [`maintaining-skill-library`](skills/meta/maintaining-skill-library/SKILL.md) | 1.0.0 | Governance loop for this skill library. Defines the single-source-of-truth map, the validation workflow, the definition of done for adding or changing skills, the evolution-log ... |
| [`reviewing-agent-skills`](skills/meta/reviewing-agent-skills/SKILL.md) | — | Acts as a QA Auditor and Red Team for new Agent Skills. Verifies structure, safety guardrails, and compliance with global-rules. |

## Engineer（工程）（14）

| Skill | Version | Description |
|---|---|---|
| [`auditing-code`](skills/engineer/auditing-code/SKILL.md) | — | Performs static analysis, security scanning, and code quality auditing to detect vulnerabilities, secrets, and anti-patterns. |
| [`brainstorming-product-design`](skills/engineer/brainstorming-product-design/SKILL.md) | — | Acts as a Socratic Product Manager to explore, clarify, and define new application ideas. Use when the user has a vague idea, wants to "brainstorm", or asks to "design this app". |
| [`conducting-postmortem`](skills/engineer/conducting-postmortem/SKILL.md) | — | Implements a systematic Incident Review & Skill Evolution loop. Analyzes project failures or debugging outcomes to identify systemic gaps and updates `skills/` to prevent recurr... |
| [`debugging-code`](skills/engineer/debugging-code/SKILL.md) | — | Systematic Root-Cause Analysis (RCA) and debugging protocol. Forces system awareness through `DEBUG_CONTEXT.md` and Mermaid diagrams before any code modification. |
| [`evaluating-models`](skills/engineer/evaluating-models/SKILL.md) | — | General framework for evaluating Machine Learning models across Computer Vision, NLP, and Classical ML. Provides data-driven insights and benchmarks performance against baselines. |
| [`handling-review`](skills/engineer/handling-review/SKILL.md) | — | Use when receiving code review feedback to enforce engineering rigor. Ensures feedback is verified, understood, and technically evaluated before implementation, preventing perfo... |
| [`instrumenting-observability`](skills/engineer/instrumenting-observability/SKILL.md) | — | Professional pre-release observability hardening. Implements structured logging, traceability (trace_id), and decision-reason logging using a strict Allowlist-first redaction po... |
| [`managing-cicd-workflow`](skills/engineer/managing-cicd-workflow/SKILL.md) | — | Professional trunk-based development with branch-for-release workflow. Focuses on automation, environment isolation, and immutable releases via tags. |
| [`managing-environment`](skills/engineer/managing-environment/SKILL.md) | — | Infrastructure Architect and Guardian of Reproducibility. Balances "Docker-First" for complex apps with "Venv-Efficiency" for lightweight projects. |
| [`planning-implementation`](skills/engineer/planning-implementation/SKILL.md) | — | Converts approved designs or detailed requirements into actionable, atomic implementation steps. Use when the user approves a design or asks "how to implement". |
| [`sdd-driven-development`](skills/engineer/sdd-driven-development/SKILL.md) | — | Guides Specification-Driven Development (SDD) from ambiguous requests to clear, testable specs before coding. Use when the user asks for 規格驅動開發, spec-first workflow, 先寫規格再寫程式, o... |
| [`using-dvc`](skills/engineer/using-dvc/SKILL.md) | — | Provides commands and patterns for Data Version Control (DVC). Use when the user asks about versioning large files, creating pipelines, or reproducing experiments. |
| [`using-mlflow`](skills/engineer/using-mlflow/SKILL.md) | — | Provides MLflow documentation covering Tracking, Projects, Models, and Registry. Use when the user asks about MLflow features, APIs, implementation, or debugging. |
| [`using-ultralytics`](skills/engineer/using-ultralytics/SKILL.md) | — | Expert system for Ultralytics YOLO workflows (including YOLO26). Use when the user asks about training, validation, inference, dataset setup, model export, tracking, or performa... |

## Finance（金融投資）（23）

| Skill | Version | Description |
|---|---|---|
| [`analyzing-business-quality`](skills/finance/analyzing-business-quality/SKILL.md) | — | Evaluates long-horizon business quality using durable economics, governance signals, and capital allocation behavior. Use when the user asks about moat, quality, or long-term co... |
| [`analyzing-macro-regime`](skills/finance/analyzing-macro-regime/SKILL.md) | — | Interprets macroeconomic regime shifts and links them to sector and valuation implications. Use when the user asks about inflation, rates, growth cycles, policy stance, or macro... |
| [`analyzing-market-expectations`](skills/finance/analyzing-market-expectations/SKILL.md) | — | 解讀市場隱含預期（估值、利率期貨、選擇權、信用利差），比對用戶觀點與市場共識的差距，找出「預期差」——這是超額報酬的真正來源。解決「只看基本面不看市場已定價多少」的盲點。 |
| [`attributing-portfolio-performance`](skills/finance/attributing-portfolio-performance/SKILL.md) | — | 對投資組合的績效進行多層歸因分析（Alpha/Beta 分離、技能層歸因、決策品質評分），並將結論回饋至上游技能以驅動系統自我進化。這是整條分析鏈的「閉環終端」——沒有它，系統只會重複犯同樣的錯誤。 |
| [`collecting-market-data`](skills/finance/collecting-market-data/SKILL.md) | — | 主動收集即時市場數據（股價、大宗商品、匯率、債券殖利率、波動率指標），確保所有估值與組合分析都基於最新數據而非過時快照。 |
| [`conducting-investment-postmortem`](skills/finance/conducting-investment-postmortem/SKILL.md) | — | Performs post-mortem analysis on investment decisions to improve long-term process quality. Use when a thesis fails, underperforms expectations, or requires systematic process u... |
| [`constructing-forward-scenarios`](skills/finance/constructing-forward-scenarios/SKILL.md) | — | 建構前瞻性情境推演，將「現在的宏觀現實」延伸為「未來 3-12 個月的多路徑演化」，並產出機率加權的最佳配置建議。與 stress-testing-portfolio（防守導向）互補，本技能聚焦於進攻性的戰略站位。 |
| [`managing-long-term-investment-policy`](skills/finance/managing-long-term-investment-policy/SKILL.md) | — | Defines and maintains long-term investment policy guardrails. Use when the user asks for portfolio discipline, rebalancing rules, risk limits, or decision frameworks for multi-y... |
| [`monitoring-geopolitical-risk`](skills/finance/monitoring-geopolitical-risk/SKILL.md) | — | 評估地緣政治事件（戰爭、制裁、貿易衝突、供應鏈斷裂）對金融資產的傳導機制與影響路徑。當宏觀掃描偵測到地緣政治紅色警報時使用。 |
| [`normalizing-financial-statements`](skills/finance/normalizing-financial-statements/SKILL.md) | — | Standardizes raw financial statements into a consistent analysis schema. Use when the user asks for ratio analysis, trend comparison, or cross-company financial comparison. |
| [`parsing-sec-filings`](skills/finance/parsing-sec-filings/SKILL.md) | — | Extracts structured facts from SEC filings and earnings documents. Use when the user mentions 10-K, 10-Q, 8-K, EDGAR, MD&A, risk factors, or filing-based financial analysis. |
| [`planning-financial-analysis`](skills/finance/planning-financial-analysis/SKILL.md) | — | Translates financial research questions into an executable analysis plan. Use when the user asks how to analyze a company, macro theme, or investment thesis in a structured and ... |
| [`reviewing-financial-analysis`](skills/finance/reviewing-financial-analysis/SKILL.md) | — | Audits financial analysis outputs for evidence quality, assumption integrity, and bias control. Use when the user asks to review, challenge, or validate a thesis before decision... |
| [`scanning-macro-news`](skills/finance/scanning-macro-news/SKILL.md) | — | 在執行任何投資分析或組合調整之前，主動上網搜尋當前宏觀經濟與地緣政治重大事件。這是一個「閘門技能」——確保所有下游分析都建立在最新現實之上，而非過時假設。 |
| [`scanning-thematic-opportunities`](skills/finance/scanning-thematic-opportunities/SKILL.md) | — | 主動掃描新興投資主題與結構性趨勢，在用戶提出研究需求之前識別潛在機會。解決「只能被動研究已知題材」的盲點，讓分析鏈從「你問我答」進化為「我主動發現」。 |
| [`sizing-portfolio-positions`](skills/finance/sizing-portfolio-positions/SKILL.md) | — | 將分析結論轉化為具體的倉位規模（Position Sizing）與風控參數（停損/證偽點）。解決「看對但賺不到錢」的執行斷層——在分析鏈（report）與實際下單之間，提供數學化的資金分配與動態風控框架。 |
| [`storytelling-financial-analysis-vincent`](skills/finance/storytelling-financial-analysis-vincent/SKILL.md) | — | Translates evidence-backed financial research into structured Traditional Chinese narrative with Vincent-like long-form explanatory cadence. Use when the user asks for education... |
| [`storytelling-financial-analysis-xie`](skills/finance/storytelling-financial-analysis-xie/SKILL.md) | — | Translates evidence-backed financial research into high-energy Traditional Chinese market storytelling with Xie-like cadence. Use when the user asks for podcast scripts, social ... |
| [`stress-testing-portfolio`](skills/finance/stress-testing-portfolio/SKILL.md) | — | 對投資組合執行情境式壓力測試，量化特定宏觀事件（戰爭升級、油價飆升、央行意外決議、科技泡沫破裂）對持倉的預估影響。將「定性擔憂」轉化為「量化損益估算」。 |
| [`tracking-catalyst-calendar`](skills/finance/tracking-catalyst-calendar/SKILL.md) | — | 建立並維護滾動式催化劑日曆，追蹤所有可能觸發持倉標的「重新定價」的事件與時間點。解決「知道標的被低估但不知道何時反映」的時機問題，讓投資決策從「我覺得便宜」進化為「便宜且即將有催化劑確認」。 |
| [`validating-financial-data`](skills/finance/validating-financial-data/SKILL.md) | — | 在數據收集（collecting-market-data, scanning-macro-news）與分析鏈之間的強制驗證閘門。執行三層數據品質檢核：多源交叉對標、統計異常偵測、LLM 邏輯與真實性審查。遵循「Garbage In, Garbage Out」原則——所有下游分析的品質上限取決於此技能。 |
| [`valuing-company`](skills/finance/valuing-company/SKILL.md) | — | Builds transparent valuation ranges using scenario-based DCF and market multiple checks. Use when the user asks for intrinsic value, fair value range, margin of safety, or valua... |
| [`verifying-financial-conclusions`](skills/finance/verifying-financial-conclusions/SKILL.md) | — | Verifies financial conclusions against primary web sources such as official company investor-relations pages and regulatory filings. Use when the user asks to fact-check analysi... |

## Career（留學與職涯）（6）

| Skill | Version | Description |
|---|---|---|
| [`benchmarking-alumni`](skills/career/benchmarking-alumni/SKILL.md) | — | 分析目標學程的校友 5-10 年職涯路徑——職位、公司、薪資級距、地理分佈。用於驗證「這個學位真的能帶你到想去的地方」。 |
| [`comparing-visa-policies`](skills/career/comparing-visa-policies/SKILL.md) | — | 追蹤並比較各國工作簽證政策——畢業後留任路徑、續簽門檻、永居條件。用於評估留學目的地的長期可行性。 |
| [`evaluating-career-roi`](skills/career/evaluating-career-roi/SKILL.md) | — | 計算不同學校 × 地區組合的留學財務 ROI——包含學費、機會成本、稅後薪資、複利終值。用於量化「這筆教育投資到底划不划算」。 |
| [`planning-application`](skills/career/planning-application/SKILL.md) | — | 管理留學申請的完整時間軸——從準備考試到拿到 offer 的全流程 checklist。用於確保不遺漏關鍵截止日期。 |
| [`researching-programs`](skills/career/researching-programs/SKILL.md) | — | 系統性研究目標學校的 AI/MLOps/AI Infra 碩士學程——課程結構、師資、研究方向、產學合作、校友出路。用於選校決策前的資訊收集。 |
| [`scanning-job-market`](skills/career/scanning-job-market/SKILL.md) | — | 掃描目標市場的 AI Infra / MLOps 職缺趨勢——薪資帶、技能需求、企業類型、成長性。用於評估留學目的地的就業前景。 |

