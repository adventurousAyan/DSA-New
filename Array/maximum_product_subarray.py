from typing import List

# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxi, mini = nums[0], nums[0]
        ans = max(nums)
        for i in range(1, len(nums)):
            
            if nums[i] < 0:
                maxi, mini = mini, maxi
            
            maxi = max(maxi*nums[i], nums[i])
            mini = min(mini*nums[i], nums[i])
            ans = max(ans, maxi)
            
        return ans