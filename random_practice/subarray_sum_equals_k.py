from typing import List

# https://leetcode.com/problems/subarray-sum-equals-k/
# https://www.youtube.com/watch?v=20v8zSo2v18&t=444s for intuition


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        d1 = {}
        d1[0] = 1

        su = 0
        cnt = 0
        for i in range(n):
            su += nums[i]
            val = (
                su - k
            )  # If lets say [0: i] is a and [0:j] is b and i < j then [i:j] will be a-b. So a-b = k, then we can write this as a-k = b. If b exists in dict then it means,
            # there exist a subarray whose sum is equal to k
            if val in d1:
                cnt += d1.get(val)
            d1[su] = d1.get(su, 0) + 1

        return cnt
