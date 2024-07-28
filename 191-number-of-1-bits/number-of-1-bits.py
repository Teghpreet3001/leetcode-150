class Solution:
    #for set bits, we basically AND the  binary representation with n - 1
    # so evertime before adding to count, we do n = n & (n-1)
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n % 2 != 0:
                count += 1
            n = n >> 1
        return count