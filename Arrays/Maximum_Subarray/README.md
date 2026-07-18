# Maximum Subarray

## Problem

https://leetcode.com/problems/maximum-subarray/

## Difficulty

Medium

## Approach

Use **Kadane's Algorithm** to maintain the maximum sum of a contiguous subarray ending at the current index. If the running sum becomes negative, reset it to `0` since it cannot contribute to a larger subarray sum. Keep track of the maximum sum encountered during the traversal.

## Time Complexity

- Time: **O(n)**

## Space Complexity

- Space: **O(1)**