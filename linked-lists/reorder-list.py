# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:59:41 2022

@author: patha
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head_list = []
        curr = head
        while curr is not None:
            head_list.append(curr.val)
            curr = curr.next
        retval = []
        for i in range((len(head_list) // 2) + 1):
            retval.append(head_list[i])
            if len(head_list) - 1 - i > i:
                retval.append(head_list[len(head_list) - 1 - i])
        curr = head
        idx = 0
        while curr is not None:
            curr.val = retval[idx]
            curr = curr.next
            idx += 1
        return None