# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        else:
            cleaned_txt = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
            l, r = 0, len(cleaned_txt)-1

            while l < r:
                if cleaned_txt[l] == cleaned_txt[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
