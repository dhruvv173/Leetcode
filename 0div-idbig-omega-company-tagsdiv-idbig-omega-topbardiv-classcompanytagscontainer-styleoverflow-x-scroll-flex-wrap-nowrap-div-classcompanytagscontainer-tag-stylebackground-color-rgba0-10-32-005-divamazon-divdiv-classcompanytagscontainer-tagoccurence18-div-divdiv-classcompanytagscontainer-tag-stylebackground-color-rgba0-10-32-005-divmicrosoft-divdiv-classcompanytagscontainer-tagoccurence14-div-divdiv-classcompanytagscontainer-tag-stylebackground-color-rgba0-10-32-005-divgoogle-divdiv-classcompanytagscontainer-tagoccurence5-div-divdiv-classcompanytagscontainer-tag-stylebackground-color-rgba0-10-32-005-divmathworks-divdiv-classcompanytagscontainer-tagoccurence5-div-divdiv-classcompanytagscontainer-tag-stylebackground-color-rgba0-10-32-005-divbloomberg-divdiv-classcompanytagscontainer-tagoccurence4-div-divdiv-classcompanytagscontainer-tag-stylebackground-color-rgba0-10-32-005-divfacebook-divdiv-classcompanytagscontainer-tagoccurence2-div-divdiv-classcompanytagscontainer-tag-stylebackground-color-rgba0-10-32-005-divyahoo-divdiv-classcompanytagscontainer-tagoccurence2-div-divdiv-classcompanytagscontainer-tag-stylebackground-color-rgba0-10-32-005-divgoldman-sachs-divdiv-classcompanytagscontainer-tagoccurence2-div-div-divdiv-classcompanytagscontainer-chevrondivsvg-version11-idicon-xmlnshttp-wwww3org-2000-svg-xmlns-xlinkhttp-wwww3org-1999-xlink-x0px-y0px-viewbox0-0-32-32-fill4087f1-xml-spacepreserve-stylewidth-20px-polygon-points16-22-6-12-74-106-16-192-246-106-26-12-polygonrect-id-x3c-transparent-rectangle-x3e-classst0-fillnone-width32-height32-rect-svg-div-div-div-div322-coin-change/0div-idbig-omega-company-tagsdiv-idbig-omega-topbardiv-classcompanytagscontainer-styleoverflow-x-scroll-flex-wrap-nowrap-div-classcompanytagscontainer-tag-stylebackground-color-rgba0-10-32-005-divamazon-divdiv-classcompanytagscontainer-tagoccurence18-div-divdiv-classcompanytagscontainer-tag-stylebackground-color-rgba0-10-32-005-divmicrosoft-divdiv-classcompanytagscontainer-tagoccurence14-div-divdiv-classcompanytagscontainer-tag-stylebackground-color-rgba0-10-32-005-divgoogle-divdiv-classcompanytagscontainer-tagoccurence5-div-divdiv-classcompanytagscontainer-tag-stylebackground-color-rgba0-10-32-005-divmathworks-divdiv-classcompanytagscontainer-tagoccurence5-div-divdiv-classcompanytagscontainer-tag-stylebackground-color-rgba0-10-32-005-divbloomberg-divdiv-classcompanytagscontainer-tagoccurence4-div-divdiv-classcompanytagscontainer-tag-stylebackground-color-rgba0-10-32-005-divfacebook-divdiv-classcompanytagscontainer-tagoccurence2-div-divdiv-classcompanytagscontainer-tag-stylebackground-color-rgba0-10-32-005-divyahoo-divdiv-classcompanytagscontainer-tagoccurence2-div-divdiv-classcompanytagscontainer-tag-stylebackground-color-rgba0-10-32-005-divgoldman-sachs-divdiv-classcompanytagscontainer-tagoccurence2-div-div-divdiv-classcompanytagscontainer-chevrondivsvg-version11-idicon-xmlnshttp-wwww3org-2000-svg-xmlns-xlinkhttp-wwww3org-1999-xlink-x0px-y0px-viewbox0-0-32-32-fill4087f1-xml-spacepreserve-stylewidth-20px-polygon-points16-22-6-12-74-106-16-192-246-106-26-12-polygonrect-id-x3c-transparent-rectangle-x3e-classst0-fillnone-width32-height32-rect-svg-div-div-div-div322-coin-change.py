class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

# TLE Aditya Verma Solution unbounded knapsack
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)
#         t = [[0] * (amount+1) for _ in range(n+1)]
        
#         for i in range(n+1):
#             t[i][0] = 0

#         for j in range(amount+1):
#             t[0][j] = float("inf") - 1
        
#         for i in range(1,n+1):
#             for j in range(1, amount+1):
#                 if coins[i-1] <= j:
#                     t[i][j] = min(1+ t[i][j - coins[i-1]], t[i-1][j])
#                 else:
#                     t[i][j] = t[i-1][j]

#         res = -1 if t[n][amount] == float("inf") - 1 else t[n][amount]
#         print(t)
#         return res