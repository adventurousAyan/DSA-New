from collections import deque
from typing import List

# https://leetcode.com/problems/duplicate-zeros/


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        q = deque()
        i = 0
        n = len(arr)
        while i < n:

            if arr[i] == 0:
                lp = i + 1
                q.append(0)
                q.append(0)
                while lp < n:
                    if arr[lp] == 0:
                        q.append(0)
                    q.append(arr[lp])
                    lp += 1

            if len(q) > 0:
                val = q.popleft()
                arr[i] = val
            i += 1
        return arr
