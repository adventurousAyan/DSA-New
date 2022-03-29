import numpy as np


def knapSack(self, W, wt, val, n):

    # code here
    N = n
    t = np.zeros((N + 1, W + 1), dtype=int)
    for i in range(0, N + 1):
        for j in range(0, W + 1):

            if i == 0 or j == 0:
                t[i][j] = 0

            else:
                if wt[i - 1] <= j:
                    t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])
                else:
                    t[i][j] = t[i - 1][j]

    return t[N][W]
