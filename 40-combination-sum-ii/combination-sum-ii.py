class Solution(object):

    def backtrack(self, result, nums, subset, target, start):
        if target < 0:
            return 
        if target == 0 :
            result.append(list(subset))
        for i in range(start, len(nums)):
            #checking that duplicaye element are not added to result
            if(i > start and nums[i] == nums[i-1]):
                continue
            subset.append(nums[i])
            self.backtrack(result, nums, subset, target - nums[i], i + 1) #i + 1  becuase we cannot reuse elements
            subset.pop()

    def combinationSum2(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        subset = []
        self.backtrack(result, nums, subset, target, 0)
        return result