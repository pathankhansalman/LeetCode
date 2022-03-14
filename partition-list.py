# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:05:38 2022

@author: patha
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        small_list = []
        large_list = []
        curr = head
        while curr is not None:
            if curr.val < x:
                small_list.append(curr.val)
            else:
                large_list.append(curr.val)
            curr = curr.next
        retval = ListNode()
        curr = retval
        for i, val in enumerate(small_list):
            curr.val = val
            if i == len(small_list) - 1:
                break
            curr.next = ListNode()
            curr = curr.next
        if small_list and large_list:
            curr.next = ListNode()
            curr = curr.next
        for i, val in enumerate(large_list):
            curr.val = val
            if i == len(large_list) - 1:
                break
            curr.next = ListNode()
            curr = curr.next
        return retval