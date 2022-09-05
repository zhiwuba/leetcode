from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        blanks = []
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    blanks.append((i, j))

        def get_blank_nums(i, j):
            current = set()
            for m in range(0, 9):
                current.add(board[i][m])
                current.add(board[m][j])

            areaX = int(i / 3) * 3
            areaY = int(j / 3) * 3
            for m in range(0, 3):
                for n in range(0, 3):
                    current.add(board[areaX + m][areaY + n])

            nums = []
            for i in range(1, 10):
                if str(i) not in current:
                    nums.append(str(i))
            return nums

        def solve(idx):
            if idx >= len(blanks):
                return True

            i, j = blanks[idx]
            nums = get_blank_nums(i, j)
            if not nums:
                return False

            for num in nums:
                board[i][j] = num
                ret = solve(idx + 1)
                if ret == True:
                    return True
                board[i][j] = "."
            return False

        ret = solve(0)
        print(ret)

if __name__ == '__main__':
    data = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(data)
