# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:53:04 2022

@author: patha
"""

class Solution(object):
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        base_str = '1'
        for i in range(n - 1):
            cnt_list = []
            prev_chr = ''
            for curr_chr in base_str:
                if len(cnt_list) == 0:
                    cnt_list.append((curr_chr, 1))
                else:
                    if prev_chr == curr_chr:
                        cnt_list[-1] = (cnt_list[-1][0], cnt_list[-1][1] + 1)
                    else:
                        cnt_list.append((curr_chr, 1))
                prev_chr = curr_chr
            base_str = ''.join([str(x[1]) + x[0] for x in cnt_list])
            # print(base_str, base_str)
        return base_str


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.countAndSay(5))
