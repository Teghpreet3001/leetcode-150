class Solution:
    #overlapping condition where the end of the previous interval is greater than the start of the next one, so we set the prevEnd to min of the end of current  interval and prevEnd
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            #overlapping occurs
            if start < prevEnd:
                res += 1
                prevEnd = min(end, prevEnd)
            else:
                #move the value of end to check next  intervals
                prevEnd = end
        return res