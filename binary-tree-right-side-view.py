# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:02:11 2022

@author: patha
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def _level_helper_(arg, level):
            if arg is None:
                return []
            return [(arg.val, level)] + _level_helper_(arg.left, level + 1) +\
                _level_helper_(arg.right, level + 1)
        level_list = _level_helper_(root, 0)
        level_dict = {}
        for item in level_list:
            if item[1] in level_dict.keys():
                level_dict[item[1]].append(item[0])
            else:
                level_dict[item[1]] = [item[0]]
        return [v[-1] for v in level_dict.values()]