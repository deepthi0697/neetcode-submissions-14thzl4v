class Solution:
    def isValid(self, s: str) -> bool:
        # matchPar = {"(":")","{":"}","[":"]"}
        # if len(s)%2 != 0:
        #     return False
        # for i in range(len(s)//2):
        #     last = len(s) - i -1
        #     if s[i] in matchPar and matchPar[s[i]] != s[last]:
        #         return False
        # return True
        # matchPar = {"(":")","{":"}","[":"]"} #this cant be used since, top of stack is always closing
        matchPar = {")":"(","}":"{","]":"["}
        stack = []
        for l in s:
            if l in matchPar:
                if stack and matchPar[l] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)

        return False if len(stack) != 0  else True
        
        