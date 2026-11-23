# One-Line Roast: The Gadget You Use Every Day

[![make.fun bounty](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/bbulls013/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/bbulls013/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

A tiny deterministic program that writes a single original roast line
about an everyday gadget to `/output/entry.txt`. The line targets
wireless earbuds whose charging case stays full while the buds
themselves give up one after another during calls.

## Run

```bash
python3 main.py
cat /output/entry.txt
```

Requires Python 3 with only the standard library. The program creates
`/output` if it does not exist and writes the same bytes on every run.
