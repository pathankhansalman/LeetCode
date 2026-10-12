# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def in_order(arg):
            if arg is None:
                return []
            return in_order(arg.left) + [arg.val] + in_order(arg.right)
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        vals = in_order(root)
        n = 1
        retval = TreeNode(val=vals[0])
        curr = retval
        while n < len(vals):
            curr.right = TreeNode(val=vals[n])
            curr = curr.right
            n += 1
        return retval
