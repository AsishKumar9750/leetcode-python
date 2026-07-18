# Sort Array by Increasing Frequency

## Problem

https://leetcode.com/problems/sort-array-by-increasing-frequency/

## Difficulty

Easy

## Approach

Count the frequency of each element using a hash map. Sort the unique elements by frequency in ascending order, and for elements with the same frequency, sort them by value in descending order. Finally, reconstruct the array using the sorted frequencies.

## Time Complexity

- Time: **O(n + k log k)**

## Space Complexity

- Space: **O(n)**