class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] += 1
            else: 
                map[nums[i]] = 1
        for key in map:
            if map[key] > 1:
                return True
        return False
        