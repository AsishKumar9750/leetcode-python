# Rotate Array

## Problem

https://leetcode.com/problems/rotate-array/

## Difficulty

Medium

## Approach

Reverse the entire array. Then reverse the first `k` elements and the remaining `n - k` elements separately. This rotates the array to the right by `k` positions in-place.

## Time Complexity

- Time: **O(n)**

## Space Complexity

- Space: **O(1)**