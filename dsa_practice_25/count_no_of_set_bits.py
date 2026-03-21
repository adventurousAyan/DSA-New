class Solution:
    def hammingWeight(self, n: int) -> int:
       # https://leetcode.com/problems/number-of-1-bits/?envType=problem-list-v2&envId=bit-manipulation

        cnt = 0
        for i in range(32):
            if n & (1 << i) > 0:
                cnt +=1
        return cnt
