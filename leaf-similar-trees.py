# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leaf_seq_helper(arg):
            if arg.left is None and arg.right is None:
                return [arg.val]
            elif arg.left is None:
                return leaf_seq_helper(arg.right)
            elif arg.right is None:
                return leaf_seq_helper(arg.left)
            else:
                return leaf_seq_helper(arg.left) + leaf_seq_helper(arg.right)
        root1_seq = leaf_seq_helper(root1)
        root2_seq = leaf_seq_helper(root2)
        return root1_seq == root2_seq
        