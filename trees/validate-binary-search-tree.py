# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:17:52 2022

@author: patha
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _valid_helper_(arg):
            if arg.left is None and arg.right is None:
                return (arg.val, arg.val, True)
            elif arg.left is None:
                ret_arr = _valid_helper_(arg.right)
                if not ret_arr[2]:
                    return (-1, -1, False)
                return (min(arg.val, ret_arr[0]), max(arg.val, ret_arr[1]), arg.val < ret_arr[0])
            elif arg.right is None:
                ret_arr = _valid_helper_(arg.left)
                if not ret_arr[2]:
                    return (-1, -1, False)
                return (min(arg.val, ret_arr[0]), max(arg.val, ret_arr[1]), arg.val > ret_arr[1])
            else:
                ret_arr = _valid_helper_(arg.right)
                ret_arr_left = _valid_helper_(arg.left)
                if not (ret_arr[2] and ret_arr_left[2]):
                    return (-1, -1, False)
                return (min(min(arg.val, ret_arr[0]), ret_arr_left[0]), max(max(arg.val, ret_arr[1]), ret_arr_left[1]), (arg.val > ret_arr_left[1]) and (arg.val < ret_arr[0]))
        # print(_valid_helper_(root))
        return _valid_helper_(root)[2]