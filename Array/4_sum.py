from typing import List

# https://leetcode.com/problems/4sum/


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        nums = sorted(nums)
        quadruplets = []
        for i in range(n):
            for j in range(i + 1, n):
                ss = target - (nums[i] + nums[j])
                lp = j + 1
                rp = n - 1

                while lp < rp:
                    tmp = nums[lp] + nums[rp]

                    if tmp < ss:
                        lp += 1
                    elif tmp > ss:
                        rp -= 1
                    else:
                        my_list = [nums[i], nums[j], nums[lp], nums[rp]]
                        if my_list not in quadruplets:
                            quadruplets.append(my_list)
                        lp += 1
                        rp -= 1

        return quadruplets
