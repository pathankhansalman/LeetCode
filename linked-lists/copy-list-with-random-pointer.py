# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:49:55 2022

@author: patha
"""


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        new_null_pt = None
        curr = head
        retval = Node(0)
        curr_retval = retval
        idx_dict = {}
        old_idx_dict = {}
        idx = 0
        while curr is not None:
            curr_retval.val = curr.val
            idx_dict[idx] = curr_retval
            old_idx_dict[idx] = curr
            curr = curr.next
            if curr is not None:
                curr_retval.next = Node(0)
                curr_retval = curr_retval.next
            else:
                curr_retval.next = new_null_pt
            idx += 1
        curr = head
        curr_retval = retval
        while curr is not None:
            # print(curr.random)
            if curr.random is None:
                curr_retval.random = new_null_pt
            else:
                curr_retval.random = idx_dict[{v: k for k, v in old_idx_dict.items()}[curr.random]]
            curr = curr.next
            curr_retval = curr_retval.next
        return retval