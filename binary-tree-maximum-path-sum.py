# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:57:44 2022

@author: patha
"""

import numpy as np
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NewNode:
    def __init__(self, val=0, leftsum=0, rightsum=0, left=None, right=None):
        self.val = val
        self.leftsum = leftsum
        self.rightsum = rightsum
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def _construct_tree_helper_(arg):
            if arg is None:
                return None
            retval = NewNode(val=arg.val)
            retval.left = _construct_tree_helper_(arg.left)
            retval.right = _construct_tree_helper_(arg.right)
            return retval
        def _path_sum_helper_(arg):
            if arg is None:
                return None
            _path_sum_helper_(arg.left)
            _path_sum_helper_(arg.right)
            if arg.left is not None:
                arg.leftsum = arg.left.val + max(max(arg.left.leftsum, arg.left.rightsum), 0)
            if arg.right is not None:
                arg.rightsum = arg.right.val + max(max(arg.right.leftsum,
                                                   arg.right.rightsum), 0)
            print(arg.val, arg.leftsum, arg.rightsum)
            return None
        def _get_sum_helper_(arg):
            if arg.left is None and arg.right is None:
                return arg.val
            elif arg.left is None:
                return max(arg.val + max(0, arg.rightsum), _get_sum_helper_(arg.right))
            elif arg.right is None:
                return max(arg.val + max(0, arg.leftsum), _get_sum_helper_(arg.left))
            else:
                return max(arg.val + max(0, arg.leftsum) + max(0, arg.rightsum),
                           max(_get_sum_helper_(arg.left), _get_sum_helper_(arg.right)))
        newroot = _construct_tree_helper_(root)
        _path_sum_helper_(newroot)
        return _get_sum_helper_(newroot)