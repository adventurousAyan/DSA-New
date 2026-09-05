class Solution:
    # https://leetcode.com/problems/contains-duplicate/
    def containsDuplicate(self, nums: List[int]) -> bool:

        d1 = {}
        for num in nums:
            d1[num] = d1.get(num, 0) + 1
            if d1[num] == 2:
                return True
        return False
    

# Hint - Could also use a set to check for duplicates, if length of set is less than length of list, then return True
            