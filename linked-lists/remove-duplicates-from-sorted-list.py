# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:01:04 2022

@author: patha
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head
        curr = head
        mydict = {}
        while curr is not None:
            if curr.val not in mydict.keys():
                mydict[curr.val] = 1
            curr = curr.next
        list_vals = list(sorted(list(mydict.keys())))
        if not list_vals:
            return None
        retval = ListNode()
        curr = retval
        for i, item in enumerate(list_vals):
            curr.val = item
            if i < len(list_vals) - 1:
                curr.next = ListNode()
                curr = curr.next
        return retval