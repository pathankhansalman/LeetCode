import numpy as np


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        zz_list = []
        for i in range(numRows):
            zz_list.append([np.nan]*len(s))
        col = 0
        row = 0
        idx = 0
        start_zz = 0
        while idx < len(s):
            zz_list[row][col] = s[idx]
            idx += 1
            if row == 0:
                start_zz = 0
                row += 1
            elif (row == len(zz_list) - 1) or (start_zz == 1):
                start_zz = 1
                if row == 0:
                    start_zz = 0
                    row += 1
                else:
                    row -= 1
                    col += 1
            else:
                row += 1
        mystr = ''
        for i in zz_list:
            for j in i:
                if type(j) == str:  # unicode also
                    mystr += j
        return mystr


if __name__ == '__main__':
    s = Solution()
    print(s.convert('PAYPALISHIRING', 3))
    s = Solution()
    print(s.convert('PAYPALISHIRING', 4))
    print(s.convert('AB', 1))
