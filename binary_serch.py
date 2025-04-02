import math

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left_index : int = 0
        right_index : int = len(nums) 
        mid_index : int = int(right_index/2)

        max_nums_of_operation : int = int(math.log2(len(nums)))
        counter : int = 0

        while(max_nums_of_operation + 1 > counter):
            print(mid_index)
            if nums[mid_index] > target:
                right_index = mid_index
                mid_index =  int((left_index + right_index) / 2)
            elif nums[mid_index] < target:
                left_index = mid_index
                mid_index = int((left_index + right_index) / 2) 
            elif nums[mid_index] == target:
                return mid_index
            
            counter += 1
            
        return -1



sol = Solution()

nums : int = [-1,0,3,5,9,12]
target : int = 2

print(sol.search(nums, target))

