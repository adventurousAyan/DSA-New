class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        def find_max_l(idx):
            lh = 0
            maxil = -1
            while lh < idx:
                if height[lh] > height[idx]:
                    maxil = max(maxil, height[lh])
                lh += 1
            return maxil

        def find_max_r(idx):
            rh = n - 1
            maxir = -1

            while rh > idx:
                if height[rh] > height[idx]:
                    maxir = max(maxir, height[rh])
                rh -= 1
            return maxir

        s1 = 0
        maxil, maxir = -1, -1
        for idx in range(n):
            maxil = find_max_l(idx)
            maxir = find_max_r(idx)
            if maxil != -1 and maxir != -1:
                s1 += (min(maxil, maxir) * 1) - height[idx]
        return s1

# Above code is O(n^2) time complexity and O(1) space complexity.
# Idea is to find the max height to the left and right of the current index and 
# then calculate the water trapped at the current index.
# Collected water is the minimum of the max height to the left and right of the current index minus the height of the current index.
# This gives a TLE on leetcode.

class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        maxil, maxir = [-1]*n, [-1]*n
        for idx in range(n):
            if idx - 1 >= 0:
                maxil[idx] = max(maxil[idx-1], height[idx])
            else:
                maxil[idx] = height[idx]

        for idx in range(n-1,-1, -1):
            if idx + 1 < n:
                maxir[idx] = max(maxir[idx+1], height[idx])
            else:
                maxir[idx] = height[idx]

        s1 = 0
        for idx in range(n):
            if maxil[idx] != -1 and maxir[idx] != -1:
                s1 += (min(maxil[idx], maxir[idx]) * 1) - height[idx]
        return s1
# Above code is O(n) time complexity and O(n) space complexity.
# Idea is to remove the nested loop by precomputing the max height to the left and right of the current index.
