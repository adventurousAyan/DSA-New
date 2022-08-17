# User function Template for python3

# https://practice.geeksforgeeks.org/problems/largest-bst/1


class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        # code here

        def dfs(root):
            if root is None:
                return (True, 0, float("inf"), float("-inf"))
            if root.left is None and root.right is None:
                return (True, 1, root.data, root.data)
            flaglh, sizelh, minlh, maxlh = dfs(root.left)
            flagrh, sizerh, minrh, maxrh = dfs(root.right)

            if flaglh and flagrh and root.data > maxlh and root.data < minrh:
                if maxrh == float("-inf"):
                    maxrh = root.data
                if minlh == float("inf"):
                    minlh = root.data
                return (True, sizelh + sizerh + 1, minlh, maxrh)
            else:
                return (False, max(sizelh, sizerh), 0, 0)

        res = dfs(root)
        return res[1]
