from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d1 = {}
        d1[0] = 1
        sm = 0
        cnt = 0
        for a in nums:
            sm += a
            if d1.get(sm - k):
                cnt = cnt + d1.get(sm - k)
            d1[sm] = d1.get(sm, 0) + 1
        return cnt
