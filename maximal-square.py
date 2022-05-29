# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:15:30 2022

@author: salman
"""

from copy import deepcopy


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1:
            if matrix[0][0] == '1':
                return 1
            return 0
        dp_arr = []
        for i in range(m):
            dp_arr.append([0]*n)
        max_val = 0
        if matrix[m - 1][n - 1] == '1':
            dp_arr[m - 1][n - 1] = [(1, 1)]
            max_val = 1
        else:
            dp_arr[m - 1][n - 1] = 0
        for i in range(n - 2, -1, -1):
            if matrix[m - 1][i] == '0':
                dp_arr[m - 1][i] = 0
            elif matrix[m - 1][i] == '1':
                if dp_arr[m - 1][i + 1] == 0:
                    dp_arr[m - 1][i] = [(1, 1)]
                    if max_val == 0:
                        max_val = 1
                else:
                    dp_arr[m - 1][i] = [(1, dp_arr[m - 1][i + 1][0][1] + 1)]
                    if max_val == 0:
                        max_val = 1
        for i in range(m - 2, -1, -1):
            if matrix[i][n - 1] == '0':
                dp_arr[i][n - 1] = 0
            elif matrix[i][n - 1] == '1':
                if dp_arr[i + 1][n - 1] == 0:
                    dp_arr[i][n - 1] = [(1, 1)]
                    if max_val == 0:
                        max_val = 1
                else:
                    dp_arr[i][n - 1] = [(dp_arr[i + 1][n - 1][0][0] + 1, 1)]
                    if max_val == 0:
                        max_val = 1
        # print(dp_arr)
        for j in range(n - 2, -1, -1):
            for i in range(m - 2, -1, -1):
                if matrix[i][j] == '0':
                    dp_arr[i][j] = 0
                elif dp_arr[i + 1][j] == 0 and dp_arr[i][j + 1] == 0:
                    dp_arr[i][j] = [(1, 1)]
                elif dp_arr[i + 1][j] == 0:
                    dp_arr[i][j] = [(1, max([x[1] for x in dp_arr[i][j + 1]]) + 1)]
                elif dp_arr[i][j + 1] == 0:
                    dp_arr[i][j] = [(max([x[0] for x in dp_arr[i + 1][j]]) + 1, 1)]
                else:
                    curr_tup_list = []
                    max_x = -1
                    max_y = -1
                    for x in dp_arr[i][j + 1]:
                        for y in dp_arr[i + 1][j]:
                            curr_tuple = (min(1 + y[0], x[0]), min(y[1], 1 + x[1]))
                            if curr_tuple[0] <= max_x and curr_tuple[1] <= max_y:
                                continue
                            max_x = max(curr_tuple[0], max_x)
                            max_y = max(curr_tuple[1], max_y)
                            if curr_tuple not in curr_tup_list:
                                curr_tup_list.append(curr_tuple)
                    for x in dp_arr[i][j + 1]:
                        curr_tuple = (1, 1 + x[1])
                        if curr_tuple[0] <= max_x and curr_tuple[1] <= max_y:
                            continue
                        max_x = max(curr_tuple[0], max_x)
                        max_y = max(curr_tuple[1], max_y)
                        if curr_tuple not in curr_tup_list:
                            curr_tup_list.append(curr_tuple)
                    for y in dp_arr[i + 1][j]:
                        curr_tuple = (1 + y[0], 1)
                        if curr_tuple[0] <= max_x and curr_tuple[1] <= max_y:
                            continue
                        max_x = max(curr_tuple[0], max_x)
                        max_y = max(curr_tuple[1], max_y)
                        if curr_tuple not in curr_tup_list:
                            curr_tup_list.append(curr_tuple)
                    curr_tup_list = list(sorted(curr_tup_list, key=lambda x: (x[0], x[1])))
                    idx = 0
                    while idx < len(curr_tup_list) - 1:
                        if curr_tup_list[idx][0] <= curr_tup_list[idx + 1][0] and\
                                curr_tup_list[idx][1] <= curr_tup_list[idx + 1][1]:
                            anomaly = True
                            curr_tup_list = curr_tup_list[0:idx] + curr_tup_list[idx + 1:]
                            continue
                        else:
                            idx += 1
                    dp_arr[i][j] = deepcopy(curr_tup_list)
                if dp_arr[i][j] == 0:
                    continue
                for x in dp_arr[i][j]:
                    if min(x[0], x[1])**2 > max_val:
                        max_val = min(x[0], x[1])**2
        # print(dp_arr)
        return max_val