# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def search_helper(arg):
            if arg is None:
                return None
            if arg.val == val:
                return arg
            if arg.left is None and arg.right is None:
                return None
            if arg.left is None or val > arg.val:
                return search_helper(arg.right)
            if arg.right is None or val < arg.val:
                return search_helper(arg.left)
        return search_helper(root)
