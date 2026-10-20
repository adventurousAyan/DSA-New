class Solution:
    def search(self, nums: List[int], target: int) -> bool:


        low, high = 0, len(nums) - 1

        # 0,1,2,4,5,6,7
        # 7,0,1,2,4,5,6


        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            # If the left part is sorted
            elif nums[low] <= nums[mid]:
                # If the target is in the left part, search in the left part
                if target >= nums[low] and target <= nums[mid]:
                    high = mid - 1
                # If the target is not in the left part, search in the right part
                else:
                    low = mid + 1
            else:
                # If the right part is sorted
                # If the target is in the right part, search in the right part
                if target >= nums[mid] and target <= nums[high]:
                    low = mid + 1
                # If the target is not in the right part, search in the left part
                else:
                    high = mid - 1
        return -1 



    

