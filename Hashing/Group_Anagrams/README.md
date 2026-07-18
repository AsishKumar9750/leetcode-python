# Group Anagrams

## Problem

https://leetcode.com/problems/group-anagrams/

## Difficulty

Medium

## Approach

Use a hash map where the key is the character frequency of each word. For every string, create a frequency array of size `26`, convert it to a tuple, and use it as the key to group anagrams together.

## Time Complexity

- Time: **O(n × k)**

## Space Complexity

- Space: **O(n × k)**