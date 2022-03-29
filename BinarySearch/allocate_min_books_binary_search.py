class Solution:

    # Function to find minimum number of pages.
    def findPages(self, A, N, M):
        # code here
        arr = A
        n = N
        student = M

        start = arr[0]
        end = sum(arr)
        minno = float("inf")
        while start <= end:
            mid = start + (end - start) // 2
            res = self.isValidAllocationPossible(student, arr, mid)
            if res:
                minno = min(minno, mid)
                end = mid - 1
            else:
                start = mid + 1
        return minno

    def isValidAllocationPossible(self, student, arr, mid):
        st = [0] * student
        pagesum = 0
        i = 0
        for a in arr:
            if a > mid:
                return False
            pagesum += a
            st[i] = pagesum
            if pagesum > mid and i + 1 < student:
                st[i] = pagesum - a
                i = i + 1
                pagesum = a
        st[i] = pagesum
        for b in st:
            if b > mid:
                return False
        return True
