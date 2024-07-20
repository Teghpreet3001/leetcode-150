class Solution(object):

    #using nums[i] in permutation check becomes trivial here because our array can have duplicates
    def backtrack(self, result, permutation, nums, used):
        if len(permutation) == len(nums):
            result.append(list(permutation))
        for i in range(len(nums)):
            #check for duplicates and if nums[i] in permutation
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            permutation.append(nums[i])
            self.backtrack(result, permutation, nums, used)
            #set used[i] to False for the next iteration
            used[i] = False
            permutation.pop()
 
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        permutation = []
        #list to track which elements are used
        used = [False]*len(nums)
        self.backtrack(result, permutation, nums, used)
        return result