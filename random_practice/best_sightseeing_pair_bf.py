class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        def f(i, dp):
            if i < 0:
                return dp
            left, right = float('-inf'), float('-inf')
            for j in range(i):
                left = max(left, arr[i] + arr[j] + j-i)
            for j in range(i+1 ,n):
                right = max(right, arr[i] + arr[j] + i-j)
            dp[i] = max(left, right)
            
            return f(i-1, dp)
        
        arr = values
      
        n = len(values)
        dp = [-1]*len(values)
       
        res = f(n-1, dp)
        print(res)
        return max(res)