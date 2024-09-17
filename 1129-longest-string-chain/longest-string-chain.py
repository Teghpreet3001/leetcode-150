class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for word in sorted(words, key = len):
            temp = []
            for i in range(len(word)):
                temp.append(dp.get(word[: i] + word[i + 1: ], 0) + 1)
            dp[word] = max(temp)
        return max(dp.values())
