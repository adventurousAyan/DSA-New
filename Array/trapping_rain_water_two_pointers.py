from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        lp = 0
        rp = len(height) - 1
        leftmax = 0
        rightmax = 0
        ans = 0

        while lp <= rp:
            if height[lp] <= height[rp]:
                if height[lp] >= leftmax:
                    leftmax = height[lp]
                else:
                    ans += leftmax - height[lp]
                lp += 1
            else:
                if height[rp] >= rightmax:
                    rightmax = height[rp]
                else:
                    ans += rightmax - height[rp]
                rp -= 1

        return ans

    # TC: O(N), SC: O(1)
