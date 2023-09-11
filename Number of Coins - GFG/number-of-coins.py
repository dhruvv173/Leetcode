class Solution:
    def minCoins(self, coins, M, V):
        dp = [[0] * (V + 1) for _ in range(M + 1)]

        # Initialize the base case
        for i in range(M + 1):
            dp[i][0] = 0

        for j in range(1, V + 1):
            dp[0][j] = float('inf') - 1

        # Populate the DP table using the given coin denominations
        for i in range(1, M + 1):
            for j in range(1, V + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        # Determine the minimum number of coins needed for the target amount
        ans = -1 if dp[M][V] == float("inf") else dp[M][V]
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends