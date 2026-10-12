# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:36:01 2022

@author: patha
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        def _is_balanced_(arg):    
            if arg is None:
                return (True, 0)
            left_bal, left_val = _is_balanced_(arg.left)
            right_bal, right_val = _is_balanced_(arg.right)
            return (left_bal and right_bal and (abs(left_val - right_val) <= 1),
                    1 + max(left_val, right_val))
        def _const_tree_helper_(arg):
            if not arg:
                return None
            elif len(arg) == 1:
                return TreeNode(arg[0])
            elif len(arg) == 2:
                retval = TreeNode(arg[1])
                retval.left = TreeNode(arg[0])
                return retval
            else:
                mid = len(arg)/2
                retval = TreeNode(arg[mid])
                retval.left = _const_tree_helper_(arg[:mid])
                retval.right = _const_tree_helper_(arg[mid + 1:])
                return retval
        if head is None:
            return None
        curr = head
        node_vals = []
        while curr is not None:
            node_vals.append(curr.val)
            curr = curr.next
        return _const_tree_helper_(node_vals)