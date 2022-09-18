import re


class Solution:
    def sort_with_merge(self, arr):

        start = 0
        end = len(arr) - 1
        return self.merge_sort(start, end, arr)

    def merge_sort(self, start, end, arr):

        if start == end:
            return arr[start]

        mid = start + (end - start) // 2

        arr1 = self.merge_sort(start, mid, arr)

        arr2 = self.merge_sort(mid + 1, end, arr)

        return self.merge(arr1, arr2)

    def merge(self, arr1, arr2):
        arr3 = []
        m = 0
        n = 0

        while m < len(arr1) and n < len(arr2):
            if arr1[m] < arr2[n]:
                arr3.append(arr1[m])
                m = m + 1
            else:
                arr3.append(arr2[n])
                n = n + 1

        while m < len(arr1):
            arr3.append(arr1[m])
            m = m + 1

        while n < len(arr2):
            arr3.append(arr2[n])
            n = n + 1

        return arr3


s = Solution()
print(s.sort_with_merge([2, 3, 1, 5, 7, 6, 8]))

print(s.sort_with_merge([15, 5, 24, 8, 1, 3, 16, 10, 20]))
