"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def _pre_order_helper_(arg):
            if arg is None:
                return []
            retval = [arg.val]
            if arg.children is None:
                return retval
            for child in arg.children:
                retval += _pre_order_helper_(child)
            return retval
        return _pre_order_helper_(root)
