from typing import List

# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

# https://www.youtube.com/watch?v=dD7N6l9z03o

# Follow this youtube video for more intuition


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        n = len(nums)

        pos = [0] * n
        neg = [0] * n

        if nums[0] > 0:
            pos[0] = 1
        if nums[0] < 0:
            neg[0] = 1

        ans = pos[0]

        for i in range(1, n):
            if nums[i] > 0:
                pos[i] = pos[i - 1] + 1
                if neg[i - 1] > 0:
                    neg[i] = neg[i - 1] + 1
            elif nums[i] < 0:
                if neg[i - 1] > 0:
                    pos[i] = neg[i - 1] + 1
                neg[i] = pos[i - 1] + 1

            ans = max(ans, pos[i])

        return ans
