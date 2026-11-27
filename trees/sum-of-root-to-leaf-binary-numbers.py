# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def bin_str_helper(arg, pre_str):
            if arg.left is None and arg.right is None:
                all_strs.append(pre_str + str(arg.val))
                return
            if arg.left is not None:
                bin_str_helper(arg.left, pre_str + str(arg.val))
            if arg.right is not None:
                bin_str_helper(arg.right, pre_str + str(arg.val))
        all_strs = []
        bin_str_helper(root, "")
        return sum([int(x, base=2) for x in all_strs])
