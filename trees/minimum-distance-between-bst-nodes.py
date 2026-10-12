# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _get_max_(arg):
            if arg.right is None:
                return arg.val
            return _get_max_(arg.right)
        def _get_min_(arg):
            if arg.left is None:
                return arg.val
            return _get_min_(arg.left)
        def _get_min_diff_(arg):
            if arg.left is None and arg.right is None:
                return 9999999999
            elif arg.left is None:
                return min(_get_min_(arg.right) - arg.val, _get_min_diff_(arg.right))
            elif arg.right is None:
                return min(arg.val - _get_max_(arg.left), _get_min_diff_(arg.left))
            else:
                return min(_get_min_(arg.right) - arg.val, arg.val - _get_max_(arg.left), _get_min_diff_(arg.right), _get_min_diff_(arg.left))
        return _get_min_diff_(root)