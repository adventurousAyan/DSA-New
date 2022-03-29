from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = float("-inf")
        n = len(height)
        lp = 0
        rp = n - 1

        while lp != rp:
            area = (rp - lp) * min(height[lp], height[rp])
            if area > max_area:
                max_area = area
            if height[lp] <= height[rp]:
                lp += 1
            else:
                rp -= 1
        return max_area
