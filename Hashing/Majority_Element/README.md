# Majority Element

## Problem

https://leetcode.com/problems/majority-element/

## Difficulty

Easy

## Approach

Use a hash map to count the frequency of each element while traversing the array. As soon as an element's frequency becomes greater than `n / 2`, return it.

## Time Complexity

- Time: **O(n)**

## Space Complexity

- Space: **O(n)**