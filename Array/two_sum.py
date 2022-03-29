from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d1 = {}
        for index, a in enumerate(nums):
            val = target - a
            if d1.get(val, -1) == -1:
                d1[a] = index
            else:
                return [d1.get(val), index]


                
