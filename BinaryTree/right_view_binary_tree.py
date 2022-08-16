# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, level):
            if root is None:
                return None
            if level == len(self.ls):
                self.ls.append(root.val)

            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        self.ls = []
        dfs(root, 0)
        return self.ls
