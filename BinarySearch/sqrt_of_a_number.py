class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 1:
            return 1
        start = 1
        end = x
        ans = 0
        while start <= end:
            mid = start + (end - start) // 2

            if mid * mid > x:
                end = mid - 1
            elif mid * mid <= x:
                ans = mid
                start = mid + 1
            else:
                return mid
        return ans
