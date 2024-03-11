import math

class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        retval = []
        for i in range(len(img)):
            curr_retval = []
            for j in range(len(img[0])):
                count = 1
                curr_sum = img[i][j]
                if i > 0 and j > 0:
                    curr_sum += img[i - 1][j - 1]
                    count += 1
                if i > 0:
                    curr_sum += img[i - 1][j]
                    if j < len(img[0]) - 1:
                        curr_sum += img[i - 1][j + 1]
                        count += 1
                    count += 1
                if j > 0:
                    curr_sum += img[i][j - 1]
                    count += 1
                    if i < len(img) - 1:
                        curr_sum += img[i + 1][j - 1]
                        count += 1
                if i < len(img) - 1 and j < len(img[0]) - 1:
                    curr_sum += img[i + 1][j + 1]
                    count += 1
                if j < len(img[0]) - 1:
                    curr_sum += img[i][j + 1]
                    count += 1
                if i < len(img) - 1:
                    curr_sum += img[i + 1][j]
                    count += 1
                curr_retval.append(int(math.floor(curr_sum*1.0/count)))
            retval.append(curr_retval)
        return retval
