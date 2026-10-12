# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 21:36:38 2022

@author: patha
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        def _path_helper_(arg, val):
            if arg.left is None and arg.right is None:
                if val == arg.val:
                    return [[arg.val]]
                return None
            elif arg.left is None:
                right_paths = _path_helper_(arg.right, val - arg.val)
                if right_paths is None:
                    return None
                return [[arg.val] + x for x in right_paths]
            elif arg.right is None:
                left_paths = _path_helper_(arg.left, val - arg.val)
                if left_paths is None:
                    return None
                return [[arg.val] + x for x in left_paths]
            else:
                left_paths = _path_helper_(arg.left, val - arg.val)
                right_paths = _path_helper_(arg.right, val - arg.val)
                if left_paths is None and right_paths is None:
                    return None
                elif right_paths is None:
                    return [[arg.val] + x for x in left_paths]
                elif left_paths is None:
                    return [[arg.val] + x for x in right_paths]
                else:
                    return [[arg.val] + x for x in left_paths] + [[arg.val] + x for x in right_paths]
        if root is None:
            return []
        return _path_helper_(root, targetSum)