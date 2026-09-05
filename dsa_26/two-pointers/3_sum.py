class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        
        
        def two_sum(nums, newt, idx):
            d1 = {}
            ls = []
            for idx1, num in enumerate(nums):
                if idx1 == idx:
                    continue
                if newt - num in d1.keys():
                    ls.append([newt-num, num])
                else:
                    d1[num] = idx1
            return ls
        
        target = 0
        ls = []
        for idx, num in enumerate(nums):
            newt = target - num
            res = two_sum(nums, newt, idx)
            if res == []:
                continue
            for r in res:
                r.append(nums[idx])
                s_res = sorted(r)
                if s_res not in ls:
                    ls.append(s_res)
        return ls


        
            

        