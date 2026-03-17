## ⚠️ Critical API Limitation (Confirmed 2026-03-17)

**ClearedStatus is READ-ONLY via QB Online API.**

- Cannot mark transactions as Cleared (C) via API
- Cannot accept bank feed matches via API
- The only ways to set Cleared status:
  1. Click green button in Bank Feed "For Review" tab (manual)
  2. Check the checkbox in the Reconciliation screen (manual)
- This is a known Intuit limitation with multiple community requests to change it

## Impact on Sisi's Daily Task
The original goal (mark matched bank feed checks as Cleared automatically) CANNOT be done via API.

## Next Steps to Discuss with Ken
- Accept limitation: Ken/Mabel click green buttons manually (fast, ~30 sec/day)
- OR: Focus Sisi on OTHER valuable tasks where API CAN help:
  - Daily anomaly/fraud monitoring on WF Deposit
  - Weekly ACH CSV processing (already working ✅)
  - Monthly WF General summary spreadsheet
  - Balance tracking and alerts
  - Bill payment verification
