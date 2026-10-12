# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 21:05:31 2022

@author: patha
"""

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def _fill_arr_():
            nonlocal seq
            def _flip_helper_(num_str, pos):
                retval = num_str
                if retval[pos] == '0':
                    rep_char = '1'
                else:
                    rep_char = '0'
                return retval[:pos] + rep_char + retval[pos+1:]
            curr_num = seq[-1]
            num_found = False
            for curr_pos in range(n - 1, -1, -1):
                next_str = _flip_helper_(curr_num, curr_pos)
                if next_str in mydict.keys():
                    continue
                elif next_str == end:
                    continue
                seq.append(next_str)
                mydict[next_str] = 1
                if len(seq) == 2**n - 1:
                    return True
                num_found = _fill_arr_()
            if not num_found:
                mydict.pop[seq[-1]]
                seq.pop()
                return False
            return True
        if n == 1:
            return [0, 1]
        start = '0'*n
        end = '1' + '0'*(n-1)
        seq = [start]
        mydict = {start: 1}
        _fill_arr_()
        seq = seq + [end]
        return [int(x, 2) for x in seq]