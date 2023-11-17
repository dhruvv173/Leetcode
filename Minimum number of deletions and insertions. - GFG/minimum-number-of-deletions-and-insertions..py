#User function Template for python3
class Solution:
	def minOperations(self, s1, s2):
		# code here
		LCS = self.longestCommonSubsequence(s1, s2)
		m = len(s1) - LCS
		n = len(s2) - LCS
		return m + n
		
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        # Bottom-up DP
        x = len(s1)
        y = len(s2)
        dp = [[0] * (y+1) for _ in range(x+1)]
        
        for i in range(1, x+1):
            for j in range(1, y+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[x][y]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends