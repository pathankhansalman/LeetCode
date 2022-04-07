# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:00:07 2022

@author: patha
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def _post_order_helper_(arg):
            if arg is None:
                return []
            return _post_order_helper_(arg.left) + _post_order_helper_(arg.right) + [arg.val]
        return _post_order_helper_(root)