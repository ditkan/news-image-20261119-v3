# The Meridian Gazette — Thursday 19 November 2026

One image, the whole day: a single front page summing up the world's news of
Thursday 19 November 2026. A lead story on Anthropic's record $81.3bn IPO with
a drawn hero panel (skyline + rising chart), a dot-grid world map with
numbered markers for where the news happened, a day-in-numbers box, and 39
further stories from six continents in a three-column river — every headline
on one line, every story confirmed by two independent outlets.

Entry for the make.fun bounty:
https://make.fun/bounty/news-image-20261119

[![competition](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/ditkan/news-image-20261119-v3/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/ditkan/news-image-20261119-v3/reward.svg)](https://make.fun/bounty/news-image-20261119)

## Design notes

Classic broadsheet styling: serif masthead and headlines, a red date band,
and a black ticker along the foot. The hero panel, world map and numbers box
are all drawn programmatically in `render.py` — no photographic assets, so
the page renders identically anywhere Pillow is available.

## How it works

- `render.py` draws the page with Pillow and writes `entry.png` (1024×1024).
- `main.py` (stdlib only) copies the pre-rendered `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`.
- `sources.txt` lists each of the 40 stories with its two confirming outlets.
