from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        total = n1 + n2

        half = total // 2

        if n2 < n1:
            nums1, nums2 = nums2, nums1

        low = 0
        high = len(nums1) - 1
        while True:
            cut1 = (low + high) // 2
            cut2 = half - cut1 - 2

            l1 = nums1[cut1] if cut1 >= 0 else float("-inf")
            r1 = nums1[cut1 + 1] if (cut1 + 1) < len(nums1) else float("inf")
            l2 = nums2[cut2] if cut2 >= 0 else float("-inf")
            r2 = nums2[cut2 + 1] if (cut2 + 1) < len(nums2) else float("inf")
            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return min(r1, r2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
