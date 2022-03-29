def solve(i, j, m, n):
    t = [[-1] * n] * m

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                t[i][j] = 1
            else:

                t[i][j] = t[i - 1][j] + t[i][j - 1]
    print(t)
    return t[m - 1][n - 1]


print(solve(0, 0, 3, 7))
