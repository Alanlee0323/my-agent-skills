---
name: comparing-visa-policies
description: 追蹤並比較各國工作簽證政策——畢業後留任路徑、續簽門檻、永居條件。用於評估留學目的地的長期可行性。
---

# Comparing Visa Policies

## When to use this skill
- 當使用者問「英國畢業後能留多久」
- 當需要比較不同國家的工作簽證難度
- 當需要評估簽證政策對職涯選擇的限制
- 當簽證政策有重大更新時，觸發重新評估

## Workflow

### 1. Plan
- 確認比較對象（國家清單）
- 確認使用者身份（台灣護照持有者、碩士畢業）
- 確認關注面向（畢業留任、轉換雇主、永居路徑、配偶簽）

### 2. Collect
- 查詢官方移民局網站：
  - 🇬🇧 UK: gov.uk (Graduate Route, Skilled Worker Visa)
  - 🇸🇬 SG: MOM.gov.sg (Employment Pass, S Pass, PEP)
  - 🇺🇸 US: USCIS (OPT, H-1B, EB-2/3)
  - 🇦🇺 AU: homeaffairs.gov.au (485 visa, 189/190)
  - 🇨🇦 CA: IRCC (PGWP, Express Entry)
- 查詢政策變動新聞（最近 6 個月）
- 查詢台灣人特殊通道（如 SG-TW 雙邊協定）

### 3. Compare
- 按統一維度建立比較矩陣
- 標註政策的「確定性」（已立法 vs 提案中 vs 傳聞）
- 計算「最差情境」（政策收緊時的退路）

### 4. Validate
- 所有資訊須來自官方來源或 Tier 1 移民律師事務所
- 標註資訊查詢日期（簽證政策變動頻繁）
- 若有衝突資訊，以官方為準

## Instructions

- 永遠標註「截至 YYYY-MM-DD」因為簽證政策變動快
- 區分「理論上可以」和「實務上容易拿到」
- 考慮配偶/家庭因素（配偶工作權、子女教育）
- 薪資門檻要換算為台幣以便比較
- 特別注意「隱藏條件」（如 UK 的 Immigration Health Surcharge、SG 的 COMPASS 評分）

### 比較維度清單
- [ ] 畢業後自動工作權（年限 + 條件）
- [ ] 工作簽證類型與薪資門檻
- [ ] 轉換雇主難度
- [ ] 永居/PR 路徑與時間
- [ ] 配偶工作權
- [ ] 稅務居民身份影響
- [ ] 投資帳戶維持（能否繼續用 IBKR）
- [ ] 回台退路（簽證失敗後的 B 計劃）
- [ ] 政策穩定性評分（近 3 年變動頻率）

### Output template

```markdown
## 簽證政策比較：<Country A> vs <Country B>

> 截至 YYYY-MM-DD

### 畢業後留任
| 維度 | 🇬🇧 UK | 🇸🇬 SG |
|------|--------|--------|
| 自動工作權 | Graduate Route 2 年 | 無（需 EP） |
| 工作簽薪資門檻 | £38,700/yr | S$5,000/mo |
| 申請成功率 | ~90% | ~80% |
| 轉換雇主 | 需重新 sponsor | EP 綁公司 |

### 永居路徑
| 維度 | 🇬🇧 UK | 🇸🇬 SG |
|------|--------|--------|
| 最快年限 | 5 年 | 2 年（可申請） |
| 條件 | ILR: 薪資+居住 | PR: COMPASS 加分 |

### 風險評估
| 風險 | 🇬🇧 UK | 🇸🇬 SG |
|------|--------|--------|
| 政策收緊趨勢 | 🔴 高 | 🟡 中 |
| 最差情境 | ... | ... |

### 結論
> <推薦 + 理由>
```

## Error handling
- 若政策正在修訂中，標註「pending legislation」並給出可能的方向
- 若無法確認台灣護照的特殊待遇，建議直接聯繫移民律師
- 若政策最近 6 個月有重大變動，觸發全面重新評估

## Resources
- `researching-programs` — 學校所在國家的簽證政策
- `evaluating-career-roi` — 簽證影響留任機率 → 影響 ROI
- `scanning-job-market` — 薪資是否達到簽證門檻
