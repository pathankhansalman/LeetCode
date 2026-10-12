# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:54:20 2022

@author: patha
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def _connect_helper_(arg, next_ptr):
            if arg is None:
                return None
            arg.next = next_ptr
            _connect_helper_(arg.left, arg.right)
            if next_ptr is None:
                _connect_helper_(arg.right, None)
            else:
                _connect_helper_(arg.right, next_ptr.left)
            return None
        _connect_helper_(root, None)
        return root
        