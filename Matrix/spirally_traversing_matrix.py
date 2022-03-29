class Solution:

    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix, r, c):
        # code here

        top = 0
        down = r - 1
        left = 0
        right = c - 1
        ls = []
        visited = [[0] * c for i in range(r)]

        while top < r and down >= 0 and left < c and right >= 0:

            for i in range(left, right + 1):
                if visited[top][i] == 0:
                    ls.append(matrix[top][i])
                    visited[top][i] = 1
            top = top + 1

            for i in range(top, down + 1):
                if visited[i][right] == 0:
                    ls.append(matrix[i][right])
                    visited[i][right] = 1
            right = right - 1

            for i in range(right, left - 1, -1):
                if visited[down][i] == 0:
                    ls.append(matrix[down][i])
                    visited[down][i] = 1
            down = down - 1

            for i in range(down, top - 1, -1):
                if visited[i][left] == 0:
                    ls.append(matrix[i][left])
                    visited[i][left] = 1
            left = left + 1

        return ls
