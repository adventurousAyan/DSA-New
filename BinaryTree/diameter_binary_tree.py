class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        self.d = 0
        self.solve(root)
        return self.d
        
    
    def solve(self, root):
        if root is None:
            return 0
        else:
            lheight = self.solve(root.left)
            rheight = self.solve(root.right)
            self.d = max(self.d, lheight + rheight + 1)
            return 1 + max(lheight, rheight)