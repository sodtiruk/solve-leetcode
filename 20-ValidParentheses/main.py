class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2 != 0:
            return False

        check = False 
        for i in s:
            if i in "([{":
                stack.append(i)        
            elif i in ")}]":
                left = "" 
                right = ""
                if len(stack) != 0:
                    left = stack.pop()
                    right = i

                paren = left + right 
                if paren not in ["()", "[]", "{}"]:
                    check = False
                    break
                else:
                    check = True

        if len(stack) > 0:
            check = False
        
        return check



so = Solution()
print(so.isValid("([{}])"))



