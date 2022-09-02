from typing import List

# https://leetcode.com/problems/word-search/


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_valid(nr, nc):
            return nr >= 0 and nr < m and nc >= 0 and nc < n and board[nr][nc]

        def dfs(r, c, idx):
            # Check if the word at index idx matches to that of board[r][c]
            if idx < len(word) and board[r][c] != word[idx]:
                return False
            # Base Case
            if idx == len(word) - 1:
                return True
            # Assign a temp variable
            tmp = board[r][c]
            # Mark board[r][c] as None
            board[r][c] = None
            # Formulate the cirections
            directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            # Loop through each of the directions and if any pne path returns True, then return True from function
            # Increment the index
            for nr, nc in directions:
                if is_valid(nr, nc) and dfs(nr, nc, idx + 1):
                    return True
            # Backtrack, set the board value to the previous
            board[r][c] = tmp
            # Returns False if none of the paths are valid
            return False

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
