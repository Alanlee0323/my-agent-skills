# agent-bootstrap Deployment Audit — 2026-07-05

- 對象：`C:/Users/alana/SideProjects/agent-bootstrap`（本 skill 庫的官方部署工具鏈，即 External Toolchain Registry 標記 TODO 的本體）
- 方法：`researching-deeply` + `verifying-changes`——全部關鍵發現皆經**實際執行**驗證，非靜態閱讀
- 實測環境：Windows 11、Git Bash、Python 3.13；以更新後的 55-skill 庫做端到端部署
- 結論：**WARN**——編譯器與排程器核心可用（55 skill 庫實測相容），但 4 個 CONFIRMED 功能缺陷中有 2 個會在這台主力機上直接打斷部署，且「最後一哩」尚未接線

## 已確認發現（依影響排序，全部 CONFIRMED）

### 1. [Critical] 兩層覆寫的「同名去重」未實作
- 宣稱：兩個 repo 的 README 均稱「同名 identifier 去重：第一個被掃到的贏（project-local 覆寫 global）」
- 實測：在目標專案建立 `skills/stress-testing-portfolio/SKILL.md` 覆寫後執行排程，**同名 skill 出現兩次**（override score=84、global score=55 並列輸出）
- 根因：`services/skill_scheduler.py` `load()` 對兩層目錄的結果無條件 `append`，全檔無任何 identifier 去重
- 影響：覆寫語意失效；agent 可能讀到被覆寫的 global 版；重複項浪費 read budget
- 佐證：官方測試套件中無任何 override/dedup 測試（負空間）
- 建議修法：`load()` 以 identifier 建 dict，先掃者贏 + 補測試

### 2. [Critical/Windows] `bootstrap_agent.sh` 的 python3 解析踩中 MS Store 假 stub
- 實測：`command -v python3` → `WindowsApps/python3`（stub），執行 exit 49 且零輸出；`resolve_python_cmd` 優先選 python3 → compile/state/health check 全數靜默失敗，只留下無診斷的「Adapter compile failed」
- 對照：`bootstrap_agent.bat` 順序正確（`py -3` → `python` → `python3`）——雙腳本已漂移
- 影響：Windows + Git Bash 使用者（含本機）走 .sh 必失敗且無法從錯誤訊息定位
- 建議修法：.sh 改為先驗證直譯器可執行（如 `"$cmd" -c "import sys"`）再採用；錯誤時附帶底層 stderr

### 3. [High] `--clean-stale` 由設計即失效
- 實測：`pytest tests/` → `test_reconcile_cleans_stale_files_and_writes_state` FAIL（1 failed, 12 passed）
- 根因：`bootstrap_state.py` 的 `current_generated` 是**掃磁碟現況**——殘留舊檔本來就在磁碟上，`previous - current` 恆為空，永遠判定無 stale。屬演算法錯誤，非平台問題
- 連帶發現：主幹測試紅燈存在 → **此 repo 無 CI 把關**
- 建議修法：reconcile 應接收「本輪實際寫出的檔案清單」（compiler 已回傳 written list）作為 current，而非掃碟

### 4. [Medium] 兩個 frontmatter parser 均不支援 `description: |` 區塊
- 實測：編譯產物 `AGENTS.generated.md` 第 68 行為「`` - `using-minimax`: | ``」——旗艦路由 skill 在所有編譯 prompt 中無描述、排程關鍵字流失
- 位置：`compiler/spec_loader.py:_parse_frontmatter` 與 `services/skill_scheduler.py:_parse_frontmatter`
- 緩解：my-agent-skills 側已將 using-minimax description 改為單行（commit 於本日）；parser 仍建議修復或明文禁止區塊寫法

### 5. [Medium] 最後一哩未接線：編譯產物沒有任何 CLI 會自動讀取
- 事實：產物寫入 `.agent/<adapter>/<bundle>/`，但 Codex 讀根目錄 `AGENTS.md`、Copilot 讀 `.github/copilot-instructions.md`、Gemini 讀 `GEMINI.md`；launcher 只 export 環境變數並 echo，無任何程式消費 `PROMPT_FILE`
- 現況：bootstrap 複製到根目錄的 `AGENTS.md` 是靜態通用版（非 bundle 特化、hardcode max reads=3，與 finance bundle 的 5 矛盾）
- 影響：「部署完成」後 agent 實際載入的不是編譯出的 bundle prompt——需人工貼接，抵銷「快速部署」的核心價值
- 建議修法：compile 後將產物寫到（或連結到）各 CLI 原生位置，或於根 AGENTS.md 動態嵌入 bundle 區塊

### 6. [Medium] 注入目標專案的檔案有副作用
- `tests/test_skill_scheduler.py` 被複製進目標專案 → 目標的 pytest 會收集執行，污染其 CI
- `--upgrade` 強制 `--force` → 會覆寫使用者已客製的根 `AGENTS.md`
- exclude 策略不一致：`.git/info/exclude` 涵蓋 AGENTS.md/scheduler/skills，但**不含 `.agent/`** → 產物+state 檔會出現在 git status
- 協作面注意：exclude 走 `.git/info/exclude`（不入版控）＝每位隊友都必須自己跑 bootstrap；這是設計選擇，但 README 的「Best for team/onboarding」敘述未說明此前提

### 7. [Minor] 其他
- Windows 主控台 zh 輸出亂碼（scheduler 未 reconfigure utf-8；參考 my-agent-skills `tools/validate_skills.py` 的做法）
- 文件漂移：README 領域清單缺 `career`；AGENTS.md 路由範例用舊名（`planning`、`brainstorming`、`cicd-skills`）
- 雙腳本 .bat/.sh 各 ~600 行重複維護，漂移已發生（見發現 2）；建議收斂為單一 Python 編排器 + 薄殼
- repo 衛生：`__pycache__/*.pyc` 已入版控、根目錄殘留 `pytest-cache-files-*`、`.tmp-pytest-local`

## 正面確認（值得保留的設計）

- 兩段式排程（索引粗排 → read-budget 內精讀 triggers）與 zh n-gram 匹配：實測「壓力測試 黑天鵝」正確路由到 `stress-testing-portfolio`，global-rules 37 條路由 hint 全數解析
- intent whitelist 由 bundle 編譯而來（55-skill 庫的 25 個 finance intent 完整進 whitelist）
- IR + manifest + state 的可稽核產物鏈、`--upgrade` 狀態恢復、`--dry-run`
- compiler 對 bundle 引用缺失 skill 的 fail-fast 驗證（與 my-agent-skills validator 形成雙保險）

## 與 my-agent-skills 的整合驗證結果

- 55-skill 庫 + 新 career bundle + bundle 註解 → compiler 全數相容 ✓
- 本日已在 my-agent-skills 側修復兩項部署相容性債務：
  - tone-example 目錄縮短（Windows 260 字元路徑上限，實測 clone checkout 失敗後修復）
  - using-minimax description 改單行（繞開 parser 缺陷）

## 建議修復優先序（agent-bootstrap 側）

1. `.sh` python 解析修復（本機部署路徑直接被打斷）
2. scheduler 同名去重 + 測試（核心宣稱功能）
3. `--clean-stale` 改用本輪寫出清單 + 讓現有測試轉綠 + 加 CI（pytest + e2e smoke）
4. 最後一哩接線（產物 → 各 CLI 原生讀取位置）
5. 停止注入 tests/ 至目標專案；exclude 補 `.agent/`；`--upgrade` 覆寫前備份 AGENTS.md
6. 雙腳本收斂為 Python 編排器；文件同步（career、新 skill 名、python 疑難排解）
