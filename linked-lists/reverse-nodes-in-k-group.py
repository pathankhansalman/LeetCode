# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 20:45:34 2022

@author: patha
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        list_head = ListNode()
        curr = list_head
        for i in head:
            curr.val = i
            curr.next = ListNode(None, None)
            curr = curr.next
        mylist = []
        curr = list_head
        while curr.val is not None:
            mylist.append(curr.val)
            curr = curr.next
        i = 0
        while i < len(mylist) - k + 1:
            mylist[i:i+k] = reversed(mylist[i:i+k])
            i += k
        retval = ListNode()
        curr = retval
        idx = 0
        for i in mylist:
            print(i)
            curr.val = i
            idx += 1
            if idx == len(mylist):
                break
            curr.next = ListNode(None, None)
            curr = curr.next
        return retval


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.reverseKGroup([1, 2, 3, 4, 5], 3))
