# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 00:45:24 2022

@author: patha
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        lens = 0
        curr = head
        while curr != None:
            lens += 1
            curr = curr.next
        true_rot = k % lens
        if true_rot == 0:
            return head
        head_list = []
        curr = head
        while curr != None:
            head_list.append(curr.val)
            curr = curr.next
        head_list[:] = head_list[-1*true_rot:] + head_list[:-1*true_rot]
        print(head_list)
        retval = ListNode()
        curr = retval
        for i, item in enumerate(head_list):
            curr.val = item
            if i == len(head_list) - 1:
                break
            curr.next = ListNode()
            curr = curr.next
        return retval