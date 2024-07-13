class Solution(object):
    def trap(self, bars):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(bars) - 1
        minimum = 0
        maximum = 0
        result = 0
        while (left < right):
            minimum = min(bars[left], bars[right])
            maximum = max(maximum, minimum)
            result += maximum - minimum
            if bars[left] < bars[right]:
                left += 1
            else: 
                right -= 1
        return result