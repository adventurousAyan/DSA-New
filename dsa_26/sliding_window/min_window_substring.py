class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l, r, n = 0,0, len(s)

        if not t:
            return ""
        if n < len(t):
            return ""

        d1 = {}
        for ch in t:
            d1[ch] = d1.get(ch, 0) + 1
        need = len(d1.keys())
        
        d2 = {}
        mini = float('inf')
        s1 = ""
        have = 0
        while r < n:

            d2[s[r]] = d2.get(s[r], 0) + 1
            
            if s[r] in d1.keys() and d2.get(s[r]) == d1.get(s[r]):
                have+=1       
            if have == need:
                while have == need:
                    if r-l+1 < mini:
                        mini = r-l+1
                        s1 = s[l:r+1] 
                    d2[s[l]] -= 1
                    if s[l] in d1.keys() and d2.get(s[l]) < d1.get(s[l]):
                        have -=1
                    
                    l+=1   
            r+=1
        return s1
            
        
            


            

        





        