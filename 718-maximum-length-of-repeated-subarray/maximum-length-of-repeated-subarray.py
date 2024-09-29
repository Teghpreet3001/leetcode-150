class Solution:

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        #DP approach similar to LCS, bottom up DP solution
        n = len(nums1)
        m = len(nums2)

        #dp stores the length of longest  repeated subarray
        dp = [[0]*(m + 1) for i in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1

        # return max of dp table
        return max(max(row) for row in dp)