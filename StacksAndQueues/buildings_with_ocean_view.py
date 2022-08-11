from typing import List

# https://leetcode.com/problems/buildings-with-an-ocean-view/


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        stack = []

        ans = []

        n = len(heights)
        stack.append(heights[n - 1])
        ans.append(n - 1)
        for i in range(n - 2, -1, -1):
            if heights[i] > stack[-1]:
                ans.append(i)
                stack.append(heights[i])
        return ans[::-1]

# TC: 0(n), SC: 0(n)
