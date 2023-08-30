#User function Template for python3
class Solution:
    def subset(self, n, k, arr):
        dp = [[False for j in range(k+1)] for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
    
        for i in range(1,n+1):
            for j in range(1,k+1):
    
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
    
        return dp[n][:(k//2)+1]  # return the first half of the last row
    
    def minDifference(self, arr, n):
    
        min_num = float("inf")
        total = sum(arr)
        number_list = self.subset(len(arr), total, arr)
    
        for inx,num in enumerate(number_list):
            if num:
                min_num = min(min_num,total-(inx*2))
        return min_num


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends