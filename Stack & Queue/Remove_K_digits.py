class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num:
            while k > 0 and stack and stack[-1] > char:
                stack.pop()
                k -= 1
            stack.append(char)
        
        stack = stack[:len(stack) - k]
        
        res = "".join(stack)
        return str(int(res)) if res else "0"    
    #checks if the result is a non empty str or not, if non empty returns 0
    #takes care of the leading zeros by converting the str to int and then back to str