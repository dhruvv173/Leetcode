#User function Template for python3
class Solution:
    def minDeletions(self, Str, n): 
        #code here
        LCS = self.longestPalindromeSubseq(Str)
        return n - LCS
        
    def longestPalindromeSubseq(self, s1):
        s2 = s1[::-1]  
        n, m = len(s1), len(s2)  

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]  # If characters match, extend the match
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # Otherwise, take the maximum

        return dp[n][m]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
       
        N = int(input())
        Str = input().strip()
        ob = Solution()
        ans = ob.minDeletions(Str, N)
        print(ans)
# } Driver Code Ends