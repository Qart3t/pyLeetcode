class Solution:

    def __init__(self):

        self.key = "%%40vol%%"


    def encode(self, strs: list[str]) -> str:
        encoced : str = ""

        for string in strs:
            encoced += string + self.key

        return encoced

    def decode(self, s: str) -> list[str]:

        decoded : list =[s for s in s.split("%%40vol%%") if s]

        return decoded
        

sol = Solution()

str_list : list = ["neet","code","love","you"]

str_list = sol.encode(str_list)
print(str_list)
str_list = sol.decode(str_list)
print(str_list)

