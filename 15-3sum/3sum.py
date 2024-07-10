class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            midNum = nums[i]
            #check if duplicate values as before so skip
            if i > 0 and midNum == nums[i-1]:
                continue
            low = i + 1
            high = len(nums) - 1
            while low < high:
                if  nums[low] + midNum + nums[high] < 0:
                    low += 1
                elif nums[low] + midNum + nums[high] > 0:
                    high -= 1
                else:
                    result.append([midNum, nums[low], nums[high]])
                    low += 1 #shift only one pointer
                    #duplicate value found, so increment pointer and low must never cross right
                    while nums[low] == nums[low - 1] and low < high: 
                        low += 1
        return result
