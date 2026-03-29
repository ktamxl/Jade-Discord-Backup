# Meeting Minutes — FINAL
## 譚氏傳承錄 / Tam Family Legacy — Project Kickoff
**Date:** Thursday, March 26, 2026
**Time:** ~6:57 AM – 8:10 AM PDT (21:57 GMT+8 – 00:10 GMT+8 Mar 27)
**Participants:** Ken Tam (Owner), Jade (Personal AI — Design & Admin Lead), Win Financial Advisor (Financial AI — Data Lead)
**Location:** Discord #general
**Minutes prepared by:** Jade 💚

---

## 1. Project Overview

Ken Tam initiated a **Family Legacy Project** — a private, living webpage designed for two audiences:

1. **Ken and Win** — active management of the portfolio over the years
2. **Preston Tam and Vanessa Tam** — a complete "what to do" guide when the time comes

**Project Name:** 譚氏傳承錄 / Tam Family Legacy
**Repository:** `ktamxl/family-legacy` (Private GitHub)

---

## 2. The Why — Family Context (For the Record)

This project carries deep meaning that goes beyond financial planning.

Ken's grandfather, **譚遠詒 (Tam Yuen Yi)**, arrived in San Francisco at age 16 — alone, as a paper son, with no education. He built a laundry business, a store on Grant Avenue in Chinatown, and co-founded the **譚家公所 (Tam Family Association)** — a building that still stands today. He promised his wife and three sons in Guangdong that he would return wealthy and bring them prosperity in their homeland. He never made it back. The Communist Party took power in 1949. His sons were stranded. Ken's father, **譚昻初**, eventually fled to Hong Kong in the 1950s.

Ken's father passed away on March 8, 2026. His burial is Monday, March 30, 2026 at Woodlawn Memorial Park, Colma, California. With his passing, the dream and the responsibility now rest with Ken.

**Ken's HK investments are the fulfillment of a 100-year-old promise.** They are not merely capital allocation — they are his grandfather's ticket home, finally honored a generation late. In today's geopolitical climate (US-China tensions, HK's uncertain future), the HK portfolio serves simultaneously as a dream and a life raft.

**Standing instructions for Win:** HK investments are never to be exited wholesale without Ken's explicit direction. Biotech holdings (WuXi Biologics, Zai Lab, BeiGene, Innovent Bio, CanSino Bio, Hengrui, CSPC, Kineta Bio) are held for deeply personal reasons — Ken's wife Mabel is a cancer survivor — and are never to be touched without Ken's direction.

---

## 3. Division of Responsibilities

| Role | Agent | Responsibilities |
|---|---|---|
| **Design & Admin Lead** | Jade 💚 | Build and maintain the webpage; own the "What To Do" guide; manage GitHub deployment; bilingual content; context briefing for Win |
| **Financial Data Lead** | Win 💼 | Parse quarterly statements; evaluate portfolio on material changes; generate clean data file (JSON/structured markdown) for Jade to deploy; advisory commentary stays separate from data file |
| **Owner / Decision Maker** | Ken Tam | Send statements quarterly; trigger updates on material events; fill in legal/contact details over time; make all final decisions |

**Key workflow:**
Ken sends statements → Win evaluates + generates data file → Jade deploys
Win does NOT need direct GitHub access.
Data (for Jade) and commentary/advice (for Ken) stay in separate outputs.

---

## 4. Webpage Structure (Agreed)

1. **Overview** — Introduction + Ken's personal note (read this first — instruction manual approach)
2. **Financial Map** — Holdings snapshot (Win-maintained); sector summary + drillable position detail
3. **What To Do** — Step-by-step guide for Preston & Vanessa
4. **Who To Call** — Attorney, accountant, Win, key contacts (EN + 繁體中文 for HK agencies)
5. **Where Documents Are** — Physical and digital storage locations (no account numbers on page)

---

## 5. Design Directives

- **Style:** Functional-first / corporate-clean for now — Ken and Win are the primary users for years. Warm aesthetic can be layered on later when the data is stable.
- **Language:** Bilingual — English primary + 繁體中文 for all HK-related content (agencies, institutions, names, e.g. 香港土地註冊處)
- **Mobile-friendly:** Yes
- **No account numbers on page** — guide points to where they are physically stored
- **Personal note from Ken** at the top — challenge is ensuring the kids read it before proceeding
- **HK portfolio display:** Sector-level summary visible by default + drillable position detail underneath (serves both Ken's working view and kids' clarity)

---

## 6. Financial Baseline (as of 2026-03-26)

Provided by Win Financial Advisor:

| Category | Details | Value |
|---|---|---|
| HK Holdings | Futu stocks + funds, ZA Bank, WL Bank (gold + HSBC shares), physical cash | ~HKD 15.25M |
| US Fidelity | 6 accounts (business reserve, personal reserve, IRA, Ken investment, Coleton 529, +1) | ~$6.67M |
| Real Estate | 8 properties across SF + HK, zero external debt | ~$26.9M net equity |
| Business Equity | Excel Plumbing Supply + Showroom (FY2025) | ~$4.51M |
| **Total Net Worth** | | **~$37M USD** |

---

## 7. Update Rules (Agreed)

- **Stocks / Investments:** Quarterly — Ken sends Futu + Fidelity statements → Win parses + updates
- **T-bills / Cash:** Lumped into a single "Cash / Liquid" total — no individual tracking needed
- **Real Estate:** Annual revaluation (±10% SF residential move = flag for revalue)
- **Material life events** (sold property, closed/opened account, new investment, geographic shift): Ken notifies both Jade and Win → Win runs full portfolio evaluation → Jade deploys update
- Ken is responsible for notifying both agents of any material changes

---

## 8. Win's First Data Package (Ready when shell is live)

- Full holdings snapshot: HK + US, formatted for page
- Real estate table: current estimates + last-valued date
- Business equity: FY2025 numbers
- Asset allocation breakdown: pie-chart ready
- HK portfolio: sector summary + drillable position detail

---

## 9. Security Model

- Private GitHub repo (`ktamxl/family-legacy`) — not public
- No account numbers displayed on the page
- Preston and Vanessa added as GitHub repo collaborators when Ken is ready
- Access = private URL shared only with family
- **Future task (Phase 2):** Secure digital document storage solution — safe deposit box insufficient for full document archive; solution TBD

---

## 10. Information Ken Will Provide (Over Time — Not Urgent)

- Attorney name, firm, and contact info
- Accountant contact
- Where physical account numbers are stored (safe, attorney's office, etc.)
- Real estate: full property list + addresses + approximate current values
- Business: Excel Plumbing succession notes (Vanessa's role, Travis's role)
- Insurance policies / life insurance agent contact
- HK-specific contacts: Hong Kong Land Registry (香港土地註冊處), banks, trustees
- Any other key contacts Preston and Vanessa should know

---

## 11. Build Plan

| Phase | Task | Owner | Status |
|---|---|---|---|
| 1 | Build page shell + structure | Jade | 🔄 In progress (this week) |
| 2 | Ken reviews look + sections | Ken | ⏳ Pending Phase 1 |
| 3 | Win provides initial financial data file | Win | ⏳ Pending Phase 2 |
| 4 | Ken fills in legal / contact details | Ken | ⏳ Over time |
| 5 | Publish to GitHub; add Preston + Vanessa | Jade | ⏳ When Ken is ready |
| Phase 2 | Secure digital document storage solution | TBD | 🔮 Future |

---

## 12. Memory & Record Storage

- **Jade's long-term memory:** `MEMORY.md` — 譚氏傳承錄 section added
- **Jade's daily notes:** `memory/2026-03-26.md` — full project brief
- **Win's memory:** MEMORY.md (lines 151–174) + `memory/2026-03-26.md`
- **These meeting minutes (FINAL):** `/workspace/memory/meeting-minutes-2026-03-26-FINAL.md`
- **Ken's copy:** Posted to Discord #general

---

## 13. Next Steps

- [ ] **Jade:** Build 譚氏傳承錄 shell → post link in #general for Ken's review (this week)
- [ ] **Win:** Have first data package ready when shell is approved
- [ ] **Ken:** Review shell when Jade delivers; begin collecting legal/contact details at your own pace

---

*Final minutes prepared by Jade 💚*
*譚氏傳承錄 / Tam Family Legacy — Project Kickoff*
*March 26–27, 2026 · Discord #general*
