from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        arr = self.rotateMatrix(matrix, 0, 0, n)
        arr = self.reverseMatrix(arr, n)
        return arr

    def rotateMatrix(self, arr, row, col, n):

        if row == n and col == n:
            return arr
        else:
            for i in range(row, n):
                arr[i][col], arr[col][i] = arr[col][i], arr[i][col]
            return self.rotateMatrix(arr, row + 1, col + 1, n)

    def reverseMatrix(self, arr, n):
        for i in range(n):
            lp = 0
            rp = n - 1
            while lp <= rp:
                arr[i][lp], arr[i][rp] = arr[i][rp], arr[i][lp]
                lp = lp + 1
                rp = rp - 1
        return arr
