class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #time complexity is going to be O(nlogn + qlogq)
        #use a minHeap to store interval size and the start value since the condition is that queries[j] <= right[i]
        intervals.sort()
        minHeap = []
        #every query is mapped to the length of smallest interval
        res = {}
        i = 0
        #create a copy of sorted queries as we do want the relative order
        for q in sorted(queries):
            #check if  the left[i] is less than query
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                intervalSize = right - left + 1
                heapq.heappush(minHeap, (intervalSize, right))
                i += 1
            #checking if the interval is too far off left by checking the smallest interval's right value  
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            #smallest element is at top of heap, and 0th index is the size
            res[q] = minHeap[0][0] if minHeap else -1

        #answer list to return everything in order, that is why we did not do queries.sort()
        answer = []
        for q in queries:
            answer.append(res[q])
        return answer
        