#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def countPartitions(self, n, d, arr):
        # Code here
        MOD = 10**9 + 7
        sum_val = sum(arr)
        if (d + sum_val) % 2:
            return 0
        t = (d + sum_val) // 2
        
        # Find count of subsets with sum equal to t
        dp = [[0] * (t + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(t + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]) % MOD
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][t]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, d = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countPartitions(n, d, arr)
        print(res)
# } Driver Code Ends