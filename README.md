# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/stanforder/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/stanforder/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

The world in one day — Wednesday 18 November 2026, summed up in one image.
Entry for the make.fun bounty
[`news-image-20261118`](https://make.fun/bounty/news-image-20261118):
sum up 18 November 2026's world news in one image.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## The image

A flat editorial poster, drawn programmatically with Pillow by
`draw_entry.py` (build-time only). The submitted program `main.py` only
copies the finished `entry.png` to `/output/entry.png` — standard library
only, no network, byte-identical on every run.

Headline: **SUMMITS AND STRIKES**

- **Summit (hero):** Xi Jinping meets Vladimir Putin in Shenzhen at APEC;
  a trilateral with Donald Trump is set for Thursday 19 November.
- **Gulf (hero):** U.S.–Iran exchange fire — Iranian drones target Gulf
  bases, the U.S. strikes a missile site on Qeshm Island.
- **Ukraine:** record 1,441-drone assault; a span of the Kerch (Crimea)
  bridge falls.
- **Gaza:** 950,000 displaced Palestinians in flood-prone ground as a
  fourth winter begins.
- **Tech / markets:** Nvidia revenue doubles to $115.8bn; its board rules
  out reinstating Jensen Huang as CEO.
- **Climate:** Cyclone Akvan forces evacuations in Odisha; COP31 in
  Antalya is deadlocked over fossil fuels.
- **Footer:** Quad meets in Manila; U.S. Senate: Democrats 56–44
  (Mary Peltola wins Alaska); Yemen: 64 children killed since 3 September.

Sources checked 19 Nov 2026: AP / AFP / Reuters reporting via
Open Chronicle's 18 Nov global brief, UN News (18 Nov 2026), and
contemporaneous Gulf / Ukraine / markets coverage.

To regenerate the image from its source (needs Pillow, build-time only):

```sh
python3 draw_entry.py
```

## Licence

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
