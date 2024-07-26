class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Sort the intervals based on the starting times
        intervals.sort(key=lambda x: x[0])
        
        result = []
        current_interval = intervals[0]
        
        for i in range(1, len(intervals)):
            if current_interval[1] >= intervals[i][0]:
                # There is an overlap, so merge the intervals
                current_interval[1] = max(current_interval[1], intervals[i][1])
            else:
                # No overlap, add the current interval to the result
                result.append(current_interval)
                current_interval = intervals[i]
        
        # Add the last interval
        result.append(current_interval)
        
        return result