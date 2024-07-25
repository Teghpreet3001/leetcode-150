class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a 2D dp array with dimensions (len(text1) + 1) x (len(text2) + 1)
        # If match found, take from diagonal + 1 
        # else, return max of above and on the left
        
        dp = [[0]*(len(text2) + 1) for _ in range(len(text1) + 1)] 

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len(text1)][len(text2)]