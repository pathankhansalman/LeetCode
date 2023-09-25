from copy import deepcopy
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        treedict = {}
        for edge in edges:
            if edge[0] not in treedict:
                treedict[edge[0]] = {}
            if edge[1] not in treedict:
                treedict[edge[1]] = {}
            treedict[edge[0]][edge[1]] = 0
            treedict[edge[1]][edge[0]] = 0
        leaves = [k for k, v in treedict.items() if len(v) == 1]
        while 1:
            if len(treedict) <= 2:
                break
            print(len(leaves))
            new_leaves = []
            for leaf in leaves:
                treedict[list(treedict[leaf].keys())[0]].pop(leaf)
                if len(treedict[list(treedict[leaf].keys())[0]]) == 1:
                    new_leaves.append(list(treedict[leaf].keys())[0])
                treedict.pop(leaf)
            leaves = deepcopy(new_leaves)
        return list(treedict.keys())
