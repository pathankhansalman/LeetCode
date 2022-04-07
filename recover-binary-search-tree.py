# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:48:41 2022

@author: patha
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def _recover_helper_(arg):
            def _get_max_(in_arg_1):
                nonlocal max_dict
                if in_arg_1 is None:
                    return -1*(2**31) - 1
                if in_arg_1.val not in max_dict.keys():
                    max_dict[in_arg_1.val] = max(max(in_arg_1.val, _get_max_(in_arg_1.left)), _get_max_(in_arg_1.right))
                return max_dict[in_arg_1.val]
            def _get_min_(in_arg_2):
                nonlocal min_dict
                if in_arg_2 is None:
                    return 2**31
                if in_arg_2.val not in min_dict.keys():
                    min_dict[in_arg_2.val] = min(min(in_arg_2.val, _get_min_(in_arg_2.left)), _get_min_(in_arg_2.right))
                return min_dict[in_arg_2.val]
            def _update_val_(new_val, old_val, in_arg_3):
                nonlocal updated
                if updated:
                    return None
                if in_arg_3 is None:
                    return None
                if in_arg_3.val == old_val:
                    # print(in_arg_3.val)
                    in_arg_3.val = new_val
                    # print(in_arg_3.val)
                    updated = True
                else:
                    _update_val_(new_val, old_val, in_arg_3.left)
                    _update_val_(new_val, old_val, in_arg_3.right)
                return None
            def _is_bst_(arg):
                if arg is None:
                    return True
                left_max = _get_max_(arg.left)
                right_min = _get_min_(arg.right)
                retval = (arg.val > left_max) and (arg.val < right_min)
                if not retval:
                    return False
                retval = retval and _is_bst_(arg.left)
                if not retval:
                    return False
                return retval and _is_bst_(arg.right)
            if arg is None:
                return None
            if arg.left is None and arg.right is None:
                return None
            if _is_bst_(arg):
                return None
            nonlocal max_dict, min_dict
            left_max = _get_max_(arg.left)
            right_min = _get_min_(arg.right)
            if arg.val < left_max and arg.val > right_min:
                updated = False
                _update_val_(right_min, left_max, arg.left)
                updated = False
                _update_val_(left_max, right_min, arg.right)
            elif arg.val < left_max:
                updated = False
                _update_val_(arg.val, left_max, arg)
                max_dict = {}
                arg.val = left_max
            elif arg.val > right_min:
                updated = False
                _update_val_(arg.val, right_min, arg)
                min_dict = {}
                arg.val = right_min
            else:
                _recover_helper_(arg.left)
                _recover_helper_(arg.right)
            return None
        max_dict = {}
        min_dict = {}
        _recover_helper_(root)