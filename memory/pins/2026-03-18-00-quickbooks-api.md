# Pin: QuickBooks API — Excel Plumbing
**Pinned:** 2026-03-18 00:14 GMT+8
**Topic:** QuickBooks Online API setup for Excel Plumbing bookkeeping automation

## Status
⏸️ PAUSED — ready to resume

## What's Done ✅
- QuickBooks Online connected via OAuth (SisiBookkeeper app)
- QB API live — all WF bank accounts accessible
- ClearedStatus confirmed READ-ONLY via API (cannot auto-click green buttons)
- WF Vendor Payment: 11 open checks, 9 cleared bank
- WF General Remittance (account ID: 268): 62 March transactions pulled ✅
- Ken created "Sisi Quickbooks Reports" custom reports folder in QB

## Key Files
- QB tokens: /workspace/qb_tokens.txt
- QB credentials: /workspace/qb_credentials.txt
- Session notes: /workspace/memory/session_handoff_2026-03-17.md
- QB limitations: /workspace/memory/qb_api_limitations.md
- Reports workflow: /workspace/memory/excel_plumbing_reports.md

## Next Steps (Two Options)
**Route A — Bank Feed Clearing (complex):**
1. Ken creates QB custom report (unmatched bank feed transactions) → saves to "Sisi QB Reports"
2. Test Sisi reading report via API
3. Test marking transactions as Cleared (C) via API

**Route B — WF General Monthly Summary (simpler, API already confirmed working):**
- Build monthly WF General account categorized summary report

## Restore Prompt
Say: "Bring back QB API pin" — Sisi will read this file and be fully up to speed.
