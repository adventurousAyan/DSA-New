from queue import PriorityQueue
from typing import List

# https://leetcode.com/problems/gas-station/


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)
        q = PriorityQueue()
        for i in range(n):
            q.put((cost[i], (gas[i], i)))

        out = -1

        # PQ Implementation:-

        while not q.empty():
            cost1, gasDels = q.get()
            tank = gasDels[0]
            idx = gasDels[1]
            for j in range(idx + 1, 2 * n - idx + 2):
                cirIdx = j % n
                if tank >= cost1:
                    tank += gas[cirIdx] - cost1
                    cost1 = cost[cirIdx]
                else:
                    break
            if idx == cirIdx and tank >= cost1:
                out = idx
                break

        return out
