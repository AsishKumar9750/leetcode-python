# Contains Duplicate

## Problem

https://leetcode.com/problems/contains-duplicate/

## Difficulty

Easy

## Approach

Traverse the array while maintaining a hash set of previously seen elements. If the current element is already present in the set, return `True`; otherwise, add it to the set. If the traversal completes without finding duplicates, return `False`.

## Time Complexity

- Time: **O(n)**

## Space Complexity

- Space: **O(n)**