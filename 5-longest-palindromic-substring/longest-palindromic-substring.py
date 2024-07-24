class Solution:
    @cache
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        maxLength = 1 
        result = s[0]
        '''
        dp = [[]]*(len(s))
        for i in range(len(s)):
            dp[i].append(False)
        '''
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for  j in range(i):
                if s[i] == s[j] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i - j + 1 > maxLength:
                        maxLength = i - j + 1
                        result = s[j:i+1]
        return result
        