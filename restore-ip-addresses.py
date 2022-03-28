# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 21:56:18 2022

@author: patha
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def _ip_helper_(arg, count):
            if not arg:
                return None
            if count == 1:
                if len(arg) > 3:
                    return None
                if len(arg) > 1 and arg[0] == '0':
                    return None
                if int(arg) > 255:
                    return None
                return [arg]
            if len(arg) < count:
                return None
            if (arg[1:], count - 1) not in mem_dict.keys():
                mem_dict[(arg[1:], count - 1)] = _ip_helper_(arg[1:], count - 1)
            one_minus = mem_dict[(arg[1:], count - 1)]
            retval = []
            if one_minus is not None:
                retval = [arg[0] + '.' + x for x in one_minus]
            if arg[0] != '0':
                if (arg[2:], count - 1) not in mem_dict.keys():
                    mem_dict[(arg[2:], count - 1)] = _ip_helper_(arg[2:], count - 1)
                two_minus = mem_dict[(arg[2:], count - 1)]
                if two_minus is not None:
                    retval += [arg[0:2] + '.' + x for x in two_minus]
                if int(arg[0:3]) <= 255:
                    three_minus = _ip_helper_(arg[3:], count - 1)
                    if three_minus is not None:
                        retval += [arg[0:3] + '.' + x for x in three_minus]
            return retval
        mem_dict = {}
        return _ip_helper_(s, 4)