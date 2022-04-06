class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        # code here
        res = self.findLargest(root)
        return res[1]

    def findLargest(self, root):
        if root is None:
            return (1, 0, float("inf"), float("-inf"))
        if root.left is None and root.right is None:
            return (1, 1, root.data, root.data)
        else:
            val1 = self.findLargest(root.left)
            val2 = self.findLargest(root.right)
            if (
                val2[0] == 1
                and val1[0] == 1
                and root.data > val1[3]
                and root.data < val2[2]
            ):
                x = val1[2]
                y = val2[3]
                if x == float("inf"):
                    x = root.data
                if y == float("-inf"):
                    y = root.data
                return (1, val1[1] + val2[1] + 1, x, y)
            else:
                return (0, max(val1[1], val2[1]), 0, 0)
