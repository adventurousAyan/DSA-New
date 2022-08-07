class Solution:
    # https://leetcode.com/problems/max-consecutive-ones/

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        n = len(nums)

        i, j = 0, 0

        maxi = float("-inf")
        cnt = 0
        while j < n:

            if nums[j] == 1:
                cnt += 1

            if nums[j] == 0:
                maxi = max(cnt, maxi)
                cnt = 0
            j += 1
        maxi = max(maxi, cnt)
        return maxi
