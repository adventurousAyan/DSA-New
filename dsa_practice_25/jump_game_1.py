class Solution:
    # Greedy approach can be solved in O(1)
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        end = n - 1

        for i in range(n-1, -1, -1):
            if i + nums[i] >= end:
                end = i
        return True if end == 0 else False