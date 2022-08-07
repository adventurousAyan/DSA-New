# Definition for a binary tree node.
from typing import List, Optional

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, inorder):
            if len(inorder) == 0:
                return None
            else:
                # TODO: Instead of looping, we could store that in hashmap
                for i in range(len(inorder)):
                    if inorder[i] == preorder[0]:
                        root = TreeNode(preorder[0])
                        lInorder = len(inorder[:i])

                        root.left = build(preorder[1 : lInorder + 1], inorder[:i])
                        root.right = build(preorder[lInorder + 1 :], inorder[i + 1 :])
                        return root

        res = build(preorder, inorder)
        return res
