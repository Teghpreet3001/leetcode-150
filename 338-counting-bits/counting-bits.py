class Solution:
    # we can also do n = n & (n-1)
    # since the bits of i shift, we must store it in temp

    def countBits(self, n: int) -> List[int]:
        result = [0]*(n+1)
        result[0] = 0
        for i in range(1, n + 1):
            count = 0
            temp = i
            while i > 0:
                if i % 2 != 0:
                    count += 1
                i = i >> 1
            result[temp] = count
        return result
