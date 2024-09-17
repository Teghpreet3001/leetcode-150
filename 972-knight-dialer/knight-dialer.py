from functools import cache
class Solution:
    def __init__(self):
        self.moves = {
            0: [4, 6],
            1 : [6, 8],
            2 : [7, 9],
            3 : [4, 8],
            4 : [3, 9, 0],
            5 : [],
            6 : [1, 7, 0],
            7 : [2, 6],
            8 : [1, 3],
            9 : [2, 4]
        }

    @cache
    def dp(self, target, pos):
        MOD = (10 ** 9) + 7
        if target == 0:
            return 1 
        ans = 0 
        for next_pos in self.moves[pos]:
            ans = (ans + self.dp(target - 1, next_pos)) % MOD
        return ans

    def knightDialer(self, n: int) -> int:
        res = 0 
        MOD = (10 ** 9) + 7
        for i in range(10):
          res = (res + self.dp(n - 1, i)) % MOD 
        return res 