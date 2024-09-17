class Solution:
    # we take side by taking the minimum of the height and width and not the max as square will go outside the matrix: side = min(h, w)
    # res = max(res, side * side)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        res = 0
        height = [0] *(n + 1)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] = height[j] + 1
                else:
                    height[j] = 0
            stack = [-1]
            for j in range(n + 1):
                while height[j] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = j - 1 - stack[-1]
                    side = min(h, w)
                    res = max(res, side * side)
                stack.append(j)
        return res 