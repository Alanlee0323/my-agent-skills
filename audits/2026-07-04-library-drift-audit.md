# Library Drift Audit — 2026-07-04

- 執行者：Claude Fable 5（最後一次 Fable session，方法論已固化至 `researching-deeply`）
- 範圍：全庫（當時 49 個 skill）＋ readme / global-rules / bundles / policies / profiles
- 方法：`researching-deeply` 流程——先測繪、跨文件一致性比對、負空間分析、自我規則檢驗
- 結論：**WARN**——架構設計優良，但 24→49 成長期間無偵測機制，累積 7 項漂移
- 後續：全部發現已於 commit `7e67092` 修復；本檔為證據基線，供未來稽核比對

## 已確認發現（依影響排序，均為 CONFIRMED）

### 1. 路由名稱與 skill name 不一致（路由失效）
- 證據：`global-rules.md:35` 路由 `storytelling-financial-analysis-vincent`，但 frontmatter name 為 `translating-financial-analysis-vincent-style`
- 影響：以 name 為 identifier 的 scheduler 會 miss 此路由
- 修復：frontmatter name 改為與資料夾/路由一致

### 2. MANDATORY 路由的 skill 不在 bundle 內（治理矛盾）
- 證據：`global-rules.md:30` 規定投資分析前必跑 `scanning-macro-news` + `monitoring-geopolitical-risk`，但 `bundles/finance.yaml` 僅 12 個 skill，缺這兩個及另外 11 個被路由的 finance skill
- 影響：由 bundle 編譯的 finance agent 無法遵守強制規則
- 修復：finance bundle 擴充至 25 個 skill

### 3. readme 索引過期且含 5 條斷鏈
- 證據：inventory 表僅 24 列（實際 49）；`readme.md:58-59` 連結指向已改名的 `skills/meta/gemini-skill-creator/`、`gemini-skill-reviewer/`
- 修復：改為生成式 `SKILL_INDEX.md`（CI 驗證同步）＋修復連結

### 4. skill 引用不存在的核心語料（有殼無魂）
- 證據：兩個 storytelling skill 引用 `tone-example/Vincent-Cheng-Wen-Yu/*.md`、`tone-example/Xie-mong-gung/*.md`，目錄不存在
- 影響：風格傳承的知識本體缺失
- 修復：建立佔位 README 標記 TODO；**語料仍待使用者補入**

### 5. using-minimax 上次修正不完整
- 證據：commit `4a446fe` 改預設模型為 M2.7，但 SKILL.md 的 curl 範例與 audit log 範例仍是 `MiniMax-Text-01`（同文件明言 Token Plan 不支援）
- 修復：兩處殘留清除

### 6. 識別子三重不一致（folder ≠ name ≠ 檔名大小寫）
- 證據：7 個 skill 資料夾名 ≠ frontmatter name（brainstorming、planning、cicd-skills、skill-creator、skill-reviewer、兩個 storytelling）；3 個檔案為小寫 `skill.md`
- 影響：不符 Anthropic skill 規格（name == 目錄名）；Linux/CI 上大小寫敏感會失效
- 修復：統一改名；validator 永久檢查

### 7. Review gate 未被執行（負空間發現）
- 證據：reviewer skill 要求每個新 skill 產出 `SKILL_AUDIT.md`，實際 49 個 skill 僅 2 個有
- 影響：品質閘門形同虛設
- 修復：validator + DoD 制度化；歷史欠審記錄於此，增量補審

## 結構性缺口（比單點發現更重要）

- A. **無一致性驗證機制** → 已建 `tools/validate_skills.py`（11 項檢查）＋ CI
- B. **核心工具鏈未版控**（`skill_scheduler.py`、`agent-bootstrap` 在 repo 外）→ 已登記於 `maintaining-skill-library` External Toolchain Registry，vendor 仍為 TODO
- C. **skill 無演化履歷** → 已建 Evolution Log 規範（version + 觸發事件）
- D. **領域分類溢出**（6 個留學/職涯 skill 在 finance/）→ 已分拆 `skills/career/`
- E. **未接入 Claude Code**（`~/.claude/skills/`）→ TODO，name 統一後已可直接掛載

## 未償債務清單（下次稽核先查這裡）

- [ ] tone-example 語料補入（使用者個人知識，無法代寫）
- [ ] `skill_scheduler.py` / `agent-bootstrap` vendor 或記錄 canonical repo
- [ ] 擴充後 finance bundle 依 `FINANCE_BUNDLE_AUDIT.md` 格式重審
- [ ] 歷史 skill 的 SKILL_AUDIT.md 增量補審（47 個欠審）
- [ ] 掛載至 Claude Code personal skills
