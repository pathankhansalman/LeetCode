# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:53:51 2022

@author: patha
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def _bot_helper_(arg, level):
            if arg is None:
                return []
            return [(arg.val, level)] + _bot_helper_(arg.left, level + 1) +\
                   _bot_helper_(arg.right, level + 1)
        mas_list = _bot_helper_(root, 0)
        # mas_list = list(reversed(mas_list))
        if not mas_list:
            return None
        mas_dict = {}
        for item in mas_list:
            if item[1] in mas_dict.keys():
                mas_dict[item[1]].append(item[0])
            else:
                mas_dict[item[1]] = [item[0]]
        return list(reversed([v for k, v in mas_dict.items()]))
        