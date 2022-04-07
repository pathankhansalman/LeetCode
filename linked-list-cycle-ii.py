# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:48:10 2022

@author: patha
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return None
        curr = head
        idx_dict = {}
        i = 0
        while curr is not None:
            idx_dict[curr] = i
            if curr.next in idx_dict.keys():
                return curr.next
            curr = curr.next
            i += 1
        return None