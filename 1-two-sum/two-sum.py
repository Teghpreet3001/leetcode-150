class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {} # mapping difference to index of the original number
        '''
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map:
                return [map[diff], i]
            map[nums[i]] = i
        '''
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in map:
                return [map[nums[i]], i]
            map[diff] = i