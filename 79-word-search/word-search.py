class Solution(object):

    def backtrack(self, board, i, j, visited, word, start):
        if start == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in visited: 
            return False
        if board[i][j] != word[start]:
            return False
            
        visited.add((i, j))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for direction in directions:
            new_i, new_j = i + direction[0], j + direction[1]
            if self.backtrack(board, new_i, new_j, visited, word, start + 1):
                return True
        visited.remove((i,j))
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        temp = []
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if self.backtrack(board, i, j, visited, word, 0):
                    return True
        return False