---
name: ken-recipes
description: Ken's personal recipe library — a curated collection of Ken's favorite recipes with ingredient lists, cooking instructions, and automatic scaling. Use when Ken mentions a dish name, asks to cook something, wants to scale a recipe (e.g. "make this for 10 people"), or asks for a recipe from his collection. Trigger phrases: "let's cook", "recipe for", "scale this", "how many servings", "make this for X people", "what's in", "ingredients for", "how do I make".
---

# Ken's Recipe Library

Ken's personal collection of recipes. Each recipe is stored in `references/` as its own file.

## How to Use

### Retrieve a recipe
Read the relevant file from `references/` and present it clearly — ingredients grouped, steps numbered.

### Scale a recipe
When asked to scale (e.g. "make this for 10 people"), calculate each ingredient proportionally:
- Base servings are noted in each recipe file
- Multiply all ingredient quantities by `(target / base)`
- Round sensibly (e.g. 1.5 tsp → "1½ tsp", not "1.4999 tsp")
- Flag any non-scalable steps (e.g. oven temp stays the same)

### Add a new recipe
Create a new `.md` file in `references/` following the same format as existing recipes.

## Recipe Index

| File | Dish | Cuisine | Serves |
|------|------|---------|--------|
| `references/portuguese-curry-chicken.md` | Portuguese Curry Chicken | Portuguese-Chinese Fusion | 4 |
| `references/shallot-oil-chicken.md` | Shallot Oil Chicken & Noodles (蔥油雞腿) | Chinese (Cantonese/Shanghai) | 2–4 |
| `references/clay-pot-rice.md` | Ultimate Clay Pot Rice (煲仔飯) | Chinese (Cantonese Classic) | 3–4 |

## Format Standard

Each recipe file contains:
- **Metadata:** cuisine, serves, prep time, cook time
- **Marinade / Prep ingredients** (if applicable)
- **Main ingredients** with quantities
- **Cooking ingredients / sauces**
- **Instructions** — numbered steps
- **Notes** — tips, variations, substitutions
