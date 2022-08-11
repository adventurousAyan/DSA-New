import heapq


class Solution:
    # https://leetcode.com/problems/kth-largest-element-in-an-array/

    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxq = []
        for val in nums:
            heappush(maxq, -val)

        ans = -1
        while k > 0:
            val = -heappop(maxq)
            k -= 1
        return val
