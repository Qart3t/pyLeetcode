class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramGroups: dict = {}
        for word in strs:
            sorted_word: str = ''.join(sorted(word))
            if sorted_word not in anagramGroups:
                anagramGroups[sorted_word] = []
            anagramGroups[sorted_word].append(word)
        return list(anagramGroups.values())

sol = Solution()

list = ["eat","tea","tan","ate","nat","bat"]

print(sol.groupAnagrams(list)) 