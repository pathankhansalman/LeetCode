# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def diam_helper(arg):
            if arg is None:
                return 0, 0
            d_l, h_l = diam_helper(arg.left)
            d_r, h_r = diam_helper(arg.right)
            if arg.left is None and arg.right is None:
                return 0, 0
            if arg.left is None:
                return max(d_r, h_r + 1), h_r + 1
            if arg.right is None:
                return max(d_l, h_l + 1), h_l + 1
            else:
                return max(max(d_l, d_r), h_r + h_l + 2), max(h_l, h_r) + 1
        return diam_helper(root)[0]
