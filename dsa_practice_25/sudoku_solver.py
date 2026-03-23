class Solution:
    # https://leetcode.com/problems/sudoku-solver/
    # Intuition - https://www.youtube.com/watch?v=FWAIf_EVUKE
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_safe(board, row, col,  c):
            val = str(c)
            for i in range(9):
                if board[i][col] == val:
                    return False
                if board[row][i] == val:
                    return False
                if board[3*(row // 3) + i // 3][3* (col // 3)+ i%3] == val:
                    return False
            return True
        
        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for c in range(1,10):
                            if is_safe(board, row, col,  c):
                                board[row][col] = str(c)
                                if solve(board):
                                    return True
                                
                                board[row][col] = "."
                        return False
            return True

        solve(board) 
        return board