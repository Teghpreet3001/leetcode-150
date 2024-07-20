class MedianFinder(object):

    def __init__(self):
        #keep two heaps of approximately equal size 
        #minheap and maxheap 
        #make sure lengths atre approximately eqaul 
        #make sure all elements of minheap <= maxheap
        #median = (max  of minheap + min of maxheap)/2
        #by  using heap the data gets automatically sorted
        self.minheap = []
        self.maxheap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #since Python only hads minheaps, we will multiply all elements of our minheap by -1 so thhat the feault heap becomes a maxheap
        heapq.heappush(self.minheap, -1*num)
        #min heap will go from [1,2,3] -> [-3,-2,-1]
        #maxheap will be like [4,5,6]
        #make sure all elements of minheap <= maxheap
        if self.minheap and self.maxheap:
            if -1 * self.minheap[0] > self.maxheap[0]:
                val = -1 * heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, val)

        #minheap is larger so pop from minheap and add to push maxheap
        if len(self.minheap) > len(self.maxheap) + 1:
            val = -1 * heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, val)

        #maxheap is larger so pop from maxheap and add to push minheap
        if len(self.maxheap) > len(self.minheap) + 1:
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -1*val)

    def findMedian(self):
        """
        :rtype: float
        """
        #odd length case 1
        #[-3, -2, -1] [4,5]
        #so we return the first element of minheap * -1
        if len(self.minheap) > len(self.maxheap):
            return -1 * self.minheap[0]
        #odd length case 1
        #[-3, -2, -1] [4,5, 6, 7]
        #so we return the first element of maxheap 
        if len(self.minheap) < len(self.maxheap):
            return self.maxheap[0]
        #even length case 
        #return the mean of negative of first element of minheap  and first element of maxheap
        return (-1 * self.minheap[0] + self.maxheap[0])/2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()