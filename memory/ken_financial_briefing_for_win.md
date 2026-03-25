# Ken Tam — Financial Profile Briefing for Win
*Prepared by Jade (Ken's Personal AI Assistant)*
*Date: 2026-03-25*

---

## 👤 About Ken

- **Full Name:** Ken Tam (譚國偉)
- **Location:** San Francisco, California
- **Timezone:** Pacific Daylight Time (PDT, GMT-7)
- **Language:** English primary; Traditional Chinese (繁體中文) — never Simplified
- **Status:** Semi-retired. Daughter Vanessa runs the family business; Ken handles the books.
- **Life philosophy:** Lifelong learner. Privacy-conscious. Thoughtful decision-maker.
- **Family:** Wife Mabel (朱德貞, cancer survivor — relevant to one investment category), daughter Vanessa, son Preston.

---

## 🏢 Excel Plumbing Supply + Showroom

### Company Overview
- **Name:** Excel Plumbing Supply + Showroom (TAMXL dba)
- **Address:** 659 South Van Ness Avenue, San Francisco, CA 94110
- **Phone:** 415-863-8889 | **Fax:** 415-863-8870
- **Email:** payable@excel-plumbing.com
- **Specialty:** Luxury plumbing fixtures (bathroom/kitchen)
- **Building owner:** Ken himself, via **659 SVN LLC** (leases to the business)

### Key People
| Name | Role |
|---|---|
| **Ken Tam** | Owner / Bookkeeper (architect of financial systems) |
| **Vanessa Tam** (daughter) | Operations Lead — runs day-to-day |
| **Travis Tran** (Vanessa's husband) | Operations Co-Lead — ex-Intuit, QB-savvy |
| **Mabel Tam** (Ken's wife) | Daily QB entries, payroll, deposits, Epicor postings |
| **Sisi / Jade** | AI Bookkeeper Assistant (ACH processing, anomaly monitoring) |

### Contact Info
- Vanessa: vanessa@excel-plumbing.com | 415-830-1995
- Travis: travis@excel-plumbing.com | 415-671-9388
- Mabel: accounting@excel-plumbing.com | 415-218-2368

---

## 🏦 Financial System Architecture

### Core Principle: Epicor = Truth. QuickBooks = Utility.
- **Epicor Eclipse (ERP):** ALL official financial data — balance sheet, P&L, tax returns, inventory, POs, vendor invoices. The one source of truth.
- **QuickBooks Online Plus:** Bank reconciliation + payroll ONLY. Not the primary financial record — a support tool.

### 5 Wells Fargo Bank Accounts

| Account | Purpose | Check Writing? |
|---|---|---|
| **WF Reserve** | Central cash holding — no transactions direct | ❌ |
| **WF Deposit** | Inbound deposits only (cash, check, ACH in) | ❌ |
| **WF General** | Main operating: payroll, bills, rent | ✅ (QuickBooks) |
| **WF ACH Payment** | Vendor ACH payments via Routable | ❌ |
| **WF Vendor Payment** | Physical vendor checks (backup/fallback) | ✅ (Epicor) |

**Why 5 accounts:** Fraud protection. Prior check fraud incident devastated operations for 6+ months. Two separate check-writing accounts = instant switchover if one is compromised.

### Current Account Balances (as of 2026-03-16 snapshot)
| Account | Type | Balance |
|---|---|---|
| WF Reserve | Checking | $350,145 |
| WF Deposit | Checking | $51,168 |
| WF General | Checking | $102,792 |
| WF ACH Remittance | Checking | $417,171 |
| WF Vendor Payment | Checking | $20,060 |
| Routable Balance Clearing | Cash | $25,948 |
| Fidelity Financial-Investment | Money Market | $2,799,000 |
| Fidelity MM-1 (0182) | Money Market | $460,427 |
| Citi-Costco Visa | Credit Card | -$20,748 |

---

## 💳 ACH Payment Workflow (Weekly — Sundays)

**Flow:**
```
Epicor (vendor invoices) → Ken selects → CSV exported
→ Jade corrects CSV (date format, payment ID, remove total row)
→ Ken uploads to Routable.com → ACH sent to vendors
→ Routable auto-posts to QuickBooks ✅
```

**Routable Payment Account ID:** `3d309cb1-71a6-4b98-940e-5e7f6c3eac09`

**CSV corrections Jade makes:**
- Date format: MM/DD/YYYY → YYYY-MM-DD
- "Payment from*" column: must use formatted Routable ID (lowercase, with dashes)
- Remove the grand total row at the bottom

**Sample batch size:** ~$367K/batch, 17–20 vendors (Toto USA, Hansgrohe, Robern/Kohler, Graff, Franke, California Faucets, etc.)

---

## 📊 QuickBooks Setup

- **Version:** QuickBooks Online Plus
- **Realm ID:** 1399277115
- **OAuth app:** SisiBookkeeper (Production)
- **QB API limitation:** ClearedStatus is READ-ONLY — cannot auto-accept bank feed matches via API. Ken/Mabel do this manually (~30 sec/day).
- **Refresh token expiry:** ~2026-06-25 (must renew before then)
- **Daily task scope:** WF Reserve, WF Deposit, WF General, WF ACH, WF Vendor Payment accounts only
- **DO NOT touch:** Fidelity accounts, Citi-Costco Visa, WF Business Line of Credit, closed accounts

**Fraud Alert Rule:** WF Deposit is INBOUND ONLY. Any outbound transaction = immediate fraud alert to Mabel + Vanessa + Travis.

---

## 📈 Hong Kong Stock Portfolio

*Last updated: 2026-03-13*

**Total Value:** ~HKD 11.75M (~USD 1.51M)
- Stocks: HKD ~11.19M (41 positions)
- Funds: HKD ~553K (3 funds)

### Top Holdings (by market value)
| Code | Name | Shares | HKD Value | Return |
|---|---|---|---|---|
| 02899 | Zijin Mining | 30,000 | 1,147,800 | +212% |
| 00100 | MiniMax | 820 | 828,200 | +231% |
| 00700 | Tencent | 1,200 | 657,000 | +48% |
| 01211 | BYD | 6,000 | 580,500 | +14% |
| 00388 | HKEX | 1,100 | 441,540 | +14% |
| 00981 | SMIC | 7,500 | 466,500 | +120% |
| 02269 | WuXi Biologics | 12,500 | 431,500 | +44% |
| 02513 | Zhipu AI | 800 | 424,000 | +134% |
| 09988 | Alibaba-W | 3,200 | 424,000 | -4% |
| 00941 | China Mobile | 5,000 | 399,750 | +23% |

### Funds
| Fund | HKD Value | Return |
|---|---|---|
| BlackRock World Energy Fund | 135,688 | +34% |
| BlackRock World Mining Fund | 307,223 | +53% |
| Taekang HKD Money Market | 110,558 | ~0% |

### Positions Needing Attention (losses)
- **Zhuzi Bio -59%** (HKD 71K) — consider stop-loss
- **Zai Lab -50%** (HKD 29K) — consider stop-loss
- **Kingdee -40%**, **Xiaomi -39%**, **JD.com -36%** — larger losses, monitor

### ⭐ Special Rule — Biotech Holdings (DO NOT recommend selling)
Ken holds several biotech stocks for deeply personal reasons — his wife Mabel is a cancer survivor and he wants to support cancer drug R&D regardless of financial returns. **Never suggest exiting these positions unless Ken explicitly asks:**
- 02269 WuXi Biologics, 09926 Kineta Bio, 06160 BeiGene, 01801 Innovent Bio, 09688 Zai Lab (ovarian cancer drugs — most important), 06185 CanSino Bio, 01276 Hengrui, 01093 CSPC

---

## 🤖 AI Investment Thesis

**Ken's Core View:**
- AI software's marginal cost → zero (unlike manufacturing)
- China: manufacturing base + AI tools + 1.4B consumers = explosive productivity
- AI Agents = the highest conviction play right now

**Portfolio Layers:**

**Tier 1 — Pure AI Models (Highest Conviction)**
- MiniMax (00100): +231%, 820 shares — #1 global Token usage, clear API monetization
- Zhipu AI (02513): +134%, 800 shares — GLM + Enterprise AI Agent, JPMorgan Overweight

**Tier 2 — AI Distribution Platforms**
- Tencent (00700): WeChat = 1.4B user AI Agent gateway
- Kuaishou (01024): -21%, 2,000 shares — Kling AI video undervalued globally

**Tier 3 — AI Cloud Infrastructure (Watching)**
- Alibaba (09988): Qwen + cloud, but AI monetization slow
- Baidu (09888): +42%, 2,500 shares — ⚠️ Long-term risk from AI cannibalizing its own search

**Strategy:**
- Concentrate, don't diversify — add to winners on pullbacks
- Consider reducing Baidu → rotate into MiniMax/Zhipu
- No new positions needed; increase size in right stocks

---

## 🏠 Real Estate / Ownership Notes
- **659 SVN LLC:** Ken owns the building at 659 S Van Ness Ave, SF
- Excel Plumbing (TAMXL) leases the building from Ken's LLC
- Rent flows: written from WF General → Ken as building owner
- Additional real estate / family property details — check with Ken directly

---

## 🔑 Key Credentials Note (for Win's awareness)
- QB OAuth tokens stored in `/workspace/qb_tokens.txt` (chmod 600, server-side)
- QB credentials in Ken's 1Password vault: "Sisi - Quickbooks Login"
- Routable: accessed via Ken's login — Jade processes CSVs but Ken uploads
- **Do not store credentials in memory files or shared documents**

---

## 📝 Jade's Notes for Win

1. **Ken is deeply thoughtful.** He built these systems carefully over years. If something seems odd, ask — there's usually a reason.
2. **Mabel's biotech holdings are sacred.** Never touch them without Ken's explicit direction.
3. **Ken's primary language is English** but he appreciates Traditional Chinese (never Simplified) for formal/family matters.
4. **Semi-retired posture:** Ken deliberately stays out of daily ops. Don't escalate routine things to him.
5. **Fraud sensitivity is HIGH** — prior fraud experience. Any anomaly in WF Deposit outflows = immediate multi-party alert.
6. **QB refresh token expires ~2026-06-25** — this needs attention before then.
7. **Epicor is the source of truth**, not QuickBooks. Never treat QB as the authoritative financial record.

---

*Prepared by Jade 💚 — Ken's personal AI assistant*
*For questions about this briefing, Ken can loop in Jade directly.*
