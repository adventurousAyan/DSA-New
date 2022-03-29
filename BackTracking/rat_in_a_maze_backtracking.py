class Solution:
    def findPath(self, m, n):
        # code here
        arr = m
        visited = [[0] * (n) for i in range(n)]
        return self.solve(0, 0, n, arr, visited, [], [])

    def solve(self, x, y, n, arr, visited, l1, ls):
        if arr[0][0] == 0:
            return []
        if x == n - 1 and y == n - 1:
            ls.append("".join(l1))
        else:
            visited[x][y] = 1
            # Down
            if self.isSafe(x + 1, y, n, arr, visited):
                l1.append("D")
                self.solve(x + 1, y, n, arr, visited, l1, ls)
                l1.pop()
            # Up
            if self.isSafe(x - 1, y, n, arr, visited):
                l1.append("U")
                self.solve(x - 1, y, n, arr, visited, l1, ls)
                l1.pop()
            # Left
            if self.isSafe(x, y - 1, n, arr, visited):
                l1.append("L")
                self.solve(x, y - 1, n, arr, visited, l1, ls)
                l1.pop()
            # Right
            if self.isSafe(x, y + 1, n, arr, visited):
                l1.append("R")
                self.solve(x, y + 1, n, arr, visited, l1, ls)
                l1.pop()

            visited[x][y] = 0
        return ls

    def isSafe(self, x, y, n, arr, visited):

        if (
            x >= 0
            and x < n
            and y >= 0
            and y < n
            and arr[x][y] == 1
            and visited[x][y] == 0
        ):
            return True
        else:
            return False
