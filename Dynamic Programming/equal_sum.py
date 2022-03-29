# User function Template for Python3
import numpy as np


class Solution:
    def equalPartition(self, N, arr):
        # code here
        sum = 0
        for a in arr:
            sum += a
        if sum % 2 != 0:
            return 0
        else:
            return self.subsetSum(N, arr, int(sum / 2))

    def subsetSum(self, N, wt, W):
        t = np.zeros((N + 1, W + 1), dtype=int)
        for i in range(0, N + 1):
            for j in range(0, W + 1):
                if i == 0:
                    t[i][j] = 0
                elif j == 0:
                    t[i][j] = 1
                else:
                    if wt[i - 1] <= j:
                        t[i][j] = t[i - 1][j - wt[i - 1]] or t[i - 1][j]
                    else:
                        t[i][j] = t[i - 1][j]
        return t[N][W]
