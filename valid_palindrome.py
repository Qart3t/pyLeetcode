class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        index : int = 0

        wordLen = len(s) - 1

        pointLeft : int = 0
        pointRight : int = wordLen 

        skip_process : bool = False


        while(index < (wordLen + 1)):

            skip_process = False

            if s[pointLeft].isalnum() or s[pointLeft].isdigit():
                pass
            else:
                #print(f"{s[pointLeft]} is not a digit or a number")
                skip_process = True   
                pointLeft += 1

            if s[pointRight].isalnum() or s[pointRight].isdigit():
                pass
            else:
                #print(f"{s[pointRight]} is not a digit or a number")
                skip_process = True  
                pointRight -= 1

            if skip_process == False:

                if s[pointLeft].lower() == s[pointRight].lower():
                    pointRight -= 1
                    pointLeft += 1
                    #print(f"wartosci dla index {pointLeft}, {pointRight} rowne")
                else:
                    #print(f"wartosci dla index {s[pointLeft]}, {s[pointRight]} nie rowne")
                    return False

            if pointLeft >= pointRight:
                break

        return True

sol = Solution()

word : str = "A man, a plan, a canal: Panama"

print(sol.isPalindrome(word))
