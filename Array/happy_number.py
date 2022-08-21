class Solution:

    # https://leetcode.com/problems/happy-number/

    def isHappy(self, n: int) -> bool:

        # This function takes the sum of squares of digits
        def solve(n, su):
            if n == 0:
                return su

            val = n % 10
            n = n // 10
            su += val * val
            return solve(n, su)

        su = n
        ls = set()
        # If the sum is not 1, add it to a set. If the same some comes, its not a happy number
        while su != 1:
            su = solve(su, 0)
            if su in ls:
                return False
            else:
                ls.add(su)
        return True
