class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #idea: buy at lowest price, sell at highest
        left = 0 #buying 
        right = 1 #selling pointer
        maxprofit = 0
        while right < len(prices):
            #is it profitable
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit, profit)
            else:
                #set left to the extreme end as we found the lowest value for left and highest value for right
                left = right
            #keep moving the right pointer 
            right += 1
        return maxprofit