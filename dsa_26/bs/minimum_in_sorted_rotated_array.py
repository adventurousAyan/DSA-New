class Solution:
    def findMin(self, nums: List[int]) -> int:

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2


            # Normal case (0,1,2,3,4,5,6,7)
            if nums[mid] >= nums[start] and nums[mid] < nums[end]:
                end = mid - 1
            #(7,0,1,2,3,4,5,6)
            elif nums[mid] <= nums[start] and nums[mid] < nums[end]:
                if nums[mid-1] <= nums[mid]:
                    end = mid
                else:
                    start = mid
            #(4,5,6,7,0,1,2)
            elif nums[mid] >= nums[start] and nums[mid] > nums[end]:
                if nums[start] > nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                return nums[start]
        return nums[start]


        


        