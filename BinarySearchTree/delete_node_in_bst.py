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


# Example1 :-

# [44,11,45,7,21,null,49,6,8,13,24,47,null,0,null,null,9,12,19,23,25,46,48,null,2,null,10,null,null,15,20,22,null,null,38,null,null,null,null,1,3,null,null,14,16,null,null,null,null,33,41,null,null,null,5,null,null,null,18,29,34,40,43,4,null,17,null,27,30,null,36,39,null,42,null,null,null,null,null,26,28,null,31,35,37,null,null,null,null,null,null,null,null,null,32]
# 49

# Example2 :-

# [15,12,22,10,13,16,25,6,11,null,14,null,17,23,29]
# 15
