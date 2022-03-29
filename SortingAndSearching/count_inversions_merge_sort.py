class Solution:
    # User function Template for python3

    # arr[]: Input Array
    # N : Size of the Array arr[]
    # Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        start = 0
        end = len(arr) - 1
        self.inversionCount = 0
        res = self.merge_sort(start, end, arr)
        return self.inversionCount

    def merge_sort(self, start, end, arr):

        if start == end:
            return arr[start : end + 1]

        mid = start + (end - start) // 2

        arr1 = self.merge_sort(start, mid, arr)

        arr2 = self.merge_sort(mid + 1, end, arr)

        return self.merge(arr1, arr2, mid)

    def merge(self, arr1, arr2, mid):
        arr3 = []
        m = 0
        n = 0

        while m < len(arr1) and n < len(arr2):
            if arr1[m] <= arr2[n]:
                arr3.append(arr1[m])
                m = m + 1
            else:
                self.inversionCount = self.inversionCount + len(arr1) - m
                arr3.append(arr2[n])
                n = n + 1

        while m < len(arr1):
            arr3.append(arr1[m])
            m = m + 1

        while n < len(arr2):
            arr3.append(arr2[n])
            n = n + 1

        return arr3
