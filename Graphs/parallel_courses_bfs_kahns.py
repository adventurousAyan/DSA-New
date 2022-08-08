from collections import defaultdict, deque
from typing import List

# https://leetcode.com/problems/parallel-courses/


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        indegree = [0] * n

        d1 = defaultdict(list)

        for edge in relations:
            d1[edge[0]].append(edge[1])
            indegree[edge[1] - 1] += 1

        q = deque()

        semes = -1
        for i in range(n):
            if indegree[i] == 0:
                q.append((i + 1, 1))

        while len(q) > 0:
            node, semes = q.popleft()
            for nei in d1[node]:
                indegree[nei - 1] -= 1
                if indegree[nei - 1] == 0:
                    q.append((nei, semes + 1))

        return semes if semes != 1 else -1
