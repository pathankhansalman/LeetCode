# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:31:50 2022

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
        def _conn_helper_(arg, level):
            nonlocal map_dict
            if arg is None:
                return None
            if level not in map_dict.keys():
                map_dict[level] = [arg]
            else:
                map_dict[level].append(arg)
            _conn_helper_(arg.left, level + 1)
            _conn_helper_(arg.right, level + 1)
            return None
        if root is None:
            return None
        map_dict = {}
        _conn_helper_(root, 0)
        # print(map_dict)
        for i in map_dict.keys():
            for j, item in enumerate(map_dict[i]):
                if j < len(map_dict[i]) - 1:
                    map_dict[i][j].next = map_dict[i][j + 1]
        return root