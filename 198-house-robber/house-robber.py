class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dp[i] = max we can steal from houses 0 to i
        #since we have to use nums in loop, we use n and not n + 1
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0]*(n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            #choose to steal at i: nums[i] + dp[i-2]
            #choose to not steal at i: dp[i-1]
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[n - 1]
        