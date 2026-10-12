# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:00:34 2022

@author: patha
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        head_list = []
        curr = head
        while curr is not None:
            head_list.append(curr.val)
            curr = curr.next
        n = len(head_list)
        for i in range(1, n):
            curr_elem = head_list[i]
            if curr_elem >= head_list[i - 1]:
                continue
            if curr_elem <= head_list[0]:
                head_list[0:i + 1] = [curr_elem] + head_list[0:i]
                continue
            for j in range(1, i):
                if curr_elem >= head_list[j - 1] and curr_elem <= head_list[j]:
                    head_list[0:i + 1] = head_list[0:j] + [curr_elem] +\
                        head_list[j:i]
                    break
        curr = head
        for num in head_list:
            curr.val = num
            curr = curr.next
        return head