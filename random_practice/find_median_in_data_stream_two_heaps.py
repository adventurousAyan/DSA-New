import heapq

from heapq import heappop, heappush

# https://leetcode.com/problems/find-median-from-data-stream/


# This approach is using two heaps. We will take maxheap and minheap both. Firsst we will put items in maxheap. If the next
# item is less, put it in maxheap , else put it in minheap. Now if counts is even, we have to balance the heaps.
# If count is odd, maxheap should always contain the top element, so maxheal items should be greater. Therefore if count is odd
# check, if maxheap contains more elements. If not, pop from minheap and put in maxheap
# Also here we have used heapq as a priority queue implementation instead of PriorityQueue


class MedianFinder:
    def __init__(self):
        self.minq = []
        self.maxq = []
        self.count = 0

    def addNum(self, num: int) -> None:
        if len(self.maxq) == 0:
            heappush(self.maxq, -num)
        else:
            val = -heappop(self.maxq)
            print(val)
            if num > val:
                heappush(self.minq, num)
            else:
                heappush(self.maxq, -num)
            heappush(self.maxq, -val)

        self.count += 1

        if self.count % 2 == 0:
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

    def findMedian(self) -> float:

        if (self.count) % 2 == 0:
            val1 = -heappop(self.maxq)
            val2 = heappop(self.minq)
            heappush(self.maxq, -val1)
            heappush(self.minq, val2)
            return (val1 + val2) / 2
        else:
            val1 = -heappop(self.maxq)
            heappush(self.maxq, -val1)
            return val1


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
