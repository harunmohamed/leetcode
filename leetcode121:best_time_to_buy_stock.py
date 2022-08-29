## LEETCODE 121: Best time to buy a stock 

## say you have an array for which the ith element is the price of a given stock on day i,

## if you were only permitted to complete at most one transaction (buy one and sell one share of the stock), design an
## algorithm to find the maximum profit

## Note that you cannot sell a stock before you buy one


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP