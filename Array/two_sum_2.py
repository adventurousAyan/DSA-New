from typing import List

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        lp = 0
        rp = len(numbers) - 1
        ans = []
        while lp <= rp:
            ss = numbers[lp] + numbers[rp]

            if ss < target:
                lp += 1
            elif ss > target:
                rp -= 1
            else:
                break
        return [lp + 1, rp + 1]
