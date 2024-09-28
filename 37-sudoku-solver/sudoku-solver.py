class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #starter code from valid sudoku puzzle 
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        grids = collections.defaultdict(set)  # key = (i /3, j /3)

        n = len(board)
        for i in range(0,9):
            for j in range(0,9):
                cell = board[i][j]
                if cell == ".":
                    continue
                cell = int(cell)
                rows[i].add(cell)
                cols[j].add(cell)
                grids[(i//3, j//3)].add(cell)
        
        def valid(i, j, cell):
            #Check if placing cell at board[i][j] is valid.
            return cell not in rows[i] and cell not in cols[j] and cell not in grids[(i // 3, j // 3)]
        
        def backtrack(i, j):
            if i == n:
                return True  # Completed all rows, puzzle solved
            if j == n:  # Move to the next row
                return backtrack(i + 1, 0)
            if board[i][j] != ".":  # Skip filled cells
                return backtrack(i, j + 1)

            for cell in range(1, 10):
                if not valid(i, j, cell):
                    continue
                # Place the value
                board[i][j] = str(cell)
                rows[i].add(cell)
                cols[j].add(cell)
                grids[(i//3, j//3)].add(cell)

                if backtrack(i, j + 1): # Recur to the next cell
                    return True

                #undo the choice or backtrack
                board[i][j] = "."
                rows[i].remove(cell)
                cols[j].remove(cell)
                grids[(i//3, j//3)].remove(cell)
            return False
        backtrack(0,0)
                
                

            
