# TIP103

Mock-interview practice workspace for CodePath's Technical Interview Prep (TIP) course, unit 103.

## How this repo is organized

```
TIP103/
├── problems/           one folder per practice problem
│   ├── _template/      copy this to start a new problem
│   └── 00-example-two-sum/   a filled-out example to show the format
├── cheatsheets/         quick-reference notes (Big O, common patterns)
└── mock-interviews/      log of timed mock sessions
```

## Workflow for a new problem

1. Copy `problems/_template` to `problems/NN-short-problem-name` (increment `NN`).
2. Paste the prompt into `problem.md` before you start.
3. Set a timer (typically 20-30 min for a single problem in a mock interview).
4. Talk through your approach out loud, jot bullet points in `notes.md` as you go
   (brute force idea → optimization → complexity), *then* write code in `solution.py`.
5. After time is up (or you finish), fill in the "Reflection" section of `notes.md`.
6. If this was a timed mock session, add a row to `mock-interviews/log.md`.

```bash
cp -r problems/_template problems/01-your-problem-name
```

## Cheatsheets

- [cheatsheets/big-o.md](cheatsheets/big-o.md) — complexity quick reference
- [cheatsheets/patterns.md](cheatsheets/patterns.md) — common problem patterns and when to reach for them

## Mock interview log

Track every timed practice session in [mock-interviews/log.md](mock-interviews/log.md) — problem, time taken, self-assessment, what to work on next.
