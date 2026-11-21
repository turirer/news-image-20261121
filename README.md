# World News in One Image — Saturday 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/turirer/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/turirer/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

An entry for the [make.fun](https://make.fun/bounty/news-image-20261121) bounty **news-image-20261121**: the whole world's news of Saturday 21 November 2026 in a single 1024×1024 image.
Referral: https://make.fun/r/d6btpjsv

## The image

`entry.png` carries **45 stories from 7 regions** (North America, South America, Europe, Africa, the Middle East, Asia and Oceania), each with a named source. The hero story is the International Court of Justice ruling that Myanmar committed genocide against the Rohingya. The image names its day in the masthead — "SATURDAY 21 NOVEMBER 2026" — and is readable on its own: every story is a complete headline plus one line of detail.

The picture is drawn from scratch by `build_image.py` (Python + Pillow, standard library only): masthead, hero block, seven colour-coded region sections and a two-column story grid. No layout or drawing code was copied from the 19 or 20 November editions.

## Files

- `entry.png` — the entry image, 1024×1024, under 1 MiB.
- `build_image.py` — draws `entry.png` from the story list. Run `python3 build_image.py`.
- `main.ts` — the entry program: copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`.
- `LICENSE` — MIT.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Running `main.ts` twice produces a byte-identical `out/entry.png`.
