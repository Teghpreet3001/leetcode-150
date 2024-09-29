class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        
        def sumDist(x1, y1):
            res = 0
            for x2, y2 in positions:
                res += math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            return res 
        
        # geometic centroid initial guess: sum of all x/y coordinates divided number of points
        x = sum(a for a, b in positions)/len(positions)
        y = sum(b for a, b in positions)/len(positions)
        
        # explore all directions from centroid 
        # exit out of loop if found a min pair
        # decrement the step
        step = 100 
        while step > 1e-6:
            
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx, dy in directions:
                nx, ny = x + step*dx, y + step*dy 
                if sumDist(nx, ny) < sumDist(x, y):  
                    x, y = nx, ny 
                    break 
            else:
                step = step/2 
        
        return sumDist(x, y)