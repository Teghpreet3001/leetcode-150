class Solution(object):
    def sortColors(self, nums):
        #create  amap of which numbers occurs how many times
        #then just overwrite the array by adding indexing from previous number
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        countMap = {0: 0, 1: 0, 2:0}
        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
        print(countMap)
        zerocount = countMap[0] if 0 in countMap else 0
        onecount = countMap[1]  if 1 in countMap else 0
        twocount = countMap[2]  if 2 in countMap else 0
        for i in range(0, zerocount):
            nums[i] = 0
        for i in range(zerocount, onecount + zerocount):
            nums[i] = 1
        for i in range(onecount + zerocount, twocount + onecount + zerocount):
            nums[i] = 2
