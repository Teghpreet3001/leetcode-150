class Solution(object):
    #we omitted the start varibale as we want all the numbers in the  permutation list  
    def backtrack(self, result, permutation, nums):
        #check if it is a valif permuattion aka lengths are equal
        if len(permutation) == len(nums):
            result.append(list(permutation))
        else:
            for i in range(len(nums)):
            # if the value already in permutation, skip
                if nums[i] in permutation:
                    continue
                permutation.append(nums[i])
                self.backtrack(result, permutation, nums)
                permutation.pop()
    
    #start withnan empty list and not nums as then result will conatin only one array nums, we fill up the permutation array and as we reach the  length of nums, we append it to result
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        #nums.sort() not necesary since we will be traversing all elements
        permutation = [] 
        self.backtrack(result, permutation, nums)
        return result

        