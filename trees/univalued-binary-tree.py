# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def _unival_helper_(arg, val):
            if arg is None:
                return True
            return arg.val == val and _unival_helper_(arg.left, val) and _unival_helper_(arg.right, val)
        return _unival_helper_(root, root.val)