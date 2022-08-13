from collections import defaultdict
from typing import List


class Solution:
    # https://leetcode.com/problems/valid-sudoku/

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        grid = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":

                    if (
                        board[i][j] in rows[i]
                        or board[i][j] in cols[j]
                        or board[i][j] in grid[(i // 3, j // 3)]
                    ):
                        return False
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    grid[(i // 3, j // 3)].add(board[i][j])
        return True

    ####################2nd Approach###########################################

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_row(i):
            s1 = set()
            for col in range(9):
                if grid[i][col] in s1:
                    return False
                if grid[i][col] != ".":
                    s1.add(grid[i][col])
            return True

        def is_valid_col(j):
            s1 = set()
            for row in range(9):
                if grid[row][j] in s1:
                    return False
                if grid[row][j] != ".":
                    s1.add(grid[row][j])
            return True

        def is_valid_grid(row, col):
            idx = (row // 3, col // 3)
            if grid[row][col] in d1[(i // 3, j // 3)]:
                return False
            if grid[row][col] != ".":
                d1[(i // 3, j // 3)].add(grid[row][col])
            return True

        def is_valid(i, j):

            return is_valid_row(i) and is_valid_col(j) and is_valid_grid(i, j)

        m = len(board)
        n = len(board[0])
        d1 = defaultdict(set)
        grid = board
        for i in range(9):
            for j in range(9):
                if not is_valid(i, j):
                    return False
        return True
