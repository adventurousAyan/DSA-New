from typing import List

# https://leetcode.com/problems/course-schedule-ii/submissions/


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        d1 = {}
        for i in range(len(prerequisites)):
            d1[prerequisites[i][1]] = d1.get(prerequisites[i][1], []) + [
                prerequisites[i][0]
            ]
        if len(d1.keys()) == 0:
            return [x for x in range(numCourses)]
        res = self.detect_cycle(numCourses, d1)
        if res:
            return []
        else:
            visited = [False] * numCourses
            my_stack = []
            for i in range(numCourses):
                if not visited[i]:
                    ls = self.topo_sort(i, d1, visited, my_stack)
            result = [-1] * len(ls)
            for i in range(len(ls)):
                result[i] = ls.pop()
            return result

    def detect_cycle(self, n, d1):
        visited = [0] * n
        dfsVisited = [0] * n

        for i in range(n):
            if visited[i] == 0:
                res = self.dfs(i, visited, dfsVisited, d1)
                if res:
                    break
        return res

    def dfs(self, i, visited, dfsVisited, d1):
        if visited[i] == 1 and dfsVisited[i] == 1:
            return True
        else:
            if visited[i] == 0:
                visited[i] = 1
                dfsVisited[i] = 1
                neighbors = d1.get(i, [])
                for neighbor in neighbors:
                    if self.dfs(neighbor, visited, dfsVisited, d1):
                        return True
                dfsVisited[i] = 0

    def topo_sort(self, source, d1, visited, my_stack):
        if not visited[source]:
            visited[source] = True
            neighbors = d1.get(source, [])
            for neighbor in neighbors:
                self.topo_sort(neighbor, d1, visited, my_stack)
            my_stack.append(source)
        return my_stack
