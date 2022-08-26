class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        data = [ [0] * n ] * m
        data[0][0] = grid[0][0]

        for i in range(0, m):
            for j in range(0, n):
                if i >0 and j > 0:
                    data[i][j] = min(data[i-1][j], data[i][j-1]) + grid[i][j]
                elif i>0:
                    data[i][j] = data[i-1][j] + grid[i][j]
                elif j >0:
                    data[i][j] = data[i][j-1] + grid[i][j]
        return data[m-1][n-1]