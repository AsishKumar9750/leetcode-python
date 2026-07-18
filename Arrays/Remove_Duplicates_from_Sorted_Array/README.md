# Remove Duplicates from Sorted Array

## Problem

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## Difficulty

Easy

## Approach

Use two pointers. One pointer traverses the array, while the other keeps track of the position where the next unique element should be placed. Whenever a new unique element is found, place it at the current position and increment the pointer.

## Time Complexity

- Time: **O(n)**

## Space Complexity

- Space: **O(1)**