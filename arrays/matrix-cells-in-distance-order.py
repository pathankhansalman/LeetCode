class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        cells = [[i, j] for i in range(rows) for j in range(cols)]
        return sorted(cells, key=lambda(x): abs(x[0] - rCenter) + abs(x[1] - cCenter))
