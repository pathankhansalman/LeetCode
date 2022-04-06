# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:55:45 2022

@author: patha
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def _tree_helper_(arg):
            if not arg:
                return None
            if len(arg) == 1:
                return TreeNode(val=arg[0])
            left = 0
            right = len(arg) - 1
            mid = (left + right) // 2
            retval = TreeNode(val=arg[mid])
            retval.left = _tree_helper_(arg[:mid])
            retval.right = _tree_helper_(arg[mid+1:])
            return retval
        return _tree_helper_(nums)