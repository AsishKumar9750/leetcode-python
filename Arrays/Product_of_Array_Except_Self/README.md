# Product of Array Except Self

## Problem

https://leetcode.com/problems/product-of-array-except-self/

## Difficulty

Medium

## Approach

Compute the prefix and suffix products for each index. The product of all elements except the current one is obtained by multiplying the corresponding prefix and suffix products.

## Time Complexity

- Time: **O(n)**

## Space Complexity

- Space: **O(n)**