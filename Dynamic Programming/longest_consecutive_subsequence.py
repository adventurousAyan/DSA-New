class Solution:

    # arr[] : the input array
    # N : size of the array arr[]

    # Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self, arr, N):
        # code here

        d = {}

        for val in arr:
            if d.get(val, -1) == -1:
                d[val] = 1
            else:
                d[val] = d[val] + 1
        maxno = 1
        for val in arr:
            if d.get(val - 1, -1) == -1:
                tmp = val + 1
                count = 1
                while not d.get(tmp, -1) == -1:
                    count += 1
                    tmp += 1
                    maxno = max(maxno, count)

        return maxno
