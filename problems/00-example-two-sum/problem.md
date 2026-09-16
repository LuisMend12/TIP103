# Two Sum

**Source:** LeetCode #1
**Difficulty:** Easy
**Topic tags:** arrays, hash map

## Prompt

Given an array of integers `nums` and an integer `target`, return the indices of
the two numbers such that they add up to `target`.

You may assume that each input has exactly one solution, and you may not use
the same element twice.

## Examples

```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] == 9

Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

## Constraints

- 2 <= nums.length <= 10^4
- Exactly one valid answer exists.

## Clarifying questions to ask

- Can the array contain duplicates? (Yes, but the two indices used must differ.)
- Do we need to return indices or the values themselves? (Indices.)
- Is the array sorted? (No — can't assume order.)
