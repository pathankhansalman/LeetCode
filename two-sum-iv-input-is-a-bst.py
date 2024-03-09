# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def _pre_order_(arg):
            if arg is None:
                return []
            return _pre_order_(arg.left) + [arg.val] + _pre_order_(arg.right)
        sorted_vals = _pre_order_(root)
        if len(sorted_vals) == 1:
            return False
        i = 0
        j = len(sorted_vals) - 1
        while 1:
            if sorted_vals[i] + sorted_vals[j] == k:
                return True
            if sorted_vals[i] + sorted_vals[j] > k:
                j -= 1
            else:
                i += 1
            if i >= j:
                break
        return False