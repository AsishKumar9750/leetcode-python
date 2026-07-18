# Longest Common Prefix

## Problem

https://leetcode.com/problems/longest-common-prefix/

## Difficulty

Easy

## Approach

Use the first string as the reference. Compare each of its characters with the corresponding character in every other string. As soon as a mismatch is found or a string ends, return the prefix built so far.

## Time Complexity

- Time: **O(n × m)**

## Space Complexity

- Space: **O(1)**
