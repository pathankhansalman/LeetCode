import numpy as np

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num_flowers = 0
        curr_num_flowers = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if i > 0:
                    flowerbed[i - 1] = -1
                if i < len(flowerbed) - 1:
                    flowerbed[i + 1] = -1
        for i in range(len(flowerbed)):
            print(num_flowers, curr_num_flowers)
            if flowerbed[i] == 1 or flowerbed[i] == -1:
                if curr_num_flowers > 0:
                    if curr_num_flowers % 2 == 0:
                        num_flowers += curr_num_flowers//2
                    else:
                        num_flowers += curr_num_flowers//2
                        num_flowers += 1
                    curr_num_flowers = 0
                continue
            else:
                curr_num_flowers += 1
        if curr_num_flowers > 0:
            if curr_num_flowers % 2 == 0:
                num_flowers += curr_num_flowers//2
            else:
                num_flowers += curr_num_flowers//2
                num_flowers += 1
        return num_flowers >= n
