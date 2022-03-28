# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:39:33 2022

@author: patha
"""

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        def _int_helper_(arg1, arg2, arg3, choice):
            # print(arg1, arg2, arg3, choice)
            nonlocal mem_dict
            if (arg1, arg2, arg3, choice) in mem_dict.keys():
                return mem_dict[(arg1, arg2, arg3, choice)]
            if choice == 1:
                if not arg1:
                    if not arg3:
                        return True
                    return False
                elif arg1 == arg3:
                    return True
                arg1_overlap = 0
                for i in range(len(arg1)):
                    if arg1[i] == arg3[i]:
                        arg1_overlap += 1
                    else:
                        break
                if arg1_overlap == 0:
                    return False
                retval = False
                for i in range(1, arg1_overlap + 1):
                    if (arg1[i:], arg2, arg3[i:], 2) not in mem_dict.keys():
                        mem_dict[(arg1[i:], arg2, arg3[i:], 2)] = _int_helper_(arg1[i:], arg2, arg3[i:], 2)
                    retval = retval or mem_dict[(arg1[i:], arg2, arg3[i:], 2)]
                    if retval:
                        return retval
                return retval
            else:
                if not arg2:
                    if not arg3:
                        return True
                    return False
                elif arg2 == arg3:
                    return True
                arg2_overlap = 0
                for i in range(len(arg2)):
                    if arg2[i] == arg3[i]:
                        arg2_overlap += 1
                    else:
                        break
                if arg2_overlap == 0:
                    return False
                retval = False
                for i in range(1, arg2_overlap + 1):
                    if (arg1, arg2[i:], arg3[i:], 1) not in mem_dict.keys():
                        mem_dict[(arg1, arg2[i:], arg3[i:], 1)] = _int_helper_(arg1, arg2[i:], arg3[i:], 1)
                    retval = retval or mem_dict[(arg1, arg2[i:], arg3[i:], 1)]
                    if retval:
                        return retval
                return retval
        mem_dict = {}
        if not s1 and not s2 and not s3:
            return True
        elif not s1 and not s2:
            return False
        elif len(s3) != len(s1) + len(s2):
            return False
        return _int_helper_(s1, s2, s3, 1) or _int_helper_(s1, s2, s3, 2)