# Maximum Product Subarray

## Problem

https://leetcode.com/problems/maximum-product-subarray/

## Difficulty

Medium

## Approach

Maintain two running products while traversing the array: a prefix product from the left and a suffix product from the right. This accounts for the effect of negative numbers, where excluding either the leftmost or rightmost negative value can produce the maximum product. Whenever a running product becomes zero, reset it to `1` to start a new subarray. Track the maximum product encountered throughout the traversal.

## Time Complexity

- Time: **O(n)**

## Space Complexity

- Space: **O(1)**