class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 1:
            return 0

        l, r = 0, 1
        n = len(prices)
        maxi = 0

        while l<=r and r<n:
            # If buy price is greater than sell price, that means there
            # is a lower price in which we can buy, hence we move the left pointer to the right
            if prices[l] > prices [r]:
                l+=1
            else:
                # If the buy price is less than sell price, then 
                # we calculate profit and move the right pointer because 
                # there might be a higher price in the future which we can sell at
                # If the right pointer is exhaused, it means there are no points in the array which is
                # lower than the buy price, so our buy price point is correctly chosen and 
                # the sell price point is the highest price in the array after the buy date, 
                # so we return the max profit    
                profit = prices[r] - prices[l]
                maxi = max(maxi, profit)
                r+=1
        return maxi
            
