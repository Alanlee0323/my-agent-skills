# Built-in Capability Gap Analysis — 2026-07-04

- 目的：盤點 Claude Code 內建能力 vs 本庫差集，將可移植的方法論納入庫中
- 執行者：Claude Fable 5（最終 session）；方法：`researching-deeply` 差集比對
- 結果：**納入 5 個新 skill（庫規模 50 → 55）**，排除 9 項並記錄理由

## 納入決策（5 項）

| 新 skill | 來源內建能力 | 分組 | 納入 bundle |
|---|---|---|---|
| `verifying-changes` | verify / run | engineer（品質三閘門 1/3） | engineer |
| `reviewing-code-changes` | code-review | engineer（品質三閘門 2/3） | engineer |
| `simplifying-code` | simplify | engineer（品質三閘門 3/3） | engineer |
| `visualizing-data` | dataviz | shared（跨領域） | engineer + finance + career |
| `initializing-agent-context` | init | shared（跨領域） | engineer |

**品質三閘門順序約定**：功能完成 → `verifying-changes`（證明存在）→
`reviewing-code-changes`（找缺陷）→ `simplifying-code`（清品質）→ commit。
此順序已註記於 `bundles/engineer.yaml`。

## 排除決策（9 項，附理由——未來重新評估時先讀這裡）

| 內建能力 | 排除理由 |
|---|---|
| security-review | 與 `auditing-code` 職責重疊；避免路由歧義。若未來安全深度不足，擴充 auditing-code 而非另立 skill |
| plan mode | `planning-implementation` 已覆蓋 |
| run | 併入 `verifying-changes` 的 runtime surface 表格，不獨立成 skill |
| loop / schedule | harness 綁定（Claude Code 排程機制），違反庫的 agent-agnostic 原則 |
| update-config / keybindings | Claude Code 設定檔專屬，無跨 agent 可移植性 |
| fewer-permission-prompts | 同上，權限系統為 harness 專屬 |
| artifact-design | 綁定 claude.ai Artifact 平台；通用視覺原則已被 `visualizing-data` 吸收 |
| claude-api | 供應商專屬參考文件；庫的模型路由已由 `using-minimax` 承擔 |
| 子代理編排（Agent tool） | 多 agent 協作已由 bundles/profiles 架構承擔；harness 差異太大不宜固化 |

## 蒸餾原則（本次遵循，未來納入外部方法論時沿用）

1. **蒸餾而非複製**：以自己的話寫方法論本質，不搬運原文（版權 + 上下文差異）。
2. **agent-agnostic 化**：移除 harness 專屬機制，保留任何 agent 可執行的紀律。
3. **在地化增值**：加入原版沒有的本庫脈絡（如台美市場紅綠慣例相反、與既有 skill 的分工聲明）。
4. **走完整 DoD**：frontmatter/Evolution Log（含觸發事件）/SKILL_AUDIT/bundle/路由/validator/index。

## 未償債務（併入下次定期稽核）

- [ ] `visualizing-data` 補 stdlib 色彩對比檢查腳本（見其 SKILL_AUDIT 建議）
- [ ] storytelling 兩 skill 的 Resources 區交叉引用 `visualizing-data`
- [ ] 品質三閘門實戰 1–2 次後，把摩擦點寫回各自 Evolution Log
