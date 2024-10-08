class Solution:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        #create dp array of size m x n
        dp = [[0]*n for i in range(m)]

        # Initialize the first row and first column to 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        #fill dp with cumulative sums of ways to reach each cell from either the top or left
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m - 1][n - 1]