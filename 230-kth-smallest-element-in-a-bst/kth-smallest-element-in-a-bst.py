# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def inorderTraversal(self, root):
        result = []
        self.inorderHelper(root,result)
        return result

    def inorderHelper(self, root, result):
        if root is None:
            return
        self.inorderHelper(root.left, result)
        result.append(root.val)
        self.inorderHelper(root.right, result)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        data = self.inorderTraversal(root)
        print(data)
        return data[k-1]