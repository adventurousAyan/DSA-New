from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lp = len(nums) - 2
        rp = len(nums) - 1

        while lp >= 0:
            if nums[lp] >= nums[rp]:
                lp -= 1
                rp -= 1
            else:
                break

        if lp != -1:
            k = len(nums) - 1
            while k >= lp:
                if nums[lp] < nums[k]:
                    nums[lp], nums[k] = nums[k], nums[lp]
                    break
                else:
                    k -= 1

        return self.reverse(nums, lp + 1, len(nums) - 1)

    def reverse(self, nums, lp, rp):

        while lp <= rp:
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp += 1
            rp -= 1
        return nums
