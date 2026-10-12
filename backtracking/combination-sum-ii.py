# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 00:01:45 2022

@author: patha
"""

from copy import deepcopy
class Solution(object):
    def combinationSum2(self, candidates, target):
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
                    if num > val:
                        continue
                    if num == val:
                        curr_list += [[val]]
                        continue
                    new_val = val - num
                    if new_val == 0:
                        continue
                    curr_num_list = []
                    if new_val in mem_dict.keys():
                        if mem_dict[new_val] is None:
                            continue
                        for comb in mem_dict[new_val]:
                            curr_num_list.append([num] + comb)
                    else:
                        # print(val, num, new_val)
                        mem_dict[new_val] = _sum_help_(new_val)
                        # print(mem_dict[new_val])
                        if mem_dict[new_val] is None:
                            continue
                        for comb in mem_dict[new_val]:
                            curr_num_list.append([num] + comb)
                    if len(curr_num_list) > 0:
                        curr_list += curr_num_list
            if len(curr_list) == 0:
                return None
            curr_list = [list(x) for x in set([tuple(sorted(x)) for x in curr_list])]
            mem_dict[val] = curr_list
            return curr_list
        new_can = list(sorted(candidates))
        mem_dict = {}
        retval = _sum_help_(target)
        # print('Outside!')
        if retval is None:
            return []
        retval = [list(x) for x in set([tuple(sorted(x)) for x in retval])]
        join_str = ','.join([str(x) for x in new_can])
        retval = [x for x in retval if ','.join([str(y) for y in x]) in join_str]
        return retval


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 30))
