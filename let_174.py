from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        height = len(dungeon)
        weight = len(dungeon[0])

        data = [[0] * weight for i in range(height)]

        for i in range(height-1, -1, -1):
            for j in range(weight-1, -1, -1):
                values = []
                if i == height - 1 and j == weight - 1:
                    values.append(dungeon[i][j])
                if i < height - 1:
                    values.append(data[i + 1][j] + dungeon[i][j])
                if j < weight - 1:
                    values.append(data[i][j + 1] + dungeon[i][j])
                data[i][j] = min(max(values), 0)

        return 0 - data[0][0] + 1



if __name__ == '__main__':
    dungeon = [
        [-2, -3,  3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    ret = Solution().calculateMinimumHP(dungeon)
    print(ret)
