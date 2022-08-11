from typing import List

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        lp = 0
        rp = 1

        while lp <= rp and rp < len(nums):
            if nums[lp] == nums[rp]:
                rp = rp + 1
            else:
                lp = lp + 1
                nums[lp] = nums[rp]

        # print(lp)
        return lp + 1
