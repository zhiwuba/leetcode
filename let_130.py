class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        height = len(board)
        weight = len(board[0])

        visited = [[0] * weight for i in range(height)]

        def get_o_region(i, j, result):
            if board[i][j] == "O":
                result.add((i, j))
            for a, b in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= a < height and 0 <= b < weight and board[a][b] == "O" and (a, b) not in result:
                    get_o_region(a, b, result)
            return result

        def surround(i, j):
            paths = set()
            get_o_region(i, j, paths)

            is_open = False
            for (a, b) in paths:
                if a == 0 or a == height - 1 or b == 0 or b == weight - 1:
                    is_open = True
                    break
            if not is_open:
                for (a, b) in paths:
                    board[a][b] = "X"
            for (a, b) in paths:
                visited[a][b] = 1

        for i in range(0, height):
            for j in range(0, weight):
                if board[i][j] == "O" and visited[i][j] == 0:
                    surround(i, j)