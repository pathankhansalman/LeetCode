# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:00:55 2022

@author: patha
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _merge_(arg1, arg2):
            m = len(arg1)
            n = len(arg2)
            i = 0
            j = 0
            retval = []
            while i < m or j < n:
                if i == m:
                    retval.append(arg2[j])
                    j += 1
                elif j == n:
                    retval.append(arg1[i])
                    i += 1
                else:
                    if arg1[i] < arg2[j]:
                        retval.append(arg1[i])
                        i += 1
                    elif arg1[i] > arg2[j]:
                        retval.append(arg2[j])
                        j += 1
                    else:
                        retval.append(arg1[i])
                        i += 1
                        retval.append(arg2[j])
                        j += 1
            return retval
        def _merge_sort_(arg):
            if len(arg) <= 1:
                return arg
            mid = len(arg) // 2
            left = _merge_sort_(arg[:mid])
            right = _merge_sort_(arg[mid:])
            return _merge_(left, right)
        if head is None:
            return None
        if head.next is None:
            return head
        curr = head
        head_list = []
        while curr is not None:
            head_list.append(curr.val)
            curr = curr.next
        retval = ListNode()
        curr = retval
        sorted_list = _merge_sort_(head_list)
        for i, num in enumerate(sorted_list):
            curr.val = num
            if i < len(sorted_list) - 1:
                curr.next = ListNode()
                curr = curr.next
        return retval