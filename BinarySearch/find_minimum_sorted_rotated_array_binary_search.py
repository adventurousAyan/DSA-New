from typing import List

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    def findMin(self, nums: List[int]) -> int:

        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = start + (end - start) // 2

            if start == mid and end == mid:
                return nums[mid]

            if start == mid:
                if nums[mid] < nums[mid + 1]:
                    return nums[mid]
                else:
                    return nums[mid + 1]

            if (
                mid - 1 >= start
                and mid + 1 <= end
                and nums[mid] < nums[mid - 1]
                and nums[mid] < nums[mid + 1]
            ):
                return nums[mid]

            else:
                if nums[mid] > nums[end]:
                    start = mid + 1
                elif nums[start] > nums[mid]:
                    end = mid - 1
                else:
                    end = mid - 1
