# User function Template for python3
class Solution:

    # https://practice.geeksforgeeks.org/problems/longest-subarray-with-sum-divisible-by-k1259/1

    def longSubarrWthSumDivByK(self, arr, n, K):
        # Complete the function
        d1 = {}
        d1[0] = -1
        s = 0
        k = K
        maxi = 0
        for i in range(n):
            s += arr[i]
            rem = s % k
            if rem < 0:
                rem += k
            # Store the index as value, so that it will help us when calculating the length
            if rem not in d1:
                d1[rem] = i
            else:
                maxi = max(maxi, i - d1.get(rem))
        return maxi
