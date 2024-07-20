class Solution(object):

    def backtrack(self, result, nums, subset, start):
        #check  for duplicates by checking if the  value is same as the value just before and weare in the correct index 
        
        result.append(list(subset))
        for i in range(start, len(nums)):
            #check for duplicates
            if i > start and nums[i] == nums[i-1]: 
                continue
            subset.append(nums[i])
            self.backtrack(result, nums, subset, i + 1)
            subset.pop()

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        subset = []
        self.backtrack(result, nums, subset, 0)
        return result
        