class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n=len(s)
        i,j,last=0,0,0
        ans=0

        while j<n:
            if j>0 and s[j]==s[j-1]:
                i=last
                last=j
            ans=max(ans,(j-i)+1) #(+1)--> because obased index
            j+=1
        return ans