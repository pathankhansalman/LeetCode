# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:58:06 2022

@author: patha
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curr = headA
        while curr is not None:
            curr.val = -1*curr.val
            curr = curr.next
        curr = headB
        while curr is not None:
            if curr.val < 0:
                break
            curr = curr.next
        if curr is None:
            curr2 = headA
            while curr2 is not None:
                if curr2.val > 0:
                    break
                curr2.val = -1*curr2.val
                curr2 = curr2.next
            return None
        curr2 = curr
        while curr2 is not None:
            curr2.val = -1*curr2.val
            curr2 = curr2.next
        curr2 = headA
        while curr2 is not None:
            if curr2.val > 0:
                break
            curr2.val = -1*curr2.val
            curr2 = curr2.next
        return curr