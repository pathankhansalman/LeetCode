import numpy as np


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        tot_len = len(nums1) + len(nums2)
        if tot_len % 2 == 1:
            first_len = int(tot_len/2) + 1
            second_len = int(tot_len/2)
        else:
            first_len = int(tot_len/2)
            second_len = int(tot_len/2)
        i = 0
        j = 0
        first_arr = []
        second_arr = []
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                if len(first_arr) == first_len:
                    second_arr.append(nums2[j])
                    j += 1
                    continue
                else:
                    first_arr.append(nums2[j])
                    j += 1
                    continue
            elif j == len(nums2):
                if len(first_arr) == first_len:
                    second_arr.append(nums1[i])
                    i += 1
                    continue
                else:
                    first_arr.append(nums1[i])
                    i += 1
                    continue
            else:
                if nums1[i] <= nums2[j]:
                    if len(first_arr) == first_len:
                        second_arr.append(nums1[i])
                        i += 1
                        continue
                    else:
                        first_arr.append(nums1[i])
                        i += 1
                        continue
                else:
                    if len(first_arr) == first_len:
                        second_arr.append(nums2[j])
                        j += 1
                        continue
                    else:
                        first_arr.append(nums2[j])
                        j += 1
                        continue
        if first_len > second_len:
            return first_arr[-1]
        else:
            return (first_arr[-1] + second_arr[0])/2
        

if __name__ == '__main__':
    mysol = Solution()
    print(mysol.findMedianSortedArrays([1, 2], [3, 4]))
