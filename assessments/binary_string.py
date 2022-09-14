# Given a binary string s and a positive integer n, return true if the binary representation of all the integers in the range [1, n] are substrings of s, or false otherwise.

# A substring is a contiguous sequence of characters within a string.
# Input: s = "0110", n = 3
# Output: true


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        def binary(n):
            # if n == 1:
            #     return "01"
            res = ""
            while n != 1:
                res += str(n % 2)
                n = n // 2
            return "1" + res[::-1]

        for i in range(1, n + 1):
            bnry = binary(i)
            if bnry not in s:
                return False
        return True
