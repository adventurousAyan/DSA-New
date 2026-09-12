class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        

        def can_finish(mid, piles, limit):
            h = 0
            if mid == 0:
                return False
            for pile in piles:
                if pile < mid:
                    h+=1
                elif pile % mid == 0:
                    h+= pile // mid
                else:
                    h+= (pile // mid) + 1
               

            if h > limit:
                return False
            return True
            
            

        
        lp, rp = 0, sum(piles)
        ans = 0
        while lp<=rp:
            mid = lp + (rp - lp) // 2

            if can_finish(mid, piles, h):
                ans = mid
                rp = mid - 1    
            else:
                lp = mid + 1

        return ans


