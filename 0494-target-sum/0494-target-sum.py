class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # exactly similar to https://practice.geeksforgeeks.org/problems/partitions-with-given-difference/1
        total_sum = sum(nums)
    
        if (total_sum - target) % 2 == 1 or target > total_sum:
            return 0
        
        n = len(nums)
        s2 = (total_sum - target) // 2
        
        dp = [[0 for _ in range(s2 + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(s2 + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][s2]