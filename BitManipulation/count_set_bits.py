class Solution:
    # https://practice.geeksforgeeks.org/problems/set-bits0143/1
    def setBits(self, N):
        # code here
        cnt = 0
        for i in range(32):
            mask = 1 << i
            if mask & N != 0:
                cnt += 1
        return cnt
