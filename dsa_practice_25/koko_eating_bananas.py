class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
            def can_eat_bananas(k):
                if k == 0: # Edge case where speed can be 0
                    return False 
                hrs = 0
                for pile in piles:
                    if pile % k == 0: # If truly divisible, we can calculate the hr
                        hrs += pile // k
                    else:
                        hrs += pile // k + 1 #Else it means, based on the spped k, koko cannot finish in pile // k hr
                if hrs > h:
                    return False
                
                

                return True

           # Identify the search space

            low, high = 0, max(piles) # Max koko can eat at a time
            ans = float('inf')

            while low <= high:
                mid = low + (high - low) // 2
                res = can_eat_bananas(mid)
                if can_eat_bananas(mid):
                    high = mid - 1
                    ans = min(ans, mid)
                else:
                    low = mid + 1

            return ans
                




   
        
