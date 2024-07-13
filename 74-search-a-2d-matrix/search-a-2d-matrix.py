class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nums = []
        for row in matrix:
            nums += row
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1      
        return False  