from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 0
        rp = 1
        max_pf = float("-inf")
        while lp < rp and rp < len(prices):
            pf = prices[rp] - prices[lp]
            if pf > max_pf:
                max_pf = pf
            if prices[lp] > prices[rp]:
                lp = rp
                rp += 1
            else:
                rp += 1

        return 0 if max_pf < 0 else max_pf
