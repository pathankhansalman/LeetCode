import numpy as np
import itertools
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 1:
            return [['Q']]
        if n == 2 or n == 3:
            return []
        q_arr = [np.array(['Q'])]
        q_arr = [np.hstack((['.']*1, x)) for x in q_arr]
        q_arr = np.insert(q_arr, 0, ['Q'] + ['.']*1, axis=0)
        q_arr = [np.array(x) for x in list(itertools.permutations(q_arr))]
        for i in range(2, n):
            q_arr = [np.hstack(([['.']]*i, x)) for x in q_arr]
            q_arr = np.concatenate((np.array([np.array([np.array(['Q'] + ['.']*i)])]*len(q_arr)), q_arr), axis=1)
            q_arr = np.array([np.array(x) for x in itertools.permutations(q_arr[0])])
        q_int_arr = np.copy(q_arr)
        q_int_arr[q_int_arr == 'Q'] = 1
        q_int_arr[q_int_arr == '.'] = 0
        q_int_arr = q_int_arr.astype(int)
        q_int_arr = q_int_arr.T
        q_flip = np.fliplr(q_int_arr)
        idx_arr = np.array([True]*len(q_arr))
        for i in range(-1*n + 1, n):
            idx_arr = idx_arr & (np.sum(np.diagonal(q_int_arr, i), axis=1) <= 1)
            idx_arr = idx_arr & (np.sum(np.diagonal(q_flip, i), axis=1) <= 1)
        return [[''.join(y) for y in x] for x in q_arr[idx_arr]]


if __name__ == '__main__':
    mysol = Solution()
    mysol.solveNQueens(5)
