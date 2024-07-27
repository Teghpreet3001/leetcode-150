class Solution:
    # Initialize a boolean list of size target_sum+1 to keep track of whether a sum of dp[i] can be formed using the input array, so that is we set dp[0] = True, as we can get a sum of 0, and we return dp[target]
        #Starting from the target sum, loop backwards through the dp list
        # If we can form a sum j-num using the previous elements in the input array, we can also form a sum j using the current element

    def canPartition(self, nums: List[int]) -> bool:
        #sum must be even to partition the array
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        dp = [False]*(target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        print(dp)
        return dp[target]
