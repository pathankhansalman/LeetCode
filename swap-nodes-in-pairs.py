# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 19:55:26 2022

@author: patha
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
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
        while i < len(mylist):
            temp = mylist[i]
            mylist[i] = mylist[i + 1]
            mylist[i + 1] = temp
            i += 2
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
    print(mysol.swapPairs([1, 2, 3, 4]))
