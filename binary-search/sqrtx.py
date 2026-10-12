# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:59:25 2022

@author: patha
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        mylist = list(range(1, 2**16))
        left = 0
        right = len(mylist) - 1
        while 1:
            mid = (right + left) // 2
            if mylist[mid]*mylist[mid] == x:
                return mylist[mid]
            elif mylist[mid + 1]*mylist[mid + 1] == x:
                return mylist[mid + 1]
            elif mylist[mid - 1]*mylist[mid - 1] == x:
                return mylist[mid - 1]
            elif mylist[mid]*mylist[mid] < x and x < mylist[mid + 1]*mylist[mid + 1]:
                return mylist[mid]
            elif mylist[mid - 1]*mylist[mid - 1] < x and x < mylist[mid]*mylist[mid]:
                return mylist[mid - 1]
            elif x < mylist[mid]*mylist[mid]:
                right = mid
            elif x > mylist[mid]*mylist[mid]:
                left = mid