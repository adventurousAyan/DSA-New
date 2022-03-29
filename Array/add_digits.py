# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
# https://leetcode.com/problems/add-digits/


class Solution:
    def addDigits(self, num: int) -> int:
        val = str(num)
        if len(val) == 1:
            return val
        else:
            sum = 0
            for a in val:
                sum += int(a)
            return self.addDigits(sum)
