from collections import defaultdict
from typing import List

# https://leetcode.com/problems/course-schedule-ii/


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        d1 = defaultdict(list)

        for val in prerequisites:
            d1[val[1]].append(val[0])

        visited = [-1] * numCourses
        dfsvisited = [-1] * numCourses
        ls = []

        def dfs(i):

            visited[i] = 1
            dfsvisited[i] = 1
            neighbrs = d1[i]

            for n in neighbrs:
                if visited[n] == -1:
                    if not dfs(n):
                        return False
                # It means that there is a cycle in the directed path
                elif dfsvisited[n] == 1:
                    return False
            # Here we are resetting the dfsvisited value as we are backtraking from the path
            # and unable to find a cycle
            dfsvisited[i] = -1
            # Append to stack here
            ls.append(i)
            return True

        for i in range(numCourses):
            if visited[i] == -1:
                if not dfs(i):
                    return []
        return ls[::-1]
