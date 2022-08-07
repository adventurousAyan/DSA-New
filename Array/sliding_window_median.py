import heapq
from heapq import heappush, heappop
from typing import List

# TODO: Needs to be revisited


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        n = len(nums)
        ls = []
        i, j = 0, 0
        self.minq = []
        self.maxq = []
        self.count = 0

        while j < n:

            num = nums[j]
            if len(self.maxq) == 0:
                heappush(self.maxq, -num)
            else:
                val = -heappop(self.maxq)
                if num > val:
                    heappush(self.minq, num)
                else:
                    heappush(self.maxq, -num)
                heappush(self.maxq, -val)

            if (j - i + 1) % 2 == 0:
                if len(self.maxq) < len(self.minq):
                    val1 = heappop(self.minq)
                    heappush(self.maxq, -val1)
                elif len(self.minq) < len(self.maxq):
                    val1 = -heappop(self.maxq)
                    heappush(self.minq, val1)
            else:
                if len(self.minq) > 0 and len(self.minq) > len(self.maxq):
                    val1 = heappop(self.minq)
                    heappush(self.maxq, -val1)

            if j - i + 1 == k:
                num1 = nums[i]
                top = -heappop(self.maxq)
                if k % 2 == 0:
                    topmin = heappop(self.minq)
                    ls.append((top + topmin) / 2)
                    heappush(self.minq, topmin)

                else:
                    ls.append(top)

                if num1 > top:
                    heappop(self.minq)
                    heappush(self.maxq, -top)
                elif num1 < top and len(self.maxq) > 0:
                    heappop(self.maxq)
                    heappush(self.maxq, -top)

                if len(self.maxq) < len(self.minq):
                    val1 = heappop(self.minq)
                    heappush(self.maxq, -val1)
                elif len(self.minq) < len(self.maxq):
                    val1 = -heappop(self.maxq)
                    heappush(self.minq, val1)

                i += 1

            j += 1
        return ls
