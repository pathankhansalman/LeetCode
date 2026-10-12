# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:20:47 2022

@author: salman
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def _inorder_helper_(arg):
            if arg is None:
                return []
            return _inorder_helper_(arg.left) + [arg.val] + _inorder_helper_(arg.right)
        val_list = _inorder_helper_(root)
        return val_list[k - 1]
