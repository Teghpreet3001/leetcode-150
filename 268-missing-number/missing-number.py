class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        res = 0
        for i in range(len(nums) + 1):
            if i in nums:
                continue
            res = i
        return res
        '''
        # we do XOR if they are same, output is 0, if they are different, 1
        # if XOR a number with itself, we get the 0
        # if we XOR something with 0, we get the same number
        # so we iterate over the range and XOR res with all numbers
        # res = 0 ^ 1 ^ 2 ^ 3
        # then we iterate over nums and XOR with each num, all the nums present will cancel out and res will be left with missing num
        # res = (0 ^ 1 ^ 2 ^ 3) ^ (3 ^ 0 ^ 1) = 2
        n =len(nums)
        res = 0
        for i in range(1, n + 1):
            res = res ^ i
        for num in nums:
            res = res ^ num
        return res