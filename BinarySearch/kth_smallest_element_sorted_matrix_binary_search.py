from typing import List


class Solution:

    # https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
    # https://www.youtube.com/watch?v=LkrsdWa69_Q

    # Almost same approach can be used to 
    # find the median in a row wise column wise sorted matrix.
    # As length is odd, on left n/2 and on right n/2 elements would be there. 
    # So first we would take
    # the min element which is mid of matrix[0][0] and max elem which is matrix[n-1][n-1].
    #  Then find middle
    # and check now many are less than mid and how many are greater than mid. 
    # If they are same, return mid
    # else increase/decrease the search space to mid-1 or mid + 1
    # Problem link - https://www.geeksforgeeks.org/find-median-row-wise-sorted-matrix/

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        m = len(matrix)
        n = len(matrix[0])

        start = matrix[0][0]
        end = matrix[n - 1][n - 1]

        while start <= end:

            mid = (start + end) // 2

            ans = 0
            for i in range(m):

                low = 0
                high = n - 1
                while low <= high:
                    mi = low + (high - low) // 2

                    if mid >= matrix[i][mi]:
                        low = mi + 1
                    else:
                        high = mi - 1

                ans += low

            if ans < k:
                start = mid + 1
            else:
                end = mid - 1

        return start
