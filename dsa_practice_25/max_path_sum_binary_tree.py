# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def maxSum(root, su):

            if root is None:
                return 0
            lsum = maxSum(root.left, root.val)
            rsum = maxSum(root.right, root.val)
            # print(f"lsum: {lsum}")
            # print(f"rsum: {rsum}")
            self.maxi = max(self.maxi, max(lsum + rsum + root.val, max(lsum, rsum) + root.val), root.val)
            # print(f"val: {lsum + rsum  + root.val}")
            return max(0, max(lsum , rsum) + root.val)

        su = 0
        self.maxi = float("-inf")
        maxSum(root, su)
        return self.maxi

# https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=problem-list-v2&envId=binary-tree