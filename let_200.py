from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        weight = len(grid[0])

        def land(m,n):
            if grid[m][n] == "1":
                grid[m][n] = "2"
                directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for a,b in directs:
                    if 0 <= m+a < height and 0 <= n+b < weight:
                        land(m+a, n+b)

        count = 0
        for i in range(0, height):
            for j in range(0, weight):
                if grid[i][j] == "1":
                    count += 1
                    land(i, j)

        return count

