class Solution:
    # https://leetcode.com/problems/reverse-bits/submissions/
    def reverseBits(self, n: int) -> int:

        mask = 1
        ans = 0
        for i in range(32):
            mask = 1 << i
            if mask & n != 0:
                ans = 1 << (31 - i) | ans
        return ans
