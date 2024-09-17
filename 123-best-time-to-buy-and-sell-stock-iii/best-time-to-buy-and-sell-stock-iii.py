class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        # All these hold the maximum profit after first buy, first sell etc

        first_buy = float("inf") #want to minimise buying price
        first_sell = 0 #want to maximise selling price

        second_buy = float("inf") 
        second_sell = 0

        for price in prices:

            # Update the minimum price for the first buy
            first_buy = min(first_buy, price)

            # Calculate profit after the first sell             
            first_sell = max(first_sell, price - first_buy)

            # Update the minimum price for the second buy
            second_buy = min(second_buy, price - first_sell)

            # Calculate profit after the second sell
            second_sell = max(second_sell, price - second_buy)

        # The final maximum profit after the second sell (max_profit_after_second_sell) is the desired result.
        return second_sell