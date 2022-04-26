class Solution:

    # https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1#
    # Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here
        c = 0
        for i in range(0, n):
            if M[c][i] == 1:
                c = i
        for i in range(n):
            if i != c and (M[c][i] == 1 or M[i][c] == 0):
                return -1
        return c
