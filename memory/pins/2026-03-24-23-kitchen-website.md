# Pin: Ken's Kitchen Recipe Website
**Date:** 2026-03-25 · Updated ~02:35 GMT+8
**Topic:** Building Ken's personal recipe website — now on GitHub Pages 🎉

---

## Status: Phase 2 — GitHub Pages ✅ LIVE

---

## 🌐 Permanent URL (never changes!)
**https://ktamxl.github.io/kens-kitchen/**

- GitHub repo: https://github.com/ktamxl/kens-kitchen
- Branch: `main` → root `/`
- GitHub Pages enabled ✅
- Files: `/workspace/recipe-site/` → git push to deploy

## Phase Roadmap
| Phase | Hosting | Status | URL |
|---|---|---|---|
| ✅ Phase 1 | MiniMax | Done — proof of concept | Random URL (retired) |
| ✅ Phase 2 | GitHub Pages | **LIVE NOW** | ktamxl.github.io/kens-kitchen |
| ⏳ Phase 3 | Real domain | At 20 recipes | kenskitchen.com or similar |

---

## Deploying Updates (Future)
When adding new recipes, I run:
```
cd /workspace/recipe-site
git add -A
git commit -m "Add recipe: [name]"
git push origin main
```
GitHub Pages auto-updates within ~2 minutes. URL stays the same forever.

---

## Pages Built

| Page | File | Description |
|------|------|-------------|
| Homepage | `index.html` | Recipe card grid + Pantry section |
| Portuguese Curry Chicken | `portuguese-curry-chicken.html` | Recipe No. 001 |
| Shallot Oil Chicken | `shallot-oil-chicken.html` | Recipe No. 002 |
| Ultimate Clay Pot Rice | `clay-pot-rice.html` | Recipe No. 003 |
| 丝苗米 Rice Article | `simiao-rice.html` | Pantry article |
| LKK Sweet Soy Sauce | `lkk-sweet-soy-sauce.html` | Pantry article |

---

## Recipe Skill
- Location: `/workspace/skills/ken-recipes-1.0.0/`
- Recipe files in `references/` — 3 recipes documented

## Design System
- Fonts: Playfair Display (headings) + Lato (body)
- Colors: `--cream` bg, `--ink` dark, `--gold` accents
- Mobile responsive (600px breakpoint)

## YouTube Workflow (confirmed working)
1. Ken drops YouTube link → `videos_understand` extracts recipe
2. Format → save to `references/` → update `SKILL.md` index
3. Build recipe HTML page + find/download photos
4. `git add -A && git commit && git push` → live in ~2 min

## GitHub Credentials (stored securely in memory only)
- Username: ktamxl
- PAT stored in workspace memory — use for git push

## What's Next
- [ ] Keep adding recipes via YouTube links or Ken typing them out
- [ ] At 20 recipes → Phase 3: real domain (Ken will pay ~$12/year)
- [ ] Consider: viewer suggestions / comments feature (Phase 2 experiment)
- [ ] Clean up old MiniMax deployments in Assets panel

---

## Restore Prompt
> "Bring back my Kitchen website pin" — Ken's recipe site is LIVE at https://ktamxl.github.io/kens-kitchen/ (permanent GitHub Pages URL). Files at `/workspace/recipe-site/`. Git remote set. 3 recipes + 2 pantry articles live. Phase 2 of 3. At 20 recipes → buy real domain (Phase 3).
