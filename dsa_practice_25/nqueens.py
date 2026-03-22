class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        
        def will_collide(matrix, i, j):
            
            nrow, ncol = i, j
            
            while nrow < n:
                if matrix[nrow][ncol] == "Q":
                    return True
                nrow += 1

            nrow, ncol = i, j

            while nrow >= 0:
                if matrix[nrow][ncol] == "Q":
                    return True
                nrow -=1

            nrow, ncol = i, j

            while ncol < n:
                if matrix[nrow][ncol] == "Q":
                    return True
                ncol +=1
            nrow, ncol = i, j
            while ncol >= 0:
                if matrix[nrow][ncol] == "Q":
                    return True
                ncol -=1
            nrow, ncol = i, j
            while nrow < n and ncol >= 0:
                if matrix[nrow][ncol] == "Q":
                    return True
                nrow +=1
                ncol -=1
            
            nrow, ncol = i, j
            while nrow >= 0 and ncol < n:
                if matrix[nrow][ncol] == "Q":
                    return True
                nrow -=1
                ncol +=1
            
            nrow, ncol = i, j
            while nrow >= 0 and ncol >= 0:
                if matrix[nrow][ncol] == "Q":
                    return True
                nrow -=1
                ncol -=1

            nrow, ncol = i, j
            while nrow < n and ncol < n:
                if matrix[nrow][ncol] == "Q":
                    return True
                nrow +=1
                ncol +=1

            return False
        
        def nqueen(matrix, j, n):
            if j == n:
                self.res.append(["".join(row) for row in matrix])
                return
            for i in range(n):
                if not will_collide(matrix, i, j):
                    matrix[i][j] = "Q"
                    nqueen(matrix, j+1, n)
                    matrix[i][j] = "."

        
        self.res = []
        matrix1 = [["."]*n for _ in range(n)]
        nqueen(matrix1, 0, n)
        return self.res





            


            

