class Solution:

    # https://leetcode.com/problems/binary-subarrays-with-sum/

    # This problem is same to subarray with sum k

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        i, j = 0, 0

        n = len(nums)

        su = 0
        cnt = 0
        d1 = {}
        d1[0] = 1

        for i in range(n):
            su += nums[i]

            val = su - goal
            if val in d1:
                cnt += d1.get(val)
            d1[su] = d1.get(su, 0) + 1
        return cnt
