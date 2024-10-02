class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        minimum = nums[0]
        maximum = nums[-1]
        res  = maximum - minimum # Initial result, the difference between the largest and smallest numbers

        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i + 1] # a < b since sorted
            # to get the new answer, we will look at the maxmimum of our current max - k and maximum value we can get which is a + k
            #  we will look at the minimum of our current min and minimum + k value we can get which is b - k
            high = max(maximum - k, a + k)
            low = min(minimum + k, b - k)
            res = min(res, high - low)
        return res