# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        st_dict = {}

        for index, val in enumerate(nums):
            tmp = target - val
            if tmp not in st_dict:
                st_dict[val] = index
            else:
                return [st_dict[tmp], index]

    #SC: O(n) and TC: O(n)
