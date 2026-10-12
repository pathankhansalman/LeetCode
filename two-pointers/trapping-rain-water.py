# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:45:48 2022

@author: patha
"""

from copy import deepcopy
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def _get_vol_(arg1, arg2, right=True):
            if right:
                bm = height_mod[arg2]
            else:
                bm = height_mod[arg1]
            water = 0
            if right:
                rng_start = arg1 + 1
            else:
                rng_start = arg1
            for k in range(rng_start, arg2):
                water += abs(height_mod[k] - bm)
            # print(arg1, arg2, water)
            return water
        if not height:
            return 0
        height_mod = deepcopy(height)
        while height_mod[0] == 0:
            height_mod[:] = height_mod[1:]
            if not height_mod:
                return 0
        while height_mod[-1] == 0:
            height_mod[:] = height_mod[:-1]
            if not height_mod:
                return 0
        n = len(height_mod)
        max_ht_idx = [0]*n
        second_max_ht_idx = [0]*n
        i = n - 1
        while i >= 0:
            if i == n - 1:
                max_ht_idx[i] = n - 1
                second_max_ht_idx[i] = n - 1
            else:
                if height_mod[i] >= height_mod[max_ht_idx[i + 1]]:
                    max_ht_idx[i] = i
                    second_max_ht_idx[i] = max_ht_idx[i + 1]
                else:
                    max_ht_idx[i] = max_ht_idx[i + 1]
                    if height_mod[i] >= height_mod[second_max_ht_idx[i + 1]]:
                        second_max_ht_idx[i] = i
                    else:
                        second_max_ht_idx[i] = second_max_ht_idx[i + 1]
            i -= 1
        # print(max_ht_idx)
        # print(second_max_ht_idx)
        i = 0
        water = 0
        while i < n - 1:
            if max_ht_idx[i] == i:
                j = second_max_ht_idx[i]
                water += _get_vol_(i, j, True)
                i = j
                continue
            else:
                j = i + 1
                while j < n:
                    if height_mod[j] >= height_mod[i]:
                        water += _get_vol_(i, j, False)
                        i = j
                        break
                    j += 1
        return water


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
