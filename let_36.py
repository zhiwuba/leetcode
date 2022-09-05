from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0, 9):
            row = set()
            col = set()
            for j in range(0, 9):
                if board[i][j] != ".":
                    if board[i][j] not in row:
                        row.add(board[i][j])
                    else:
                        return False
                if board[j][i] != ".":
                    if board[j][i] not in col:
                        col.add(board[j][i])
                    else:
                        return False

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                data = set()
                for m in range(0, 3):
                    for n in range(0, 3):
                        if board[i + m][j + n] != ".":
                            if board[i + m][j + n] not in data:
                                data.add(board[i + m][j + n])
                            else:
                                return False

        return True