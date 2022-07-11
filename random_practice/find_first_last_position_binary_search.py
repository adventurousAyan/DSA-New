from typing import List

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        lb = self.binarySearch(nums, target, True)
        rb = self.binarySearch(nums, target, False)

        return [lb, rb]

    def binarySearch(self, nums, target, flag):

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                if flag:
                    end = mid - 1
                else:
                    start = mid + 1
        val = start if flag else end
        if val < len(nums) and len(nums) > 0 and nums[val] == target:
            return val
        else:
            return -1
