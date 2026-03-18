# 📌 Pin — Context Management & Session Hygiene
**Pinned:** 2026-03-17 21:47 HK / 06:47 SF PDT
**Topic:** Keeping Sisi healthy long-term — context management, Pin it system

---

## Status: ✅ COMPLETED — All systems set up

## What We Did
1. **Diagnosed yesterday's 20K credit burn** — cause: very long session accumulating context over time
2. **Explained MEMORY.md risk** — it's injected every session; if it grows to 80K+, even /new starts at 40% full
3. **Designed the "Pin it" workflow:**
   - Say "Pin it" → Sisi saves session snapshot to `/workspace/memory/pins/`
   - `/new` → fresh session, clean context
   - "Bring back [topic]" → Sisi reads pin, summarizes where we were, Ken guides next steps (Option A)
4. **Set up context warnings** in AGENTS.md — Sisi checks % at every session start and warns at 25% / 50%
5. **Set up monthly compression cron** — 1st of every month, 9 AM SF time, checks MEMORY.md size and reminds Ken if compression needed (Cron ID: fe37cb13-b330-459b-b9ed-95ccf372e0ed)

## Files Modified
- `/workspace/AGENTS.md` — Added: Pin It protocol, Context Warning rules, MEMORY.md compression reminder
- `/workspace/memory/pins/` — Created directory (this file is the first pin)

## Key Decisions
- "Bring back" = **Option A**: Sisi summarizes → Ken drives (not auto-resume)
- Context warning thresholds: 25% = gentle heads up, 50% = clear warning
- MEMORY.md target: keep under 15K tokens / ~600 lines
- Monthly compression: archive resolved items to `/workspace/memory/archive/`

## Next Steps / Pending
- None for this topic — fully implemented ✅
- Future: Ken will naturally test "Pin it" and "bring back" flow in real sessions

## Restore Prompt
> "Bring back context management" or "Bring back the Pin it session"

---
*Pin created by Sisi 🌸*
