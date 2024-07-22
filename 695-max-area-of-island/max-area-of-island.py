class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def calculateArea(grid, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0

            #check if not an island and check if visited before
            if grid[i][j] != 1 or (i,j) in visited:
                return 0
            visited.add((i,j))
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            localArea = 0
            for direction in directions:
                new_i, new_j = i + direction[0], j + direction[1]
                localArea += calculateArea(grid, new_i, new_j)
            print(1+localArea)
            return 1 + localArea

        for i in range(m):
            for j in range(n):
                area = max(area, calculateArea(grid, i, j))
        return area
        
    