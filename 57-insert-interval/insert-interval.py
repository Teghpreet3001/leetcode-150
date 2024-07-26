class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):

            #if the interval end is smaller than current, then add it to result, and return result with all the remaining  
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i: ]
            
            #if the interval is large enough, then add all the intervals before the  newInterval, then append it (done outside loop)
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            #if the interval is in the middle, then find the  min of the start of both the intervals and max of both the ends to construct the widest interval 
            else:
                newStart = min(newInterval[0], intervals[i][0])
                newEnd = max(newInterval[1], intervals[i][1])
                newInterval = [newStart, newEnd]
        result.append(newInterval)
        return result

        