# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        def ret_helper(arg1, arg2):
            if arg1 is None and arg2 is None:
                return None
            if arg1 is None:
                return arg2
            if arg2 is None:
                return arg1
            retval = TreeNode(arg1.val + arg2.val)
            retval.left = ret_helper(arg1.left, arg2.left)
            retval.right = ret_helper(arg1.right, arg2.right)
            return retval
        return ret_helper(root1, root2)
        