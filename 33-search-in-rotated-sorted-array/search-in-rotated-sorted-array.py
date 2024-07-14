class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high: 
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            #left portion is sorted
            elif nums[low] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1 #check right portion
                else:
                    high = mid - 1 #check left portion
            #right sorted portion
            else:
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1  #check left portion
                else:
                    low = mid + 1 #check right portion
        return -1