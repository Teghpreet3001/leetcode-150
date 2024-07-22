class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if self.check(grid, i,j):
                        count += 1
        return count
    
    def check(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return False 
        if grid[i][j] != "1":
            return False
        #Mark the current cell visited
        grid[i][j] = "#"
        directions = [(1,0), (0,1), (-1, 0), (0,-1)]
        for direction in directions:
            new_i, new_j = i + direction[0], j + direction[1]
            self.check(grid, new_i, new_j)
        return True
