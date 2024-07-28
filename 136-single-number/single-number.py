class Solution:
    # XOR a number with itself equals 0 
    # we set res = 0 and XOR it with the array 
    # we iterate overs nums and set res = tes ^ nums[i]
    # all pairs will get cancelled and we are left with Single Number
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res