class Solution(object):

    def isValid(self, unit):
        unitSet = set()
        for num in unit:
            if num != ".":
                if num in unitSet:
                    return False
                unitSet.add(num)
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if not self.isValid(row):
                return False
        
        for i in range(len(board)):
            row = board[i]
            col = []
            for j in range(len(row)):
                cell = board[j][i]
                col.append(cell)
            if not self.isValid(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid = []
                for k in range(3):
                    row = board[i+k][j:j+3]
                    for cell in row:
                        grid.append(cell)
                if not self.isValid(grid):
                    return False
        return True

        