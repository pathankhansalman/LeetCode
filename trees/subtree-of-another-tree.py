# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def _subtree_helper_(arg1, arg2):
            if arg1 is None and arg2 is None:
                return True
            if arg1 is None or arg2 is None:
                return False
            if arg1.val == arg2.val:
                return _subtree_helper_(arg1.left, arg2.left) and _subtree_helper_(arg1.right, arg2.right)
            return False
        def _subtree_helper_2_(arg1, arg2):
            if _subtree_helper_(arg1, arg2):
                return True
            if arg1 is None:
                return False
            if _subtree_helper_2_(arg1.left, arg2):
                return True
            if _subtree_helper_2_(arg1.right, arg2):
                return True
            if arg1.val != arg2.val:
                return False
            return _subtree_helper_(arg1.left, arg2.left) and _subtree_helper_(arg1.right, arg2.right)
        return _subtree_helper_2_(root, subRoot)