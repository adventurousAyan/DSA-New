class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        l,r, n =  0,0 , len(fruits)

        d1 = {}

        maxi = 1
        have = 0
        need = 2

        while r < n:

            d1[fruits[r]] = d1.get(fruits[r], 0) + 1
            if d1[fruits[r]] == 1:
                have +=1
            if have <= need:
                maxi = max(maxi, r-l+1)
            elif have > need:
                d1[fruits[l]] -=1
                if d1[fruits[l]] == 0:
                    have -=1
                l+=1
            r+=1
        return maxi

# Approach 2:

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        l,r, n =  0,0 , len(fruits)

        d1 = {}

        maxi = 1
        have = 0
        need = 2



        while r < n:

            d1[fruits[r]] = d1.get(fruits[r], 0) + 1
            if d1[fruits[r]] == 1:
                have +=1
            if have <= need:
                maxi = max(maxi, r-l+1)
            elif have > need:
                while have > need:
                    d1[fruits[l]] -=1
                    if d1[fruits[l]] == 0:
                        have -=1
                    l+=1
            r+=1
        return maxi

        