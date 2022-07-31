from typing import List

# https://leetcode.com/problems/subarray-sums-divisible-by-k/


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        n = len(nums)

        d1 = {}

        d1[0] = 1

        su = 0
        cnt = 0
        for i in range(n):
            su += nums[i]
            rem = su % k
            if rem < 0:
                rem += k
            if rem in d1:
                cnt += d1.get(rem)
            d1[rem] = d1.get(rem, 0) + 1

        return cnt
