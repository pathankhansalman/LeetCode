# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 10:24:05 2022

@author: patha
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        elif target > matrix[-1][0]:
            arr_idx = len(matrix) - 1
        else:
            left = 0
            right = len(matrix) - 1
            arr_idx = -1
            while 1:
                # print(left, right)
                # print(matrix[left][0], matrix[right][0])
                if right - left == 1:
                    if matrix[left][0] == target:
                        return True
                    elif matrix[right][0] == target:
                        return True
                    elif matrix[left][0] < target and target < matrix[right][0]:
                        arr_idx = left
                        break
                    else:
                        print('Not found!')
                mid = (left + right) // 2
                if matrix[mid][0] == target:
                    return True
                elif matrix[mid][0] > target:
                    right = mid
                else:
                    left = mid
        left = 0
        right = len(matrix[arr_idx]) - 1
        if target > matrix[arr_idx][-1]:
            return False
        while 1:
            if right - left == 1:
                if matrix[arr_idx][left] == target:
                    return True
                elif matrix[arr_idx][right] == target:
                    return True
                elif matrix[arr_idx][left] < target and target < matrix[arr_idx][right]:
                    return False
            mid = (left + right) // 2
            if matrix[arr_idx][mid] == target:
                return True
            elif matrix[arr_idx][mid] > target:
                right = mid
            else:
                left = mid
        return None