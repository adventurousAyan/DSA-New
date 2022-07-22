from queue import PriorityQueue
from typing import List

# https://leetcode.com/problems/cheapest-flights-within-k-stops/


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:

        ls = [(float("inf"), 0)] * n
        q = PriorityQueue()
        q.put((0, src, 0))
        d1 = {}
        ls[src] = (0, 0)

        for val in flights:
            d1[val[0]] = d1.get(val[0], []) + [(val[1], val[2])]

        while not q.empty():
            wt, val, path = q.get()
            neighbors = d1.get(val, [])

            if val == dst:
                return wt
            if path > k:
                continue

            for neigh in neighbors:
                com_wt = wt + neigh[1]
                stop = 1 + path
                if com_wt < ls[neigh[0]][0] or stop < ls[neigh[0]][1]:
                    ls[neigh[0]] = (com_wt, stop)
                    q.put((com_wt, neigh[0], stop))

        return ls[dst][0] if ls[dst][0] != float("inf") else -1
