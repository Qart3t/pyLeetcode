class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dictionary : dict = {}

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        sorted_by_value_desc = dict(sorted(dictionary.items(), key=lambda kvp: kvp[1], reverse=True))

        list_  = list(sorted_by_value_desc.keys())

        i = 0
        ans = []
        while(i < k):
            ans.append(list_[i])
            i += 1

        return ans



sol = Solution()

list_ : list = [1]
k : int = 1

print(sol.topKFrequent(list_, k))
        