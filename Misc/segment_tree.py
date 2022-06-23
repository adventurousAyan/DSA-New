class Solution:
    def __init__(self, arr):
        self.seg = [None] * 4 * 20
        self.arr = arr

    def buildSegmentTree(self, ind, low, high):

        if low == high:
            self.seg[ind] = self.arr[low]
            return

        mid = low + (high - low) // 2
        self.buildSegmentTree(2 * ind + 1, low, mid)
        self.buildSegmentTree(2 * ind + 2, mid + 1, high)
        self.seg[ind] = max(self.seg[2 * ind + 1], self.seg[2 * ind + 2])

    def query(self, ind, low, high, l, r):

        if low >= l and high <= r:
            return self.seg[ind]
        if r < low or high < l:
            return float("-inf")
        mid = low + (high - low) // 2
        left = self.query(2 * ind + 1, low, mid, l, r)
        right = self.query(2 * ind + 2, mid + 1, high, l, r)
        return max(left, right)


    def point_update(self, ind, low, high, node,  val):

        if low == high:
            self.seg[ind] += val
        else:
            mid = low + (high - low) // 2
            if node <= mid and node >= low:
                self.point_update(2*ind + 1, low, mid, node, val)
            else:
                self.point_update(2*ind + 2, mid+1, high, node, val)
            self.seg[ind] = max(self.seg[2 * ind + 1], self.seg[2 * ind + 2])



arr = [8, 2, 5, 1, 4, 5, 3, 9, 6, 10]
s = Solution(arr)
n = len(arr)
s.buildSegmentTree(0, 0, n - 1)
print(s.seg)

print(s.query(0, 0, n - 1, 0, 7))


