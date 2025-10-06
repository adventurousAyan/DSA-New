class Solution:
    # https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        s = 0
        max_sum = -1000000
        i, j = 0, 0
        d = {}

        while i <= j and j < len(nums):
            s += nums[j]
            d[nums[j]] = d.get(nums[j], 0) + 1
            if j-i+1 == k:
                if len(d) == k:
                    max_sum = max(s, max_sum)
                s-= nums[i]
                d[nums[i]] = d.get(nums[i], 0) - 1
                if d[nums[i]] == 0:
                    d.pop(nums[i])
                i+=1
            j+=1
        return max_sum if max_sum != -1000000 else 0