class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0]*numCourses
        queue = deque()
        graph = defaultdict(list)

        for dest, src in prerequisites:
            indegree[dest] +=1
            graph[src].append(dest)

        for idx in range(len(indegree)):
            if indegree[idx] == 0:
                queue.append(idx)

        ls = []

        processed = 0

        while len(queue) > 0:
            item = queue.popleft()
            processed += 1
            ls.append(item)
            if graph.get(item):
                for nei in graph.get(item):
                    indegree[nei] -=1
                    if indegree[nei] == 0:
                        queue.append(nei)
        if numCourses != processed:
            return []
        return ls
        