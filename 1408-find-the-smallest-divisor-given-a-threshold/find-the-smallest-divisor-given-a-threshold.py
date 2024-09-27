class Solution:

    def sumArr(self, div, nums):
        res = 0
        for i in range(len(nums)):
            res += math.ceil(nums[i]/div)
        return res


    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1 
        high = max(nums)
        while low <= high:
            mid = math.floor((low+high)/2)
            if self.sumArr(mid, nums) <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low
    