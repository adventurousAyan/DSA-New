class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d1 = {}

        n = len(s)

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        l, r = 0, 1
        maxi = 0

        d1[s[l]] = 1
        while l < r and r < n:
            
            d1[s[r]] = d1.get(s[r], 0) + 1
            # Loop until the duplicate character is removed from the dictionary. For eg: "pwwkew", once it detects a duplicate
            # it will first remove p but still w is in the dictionary and there are duplicate although we slide the left pointer. 
            # Hence we have to keep sliding until the duplicate is removed.
            while d1[s[r]] > 1:
                d1[s[l]] -= 1
                l += 1
            maxi = max(maxi, r - l + 1)    
            r += 1
        return maxi
            


            
            
            

            

        