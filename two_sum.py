'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        pointerRight = len(nums) - 1
        
        indexi = 0 
        indexj = 0 

        while(indexi < pointerRight):

            while(indexj < pointerRight + 1):

                if(nums[indexi] + nums [indexj] == target and indexi != indexj):
                    return [indexi, indexj]
                
                indexj += 1

            indexj = 0 
            indexi += 1 
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {} 
        for i, num in enumerate(nums):
            complement = target - num 
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

sol = Solution()

list = [3,2,4]
t = 6

print(sol.twoSum(list, t)) 


