# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        #result array to update the max path sum
        result = [root.val]

        def helper(root):
            if not root :
                return 0
                
            leftResult = helper(root.left)
            rightResult = helper(root.right)

            #update path sum to 0 if either result is negative
            leftResult = max(0, leftResult)
            rightResult = max(0, rightResult)

            #update result if we are getting a better path sum by moving left or right
            result[0] = max(result[0], root.val + leftResult + rightResult)
            #return only the max of left and rigt results since we can move only in one direction
            return root.val + max(leftResult, rightResult)

        helper(root)
        return result[0]