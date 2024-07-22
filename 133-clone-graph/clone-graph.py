"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):

    def dfs(self, oldToNewMap, startNode):
        if startNode in oldToNewMap:
            return oldToNewMap[startNode]

        copy = Node(startNode.val)
        oldToNewMap[startNode] = copy

        for neighbor in startNode.neighbors:
            neighborCopy = self.dfs(oldToNewMap, neighbor)
            copy.neighbors.append(neighborCopy)
            
        return copy

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        #map of old nodes to new nodes
        oldToNewMap = {}
        return self.dfs(oldToNewMap, node)
    