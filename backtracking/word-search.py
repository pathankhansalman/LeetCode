# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:50:51 2022

@author: patha
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def _find_helper_(arg_str, arg_idx_x, arg_idx_y):
            # print(arg_str, arg_idx_x, arg_idx_y)
            # nonlocal mem_dict
            nonlocal explored_dict
            # if (arg_idx_x, arg_idx_y, arg_str) in mem_dict.keys():
            #    explored_set.add((arg_idx_x, arg_idx_y))
            #    return mem_dict[(arg_idx_x, arg_idx_y, arg_str)]
            if not (board[arg_idx_x][arg_idx_y] == arg_str[0]):
                explored_dict[(arg_idx_x, arg_idx_y)] = True
                # mem_dict[(arg_idx_x, arg_idx_y, arg_str)] = False
                return False
            if len(arg_str) == 1:
                explored_dict[(arg_idx_x, arg_idx_y)] = True
                #   mem_dict[(arg_idx_x, arg_idx_y, arg_str)] = True
                return True
            explored_dict[(arg_idx_x, arg_idx_y)] = True
            # add_path = '%d%d' % (arg_idx_x, arg_idx_y)
            # curr_path += add_path
            # if arg_str == 'EEFS' and arg_idx_x == 2 and arg_idx_y == 2:
            #    print(explored_set)
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if abs(i) + abs(j) > 1:
                        continue
                    new_idx_x = min(max(arg_idx_x + i, 0), len(board) - 1)
                    new_idx_y = min(max(arg_idx_y + j, 0), len(board[0]) - 1)
                    # if arg_str == 'EEFS' and arg_idx_x == 2 and arg_idx_y == 2:
                    #    print((new_idx_x, new_idx_y))
                    # if (new_idx_x, new_idx_y, arg_str[1:]) in mem_dict.keys():
                        # if arg_str == 'EEFS' and arg_idx_x == 2 and arg_idx_y == 2:
                        #    print((new_idx_x, new_idx_y))
                    #     if mem_dict[(new_idx_x, new_idx_y, arg_str[1:])]:
                    #        return True
                    #    else:
                    #        continue
                    if (new_idx_x, new_idx_y) in explored_dict.keys():
                        # if arg_str == 'EEFS' and arg_idx_x == 2 and arg_idx_y == 2:
                        #    print('explored!', (new_idx_x, new_idx_y))
                        continue
                    if _find_helper_(arg_str[1:], new_idx_x, new_idx_y):
                        # mem_dict[(arg_idx_x, arg_idx_y, arg_str, tuple(explored_dict.keys()))] = True
                        # if arg_str == 'EEFS' and arg_idx_x == 2 and arg_idx_y == 2:
                        #    print('here!', mem_dict[(new_idx_x, new_idx_y, arg_str[1:])])
                        return True
                    else:
                        if (new_idx_x, new_idx_y) in explored_dict.keys():
                            explored_dict.pop((new_idx_x, new_idx_y), None)
                            # mem_dict[(new_idx_x, new_idx_y, arg_str[1:], tuple(explored_dict.keys()))] = False
            # mem_dict[(arg_idx_x, arg_idx_y, arg_str, tuple(explored_dict.keys()))] = False
            # print(tuple(explored_dict.keys()))
            return False
        board_counts = {}
        str_counts = {}
        for arr in board:
            for char in arr:
                if char not in board_counts.keys():
                    board_counts[char] = 1
                else:
                    board_counts[char] += 1
        for char in word:
            if char not in str_counts.keys():
                str_counts[char] = 1
            else:
                str_counts[char] += 1
        for char in str_counts.keys():
            if char not in board_counts.keys():
                return False
            elif str_counts[char] > board_counts[char]:
                return False
        mem_dict = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                curr_path = ''
                explored_dict = {}
                if _find_helper_(word, i, j):
                    return True
        # print(mem_dict)
        return False