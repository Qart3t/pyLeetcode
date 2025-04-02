
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            #print("inna dlugosc")
            return False
        
        dictionary = {}
        index = 0

        while(index <= len(t) - 1):

            if dictionary.__contains__(t[index]):
                dictionary[t[index]] = dictionary.get(t[index], 0) + 1
            else:
                dictionary[t[index]] = 1

            if dictionary.__contains__(s[index]):
                dictionary[s[index]] = dictionary.get(s[index], 0) - 1
            else:
                dictionary[s[index]] = - 1
            
            index += 1  

        for key,val in dictionary.items():
            if val == 0:
                pass
            else:
                return False
            
        return True
'''

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        
s = "aaa"
t = "aaa"

sol = Solution()
print(sol.isAnagram(t,s))

