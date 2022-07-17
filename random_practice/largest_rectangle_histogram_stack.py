from typing import List

# https://leetcode.com/problems/largest-rectangle-in-histogram/


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        dr = n - 1
        dl = -1
        right_smaller = [dr] * n
        left_smaller = [dl] * n
        stack = []

        # Right smaller

        for i in range(n - 1, -1, -1):

            while len(stack) > 0 and heights[i] <= stack[-1][1]:
                stack.pop()
            if len(stack) > 0 and heights[i] > stack[-1][1]:
                right_smaller[i] = stack[-1][0] - 1

            stack.append((i, heights[i]))

        # Left Smaller

        stack = []
        for i in range(n):

            while len(stack) > 0 and heights[i] <= stack[-1][1]:
                stack.pop()
            if len(stack) > 0 and heights[i] > stack[-1][1]:
                left_smaller[i] = stack[-1][0]

            stack.append((i, heights[i]))

        maxi = 0
        for i in range(n):
            maxi = max(abs(right_smaller[i] - left_smaller[i]) * heights[i], maxi)
        return maxi
