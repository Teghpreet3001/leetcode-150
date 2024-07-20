class Solution(object):

    def backtrack(self, result, subset, nums, target, start):
        # use  i + 1 when we do not want duplicate elements
        #use i when we want duplicate elements
        if  target < 0:
            return
        if target == 0:
            result.append(list(subset))
        for i in range(start,len(nums)):
            subset.append(nums[i])
            self.backtrack(result, subset, nums, target - nums[i], i) #not i + 1 because we can reuse same elements
            subset.pop()

    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        subset = []
        self.backtrack(result, subset, nums, target,  0)
        return result
