from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        prev = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= prev:
                prev = i
        return True if prev == 0 else False


#         lp = 0
#         rp = len(nums)-1
#         n = len(nums)-1

#         l = 0
#         while lp <= rp and lp >= 0:
#             val = nums[lp]
#             if lp == rp and nums[lp] == nums[rp]:
#                 return True
#             if val == 0:
#                 l += 1
#                 lp = lp - l
#             elif val < rp-lp:
#                 lp = lp + val
#             else:
#                 lp = lp + (rp-lp)
#         return False
