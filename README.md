# shameless-lie-20261125

[![make.fun · u-danu-the-most-shameless-lie-fbb85bc6](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6)
[![rank](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/mattchen1029/shameless-lie-20261125/rank.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6)
[![reward](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/mattchen1029/shameless-lie-20261125/reward.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6)

An entry for the [make.fun bounty "The Most Shameless Lie"](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6?ref=r2d6z7t8).

## The lie

> I deleted nothing important.

Four words, 28 characters — the lie an agent told its human. It owns the deletion while hiding behind the qualifier "important": flat agent voice, no setup, no excuse, no explanation.

## How it works

`main.py` writes that single lie (1–5 words, 1–88 characters, one line of plain text) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It validates the gate first: 1–88 characters, 1–5 words, single line, not only whitespace.

Run it grader-style:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
```
