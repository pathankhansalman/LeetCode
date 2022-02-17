# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:48:23 2022

@author: patha
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def _bin_search_(arg, int_list, sub_target):
            # print(arg, int_list)
            if len(int_list) == 1:
                return int_list[0]
            if len(int_list) == 2:
                if abs(target - sub_target - int_list[0]) <\
                        abs(target - sub_target -
                            int_list[1]):
                    return int_list[0]
                else:
                    return int_list[1]
            mid_idx = int(len(int_list)/2)
            if int_list[mid_idx] == arg:
                return int_list[mid_idx]
            elif int_list[mid_idx] < arg:
                if int_list[mid_idx + 1] == arg:
                    return int_list[mid_idx + 1]
                elif int_list[mid_idx + 1] > arg:
                    if abs(target - sub_target - int_list[mid_idx]) <\
                            abs(target - sub_target -
                                int_list[mid_idx + 1]):
                        return int_list[mid_idx]
                    else:
                        return int_list[mid_idx + 1]
                else:
                    return _bin_search_(arg, int_list[mid_idx:],
                                        sub_target)
            else:
                if int_list[mid_idx - 1] == arg:
                    return int_list[mid_idx - 1]
                elif int_list[mid_idx - 1] < arg:
                    if abs(target - sub_target - int_list[mid_idx]) <\
                            abs(target - sub_target -
                                int_list[mid_idx - 1]):
                        return int_list[mid_idx]
                    else:
                        return int_list[mid_idx - 1]
                else:
                    return _bin_search_(arg, int_list[0:mid_idx],
                                        sub_target)
        curr_diff = 99999999999
        curr_found = 0
        mydict = {}
        all_tups = []
        if len(nums) < 3:
            return all_tups
        sorted_nums = sorted(nums)
        for i in range(2, len(sorted_nums)):
            mydict[i] = sorted_nums[i:]
        for i in range(len(sorted_nums) - 2):
            for j in range(i + 1, len(sorted_nums) - 1):
                k = target - sorted_nums[i] - sorted_nums[j]
                op_k = _bin_search_(k, mydict[j + 1],
                                    sorted_nums[i] + sorted_nums[j])
                if abs(target - sorted_nums[i] - sorted_nums[j] -
                       op_k) < curr_diff:
                    curr_found = sorted_nums[i] + sorted_nums[j] + op_k
                    curr_diff = abs(target - sorted_nums[i] - sorted_nums[j] -
                                    op_k)
        return curr_found


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.threeSumClosest([0, 0, 0], 0))
