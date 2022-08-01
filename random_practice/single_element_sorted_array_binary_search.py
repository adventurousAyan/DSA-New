from typing import List

# https://leetcode.com/problems/single-element-in-a-sorted-array/


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if start == mid and end == mid:
                return nums[mid]

            if (
                mid - 1 >= start
                and mid + 1 <= end
                and nums[mid] != nums[mid - 1]
                and nums[mid] != nums[mid + 1]
            ):
                return nums[mid]
            else:
                if nums[mid] == nums[mid - 1]:
                    ln = mid - start + 1
                    if ln % 2 == 0:
                        start = mid + 1
                    else:
                        end = mid
                elif nums[mid] == nums[mid + 1]:
                    ln = end - mid + 1
                    if ln % 2 == 0:
                        end = mid - 1
                    else:
                        start = mid
