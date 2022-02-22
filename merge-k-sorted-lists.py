# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 01:46:26 2022

@author: patha
"""
from copy import deepcopy
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        all_none = True
        for mylist in lists:
            if mylist is not None:
                all_none = False
                break
        if all_none:
            return None
        lists_arr = [0]*len(lists)
        idx = 0
        for mylist in lists:
            list_head = ListNode()
            curr = list_head
            for i in mylist:
                # print(i)
                curr.val = i
                curr.next = ListNode(None, None)
                curr = curr.next
            lists_arr[idx] = deepcopy(list_head)
            idx += 1
        # print(len(lists_arr))
        retval_list = []
        for mylist in lists_arr:
            curr = mylist
            # print(mylist.val)
            while curr.val is not None:
                # print(curr.val)
                retval_list.append(curr.val)
                curr = curr.next
        retval_list = sorted(retval_list)
        list_head2 = ListNode()
        curr = list_head2
        idx = 0
        for i in retval_list:
            curr.val = i
            idx += 1
            if idx == len(retval_list):
                break
            curr_next = ListNode(None, None)
            curr.next = curr_next
            curr = curr_next
        return retval_list
        


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.mergeKLists([[1,4,5],[1,3,4],[2,6]]))
