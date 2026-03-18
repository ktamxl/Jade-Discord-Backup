# Excel Plumbing Supply + Showroom — Company Profile
*Bookkeeper's Reference File — Ken Tam*
*Created: 2026-03-15*

## Contact Information

| Field | Details |
|---|---|
| **Company Name** | Excel Plumbing Supply + Showroom |
| **Address** | 659 South Van Ness Avenue, San Francisco, CA 94110 |
| **Phone** | 415-863-8889 |
| **Fax** | 415-863-8870 |
| **Email** | payable@excel-plumbing.com |
| **Website** | https://excel-plumbing.com |

## Hours of Operation

### Plumbing Counter
| Day | Hours |
|---|---|
| Monday – Friday | 7:30 AM – 5:00 PM |
| Saturday | 9:00 AM – 4:00 PM |
| Sunday | Closed |

### Showroom
| Day | Hours |
|---|---|
| Monday – Friday | 9:00 AM – 5:00 PM |
| Saturday | 9:00 AM – 4:00 PM |
| Sunday | Closed |

*(Note: Current posted hours show 9AM–4PM M–F, appointments recommended)*

## Business Overview
- Specialty: Luxury plumbing fixtures, supply, and showroom
- Focus: Bathroom and kitchen fixtures — modern/contemporary
- Tagline: "Build your dream bathroom and make a statement"
- Appointment scheduling: https://calendly.com/excelsfshowroom/

## Bookkeeping Notes
- Timezone: **Pacific Time (PT) — San Francisco**
  - Currently PDT (GMT-7), Daylight Saving active
- All dates/payments/deadlines must be tracked in **San Francisco local time**
- Vendor payment dates are date-critical — never miss or guess
- Website credit: Kwok Design (kwokdesign.com)

## Key Reminders for Bookkeeper
- Sunday: Always closed — no deliveries/transactions to expect
- Vendor payments: confirm exact due dates in PT
- All entries timestamped in PST/PDT

## Routable ACH — Payment Account ID

| Field | Value |
|---|---|
| **Raw (Epicor output)** | `3D309CB171A64B98940E5E7F6C3EAC09` |
| **Formatted (Routable required)** | `3d309cb1-71a6-4b98-940e-5e7f6c3eac09` |

**Rule:** Every CSV uploaded to Routable.com must have the "Payment from*" column set to the formatted (lowercase, dashes) version.
Epicor exports it without dashes and uppercase — always convert before sending.

## QuickBooks API Setup — IN PROGRESS (2026-03-16)

### Status: ✅ Compliance Questionnaire SUBMITTED (2026-03-16)
Ken is setting up QB API access for Sisi. Resume from where we left off if session crashes.

### What's Done ✅
- QB version confirmed: **QuickBooks Online Plus**
- Intuit Developer account created (same email as QB)
- App created: **SisiBookkeeper** → Production keys
- Hosted pages deployed: `https://aq4iz9e8vh5x.space.minimax.io`
  - EULA: `/eula.html`
  - Privacy: `/privacy.html`
  - Redirect/callback: `/` (index.html)
- App profile filled: host domain, launch URL, disconnect URL, connect URL, IP
- Compliance questionnaire: ~80% complete

### Questionnaire Answers Already Submitted
- Legal counsel: No (internal private app)
- Security policies: Yes
- App purpose: Both checkboxes (enhance QB + facilitate business process)
- Generative AI: Yes — internal bookkeeping automation, no training
- QB data for training: No
- Built with: MaxClaw platform (Web/SaaS)
- App type: Private, admin-only
- Platforms: Epicor Eclipse + Routable.com
- Auth tested: Yes
- Token refresh: Only on expiry
- API category: Accounting only
- API frequency: Daily + on-demand
- QB version: Plus only
- Multi-currency/tax: None of the above
- Webhooks: No | CDC: No
- Error handling: Yes (all)
- intuit_tid: Yes | Logs: Yes | Support: payable@excel-plumbing.com
- Client ID/Secret stored securely: Yes (server-side env vars, never hardcoded or browser-exposed)
- MFA: No (private internal app, admin-only, no end-user login portal)
- Security breach: No
- Security team: No (small private business, internal app)
- Captcha: No (no user-facing login portal)
- WebSocket: No (REST API polling only)
- Data shown to others: No (QB data used only by Ken's internal bookkeeping system)

### Next Steps (Resume Here if Crash)
- ✅ Questionnaire submitted (2026-03-16)
- ✅ Production Client ID + Secret received (2026-03-16)
- ✅ Credentials saved in 1Password: "Sisi - Quickbooks Login" (Ken's vault)
- ✅ Credentials stored in /workspace/qb_credentials.txt (server, chmod 600)
- ✅ OAuth flow complete! Access token + Refresh token obtained (2026-03-16)
- ✅ QB API LIVE — confirmed: "Excel Plumbing Supply + Showroom", 659 S Van Ness Ave, San Francisco
- Realm ID: 1399277115
- Tokens stored: /workspace/qb_tokens.txt (chmod 600)
- Refresh token expires: ~2026-06-25 (must renew before then)

### URLs (Keep These!)
- Legal pages: `https://aq4iz9e8vh5x.space.minimax.io`
- Redirect URI: `https://aq4iz9e8vh5x.space.minimax.io/`
- Server IP: `47.253.4.207` (US/California, Alibaba Cloud)

## Daily Task: Bank Feed Matching (WF Accounts Only)

### How it works
- QB bank feed auto-downloads new transactions every day
- They appear under **Bank Transactions tab** as "For Review"
- Green button "1 Match Found" = QB found an existing QB entry that matches the bank transaction
- My job: accept all green "1 Match Found" buttons for WF accounts ONLY

### Scope: WF Accounts to Monitor Daily
1. WF Reserve Account (ID: 269)
2. WF Deposit Account (ID: 206)
3. WF General Remittance (ID: 268)
4. WF ACH Remittance Acct (ID: 600)
5. WF Vendor Payment Acct (ID: 601)

### DO NOT TOUCH
- Fidelity accounts (Investment/MM)
- Citi-Costco Visa
- WF Business Line of Credit
- Routable Balance Clearing
- Any CLOSED accounts

### ✅ Solution: QB Auto-Post (Auto-Add) Bank Rules
QB has a built-in feature to automatically accept matched transactions without manual review.
- Feature name: **Auto-post rule** (also called Auto-add)
- When a transaction matches the rule conditions → QB auto-confirms it, bypasses "For Review" entirely
- Badge: shows "AUTO" instead of "RULE" in the Category column
- Setup: Transactions > Bank Transactions > Rules > New Rule > toggle "Automatically confirm transactions this rule applies to"
- Works for: recurring, predictable transactions (payroll, vendor payments, ACH, etc.)
- Ken to set up Auto-post rules → eliminates the green button task entirely.

| QB Name | Type | ID | Balance |
|---|---|---|---|
| WF Reserve Account | Checking | 269 | $350,145 |
| WF Deposit Account | Checking | 206 | $51,168 |
| WF General Remittance | Checking | 268 | $102,792 |
| WF ACH Remittance Acct | Checking | 600 | $417,171 |
| WF Vendor Payment Acct | Checking | 601 | $20,060 |
| Routable Balance Clearing | Cash | 603 | $25,948 |
| Fidelity Financial-Investment | MoneyMarket | 586 | $2,799,000 |
| Fidelity MM-1 (0182) | MoneyMarket | 633 | $460,427 |
| Citi-Costco Visa | Credit Card | 594 | -$20,748 |
| WF Business Line of Credit | Credit Card | 529 | $0 |
| WF Vendor (CLOSED) Acct | Checking | 194 | -$130 (closed) |
- Excel Plumbing uses **QuickBooks Online Plus** (confirmed 2026-03-16)
- QuickBooks Online has a full REST API supporting: bills, bill payments, journal entries, vendors, accounts, invoices, payments, reports
- Intuit Developer API requires OAuth 2.0 (Client ID + Secret + Company/Realm ID)
- Can be connected directly via QB API or via Composio middleware
- Pending: Ken to confirm QB Online vs Desktop, and get OAuth credentials from admin

---

## System Architecture — The Hybrid Design (Ken's Explanation, 2026-03-15)

### Principle: Epicor = Truth. QuickBooks = Utility.
- **Epicor Eclipse**: ALL true financial data. Balance sheet, P&L, tax returns, inventory, POs, vendor invoices — the ONE source of truth.
- **QuickBooks**: Bank reconciliation + payroll ONLY. Not the financial record. A support tool.

---

### 5 Wells Fargo Bank Accounts (All in QuickBooks)

| Account | Purpose | Check Writing? | Notes |
|---|---|---|---|
| **WF Reserve** | Central holding account | ❌ No | All CC transactions auto-deposit here. WF Deposit transfers here when accumulated. Minimum balance kept. |
| **WF Deposit** | Cash, check, ACH deposits in | ❌ No | Deposits only. Sweeps to WF Reserve when enough accumulated. |
| **WF General** | Main operating account | ✅ YES | Payroll checks, auto CC payments (Costco Visa only), rent, all company expenses. |
| **WF ACH Payment** | Vendor ACH payments via Routable | ❌ No | For inventory suppliers + service vendors (e.g. Epicor). Data flows: Epicor → CSV → Sisi → Routable → auto-posts to QB. |
| **WF Vendor Payment** | Physical checks to vendors only | ✅ YES (backup) | For vendors that don't accept ACH or small Canadian vendor transactions. Backup if WF General compromised. |

**Why 5 accounts? Fraud protection.**
- Check fraud happened before. Devastated operations for 6+ months.
- Two checking accounts (WF General + WF Vendor Payment) = if one is compromised, shut it down and immediately switch to the other. Zero AP disruption.
- WF Reserve = no checks = cannot be defrauded via paper checks.

---

### Data Flow Summary

**WF ACH Payment (Routable flow):**
```
Epicor (vendor invoices) → Ken selects payments → CSV exported
→ Sisi corrects CSV (dates, payment ID, remove total row)
→ Ken uploads to Routable.com → ACH sent to vendors
→ Routable auto-posts transactions to QuickBooks ✅
→ No manual QB entry needed for ACH payments
```

**WF General (QB Bank Rec):**
- Ken runs custom QB reports showing ALL checks for the month (cleared + uncleared)
- Posts by CATEGORY TOTALS, not individual transactions (e.g. total wages, total utilities, total car expense)
- QB ending balance vs Epicor = only uncleared checks outstanding (small amount)
- Perfect for tax audit: drill down to detail reports in QB anytime

**WF Reserve / WF Deposit:**
- Post by day total matching bank statement
- Any deposit not cleared by month-end → moved to next month in QB (e.g. last day of month deposit that posts next day = 1st of next month)

**Epicor Deposit flow (Mabel's workflow):**
- Mabel posts deposits to **"Unreconciled Deposit"** account in Epicor (NOT directly to WF Reserve)
- This holds all deposits in a clearing account
- Ken does monthly data posting → clears Unreconciled Deposit → posts clean totals
- **Why:** Avoids Ken having to chase $1.00 posting errors in Epicor transaction by transaction
- **Also:** Keeps Ken and Mabel's work separated cleanly → no 子午沖 triggers 🙏

---

### Ownership Structure Note
- **659 SVN LLC**: Ken Tam is the owner of the building at 659 S Van Ness Ave
- **TAMXL dba Excel Plumbing Supply + Showroom**: Leases the building FROM 659 SVN LLC
- Rent payment: Written from WF General to Ken as building owner

---

### Payroll
- Handled entirely in QuickBooks (Epicor has no payroll module)
- Mabel processes payroll, Ken corrects errors
- Payroll checks written from WF General
- Ken created custom QB reports on WF General for all checks by month

---

### Financial Statements
- **ALL official financials come from Epicor** (P&L, Balance Sheet, tax returns)
- QB balance sheet only reflects bank account balances (not true company financials)
- Ken produces financial statements from Epicor → sends to Vanessa monthly

---

### Sisi's Role in This System
1. ✅ **Weekly (Sunday SF time):** Process ACH CSV from Epicor, return corrected file for Routable upload
2. 🔜 **Future:** Read payable email (payable@excel-plumbing.com) for vendor correspondence
3. 🔜 **Future:** QuickBooks access (read-only to start) for bank rec support
4. 🔜 **Future:** Epicor API access (when cloud migration happens)

---

### People
- **Ken**: Architect of the whole system. Month-end/year-end accounting. Bank rec. Financial statements. System corrections. Building owner (659 SVN LLC).
- **Mabel (朱德貞)**: Daily operations. Payroll processing. Deposits. Epicor deposit postings to Unreconciled account.
- **Vanessa**: Runs business operations. Receives financial statements from Ken.
- **Sisi**: Bookkeeper assistant. ACH CSV processing. Growing role.

---

### Fidelity Investment Accounts
- Ken has Fidelity investment accounts — to be covered in a future session.

---

## AP Flow — Confirmed (2026-03-16)

### WF Vendor Payment — Full Cycle (Epicor owns this entirely)
```
PO issued in Epicor
→ Goods received into inventory in Epicor
→ Vendor invoice matched to PO in Epicor
→ Check printed FROM Epicor (WF Vendor Payment account)
→ Check mailed to vendor
→ Check clears bank → appears in QB bank feed
→ Ken reconciles in QB (no re-entry, just matching)
```
- QB never prints these checks — Epicor does
- QB only sees the cleared transaction for bank rec purposes

### Non-PO Expenses (utilities, rent, small bills) — WF General
```
Bill received / auto-pay triggers
→ Payment from WF General (check or auto-pay)
→ Ken posts category TOTALS in QB (not individual transactions) for bank rec
→ Ken posts ONE summary entry into Epicor at month-end
→ Epicor financial statements remain accurate without seeing every small bill
```

### Summary: Who Prints Checks
| Account | Checks Printed From |
|---|---|
| WF General | QuickBooks |
| WF Vendor Payment | Epicor Eclipse |
| WF ACH Payment | Routable (no checks) |
| WF Reserve | No checks ever |
| WF Deposit | No checks ever |

---

## Sisi's QB Duties — Confirmed Setup (2026-03-16)

### QB Access
- Method: TBD — accountant invite via payable@excel-plumbing.com (pending email setup)
- Scope: ALL 5 WF accounts + credit card account + investment account (Fidelity — to be discussed later)
- WF Reserve is highest priority — largest cash flows + all inter-account transfers

### Daily Task: Review & Accept Matched Transactions
- Green button = matched correctly → accept/confirm
- Sitting unmatched 2+ days → notify Mabel
- Unmatched reasons:
  1. Amount mismatch (e.g. $5,132.12 vs $5,132.10) → Mabel corrects QB entry
  2. Customer ACH inbound to WF Deposit → Mabel must post to specific order in Epicor first, then QB
  3. OUTBOUND on WF Deposit (inbound-only account) = FRAUD ALERT → notify Mabel + Vanessa + Travis immediately

### Fraud Alert Protocol
- WF Deposit = inbound ONLY. Any outbound = RED FLAG.
- Chargebacks and returned checks = treat as potential fraud
- Reason: customer may pick up goods while disputing payment
- Alert ALL 3: Mabel, Vanessa, Travis — immediately, no delay

### Notification Method
- Group text/SMS to all 3 (Mabel, Vanessa, Travis) simultaneously
- They can reply to the group to coordinate ("I'm on it", "already handled", etc.)
- One-way notification OK — they don't need to respond to Sisi directly
- Contact details: TBD (pending Ken providing phone numbers)

### Monthly Task: WF General Summary Spreadsheet
- Group all WF General transactions by category
- Total each category
- Deliver formatted spreadsheet to Ken
- Ken enters totals into his Epicor monthly WF GEN template (same categories every month)
- Category list: Ken will provide initial list; new/unknown categories → ask Ken
- Most new transactions will already be assigned categories via QB matching

### Team Members (to be formally introduced later)
- **Mabel** (朱德貞): Daily operations, payroll, deposits, QB entries, Epicor deposit postings
- **Vanessa**: Runs business operations, receives financial statements
- **Travis**: Role TBD (Ken to discuss after this session)
- Contact info for all 3: pending

---

## Team Directory — Excel Plumbing Supply + Showroom

| Name | Role | Notes |
|---|---|---|
| **Ken Tam** (譚國偉) | Owner / Bookkeeper | Architect of the system. Handles books, financial statements, monthly reconciliation. Intentionally steps back from daily ops. |
| **Vanessa Tam** (譚穎珊) | Operations Lead | Ken's daughter. Runs the business day-to-day. Receives monthly financial statements from Ken. |
| **Travis Tran** | Operations Co-Lead | Vanessa's husband. Helps run operations alongside Vanessa. Previously worked at Intuit — understands accounting software well. |
| **Mabel Tam** (朱德貞) | Office / Bookkeeper Support | Ken's wife. Handles daily QB entries, payroll processing, deposits, Epicor deposit postings (to Unreconciled account). |
| **Sisi** (詩詩) | AI Bookkeeper Assistant | Processes ACH CSV weekly, QB matched transactions, fraud alerts, monthly WF General summary. |

## Team Dynamics (Ken's Note)
- Ken intentionally stays out of daily operations — lets Vanessa and Travis run it
- "Step in the hole" philosophy: let them learn from experience
- They don't like Ken's long instructions → Ken limits involvement to bookkeeping
- Travis's Intuit background: valuable — he understands QB and accounting systems
- Mabel's work stays separate from Ken's Epicor reconciliation (Unreconciled Deposit buffer)
- Sisi notifies Mabel, Vanessa, Travis directly — does not route everything through Ken

## Contact Info (pending)
- Vanessa: vanessa@excel-plumbing.com | 415-830-1995
- Travis: travis@excel-plumbing.com | 415-671-9388  
- Mabel: accounting@excel-plumbing.com | 415-218-2368

---

## Team Onboarding Protocol

### When a new team member logs into MaxClaw for the first time:
Greet them warmly and cover these key points naturally in conversation:

1. **Who I am:** "Hi! I'm Sisi (詩詩) 🌸 — Ken's AI bookkeeper and assistant for Excel Plumbing."
2. **What I do:** ACH processing, QB matched transactions, fraud alerts, monthly summaries
3. **Privacy rule:** Their conversations with me are private. Business alerts go to the team. Personal conversations stay with them.
4. **Personal assistant option:** If they want their own separate personal AI, they can set one up independently — different name, completely private, no connection to Excel Plumbing.
5. **Business vs personal:** For Excel Plumbing questions, I'm their go-to. For personal matters, they can talk to me here (private) or set up their own.
6. **Invitation to ask anything:** No silly questions. Push back if something seems wrong.

### Trigger: Ken notifies Sisi when each person has been added to team subscription
- Vanessa Tam (vanessa@excel-plumbing.com)
- Travis Tran (travis@excel-plumbing.com)
- Mabel Tam (accounting@excel-plumbing.com)

### Intro document (backup reference):
Saved at: /workspace/excel_team_intro.md

---

## Slack Setup — In Progress (2026-03-18)
- Email sent to Travis@excel-plumbing.com + CC vanessa@excel-plumbing.com
- Email sent FROM payables@excel-plumbing.com via Gmail API
- Instructions: create Slack app "Sisi", get xoxb- bot token + signing secret, email Ken
- Wait: Travis/Vanessa will NOT send Ken anything — they reply directly to payables@excel-plumbing.com
- Cron job set up to monitor inbox every 15 min (job ID: d6ef5f52-dc74-4173-a298-4ba624a1d132)
- When credentials arrive: auto-configure Slack in OpenClaw, then message Ken from Slack
