 # https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}
        for idx, num in enumerate(nums):
            if target - num in d1:
                return [d1[target-num], idx]
            else:
                d1[num] = idx