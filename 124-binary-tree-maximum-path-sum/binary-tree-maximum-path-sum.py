# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        self.helper(root)
        return self.max_sum

    def helper(self, node):
        if not node:
            return 0
        leftResult = self.helper(node.left)
        rightResult = self.helper(node.right)
        
        leftResult = max(0, leftResult)
        rightResult = max(0, rightResult)

        self.max_sum = max(self.max_sum, node.val + leftResult + rightResult)
        return node.val + max(leftResult, rightResult)
