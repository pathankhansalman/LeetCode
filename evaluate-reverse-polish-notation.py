# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:02:29 2022

@author: patha
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_number(s):
             try:
                float(s)
                return True
             except ValueError:
                return False
        stack = []
        for token in tokens:
            stack.append(token)
            if len(stack) >= 3:
                if is_number(stack[-3]) and is_number(stack[-2]) and not is_number(stack[-1]):
                    stack = stack[:-3] + [eval('int(%s%s%s)' % (stack[-3],
                                                                stack[-1],
                                                                stack[-2]))]
        return int(stack[0])