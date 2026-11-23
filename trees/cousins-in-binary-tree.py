# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        def depth_helper(arg, val, depth):
            if arg is None:
                return None
            if arg.val == val:
                return depth
            if arg.left is None and arg.right is None:
                return None
            if arg.left is not None:
                left_depth = depth_helper(arg.left, val, depth + 1)
                if left_depth is not None:
                    return left_depth
            return depth_helper(arg.right, val, depth + 1)
        def parent_helper(arg, val):
            if arg is None:
                return None
            if arg.left is None and arg.right is None:
                return None
            if arg.left is not None:
                if arg.left.val == val:
                    return arg.val
            if arg.right is not None:
                if arg.right.val == val:
                    return arg.val
            left_parent = parent_helper(arg.left, val)
            if left_parent is None:
                right_parent = parent_helper(arg.right, val)
                return right_parent
            else:
                return left_parent
        #print(depth_helper(root, x, 0))
        #print(depth_helper(root, y, 0))
        #print(parent_helper(root, x))
        #print(parent_helper(root, y))
        return (depth_helper(root, x, 0) == depth_helper(root, y, 0)) and (parent_helper(root, x) != parent_helper(root, y))
