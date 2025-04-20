class Stack:

    def __init__(self):
        self.stack : list = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    

def is_matching_pairs(val1, val2) -> bool:

    if val1 == '(' and val2 == ')':
        return True
    elif val1 == '[' and val2 == ']':
        return True
    elif val1 == '{' and val2 == '}':
        return True
    else:
        return False
    
class Solution:
    def isValid(self, s: str) -> bool:
        stc : Stack = Stack()

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stc.push(c)
            elif c == ')' or c == '}' or c == ']':
                if stc.count() == 0:
                    print("a")
                    return False
                top = stc.pop()
                if is_matching_pairs(top, c) == False:
                    print("b")
                    return False
            else:
                print("c")
                return False
        print("d")
        return stc.count() == 0



sol = Solution()
print(sol.isValid("()[]{}"))