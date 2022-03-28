# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 22:24:02 2022

@author: patha
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def _help_inorder_(arg):
            if arg is None:
                return []
            return _help_inorder_(arg.left) + [arg.val] + _help_inorder_(arg.right)
        if root is None:
            return []
        return _help_inorder_(root)