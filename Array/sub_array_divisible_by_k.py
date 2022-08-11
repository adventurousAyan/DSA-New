from typing import List

# https://leetcode.com/problems/subarray-sums-divisible-by-k/


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        # If one subarray[0:i]  when dividing by k gives remainder x and the other subarray[0:j] when divided by k yields the same remainder,
        # then subarray [i:j] would be divisible by k
        # Ex:- [0:i] = km + x,  [0:j] = k*n + x, therefore [i:j] = k(m-n) which is multiple of k.
        # This concept would be used in the problem

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
