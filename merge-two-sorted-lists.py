# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 23:07:39 2022

@author: patha
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list_head = ListNode()
        curr = list_head
        for i in list1:
            curr.val = i
            curr_next = ListNode(None, None)
            curr.next = curr_next
            curr = curr_next
        list_head2 = ListNode()
        curr = list_head2
        for i in list2:
            curr.val = i
            curr_next = ListNode(None, None)
            curr.next = curr_next
            curr = curr_next
        curr1 = list_head
        curr2 = list_head2
        retval = ListNode(-1, None)
        curr = retval
        while curr1.val != None or curr2.val != None:
            if (curr1.val != None and curr2.val == None) or curr1.val < curr2.val:
                curr.val = curr1.val
                curr1 = curr1.next
            else:
                curr.val = curr2.val
                curr2 = curr2.next
            # print(curr.val)
            curr.next = ListNode(None, None)
            curr = curr.next
        retval_list = []
        curr = retval
        while curr.val is not None:
            retval_list.append(curr.val)
            curr = curr.next
        return retval_list


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.mergeTwoLists([1, 2, 4], [1, 3, 4]))
