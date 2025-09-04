class Solution:
    # Optimized solution can be derived in O(1) using Bayer Moore's voting algorithm
    # Intuition here - https://www.geeksforgeeks.org/theory-of-computation/boyer-moore-majority-voting-algorithm/
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
             return -1

        cnt, elem = 0, nums[0]

        for num in nums:
            if num == elem:
                cnt +=1
            else:
                cnt-=1
                if cnt == 0:
                    elem = num
                    cnt = 1
        
        cnt = 0
        for num in nums:
            if num == elem:
                cnt+=1
        if cnt > len(nums) // 2:
            return elem
        return -1






        