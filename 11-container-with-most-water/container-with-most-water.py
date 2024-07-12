class Solution(object):
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
            whatever value is smaller, we increment that since we want 
            to find the maximum area from both the ends, by not moving
            the larger value, we are preserving it by taking the maximum 
        '''
        left = 0 
        right = len(heights) - 1
        result = - float('inf')
        while left < right:
            area = (right - left)*min(heights[left], heights[right])
            result = max(result, area)
            if heights[left] < heights[right]:
                left += 1
            else: 
                right -= 1
        return result