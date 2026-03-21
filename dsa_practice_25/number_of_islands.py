class Solution:
    # https://leetcode.com/problems/number-of-islands/
    def numIslands(self, grid: List[List[str]]) -> int:



        def dfs(rw, col, grid, m, n , vis):

            
            vis[rw][col] = 1
            row_dirs = [-1,0,1,0]
            col_dirs = [0,-1,0,1]
            for idx in range(4):
                nrow, ncol = rw + row_dirs[idx], col + col_dirs[idx]
                if nrow >= 0 and nrow < m and ncol >=0 and ncol < n and grid[nrow][ncol] == "1" and vis[nrow][ncol] == -1:
                    dfs(nrow, ncol, grid, m ,n, vis)
                

        m, n = len(grid), len(grid[0])

        vis = [[-1]*n for _ in range(m)]

        self.num_islands = 0

        for rw in range(m):
            for col in range(n):
                if rw >=0 and rw < m and col >=0 and col < n and grid[rw][col] == "1" and vis[rw][col] == -1:
                    dfs(rw, col, grid, m, n, vis)
                    self.num_islands +=1
        



        return self.num_islands


        