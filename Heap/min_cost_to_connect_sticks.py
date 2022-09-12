import heapq
from typing import List

# https://leetcode.com/problems/minimum-cost-to-connect-sticks/


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        minq = []

        for stk in sticks:
            heapq.heappush(minq, stk)

        su = 0
        while len(minq) > 1:
            item1 = heapq.heappop(minq)
            item2 = heapq.heappop(minq)
            val = item1 + item2
            su += val
            heapq.heappush(minq, val)
        return su
