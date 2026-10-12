# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = []
        curr_l1 = l1
        while curr_l1 is not None:
            l1_list.append(str(curr_l1.val))
            curr_l1 = curr_l1.next
        l2_list = []
        curr_l2 = l2
        while curr_l2 is not None:
            l2_list.append(str(curr_l2.val))
            curr_l2 = curr_l2.next
        num_l1 = int(''.join(reversed(l1_list)))
        num_l2 = int(''.join(reversed(l2_list)))
        mysum = num_l1 + num_l2
        retval = ListNode()
        curr_retval = retval
        mysum = list(reversed(list(str(mysum))))
        for i, sums in enumerate(mysum):
            curr_retval.val = sums
            if i == (len(mysum) - 1):
                continue
            curr_retval.next = ListNode()
            curr_retval = curr_retval.next
        return retval


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    sol = Solution()
    print(sol.addTwoNumbers())
