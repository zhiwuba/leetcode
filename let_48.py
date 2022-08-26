from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)

        for ring in range(int(length / 2)):
            for i in range(0, length - ring * 2 -1):
                a = matrix[ring][ring + i]
                b = matrix[ring + i][length - ring - 1]
                c = matrix[length - ring - 1][length - ring - 1 - i]
                d = matrix[length - ring - 1 - i][ring]

                print(i, a,b,c,d)

                matrix[ring][ring + i] = d
                matrix[ring + i][length - ring - 1] = a
                matrix[length - ring - 1][length - ring - 1 - i] = b
                matrix[length - ring - 1 - i][ring] = c






if __name__ == '__main__':
    """
    [1,2,3]
    [4,5,6]
    [7,8,9]    
    """


    s = Solution()
    d = [[1,2,3],[4,5,6],[7,8,9]]
    s.rotate(d)
    print(d)
