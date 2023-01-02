class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        allPs = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if len(stack) != 0 and stack[-1] == allPs[c]:
                    stack.pop()
                else:
                    return False 
        return True if not stack else False