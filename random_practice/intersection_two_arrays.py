from typing import List


class Solution:
    # https://leetcode.com/problems/intersection-of-two-arrays/
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        d1 = {}
        ls = []
        for val in nums1:
            d1[val] = d1.get(val, 0) + 1

        for val in nums2:
            if val in d1 and val not in ls:
                ls.append(val)

        return ls
