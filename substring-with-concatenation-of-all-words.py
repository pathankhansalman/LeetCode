# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 23:05:22 2022

@author: patha
"""
# Current status - TLE
import re
from copy import deepcopy

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        un_words = words
        substr_idx_dict = {}
        done_idx_dict = {}
        curr_done_idx_dict = {}
        for i, word in enumerate(un_words):
            substr_idx_dict[i] = set([m.start() for m in re.finditer('(%s)(?=(%s))' % (word[0], word[1:]), s)])
            done_idx_dict[i] = False
            curr_done_idx_dict[i] = False
        ret_idxs = []
        for i in range(len(s) - len(un_words[0])*len(un_words) + 1):
            start_idx = i
            # print(i)
            # start_idx_found = False
            num_words_found = 0
            prev_start_idx = start_idx
            all_words_found = True
            curr_done_idx_dict = deepcopy(done_idx_dict)
            while num_words_found < len(un_words):
                for j in done_idx_dict.keys():
                    if curr_done_idx_dict[j] == False and start_idx in substr_idx_dict[j]:
                        start_idx += len(un_words[0])
                        curr_done_idx_dict[j] = True
                        num_words_found += 1
                        break
                if start_idx > prev_start_idx:
                    prev_start_idx = start_idx
                    continue
                elif num_words_found == len(un_words):
                    break
                else:
                    all_words_found = False
                    break
            if all_words_found:
                ret_idxs.append(i)
        return ret_idxs


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.findSubstring('ababababab', ["ababa","babab"]))
