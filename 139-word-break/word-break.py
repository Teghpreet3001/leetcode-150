class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        #dp[i] = string from 0 to i is  in wordDict
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                word = s[j:i]
                if dp[j] and word in wordDict:
                    dp[i] = True
                    break
        return dp[n]