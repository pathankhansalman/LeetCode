# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:28:21 2022

@author: patha
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list_head = ListNode()
        curr = list_head
        for i in head:
            curr.val = i
            curr_next = ListNode(None, None)
            curr.next = curr_next
            curr = curr_next
        curr = list_head
        i = 0
        while curr.val is not None:
            i += 1
            curr = curr.next
        if i == 1:
            return []
        curr = list_head
        parent = ListNode(-1, curr)
        curr_parent = parent
        j = 0
        while curr.val is not None:
            j += 1
            if j == i - n + 1:
                curr_parent.next = curr.next
                break
            curr_parent = curr
            curr = curr.next
        parent = parent.next
        curr = parent
        retval = []
        while curr.val is not None:
            retval.append(curr.val)
            curr = curr.next
        return retval
        


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.removeNthFromEnd([1, 2, 3, 4, 5], 2))
