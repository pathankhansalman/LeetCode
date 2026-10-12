# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:47:08 2022

@author: patha
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # construct adjoining dictionary
        adj_dict = {}
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    adj_dict[(i, j)] = []
                    if i < m - 1:
                        if board[i + 1][j] == 'O':
                            adj_dict[(i, j)].append((i + 1, j))
                    if i > 0:
                        if board[i - 1][j] == 'O':
                            adj_dict[(i, j)].append((i - 1, j))
                    if j < n - 1:
                        if board[i][j + 1] == 'O':
                            adj_dict[(i, j)].append((i, j + 1))
                    if j > 0:
                        if board[i][j - 1] == 'O':
                            adj_dict[(i, j)].append((i, j - 1))
        if not adj_dict:
            return None
        print(adj_dict)
        start_vers = []
        non_flip = []
        for key in adj_dict.keys():
            i = key[0]
            j = key[1]
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                start_vers.append(key)
                if not adj_dict[key]:
                    non_flip.append(key)
        if not start_vers:
            # All Os are inland
            for key in adj_dict.keys():
                board[key[0]][key[1]] = 'X'
            return None
        while 1:
            curr_start_ver = start_vers[0]
            non_flip.append(curr_start_ver)
            start_vers += list([x for x in adj_dict[curr_start_ver]
                                if x not in non_flip])
            for ver in adj_dict[curr_start_ver]:
                non_flip.append(ver)
            start_vers = start_vers[1:]
            if not start_vers:
                break
        for key in adj_dict.keys():
            if key not in non_flip:
                board[key[0]][key[1]] = 'X'
        return None