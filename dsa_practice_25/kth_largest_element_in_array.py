
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxq = []

        for num in nums:
            heapq.heappush(maxq, -num)

        while k != 0:
            res = -heapq.heappop(maxq)
            k -=1
        return res