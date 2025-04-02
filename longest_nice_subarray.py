class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:

        nums_len : int = len(nums)

        p : int = 0 
        index : int = 0
        i : int = 0
        j : int = 1

        max_nice_array_lenght = 0
        current_nice_array_lenght = 1
        tmp : bool = False


        for num in nums:

            while(index < nums_len):

                if tmp == True:
                    k : int = index
                    while(k < current_nice_array_lenght and current_nice_array_lenght < nums_len - 1):
                        if nums[k] & nums[k+1]:
                            print("pass")
                        else:
                            tmp = False
                            print(f"breka at k: {k} ")
                            break
                        if k == current_nice_array_lenght :
                            print(f"add at p {p} index {index} k {k} ")
                            current_nice_array_lenght += 1

                            if max_nice_array_lenght < current_nice_array_lenght:
                                max_nice_array_lenght = current_nice_array_lenght
                            
                            current_nice_array_lenght = 0

                            break

                if nums[i] & nums[j] and tmp == False:
                    tmp = True
                    current_nice_array_lenght += 1

                index +=1

        
            
            current_nice_array_lenght = 1

            p += 1
            index = p
            tmp = False

        return max_nice_array_lenght


sol : Solution = Solution()

nums_list : list = [1, 3, 8, 48, 10]

print(sol.longestNiceSubarray(nums_list))