from queue import PriorityQueue
from typing import List

# https://leetcode.com/problems/sliding-window-maximum/


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        lp = 0

        n = len(nums)

        rp = k - 1
        ls = []

        while lp <= rp and rp < n:
            q = PriorityQueue()
            l = lp
            for i in range(l, l + k):
                # -1 multiplication is done for max heap as PQ in Python is min heap by default
                q.put(-1 * nums[i])
            ls.append(q.get() * -1)
            lp += 1
            rp += 1
        return ls

    ####### Second approach ##############

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        lp = 0

        n = len(nums)

        rp = k - 1
        ls = []

        q1 = collections.deque()
        while lp <= rp and rp < n:
            maxi = float("-inf")
            l = lp
            for i in range(l, l + k):
                maxi = max(maxi, nums[i])
                q1.append(nums[i])
            ls.append(maxi)
            lp += 1
            rp += 1
            q1.popleft()
        return ls
