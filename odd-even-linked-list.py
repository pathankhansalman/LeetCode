# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head_list = []
        curr = head
        while curr is not None:
            head_list.append(curr.val)
            curr = curr.next
        # print(head_list[0::2] + head_list[1::2])
        if len(head_list) <= 2:
            return head
        retval = ListNode()
        curr = retval
        for i, val in enumerate(head_list[0::2] + head_list[1::2]):
            curr.val = val
            if i < len(head_list) - 1:
                curr.next = ListNode()
                curr = curr.next
        return retval