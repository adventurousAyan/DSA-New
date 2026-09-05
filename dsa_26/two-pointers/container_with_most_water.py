class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxi = float('-inf')

        l, r = 0, len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r-l)
            maxi = max(maxi, area)
            if height[l] < height [r]:
                l +=1
            else:
                r -=1
        return maxi

# The idea is to use two pointers to find the maximum area. We start with
# left pointer and right pointer wide part first
# If the height of left pointer is less, that means we cant make larger area, so we move left pointer
# to the right. If the height of right pointer is less, that means we cant make larger area, so we move right pointer
# to the left. We continue this process until the left pointer is greater than the right pointer.
# We return the maximum area found.
# Time complexity: O(n)
# Space complexity: O(1)