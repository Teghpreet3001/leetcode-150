class TrieNode:
    def __init__(self): 
        self.children = {}
        self.word = None

    def __repr__(self):
        # Provide a concise representation of the TrieNode
        return f"TrieNode(children={list(self.children.keys())}, word={self.word})"

class Trie:
    def __init__(self): 
        self.root = TrieNode()
    
    def insert(self, word): 
        node = self.root 
        for letter in word: 
            if letter not in node.children: 
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word = word

class Solution:
    # create a trie data structure from words to check if we are exploring the correct the child of a TrieNode

    def backtrack(self, board, i, j, words, startNode, res): 
        m = len(board)
        n = len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n: 
            return
        letter = board[i][j] 
        currNode = startNode.children.get(letter)
        if not currNode: 
            return
        if currNode.word is not None: 
            res.append(currNode.word)
            currNode.word = None

        board[i][j] = "#"
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in directions: 
            new_i, new_j = i + dx, j + dy
            self.backtrack(board, new_i, new_j, words, currNode, res)
        
        board[i][j] = letter
        if not currNode.children: 
            startNode.children.pop(letter)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        for word in words: 
            trie.insert(word)
        
        m = len(board)
        n = len(board[0])
        for i in range(m): 
            for j in range(n):
                self.backtrack(board, i, j, words, trie.root, res)
        return res
    
# W - words quantity
# L - average word length
# M, N - board's sizes

# Time complexity: O(W * L + W * L * M * N)

# Space complexity: O(W * L)

        