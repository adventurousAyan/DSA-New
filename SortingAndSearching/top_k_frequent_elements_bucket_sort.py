from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d1 = defaultdict(int)
        ls = [[] for _ in range(len(nums) + 1)]

        for val in nums:
            d1[val] += 1

        for key, value in d1.items():
            ls[value].append(key)

        ans = []
        for i in range(len(ls) - 1, -1, -1):
            if len(ls[i]) > 0:
                while k > 0 and len(ls[i]) > 0:
                    ans.append(ls[i].pop())
                    k -= 1
        return ans


# TC: 0(n), SC: 0(n)
