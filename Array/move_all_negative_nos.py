class Solution:
    def __init__(self):
        pass

    def solve(self, arr):

        lp = 0
        rp = len(arr) - 1

        while lp <= rp:
            if arr[lp] < 0 and arr[rp] < 0:
                lp = lp + 1
            elif arr[lp] > 0 and arr[rp] < 0:
                arr[lp], arr[rp] = arr[rp], arr[lp]
                rp = rp - 1
            elif arr[lp] < 0 and arr[rp] > 0:
                lp = lp + 1
                rp = rp - 1
            else:
                lp = lp + 1
                rp = rp - 1
        return arr


s = Solution()
print(s.solve([-12, 11, -13, -5, 6, -7, 5, -3, -6]))

print(s.solve([5, 4, -3, -2, 6, -7, 8, -9]))
