# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 22:07:03 2022

@author: patha
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        i = 0
        j = 0
        retval = []
        while i < m or j < n:
            if i == m:
                retval.append(nums2[j])
                j += 1
            elif j == n:
                retval.append(nums1[i])
                i += 1
            else:
                if nums1[i] < nums2[j]:
                    retval.append(nums1[i])
                    i += 1
                elif nums1[i] > nums2[j]:
                    retval.append(nums2[j])
                    j += 1
                else:
                    retval.append(nums2[j])
                    retval.append(nums1[i])
                    i += 1
                    j += 1
        print(retval)
        nums1[:] = retval
        return nums1