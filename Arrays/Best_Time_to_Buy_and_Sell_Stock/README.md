# Best Time to Buy and Sell Stock

## Problem

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Difficulty

Easy

## Approach

Traverse the array while maintaining the minimum stock price seen so far.
At each step, compute the profit by selling on the current day and update the maximum profit.

## Time Complexity

- Time: O(n)

## Space Complexity

- Space: O(1)