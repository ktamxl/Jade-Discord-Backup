# Pin: Ken's Kitchen — Recipe Library & Skills Session
**Date:** 2026-03-24 · ~16:51 GMT+8 (01:51 AM PDT Monday March 23)
**Topic:** Recipe Library skill, webpage, history, YouTube extraction

---

## Status: Active & Growing 🟢

---

## What Was Built

### 1. Recipe Skill — `ken-recipes-1.0.0`
- Location: `/workspace/skills/ken-recipes-1.0.0/`
- `SKILL.md` — trigger descriptions, recipe index, scaling rules
- `references/portuguese-curry-chicken.md` — full recipe in structured format
- Auto-triggers when Ken mentions dish names, scaling, or cooking
- Scaling: reads recipe → multiplies all quantities by (target ÷ base)
- Oven temp/time stays fixed when scaling

### 2. Recipe Webpage — Portuguese Curry Chicken
- File: `/workspace/recipes/portuguese-curry-chicken.html`
- Live URL: **https://w1pcu17zy8n5.space.minimax.io**
- Images: `/workspace/recipes/imgs/` (4 photos)
- Sections: Hero · Intro · Photo strip · **History** · **Legendary Spots** · Scaling widget · Ingredients · Instructions · Chef's Notes
- History section covers: Macau 1557 origin, UNESCO fusion cuisine, cha chaan teng rise, timeline 1557→Today, 6 legendary restaurant cards

### 3. YouTube Recipe Extraction — CONFIRMED WORKING ✅
- Tool: `videos_understand` with YouTube URL
- Demo: https://www.youtube.com/watch?v=P7rwibqju6U (W2 Kitchen Portuguese Chicken)
- Successfully extracted full ingredient list + step-by-step instructions
- Workflow: Ken pastes YouTube URL → Jade watches + extracts → formats + saves to skill → optional web deploy

---

## Key Decisions
- Ken's library is a personal **playbook** — learning from masters, adapting to his own taste. Not copying, learning.
- Each recipe: structured md file in `references/`, added to SKILL.md index
- Recipes will accumulate over time — Ken cooks many dishes weekly
- Goal: leave a culinary legacy for his kids (Preston & daughter)

---

## Files Involved
| File | Purpose |
|------|---------|
| `/workspace/skills/ken-recipes-1.0.0/SKILL.md` | Skill trigger + recipe index |
| `/workspace/skills/ken-recipes-1.0.0/references/portuguese-curry-chicken.md` | Recipe No. 001 |
| `/workspace/recipes/portuguese-curry-chicken.html` | Recipe webpage |
| `/workspace/recipes/imgs/` | 4 food photos |

---

## Next Steps / Pending
- [ ] Add more recipes (Ken has many weekly dishes)
- [ ] Each new recipe: save to `references/` + update SKILL.md index + optionally deploy new page
- [ ] Build a recipe **index/home page** once library grows (2–3+ recipes)
- [ ] Ken to send YouTube links for dishes he wants extracted
- [ ] Consider: John Fong agent (SF Bay Area real estate specialist) — separate future project

---

## Restore Prompt
> "Bring back my kitchen recipes pin" — Ken is building a personal recipe library. Recipe No. 001 is Portuguese Curry Chicken. The skill is live at `/workspace/skills/ken-recipes-1.0.0/`. The webpage is at https://w1pcu17zy8n5.space.minimax.io. Next: add more recipes via YouTube links or Ken typing them out.
