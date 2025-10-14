class Solution:
    # https://leetcode.com/problems/find-the-middle-index-in-array/
    # https://www.youtube.com/watch?v=u89i60lYx8U
    # TC: O(n)
    # SC: O(n)
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pref_arr  = [0]*n
        suff_arr = [0]*n
        pref_arr[0] = nums[0]
        suff_arr[n-1] = nums[n-1]
        i, j, k = 1, n-2, 0
        
        while i < n and j >= 0:
            pref_arr[i] = pref_arr[i-1] + nums[i]
            suff_arr[j] = suff_arr[j+1] + nums[j]
            i+=1
            j-=1
        while k < n:
            if pref_arr[k] == suff_arr[k]:
                return k
            k+=1
        return -1
        