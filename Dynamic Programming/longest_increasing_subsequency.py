# User function Template for python3


class Solution:

    # Function to find length of longest increasing subsequence.
    def longestSubsequence(self, a, n):
        # code here
        lis = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if a[i] < a[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
        return max(lis)
