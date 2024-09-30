class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        #DP problem similar to house roberer
        # make points = {} which maps numbers to points they can earn
        points = defaultdict(int)

        for num in nums:
            points[num] += num

        maxNum = max(nums)
       
        #dp[i] = max number of points we can gain from 0 to i (inclusive)
        dp = [0]*(maxNum + 1)
        dp[1] = points[1] #base case

        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] +  points[i])
        return  dp[maxNum]
 