class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)

        rows = defaultdict(set) 
        cols = defaultdict(set)
        box = defaultdict(set)
        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in box[(i//3, j//3)]:
                        return False
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    box[(i//3, j//3)].add(board[i][j])
        return True

    #Hint - Use a set to check if the number is already in the row, column, or box
    # For box, use a tuple of the row and column divided by 3 to get the box number