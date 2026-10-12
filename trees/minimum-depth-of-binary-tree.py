# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:08:52 2022

@author: patha
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _min_helper_(arg):
            if arg is None:
                return 0
            if arg.left is None and arg.right is None:
                return 1
            elif arg.left is None:
                return 1 + _min_helper_(arg.right)
            elif arg.right is None:
                return 1 + _min_helper_(arg.left)
            else:
                return 1 + min(_min_helper_(arg.left), _min_helper_(arg.right))
        return _min_helper_(root)