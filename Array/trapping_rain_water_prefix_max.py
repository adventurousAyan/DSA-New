from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        arr = height
        arr1 = [-1] * n
        arr2 = [-1] * n
        arr1[0] = height[0]
        arr2[n - 1] = height[n - 1]
        ans = 0

        # Prefix Max Array
        for i in range(1, n):
            arr1[i] = max(arr1[i - 1], arr[i])

        # Suffix Max Array
        for i in range(n - 2, -1, -1):
            arr2[i] = max(arr2[i + 1], arr[i])

        for i in range(n):
            ans += min(arr1[i], arr2[i]) - height[i]

        return ans
