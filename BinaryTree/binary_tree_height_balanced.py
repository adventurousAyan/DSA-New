class Solution:
    def isBalanced(self,root):
        self.heightBal = True
        self.solve(root)
        return self.heightBal
        
        
            
    def solve(self, root):
        if root is None:
            return 0
        elif self.heightBal == False:
            return 0
        else:
            lh = self.solve(root.left)
            rh = self.solve(root.right)
            if abs(lh - rh) > 1:
                self.heightBal = False
            return 1 + max(lh, rh)