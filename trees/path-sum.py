# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:53:11 2022

@author: patha
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def _help_path_finder_(arg, val):
            if arg is None:
                return False
            if arg.left is None and arg.right is None:
                if arg.val == val:
                    return True
                return False
            else:
                return _help_path_finder_(arg.left, val - arg.val) or\
                       _help_path_finder_(arg.right, val - arg.val)
        return _help_path_finder_(root, targetSum)