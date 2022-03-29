class Solution:

    # Function to return a list of indexes denoting the required
    # combinations whose sum is equal to given number.
    def combinationalSum(self, A, B):
        # code here
        ls = []
        arr = sorted(A)
        b = B
        l1 = []
        return self.solve(arr, b, ls, l1, 0)

    def solve(self, arr, b, ls, l1, j):
        if b == 0:
            temp = tuple(l1)
            ls.append(temp)

        elif b < 0:
            return
        else:
            prev = 0
            for i in range(j, len(arr)):
                val = arr[i]
                if prev != val:
                    l1.append(val)
                    b = b - val
                    self.solve(arr, b, ls, l1, i)
                    b = b + val
                    l1.pop()
                prev = val
        return ls
