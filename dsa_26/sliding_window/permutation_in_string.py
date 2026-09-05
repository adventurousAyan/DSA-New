class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        d1 = {}
        k = len(s1)
        j = 0
        
        for s in s1:
            d1[s] = d1.get(s, 0) + 1

        l, r, n = 0, 0, len(s2)
        

        while r < n:
            if r-l+1 < k:
                r+=1
            else:
                s3 = s2[l:r+1]
                cnt = 0
                d2 = {}
                for t in s3:
                    d2[t] = d2.get(t, 0) + 1
                   
                if d1 == d2:
                    return True

                l+=1
            
        return False

            


            


        