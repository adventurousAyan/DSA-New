import collections
from typing import List


class Solution:

    # https://leetcode.com/problems/sliding-window-maximum/

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        i, j = 0, 0

        q = collections.deque()
        ls = []
        while j < n:
            while len(q) > 0 and q[-1] < nums[j]:
                q.pop()
            q.append(nums[j])

            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                val = q[0]
                ls.append(val)
                if nums[i] == q[0]:
                    q.popleft()

                i += 1
                j += 1
        return ls
