class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        print(nums)
        if len(nums) % 2 != 0:
            index = (len(nums) + 1)/2
            return float(nums[index - 1])
        else :
            index1 = len(nums)/2
            num1 = nums[index1 - 1]
            print(num1)
            index2 = (len(nums)/2) + 1
            num2 = nums[index2 - 1]
            print(num2)
            return (num1 + num2)/2.0