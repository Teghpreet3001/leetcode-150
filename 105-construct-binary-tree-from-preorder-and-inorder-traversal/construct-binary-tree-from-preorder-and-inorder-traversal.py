# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        #first value in preorder is always going to root
        root = TreeNode(preorder[0])
        midIndex = -1
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                midIndex = i
        #every value on the left of root in inorder is going to on the left subtree and every value on right is going to be right subtree
        leftSubArray = inorder[:midIndex]
        rightSubArray = inorder[midIndex + 1:]
        root.left = self.buildTree(preorder[1:midIndex + 1], leftSubArray)
        root.right = self.buildTree(preorder[midIndex + 1:], rightSubArray)
        return root