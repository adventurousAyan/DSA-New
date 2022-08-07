from typing import List

# https://leetcode.com/problems/surrounded-regions/


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n

        def dfs(i, j, is_boundary):

            if board[i][j] == "X":
                return 1
            if visited[i][j][0] == 1 and board[i][j] == "O":
                return visited[i][j][1]
            if is_boundary:
                visited[i][j] = (1, 0)
            else:
                visited[i][j] = (1, 1)

            # Up
            up, down, left, right = 0, 0, 0, 0
            if is_valid(i - 1, j):
                up = dfs(i - 1, j, is_boundary)

            # Down
            if is_valid(i + 1, j):
                down = dfs(i + 1, j, is_boundary)

            # Left
            if is_valid(i, j - 1):
                left = dfs(i, j - 1, is_boundary)

            # Right
            if is_valid(i, j + 1):
                right = dfs(i, j + 1, is_boundary)

            if up + down + left + right == 4 and board[i][j] == "O" and not is_boundary:
                board[i][j] = "X"
                return 1
            return 0

        m = len(board)
        n = len(board[0])

        visited = [[(-1, -1)] * n for _ in range(m)]
        # Traverse and mark the boundary elements first
        for i in [0, m - 1]:
            for j in range(n):
                dfs(i, j, True)

        for i in range(m):
            for j in [0, n - 1]:
                dfs(i, j, True)

        # Traverse rest of the elements

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                dfs(i, j, False)

        return board
