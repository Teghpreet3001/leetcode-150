class Solution:

    #at every stage, the length of LIS will either be whatever is present at the curr index (dp[i]) or it will be LIS of the list[i: ] + 1 which comes from i itself (dp[j] + 1)
    # we check nums[i] > nums[j] since that is where a subsequemce breaks and a new subsequence starts
    # for example, [1, 2, 4, 3] so when we reach 4 and 3, we compare LIS at 4 which is 3 and LIS at 3  + 1 which is 2, so LIS at 4 is max(3,2) = 3

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        #length of LID starting at any index will be 1
        dp =[1]*(n)
        dp[0] = 1
        for i in range(1, len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp) #and not dp[n-1] resent anywsince the longest LIS can end anywhere in the list and beyond that we have smaller numbers