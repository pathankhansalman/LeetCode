# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:09:56 2022

@author: patha
"""

from copy import deepcopy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def _lev_helper_(arg, level):
            if arg is None:
                return []
            return [(arg.val, level)] + _lev_helper_(arg.left, level + 1) + _lev_helper_(arg.right, level + 1)
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        mas_list = _lev_helper_(root, 0)
        # print(mas_list)
        mydict = {}
        for vals in mas_list:
            if vals[1] not in mydict.keys():
                mydict[vals[1]] = [vals[0]]
            else:
                mydict[vals[1]].append(vals[0])
        return [v for k, v in mydict.items()]