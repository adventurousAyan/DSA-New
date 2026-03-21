class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])
        mins = 0

        grid1 = grid.copy()

        vis = [[-1]*n for _ in range(m)]
        queue = deque()
        

        for i in range(m):
            for j in range(n):
                if i >= 0 and i < m and j >= 0 and j < n and grid1[i][j] == 2 and vis[i][j] == -1:
                    queue.append((i, j, mins))

        while len(queue) > 0:
            row, col, mins = queue.popleft()
            vis[row][col] = 1
            row_dirs = [1, 0 , -1, 0]
            col_dirs = [0, 1, 0, -1]
            for idx in range(4):
                nrow, ncol = row + row_dirs[idx], col + col_dirs[idx]
                if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and grid1[nrow][ncol] == 1 and vis[nrow][ncol] == -1:
                    queue.append((nrow, ncol, mins + 1))
                    grid1[nrow][ncol] = 2
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and grid1[i][j] == 1 and vis[i][j] == -1:
                    return -1
        return mins




        