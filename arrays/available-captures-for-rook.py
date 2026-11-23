class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        pawns = []
        rook = None
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    rook = [i, j]
                    break
        for i in range(8):
            for j in range(8):
                if board[i][j] == "p":
                    if i == rook[0] or j == rook[1]:
                        pawns.append([i, j])
        attack_count = 0
        for pawn in pawns:
            attack = True
            if pawn[0] == rook[0]:
                for j in range(min(pawn[1], rook[1]) + 1, max(pawn[1], rook[1])):
                    if board[pawn[0]][j] != ".":
                        attack = False
                        break
            if not attack:
                continue
            if pawn[1] == rook[1]:
                for i in range(min(pawn[0], rook[0]) + 1, max(pawn[0], rook[0])):
                    if board[i][pawn[1]] != ".":
                        attack = False
                        break
            if attack:
                attack_count += 1
        return attack_count
