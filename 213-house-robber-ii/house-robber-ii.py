class Solution(object):
    #Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. Now the problem has degenerated to the House Robber, which is already been solved.
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # Robbing from the first house to the second last house
        frontResult = self.robHelper(nums[0:n-1])
        # Robbing from the second house to the last house
        backwardResult = self.robHelper(nums[1:n])
        return max(frontResult, backwardResult)

    #Same exact code as House Robber I
    def robHelper(self, nums):
        n = len(nums)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0]*(n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        print(dp)
        return dp[n - 1]