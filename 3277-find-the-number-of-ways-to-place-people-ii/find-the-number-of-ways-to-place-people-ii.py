class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : (x[0], -x[1]))
        res = 0 
        for i, (x1, y1) in enumerate(points): 
            y = float("-inf")
            for (x2, y2) in points[i + 1:]:
                if y1 >= y2 > y: 
                    res += 1
                    y = y2
        return res
