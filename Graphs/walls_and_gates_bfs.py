from collections import deque
from typing import List

# https://leetcode.com/problems/walls-and-gates/


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        m = len(rooms)
        n = len(rooms[0])
        visited = [[-1] * n for _ in range(m)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
                elif rooms[i][j] == -1:
                    visited[i][j] = 1

        def is_valid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n and visited[i][j] != 1

        while len(q) > 0:
            r, c, dis = q.popleft()
            visited[r][c] = 1
            if rooms[r][c] != 0:
                rooms[r][c] = min(dis, rooms[r][c])
            directions = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]
            for dir in directions:
                if is_valid(dir[0], dir[1]):
                    q.append((dir[0], dir[1], dis + 1))
