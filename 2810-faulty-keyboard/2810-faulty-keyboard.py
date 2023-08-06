class Solution:
    def finalString(self, s: str) -> str:
        answ = ""
        for i in range(len(s)):
            if s[i] == "i":
                answ = answ[::-1]
            else:
                answ += s[i]
        return answ

        
        