 
 
 # https://leetcode.com/problems/sudoku-solver/

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(r, c, num, board):
            for i in range(n):
                if board[r][i] == num:
                    return False
                if board[i][c] == num:
                    return False
                if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == num:
                    return False
            return True

        def f(board):
            for r in range(m):
                for c in range(n):
                    if board[r][c] == ".":
                        for num in range(1, 10):
                            num = str(num)
                            if is_valid(r, c, num, board):
                                board[r][c] = num
                                if f(board):
                                    return True
                                else:
                                    board[r][c] = "."
                        return False
            return True

        m, n = len(board), len(board[0])
        f(board)
