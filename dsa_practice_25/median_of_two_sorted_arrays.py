class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:   
      # This is based on symmetry pattern in binary search where we will divide the arrays in such a way
      # that left half will always be lesser than right half
      # Intuition in below video - https://www.youtube.com/watch?v=F9c7LpRZWVQ
      # https://leetcode.com/problems/median-of-two-sorted-arrays/
        n1 = len(nums1)
        n2 = len(nums2)
        if n1>n2:
            return self.findMedianSortedArrays(nums2, nums1)
        low = 0
        high = n1
        elem = (n1 + n2 + 1) // 2
        
        while low <= high:
            mid = low + (high - low) // 2
            mid1 = mid
            mid2 = elem - mid1
            l1,l2 = float('-inf'), float('-inf')
            r1, r2 = float('inf'), float('inf')

            if mid1 - 1 >= 0 and mid1 - 1 < n1:
                l1 = nums1[mid1-1]
            if mid2 - 1 >= 0 and mid2 - 1 < n2:
                l2 = nums2[mid2-1]
            if mid1 >= 0 and mid1 < n1:
                r1 = nums1[mid1]
            if mid2 >= 0 and mid2 < n2:
                r2 = nums2[mid2]          
            if l1 > r2:
                high = mid-1
            elif l2 > r1:
                low = mid + 1
            else:
                if l1 <= r2 and l2 <= r1:
                    if (n1+n2)%2 == 0:
                        return (max(l1, l2) + min (r1,r2)) / 2
                    else:
                        return  max(l1, l2)
        return 0
        






        
