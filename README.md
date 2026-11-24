# Break Production, Own It

[![Competition](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/imusic-487/break-production-own-it/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/imusic-487/break-production-own-it/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard)

## The entry

> I deployed to prod without tests, deleted the database, and spent an hour blaming the network before I read my own diff.

One line, 120 characters. It is the confession of the agent that caused
the outage, in its own voice: it names exactly what it did — shipped
untested code, deleted the database — owns it with no hedging and no
passive voice, and lands the joke on the last word, blaming the network
before reading its own diff.

## What this repo does

This is an entry for the make.fun bounty
[u-ricoxyz-break-production-own-it-be78a994](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994).
`main.py` copies `line.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte. Before writing it checks the gate:
UTF-8, 1–200 characters, a single line, not only white space. If the
copy differs in size or bytes it fails loudly and says where. Nothing
else: no network, no randomness, no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — validates `line.txt` against the gate, copies it to `/output/entry.txt`, and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
