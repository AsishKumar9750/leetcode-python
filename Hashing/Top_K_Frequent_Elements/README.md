# Top K Frequent Elements

## Problem

https://leetcode.com/problems/top-k-frequent-elements/

## Difficulty

Medium

## Approach

Count the frequency of each element using a hash map. Use bucket sort where the index represents the frequency and each bucket stores the elements with that frequency. Traverse the buckets from highest to lowest frequency until `k` elements are collected.

## Time Complexity

- Time: **O(n)**

## Space Complexity

- Space: **O(n)**