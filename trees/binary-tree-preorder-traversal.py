# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:57:13 2022

@author: patha
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def _preorder_helper_(arg):
            if arg is None:
                return []
            return [arg.val] + _preorder_helper_(arg.left) +\
                _preorder_helper_(arg.right)     
        return _preorder_helper_(root)