from collections import deque
class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        fresh_oranges = 0
        res = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i,j, 0))  # (row, column, minutes)
        
        if fresh_oranges == 0:
            return 0
        
        while queue:
            x, y, minutes = queue.popleft()

            directions = [(1,0), (0,1), (-1,0),(0,-1)]
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 2
                    queue.append((new_x, new_y, minutes + 1))
                    fresh_oranges -= 1
                    res = max(res, minutes + 1)
            
        if fresh_oranges == 0:
            return res
        else:
            return -1 

