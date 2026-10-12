# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 21:28:47 2022

@author: patha
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        mylist = []
        curr = head
        while curr is not None:
            mylist.append(curr.val)
            curr = curr.next
        mylist[left-1:right] = list(reversed(mylist[left-1:right]))
        retval = ListNode()
        curr = retval
        for i, val in enumerate(mylist):
            curr.val = val
            if i != len(mylist) - 1:
                curr.next = ListNode()
                curr = curr.next
        return retval