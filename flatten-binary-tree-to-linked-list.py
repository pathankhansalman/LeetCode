# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:51:17 2022

@author: patha
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def _get_inorder_list_(arg):
            if arg is None:
                return []
            return [arg.val] + _get_inorder_list_(arg.left) +\
                   _get_inorder_list_(arg.right)
        if root is None:
            return None
        val_list = _get_inorder_list_(root)
        # print(val_list)
        if len(val_list) > 1:
            root.left = None
            if root.right is None:
                root.right = TreeNode()
            curr = root.right
        for i, val in enumerate(val_list[1:]):
            # print(val)
            curr.val = val
            if i < len(val_list) - 2:
                curr.left = None
                curr.right = TreeNode()
                curr = curr.right
        return root