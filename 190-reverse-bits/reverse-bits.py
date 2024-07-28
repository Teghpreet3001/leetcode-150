class Solution:
    # to set the bits, we & with 1
    # then we just shift to right using >> by i
    # we will have a result which is 0
    # to replace the 0 in result with the bit, we use | with bit 
    # but we have to shift to left first using << by 31 - i
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            shiftedright = (n >> i)
            bit = shiftedright & 1
            shiftedleft = bit << (31 - i)
            res = res | shiftedleft
        return res