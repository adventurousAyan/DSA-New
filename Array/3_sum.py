class Solution:

    # Function to find if there exists a triplet in the
    # array A[] which sums up to X.
    def find3Numbers(self, A, n, X):
        # Your Code Here
        res = False
        d1 = {}
        for a in A:
            if d1.get(a, 0) == 0:
                d1[a] = 1
            else:
                d1[a] = d1[a] + 1
        for index, a in enumerate(A):
            twosum = X - a
            if twosum > 0:
                if not d1.get(a, 0) == 0:
                    d1[a] = 0
                res = self.findTwoNos(A, n, twosum, d1)
                if res:
                    break
        return res

    def findTwoNos(self, A, n, X, d1):
        res = False
        for a in A:
            tmp = X - a
            if tmp in d1.keys() and a != tmp and d1[tmp] != 0:
                res = True
                break
        return res
