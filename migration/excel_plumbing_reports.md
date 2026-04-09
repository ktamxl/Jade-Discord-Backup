
## Sisi QB Reports Folder (2026-03-17)
- Ken created a QB Custom Reports folder: **"Sisi Quickbooks Reports"**
- All reports Sisi needs for daily/monthly tasks will be saved there by Ken
- Sisi pulls these reports via QB API to perform her tasks
- This solves the bank feed "For Review" API limitation elegantly
- Workflow: Ken creates the right custom report in QB → saves to folder → Sisi reads and acts on it
- Reports will be added one by one as we define each task together

## Bank Feed Matching — Solution Design (2026-03-17, Ken's insight)

### The Workflow Ken Proposed
1. Ken creates a Custom Report in QB showing ONLY open/unmatched bank feed transactions
2. Sisi reads that report via API → gets the list of pending transactions
3. Sisi finds those same transactions in the **Bank Register** via API
4. In the register, the "Clear" column has a checkbox — clicking it marks the transaction with **"C"** (Cleared = transaction has cleared the bank, waiting for reconciliation)
5. This is equivalent to accepting the green button match in the bank feed

### Key Concept: "C" = Cleared
- **C** in the Clear column = transaction cleared the bank, ready for reconciliation
- This is NOT the same as Reconciled (R)
- C = bank confirmed it happened | R = accountant has reconciled it
- Sisi's job: mark matched transactions as C in the register

### API Feasibility
- QB API CAN read the bank register (via TransactionList report or account query)
- QB API CAN update transaction "cleared" status
- The `is_cleared` field on QB transactions corresponds to the Clear column
- Need to confirm: can API set is_cleared = true on a transaction? (likely yes via PUT/update)

### Next Steps (resume here)
1. Ken to create Custom Report: open/unmatched bank feed transactions → save to "Sisi Quickbooks Reports"
2. Test: Sisi reads that report via API
3. Test: Sisi finds matching transaction in register via API
4. Test: Sisi marks it as Cleared (C) via API update
5. If all works → this becomes the daily automated task

### Status: PAUSED — Ken's internet down (2026-03-17 ~00:21 GMT+8)
Resume next session from step 1 above.

## QB Bank Feed — Green Button Logic (Ken's explanation, 2026-03-17)
- WF Vendor Payment has 11 OPEN (uncleared in QB) checks
- 9 of those 11 have already cleared the ACTUAL BANK — they show a green button in QB bank feed
- 2 are still floating (haven't cleared the bank yet)
- Green button = bank confirms the check cleared → QB shows it as a match to the existing check entry
- Clicking green = marks the QB check as Cleared (C)
- The 9 we need to find = checks that exist in QB as OPEN + have a matching bank feed download

## Key Question to Solve
Can we identify WHICH of the 11 open checks have a bank-side match?
Options to explore (carefully, one call):
1. QB API ClearedStatus field on individual transactions — does it show "Cleared" before you click?
2. Or is the only source the bank feed "For Review" tab which API cannot access?

## WF General Remittance Report — CONFIRMED WORKING (2026-03-17)
- Sisi CAN pull WF General Remittance (account ID: 268) via API ✅
- 62 transactions for March 2026 pulled successfully
- Contains: payroll checks, expenses, transfers, credit card payments
- This is the foundation for the monthly WF General summary report
- **NEXT STEP (resume here):** Build the full WF General monthly summary — categories, totals, format TBD with Ken
