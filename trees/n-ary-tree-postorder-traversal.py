"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def _post_order_helper_(arg):
            if arg is None:
                return []
            if arg.children is None:
                return [arg.val]
            retval = []
            for child in arg.children:
                retval += _post_order_helper_(child)
            return retval + [arg.val]
        return _post_order_helper_(root)