import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        exp = r'[a-zA-Z0-9]+'
        res = re.findall(exp, s)
        s1 = "".join(res)
      
        l, r = 0, len(s1)-1
        s1 = s1.lower()
        while l <= r:
            if s1[l] == s1[r]:
                l+=1
                r-=1
            else:
                return False
        return True