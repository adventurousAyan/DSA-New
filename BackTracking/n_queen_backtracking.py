from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        t = [["."] * n for i in range(n)]
        self.ls = []
        return self.solve(t, 0, n)
       
        
            
    
    def solve(self, t, i, n):
        if n == i:
            print(t)
            return t
        else:
            for j in range(n):
                res = self.isValid(t, i, j)
                if res:
                    t[i][j] = 'Q'
                    self.solve(t, i+1, n)
                    t[i][j] = "."
        
    def isValid(self, t, i, j):
            k = i-1 
            while k >= 0:
                if t[k][j] == 'Q':
                    return False
                k = k - 1
            m = j + 1 
            k = i-1 
            while k >= 0 and m < len(t[0]):
                if t[k][m] == 'Q':
                    return False
                k = k - 1
                m = m + 1
            m = j-1  
            k = i-1 
            while k >= 0 and m >= 0:
                if t[k][m] == 'Q':
                    return False
                k = k-1
                m = m-1
            return True