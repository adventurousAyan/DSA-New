class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # https://leetcode.com/problems/median-of-two-sorted-arrays/

        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        hf = (n1 + n2 + 1) // 2

        low = 0
        high = n1
        while low <= high:
            cut1 = low + high >> 1
            cut2 = hf - cut1

            l1 = nums1[cut1 - 1] if cut1 >= 1 else float("-inf")
            l2 = nums2[cut2 - 1] if cut2 >= 1 else float("-inf")

            r1 = nums1[cut1] if cut1 <= n1 - 1 else float("inf")
            r2 = nums2[cut2] if cut2 <= n2 - 1 else float("inf")

            if l1 <= r2 and l2 <= r1:
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1

    # TC: O(log(min(n1,n2)))
    # SC: O(1)
