class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
      # https://leetcode.com/problems/hamming-distance/?envType=problem-list-v2&envId=bit-manipulation
      # Intuition is for diff bits, it will return 1 if we only do a XOR and then we just have to count the no of set bits
        z = x ^ y

        cnt = 0
        for i in range(32):
            if z & (1 << i) > 0:
                cnt +=1
        return cnt
