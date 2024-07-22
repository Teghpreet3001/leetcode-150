class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                area = max(area, self.calculateArea(grid, i, j))
        return area
        
    def calculateArea(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return 0
        #check if not an island and check if visited before
        if grid[i][j] != 1 or grid[i][j] == "#":
            return 0
        grid[i][j] = "#"
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        localArea = 0
        for direction in directions:
            new_i, new_j = i + direction[0], j + direction[1]
            localArea += self.calculateArea(grid, new_i, new_j)
        print(1+localArea)
        return 1 + localArea