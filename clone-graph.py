# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:56:26 2022

@author: patha
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def _graph_helper_(arg):
            nonlocal exp_dict
            if arg is None:
                return None
            if arg.val in exp_dict.keys():
                return exp_dict[arg.val]
            retval = Node(arg.val)
            exp_dict[arg.val] = retval
            neigh_list = deepcopy(arg.neighbors)
            if not neigh_list:
                return retval
            new_neigh_list = [_graph_helper_(x) if x not in exp_dict.keys()
                              else exp_dict[x.val] for x in neigh_list]
            retval.neighbors = new_neigh_list
            return retval
        if node is None:
            return None
        if not node.neighbors:
            return Node(node.val)
        exp_dict = {}
        return _graph_helper_(node)