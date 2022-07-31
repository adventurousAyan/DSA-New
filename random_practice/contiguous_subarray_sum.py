from typing import List

# https://leetcode.com/problems/continuous-subarray-sum/
# https://www.youtube.com/watch?v=QM0klnvTQzk


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        n = len(nums)

        d1 = {}

        d1[0] = -1

        su = 0
        for i in range(n):
            su += nums[i]
            rem = su % k
            if rem not in d1:
                d1[rem] = i
            else:
                if i - d1[rem] >= 2:
                    return True

        return False
