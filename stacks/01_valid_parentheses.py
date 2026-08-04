
class Solution:
    def isValid(self, s: str) -> bool:
        braces = {"(":")", "{":"}", "[":"]"}
        stack = [None]*(len(s))
        top = -1
        for ch in s:
            if ch in braces:
                top += 1
                stack[top] = ch
            else:
                if top == -1:
                    return False
                if ch != braces[stack[top]]:
                    return False
                top -= 1
        return top == -1  
