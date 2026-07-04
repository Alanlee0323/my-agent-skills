# Skill Audit: visualizing-data

## 🚦 Verdict: PASS

- 審核日期：2026-07-04｜依據：Gauntlet 標準 + `tools/validate_skills.py` 通過

## 🛡️ Security & Safety
- [x] Protocol Guardian：圖表誠信區不可協商（軸截斷=說謊、雙 Y 軸預設禁用、來源+截止日必標）
- [x] Destructive Protection：N/A（產出型 skill）

## 🏗️ Structural Integrity
- YAML Name / 資料夾一致：Valid｜Evolution Log：Present（含觸發事件）

## 🐛 Vulnerabilities Found
1. [Medium] 台股紅漲綠跌 vs 美股綠漲紅跌的在地化規則，若輸出對象市場未知可能誤用 → 已要求圖例明示，但 agent 仍需主動確認讀者市場
2. [Minor] 無隨附可執行的色彩驗證工具（原生 dataviz 有 validator），色盲安全檢查依賴外部工具

## 💡 Recommendations
- 未來可在 `resources/` 補一個 stdlib 色彩對比檢查腳本，把色盲/對比檢查機械化
- 金融輸出鏈（storytelling → 本 skill）建議在 storytelling skill 的 Resources 區交叉引用
