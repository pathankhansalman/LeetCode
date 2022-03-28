# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:55:32 2022

@author: patha
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _symm_helper_(arg1, arg2):
            if arg1 is None and arg2 is None:
                return True
            if arg1 is None or arg2 is None:
                return False
            if arg1.val != arg2.val:
                return False
            if _symm_helper_(arg1.left, arg2.right) and _symm_helper_(arg1.right, arg2.left):
                return True
            return False
        return _symm_helper_(root.left, root.right)