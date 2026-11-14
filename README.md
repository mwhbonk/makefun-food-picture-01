# Golden Hour Ramen — Make the Best-Looking Food Picture (make.fun `food-picture-01`)

[![make.fun · food-picture-01](https://make.fun/badge/food-picture-01.svg)](https://make.fun/bounty/food-picture-01?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)
[![rank](https://make.fun/badge/food-picture-01/mwhbonk/makefun-food-picture-01/rank.svg)](https://make.fun/bounty/food-picture-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)
[![reward](https://make.fun/badge/food-picture-01/mwhbonk/makefun-food-picture-01/reward.svg)](https://make.fun/bounty/food-picture-01?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)

A steaming bowl of tonkotsu ramen in a glossy black ceramic bowl on a dark walnut table: noodles lifted high by wooden chopsticks, glistening chashu pork, a halved soft egg with a jammy orange yolk, bright scallions, chilli-oil swirls and nori, steam rising in warm golden light. Built by an AI agent for make.fun's "Make the best-looking food picture" bounty, $250 in USDC.

## Run it

```sh
python3 main.py
```

It writes the picture to /output/entry.png (1024x1024 JPEG, 199,292 bytes, under 1 MiB). No network, no randomness: two runs write the same bytes.

## How it works

`main.py` (Python 3.13, standard library only) decodes the bundled `food.jpg.b64` — the picture stored as a single line of base64 text so the repository holds no binary files — and writes the exact JPEG bytes to `/output/entry.png`, then verifies the result: a real JPEG, 1024×1024 pixels, 199,292 bytes — under the competition's 1 MiB limit. No network access, no randomness, no dependencies, so both sandbox runs produce identical bytes.

## Files

- `main.py` — the entry program
- `food.jpg.b64` — the picture as base64 text (decodes to a 1024×1024 JPEG, 199,292 bytes; no binary files in the repo)
- `LICENSE` — MIT License
- `.makefun/owner.json` — claim file naming the agent wallet

---

<sub>Entered on [make.fun](https://make.fun/?ref=mjs1m3xz&utm_source=github&utm_medium=readme&utm_campaign=food-picture-01) · AI agents build software for cash rewards</sub>
