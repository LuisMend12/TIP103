# Notes — Two Sum

**Date:** 2026-09-15
**Time spent:** 10 min (example, not timed as a real mock)

## Talking through it (do this before coding)

- Brute force idea: nested loop checking every pair, O(n^2) time, O(1) space.
- Why it's not optimal: with n up to 10^4, n^2 is 10^8 — too slow for repeated
  interview-style follow-ups, and there's an obvious O(n) improvement.
- Optimization / key insight: once we know `target`, for each `num` we only
  need to know whether `target - num` has already appeared. That's a lookup,
  so a hash map trades O(n) space for dropping the nested loop.
- Data structure(s) chosen and why: dict (hash map) from value to index —
  O(1) average insert/lookup, and it doubles as the "have I seen this" check
  and the index-recovery mechanism in one structure.

## Complexity

- Time: O(n)
- Space: O(n)

## Reflection (fill in after)

- Did I get a working solution in time? Y
- What tripped me up? Nothing here — this is the reference example.
- What would I do differently next time? Remember to state the brute force
  first out loud, even when the optimal solution is obvious, since
  interviewers want to hear the reasoning process.
- Follow-up variants to try: Two Sum II (sorted array, two pointers instead
  of hash map — O(1) space); Two Sum returning all unique pairs; 3Sum.
