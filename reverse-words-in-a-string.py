# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:02:56 2022

@author: patha
"""

import re
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(reversed(re.sub(r'(\W)(?=\1)', '', s.strip()).split(' '))))