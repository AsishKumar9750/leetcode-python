# Single Number

## Problem

https://leetcode.com/problems/single-number/

## Difficulty

Easy

## Approach

Use the XOR (`^`) operator to cancel out duplicate elements. Since `a ^ a = 0` and `a ^ 0 = a`, all duplicate numbers are eliminated, leaving only the element that appears once.

## Time Complexity

- Time: **O(n)**

## Space Complexity

- Space: **O(1)**