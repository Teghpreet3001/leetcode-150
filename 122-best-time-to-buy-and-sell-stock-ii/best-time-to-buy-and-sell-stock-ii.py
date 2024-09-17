class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        start = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > start:
                maxProfit += prices[i] - start
            start = prices[i]
        return maxProfit