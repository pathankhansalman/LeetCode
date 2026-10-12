# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 23:11:38 2022

@author: patha
"""
import itertools

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def _sum_help_(val):
            if val < new_can[0]:
                return None
            else:
                curr_list = []
                for num in new_can:
                    if num == val:
                        curr_list += [[val]]
                        continue
                    new_val = val - num
                    curr_num_list = []
                    if new_val in mem_dict.keys():
                        if mem_dict[new_val] is None:
                            continue
                        for comb in mem_dict[new_val]:
                            curr_num_list.append([num] + comb)
                    else:
                        mem_dict[new_val] = _sum_help_(new_val)
                        if mem_dict[new_val] is None:
                            continue
                        for comb in mem_dict[new_val]:
                            curr_num_list.append([num] + comb)
                    if len(curr_num_list) > 0:
                        curr_list += curr_num_list
            if len(curr_list) == 0:
                return None
            return curr_list
        new_can = list(sorted(candidates))
        mem_dict = {}
        retval = _sum_help_(target)
        if retval is None:
            return []
        retval = [list(x) for x in set([tuple(sorted(x)) for x in retval])]
        return retval


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.combinationSum([2, 3, 5], 8))
