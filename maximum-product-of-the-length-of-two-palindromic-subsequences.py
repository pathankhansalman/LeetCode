# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:58:16 2022

@author: patha
"""

from itertools import combinations
class Solution:
    def maxProduct(self, s: str) -> int:
        def _is_palin_(arg):
            nonlocal mem_dict
            if not arg:
                return True
            if len(arg) == 1:
                return True
            if arg in mem_dict.keys():
                return mem_dict[arg]
            if arg[0] != arg[-1]:
                mem_dict[arg] = False
                return False
            mem_dict[arg] = _is_palin_(arg[1:-1])
            return mem_dict[arg]
        mem_dict = {}
        # mem_dict_2 = {}
        all_comb = []
        all_comb_set = []
        all_comb_str = []
        str_list = list(range(len(s)))
        for i in range(1, len(s) + 1):
            all_comb += [list(x) for x in list(combinations(str_list, i))]
            all_comb_set += [set(x) for x in list(combinations(str_list, i))]
            all_comb_str += [''.join([s[y] for y in x]) for x in list(combinations(str_list, i))]
        # print(all_comb_str)
        is_palin_arr = [_is_palin_(x) for x in all_comb_str]
        all_comb = [all_comb[i] for i, _ in enumerate(all_comb) if is_palin_arr[i]]
        all_comb_set = [all_comb_set[i] for i, _ in enumerate(all_comb_set) if is_palin_arr[i]]
        is_palin_arr = [x for x in is_palin_arr if x]
        max_prod = 1
        print(all_comb_set)
        print(len(all_comb))
        for i in range(len(all_comb)):
            for j in range(i, len(all_comb)):
                if not all_comb_set[i].intersection(all_comb_set[j]):
                    if is_palin_arr[i] and is_palin_arr[j]:
                            # print(''.join([s[k] for k in all_comb[i]]), ''.join([s[k] for k in all_comb[j]]))
                            if len(all_comb[i])*len(all_comb[j]) > max_prod:
                                max_prod = len(all_comb[i])*len(all_comb[j])
        return max_prod