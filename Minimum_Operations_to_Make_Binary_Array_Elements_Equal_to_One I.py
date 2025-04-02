'''
class Solution:
    def minOperations(self, nums: list[int]) -> int:

        nums_len : int = len(nums)
        index : int = 0

        numb_of_flips : int = 0

        while(index < nums_len - 2):

            if nums[index] == 0:

                nums[index] = 1 

                if nums[index + 1] == 0:
                    nums[index + 1] = 1
                else:
                    nums[index + 1] = 0

                if nums[index + 2] == 0:
                    nums[index + 2] = 1
                else:
                    nums[index + 2] = 0

                numb_of_flips += 1
                print("flip")

            index +=1

        print(nums)

        if all(num == 1 for num in nums):
            return numb_of_flips
        else:
            return -1'
'''

class Solution:
    def minOperations(self, nums: list[int]) -> int:

        nums_len : int = len(nums)
        index : int = 0

        numb_of_flips : int = 0

        while(index < nums_len - 2):

            if nums[index] == 0:

                nums[index] ^= 1
                nums[index + 1] ^= 1
                nums[index + 2] ^= 1
                numb_of_flips += 1

            index +=1

        if sum(nums) == nums_len:
            return numb_of_flips
        return -1

sol = Solution()


nums_list : list = [0,1,1,1,0,0]

print(sol.minOperations(nums_list))