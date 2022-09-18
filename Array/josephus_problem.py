class Solution:

    # https://www.youtube.com/watch?v=Qej8V1M1e2A for intuition

    def josephus(self,n,k):
        #Your code here
        if n == 1:
            return 1
        return (self.josephus(n-1, k) + k-1)%n + 1