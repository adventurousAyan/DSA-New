class Solution:
    # https://leetcode.com/problems/product-of-array-except-self/
    # Intuition here - https://www.youtube.com/watch?v=bNvIQI2wAjk
    # TC: O(n)
    # SC: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1]*(n+1)
        suff = [1]*(n+1)
        pref[0] = nums[0]
        suff[n-1] = nums[n-1]
        answer = [0]*n

        for i in range(1,n):
            pref[i] = nums[i]*pref[i-1]

        for j in range(n-2, -1, -1):
            suff[j] = nums[j]* suff[j+1]
        
        for i in range(n):
            answer[i] = pref[i-1]*suff[i+1]
        return answer

    # Space optimized solution
    class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = 1
        suff = 1
        ans = [1]*n
        for i in range(n):
            ans[i] = pref
            pref = pref* nums[i]

        for j in range(n-1, -1, -1):
            ans[j] = ans[j]*suff
            suff = suff*nums[j]

        return ans

   
    # TC: O(n)
    # SC: O(1)