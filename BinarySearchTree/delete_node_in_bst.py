# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(root, key, par=None):
            if root is None:
                return
            elif root.val == key:
                # If matches
                if root.right:
                    # If right exists, we need to traverse till we found left just smaller than root
                    cur = root.right
                    prev = cur
                    while cur.left:
                        prev = cur
                        cur = cur.left
                    root.val = cur.val
                    if cur.val == prev.val:
                        root.right = cur.right
                    else:
                        prev.left = cur.right
                elif root.left:
                    # If left exists, we need to traverse till we found right just larger than root
                    cur = root.left
                    prev = cur
                    while cur.right:
                        prev = cur
                        cur = cur.right
                    root.val = cur.val
                    if cur.val == prev.val:
                        root.left = cur.left
                    else:
                        prev.right = cur.left

                else:
                    # If Leaf Node
                    if root.val < par.val:
                        par.left = None
                    else:
                        par.right = None

            else:
                dfs(root.left, key, root)
                dfs(root.right, key, root)

        if root and root.left is None and root.right is None and root.val == key:
            return None
        dfs(root, key)
        return root
