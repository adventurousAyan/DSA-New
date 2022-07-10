from typing import List

# Two sum unsorted approach
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = []
        # Sort the nums array
        nums = sorted(nums)
        for index in range(len(nums)):
            twoSum = 0 - nums[index]
            twoSumList = self.twoSum(nums[index + 1 :], twoSum)
            for item in twoSumList:
                my_list = [nums[index], item[0], item[1]]
                if my_list not in triplets:
                    triplets.append(my_list)

        return triplets

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st_dict = {}
        ls = []
        for index in range(len(nums)):
            tmp = target - nums[index]
            if tmp not in st_dict:
                st_dict[nums[index]] = index
            else:
                ls.append([nums[st_dict[tmp]], nums[index]])

        return ls
