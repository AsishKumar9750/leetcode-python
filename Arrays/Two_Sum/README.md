# Two Sum

## Problem

https://leetcode.com/problems/two-sum/

## Difficulty

Easy

## Approach

Traverse the array while storing each element and its index in a hash map. For every element, check if its complement (`target - current element`) already exists in the hash map. If it does, return the indices of the two numbers.

## Time Complexity

- Time: **O(n)**

## Space Complexity

- Space: **O(n)**