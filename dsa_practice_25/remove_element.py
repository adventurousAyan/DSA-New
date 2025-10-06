# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        for idx, num in enumerate(nums):
            if num == val:
                nums[idx] = 100
            else:
                k+=1
        nums.sort()    
        return k
    

# Optimized solution without sorting
# Intuition here for implace array operations
# https://www.youtube.com/watch?v=zENCNXbFH8A

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for idx, num in enumerate(nums):
            if num != val:
                nums[k] = num
                k+=1   
        return k
        