# User function Template for python3


class Solution:
    def kthSmallest(self, arr, l, r, k):
        """
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        """
        return self.quick_select(arr, l, r, k - 1)

    def quick_select(self, arr, l, r, k):

        if l < r:
            loc = self.partition(arr, l, r)
            if loc == k:
                return arr[loc]
            elif k > loc:
                self.quick_select(arr, loc + 1, r, k)
            else:
                self.quick_select(arr, l, loc - 1, k)

        return arr[k]

    def partition(self, arr, l, r):
        start = l
        end = r
        pivot = arr[start]
        while start < end:

            while start < len(arr) and arr[start] <= pivot:
                start += 1

            while arr[end] > pivot:
                end -= 1

            if start < end:
                arr[start], arr[end] = arr[end], arr[start]

        arr[l], arr[end] = arr[end], arr[l]
        return end


arr = [7, 10, 4, 3, 20, 15]

s = Solution()
print(s.kthSmallest(arr, 0, 5, 4))
