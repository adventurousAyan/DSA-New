from typing import List

# https://leetcode.com/problems/3sum-closest/

# Two Pointer approach
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums = sorted(nums)
        n = len(nums)
        mini = float("inf")
        ans = 0
        for i in range(n):
            lp = i + 1
            rp = n - 1
            while lp < rp:
                ss = nums[i] + nums[lp] + nums[rp]
                if ss < target:
                    lp += 1
                else:
                    rp -= 1
                diff = abs(target - ss)
                if diff < mini:
                    mini = diff
                    ans = ss

        return ans

    # TC: O(n2) and SC:O(1)
