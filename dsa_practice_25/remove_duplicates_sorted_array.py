class Solution:
    # We need to use two pointers and basically a fast and sloe pointer. We have to find the number of unique values encountered, 
    # where it would result in a replace
    # More intuition here - https://www.youtube.com/watch?v=DEJAZBq0FDA
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 1, 1

        while l <= r and r < len(nums):
            if nums[r-1] == nums[r]:
                r+=1
            else:
                nums[l] = nums[r]
                l+=1
                r+=1
        return l