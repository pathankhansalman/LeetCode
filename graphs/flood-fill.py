from copy import deepcopy
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if color == image[sr][sc]:
            return image
        linked_cells = []
        for i in range(len(image)):
            row = []
            for j in range(len(image[0])):
                row.append(False)
            linked_cells.append(row)
        next_cells = [(sr, sc)]
        while next_cells:
            #print(next_cells)
            curr_next_cells = []
            for next_cell in next_cells:
                if linked_cells[next_cell[0]][next_cell[1]]:
                    continue
                linked_cells[next_cell[0]][next_cell[1]] = True
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if abs(i + j) != 1:
                            continue
                        if next_cell[0] + i < 0 or next_cell[0] + i >= len(image) or next_cell[1] + j < 0 or next_cell[1] + j >= len(image[0]):
                            continue
                        if linked_cells[next_cell[0] + i][next_cell[1] + j]:
                            continue
                        if image[next_cell[0] + i][next_cell[1] + j] == image[next_cell[0]][next_cell[1]]:
                            curr_next_cells.append((next_cell[0] + i, next_cell[1] + j))
            next_cells = deepcopy(curr_next_cells)
        for i in range(len(image)):
            for j in range(len(image[0])):
                if linked_cells[i][j]:
                    image[i][j] = color
        return image
