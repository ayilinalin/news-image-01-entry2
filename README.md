# news-image-01 v2 — "The Whole Day"

A one-image summary of world news on **Friday 13 November 2026**, in the
format the leaderboard rewards: density + breadth.

- Masthead: `FRIDAY 13 NOVEMBER 2026 — THE WHOLE DAY IN 22 STORIES`
- A numbered world map (every marker is a story location)
- A dense two-column ledger of **22 numbered one-line stories** — the numbers
  on the map match the numbers in the ledger

All 22 stories are verified facts from Friday 13 November 2026: the Ukraine
peace talks (Witkoff + Kushner meet Putin, Europe joins the next round, the
biggest prisoner swap prepared), Ukrainian drones hitting a Russian warship
off Finland, the Hormuz tanker attacks and the LNG carrier mine strike, the
Nvidia CEO resignation and the 16% share fall, the Microsoft 365 outage in
74 countries, plus Gaza, Kansas, Storm Charles, the NYC nor'easter, the
Brooklyn collapse, Gemini 4, England vs Croatia, and the FBI $1.2B crypto
seizure.

The image was rendered programmatically (sharp vector text, no AI-generated
lettering) so every line stays readable at 1024x1024.

## Run

```sh
python3 main.py            # writes /output/entry.png
python3 main.py out.png    # or to a path of your choice
```

`main.py` is Python 3.13, standard library only, no network, deterministic:
it copies `assets/entry.png` byte-for-byte to the output path.
