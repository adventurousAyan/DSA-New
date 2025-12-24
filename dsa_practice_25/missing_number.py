class Solution:
    def missingNumber(self, nums: List[int]) -> int:

      # https://leetcode.com/problems/missing-number/
      # Intuition is first I will loop through original nums and do xor
      # Next I will loop through all the indexes in [0, n] and do xor
      # Here after two operatations, the duplicate elements will cancel each other and the missing 
      # element will remain only

        n1 = len(nums)
        res = 0
        for num in nums:
            res ^= num
        for i in range(n1+1):
            res ^=i
        return res
