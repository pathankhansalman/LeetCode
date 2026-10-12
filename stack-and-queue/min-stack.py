# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:04:19 2022

@author: patha
"""

class MinStack:

    def __init__(self, minval=[], mems=[], currmin=2**33):
        self.minval = minval[:]
        self.mems = mems[:]
        self.currmin = currmin

    def push(self, val: int) -> None:
        self.mems.append(val)
        if val < self.currmin:
            self.minval.append(val)
            self.currmin = val
        else:
            self.minval.append(self.currmin)

    def pop(self) -> None:
        self.mems = self.mems[:-1]
        self.minval = self.minval[:-1]
        if self.minval:
            self.currmin = self.minval[-1]
        else:
            self.currmin = 2**33
        # print(self.minval)

    def top(self) -> int:
        return self.mems[-1]

    def getMin(self) -> int:
        # print(self.minval)
        return self.minval[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()