class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        grids = collections.defaultdict(set)  # key = (i /3, j /3)
        for i in range(0,9):
            for j in range(0,9):
                cell = board[i][j]
                if cell == ".":
                    continue
                if cell in rows[i] or cell in cols[j] or cell in grids[(i//3, j//3)]:
                        return False
                rows[i].add(cell)
                cols[j].add(cell)
                grids[(i//3, j//3)].add(cell)
        return True

        