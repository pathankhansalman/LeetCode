# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:04:53 2022

@author: patha
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _balanced_helper_(arg):
            if arg is None:
                return (True, 0)
            left_bal, left_ht = _balanced_helper_(arg.left)
            right_bal, right_ht = _balanced_helper_(arg.right)
            return (left_bal and right_bal and (abs(left_ht - right_ht) <= 1), max(left_ht, right_ht) + 1)
        return _balanced_helper_(root)[0]