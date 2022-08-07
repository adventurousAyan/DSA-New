from typing import List

# https://leetcode.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1
        arr = nums

        while start <= end:
            mid = start + (end - start) // 2

            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return start
