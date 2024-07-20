class MedianFinder(object):

    def __init__(self):
        self.nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.nums.append(num)

    def findMedian(self):
        """
        :rtype: float
        """
        nums = self.nums
        if not nums:
            return 0
        nums.sort()
        if len(nums) % 2 != 0:
            index = (len(nums) + 1)/2
            return float(nums[index - 1])
        else :
            index1 = len(nums)/2
            num1 = nums[index1 - 1]
            index2 = (len(nums)/2) + 1
            num2 = nums[index2 - 1]
            return (num1 + num2)/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()