from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ls = []
        pf = 1
        pof = 1
        n = len(nums)
        for index in range(n):
            ls.append(pf)
            pf = nums[index] * pf

        for index in range(n - 1, -1, -1):
            ls[index] = pof * ls[index]
            pof = pof * nums[index]
        return ls
