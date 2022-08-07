from typing import List


class Solution:

    # https://leetcode.com/problems/split-array-largest-sum/

    def splitArray(self, nums: List[int], m: int) -> int:
        def check_feasible(capacity, m):
            su = 0
            no_of_arrays = 0
            for num in nums:
                if num > capacity:
                    return False
                if su + num <= capacity:
                    su += num
                else:
                    no_of_arrays += 1
                    su = num
            no_of_arrays += 1
            return True if no_of_arrays <= m else False

        start = 0
        end = sum(nums)

        while start <= end:

            mid = (start + end) // 2

            if check_feasible(mid, m):
                end = mid - 1
            else:
                start = mid + 1

        return start
