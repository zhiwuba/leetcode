#
#  https://leetcode.cn/problems/word-search/
#
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        weight = len(board[0])

        visted = [[0] * weight for i in range(height)]

        def search_word(i, j, d):
            if board[i][j] == word[d]:
                if d == len(word) - 1:
                    return True

                visted[i][j] = 1
                r1 = r2 = r3 = r4 = False
                if i + 1 < height and visted[i + 1][j] == 0:
                    r1 = search_word(i + 1, j, d + 1)

                if j + 1 < weight and visted[i][j + 1] == 0:
                    r2 = search_word(i, j + 1, d + 1)

                if i - 1 >= 0 and visted[i - 1][j] == 0:
                    r3 = search_word(i - 1, j, d + 1)

                if j - 1 >= 0 and visted[i][j - 1] == 0:
                    r4 = search_word(i, j - 1, d + 1)
                visted[i][j] = 0

                if r1 or r2 or r3 or r4:
                    return True
                return False
            else:
                return False

        for i in range(0, height):
            for j in range(0, weight):
                if search_word(i, j, 0):
                    return True
        return False