class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0]*numCourses
        queue = deque()
        graph = defaultdict(list)

        for dep in prerequisites:
            indegree[dep[0]] +=1
            graph[dep[1]].append(dep[0])

        for idx in range(len(indegree)):
            if indegree[idx] == 0:
                queue.append(idx)
        vis = [-1]*numCourses

        while len(queue) > 0:
            item = queue.popleft()
            vis[item] = 1

            if graph.get(item):
                for nei in graph.get(item):
                    if vis[nei]== -1:
                        indegree[nei] -=1
                        if indegree[nei] == 0:
                            queue.append(nei)

        for v in vis:
            if v == -1:
                return False

        return True


        









        