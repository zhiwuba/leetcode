class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        weight = len(matrix[0])

        row_flag0 = False
        col_flag0 = False
        for i in range(0, height):
            if matrix[i][0] == 0:
                col_flag0 = True
                break
        for i in range(0, weight):
            if matrix[0][i] == 0:
                row_flag0 = True
                break

        for i in range(1, height):
            for j in range(1, weight):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, height):
            if matrix[i][0] == 0:
                for j in range(1, weight):
                    matrix[i][j] = 0

        for i in range(1, weight):
            if matrix[0][i] == 0:
                for j in range(1, height):
                    matrix[j][i] = 0

        if col_flag0:
            for i in range(0, height):
                matrix[i][0] = 0

        if row_flag0:
            for i in range(0, weight):
                matrix[0][i] = 0