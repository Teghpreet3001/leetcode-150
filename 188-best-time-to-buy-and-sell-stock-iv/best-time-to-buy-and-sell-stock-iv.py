class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        
        n = len(prices)
        
        # If k is larger than n//2, it becomes equivalent to an unlimited transactions problem
        if k >= n // 2:
            return self.maxProfitUnlimited(prices)
        
        # DP table to store the maximum profit
        dp = [[0] * (k + 1) for _ in range(n)]
        
        for j in range(1, k + 1):  # for each transaction
            max_diff = -prices[0]  # max of dp[i-1][j-1] - prices[i]
            for i in range(1, n):  # for each day
                dp[i][j] = max(dp[i-1][j], prices[i] + max_diff)  # sell at day i
                max_diff = max(max_diff, dp[i][j-1] - prices[i])  # buy at day i
                
        return dp[-1][k]
    
    def maxProfitUnlimited(self, prices: List[int]) -> int:
        # Helper function to calculate the max profit with unlimited transactions
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
        