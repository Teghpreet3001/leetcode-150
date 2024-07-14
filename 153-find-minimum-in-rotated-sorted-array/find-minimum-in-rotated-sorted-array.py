class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        low = 0
        high = len(nums) - 1

        while low <= high:

            #check if the array is already sorted and return the left
            if nums[low] < nums[high]:
                result = min(result, nums[low])
                break

            mid = (low + high)//2
            result = min(result, nums[mid])
            if nums[low] <= nums[mid]: #left portion is sorted so we look at right sorted portion
                low = mid + 1
            else: #right portion is sorted so we look at left sorted portion
                high = mid - 1 
        return result 
                
        