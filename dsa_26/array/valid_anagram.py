class Solution:
    # Check if two strings are anagrams of each other
    # https://leetcode.com/problems/valid-anagram/
    def isAnagram(self, s: str, t: str) -> bool:

        d1 = {}

        for c in s:
            d1[c] = d1.get(c, 0) + 1
        
        for c in t:
            if c not in d1.keys():
                return False
            d1[c] -= 1
            if d1[c] == 0:
                d1.pop(c)

        return len(d1.keys()) == 0
    
# Hint - Check for early exit as well , if length differs, just return False immediately