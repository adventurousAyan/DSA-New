from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        return self.solve(nums, 0, len(nums) - 1)

    def solve(self, nums, start, end):

        if start <= end:

            mid = start + (end - start) // 2

            if start == mid and end == mid:
                return mid
            if start == mid and nums[mid] > nums[end]:
                return mid

            if (
                mid - 1 >= start
                and mid + 1 <= end
                and nums[mid] > nums[mid - 1]
                and nums[mid] > nums[mid + 1]
            ):
                return mid
            else:
                if nums[mid] < nums[mid + 1]:
                    return self.solve(nums, mid + 1, end)
                else:
                    return self.solve(nums, start, mid - 1)
