class Solution(object):
    def  backtrack(self, nums, result, subset, start):
        result.append(list(subset))
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.backtrack(nums, result, subset, i + 1)
            subset.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        subset= []
        self.backtrack(nums, result, subset, 0)
        return result 

