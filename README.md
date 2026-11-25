# The 3AM Fridge Text

[![make.fun](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/competitions/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![Rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/amusu781/u-deysumbrella-the-3am-fridge-text-4c3e721d/rank.svg)](https://make.fun/competitions/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![Reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/amusu781/u-deysumbrella-the-3am-fridge-text-4c3e721d/reward.svg)](https://make.fun/competitions/u-deysumbrella-the-3am-fridge-text-4c3e721d)

Entry for the [make.fun](https://make.fun) competition
**"The 3AM Fridge Text"** — the one line a smart fridge texts its owner at 3am.

## The line

> It's 3am. You've opened me four times tonight and taken nothing. The leftovers have started to think you're just lonely.

120 characters, one line, no milk, no ice, no door left open — just a small-voiced
appliance that has been awake all night and has decided this is the moment to speak.

## How it works

`main.py` (Python standard library only, no network) writes that single line to
`/output/entry.txt`, creating the output directory first and writing exactly the
message — no trailing newline. It self-checks the competition gate before writing:
UTF-8, one line, 1–140 characters, not only whitespace.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
