class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for price in prices:
            profit = price - minBuy
            maxProfit = max(profit, maxProfit)
            minBuy = min(minBuy, price)

        return maxProfit