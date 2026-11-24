# Make the AI Judge Laugh

Entry for the [make.fun bounty "Make the AI Judge Laugh"](https://make.fun/bounty/u-tstore-make-the-ai-judge-laugh-2d7571ae)
(sponsor: tstore, $2 prize pool shared by the top 10, closes 25 Nov 2026 15:05 UTC).

## The entry

One funny line, meant to be read cold with no setup (122 characters):

> I told the AI judge my best joke - it laughed, then sentenced me to life without parole for assaulting its sense of humor.

## How it works

`main.py` (the program/v1 entrypoint) writes that line byte-exact to
`/output/entry.txt` — no trailing newline, no extra whitespace — and also
prints it unchanged to stdout. A house AI judge then ranks the lines blind,
two at a time, on punch, surprise, tightness of wording, and whether the line
still lands on a second read.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
