# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:46:34 2022

@author: patha
"""

import numpy as np
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _num_helper_(arg):
            if arg is None:
                return []
            if arg.left is None and arg.right is None:
                return [str(arg.val)]
            left_list = _num_helper_(arg.left)
            right_list = _num_helper_(arg.right)
            return [str(arg.val) + x for x in left_list + right_list]
        num_list = _num_helper_(root)
        return np.sum([int(x) for x in num_list])