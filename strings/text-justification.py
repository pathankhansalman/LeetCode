# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 01:00:56 2022

@author: patha
"""
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        retval = []
        curr_str = ''
        i = 0
        while i < len(words):
            curr_str += words[i]
            if len(curr_str) == maxWidth:
                retval.append(curr_str)
                curr_str = ''
                i += 1
            elif len(curr_str) > maxWidth:
                curr_str = curr_str[:-1*len(words[i])]
                curr_str = curr_str.rstrip()
                num_spaces_req = maxWidth - len(curr_str)
                count_sp = curr_str.count(' ')
                if count_sp == 0:
                    retval.append(curr_str + ' '*(maxWidth - len(curr_str)))
                    curr_str = ''
                elif (num_spaces_req % count_sp) == 0:
                    curr_str = curr_str.replace(' ', ' '*((num_spaces_req // count_sp) + 1))
                    retval.append(curr_str)
                    curr_str = ''
                else:
                    curr_str = curr_str.replace(' ', ' '*((num_spaces_req // count_sp) + 1))
                    curr_str = curr_str.replace(' '*((num_spaces_req // count_sp) + 1),
                                                ' '*((num_spaces_req // count_sp) + 2), num_spaces_req % count_sp)
                    retval.append(curr_str)
                    curr_str = ''
            else:
                curr_str += ' '
                i += 1
        if curr_str != '':
            retval.append(curr_str + ' '*(maxWidth - len(curr_str)))
        return retval