# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:52:01 2022

@author: patha
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def _part_helper_(arg):
            def _is_palin_(in_arg):
                if len(in_arg) <= 1:
                    return True
                if in_arg[0] != in_arg[-1]:
                    return False
                return _is_palin_(in_arg[1:-1])
            # print(arg)
            if len(arg) == 0:
                return [[]]
            if len(arg) == 1:
                return [[arg]]
            else:
                retval = []
                for i in range(1, len(arg) + 1):
                    if _is_palin_(arg[0:i]):
                        curr_retval = _part_helper_(arg[i:])
                        # print(curr_retval)
                        if not curr_retval:
                            continue
                        retval += [[arg[0:i]] + x for x in curr_retval]
                return retval
        return _part_helper_(s)