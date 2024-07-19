# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def helper(self, root, low=float('-inf'), high=float('inf')):
        if not root:
            return True
        if not (low < root.val and root.val < high):
            return False
        return self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root)
            