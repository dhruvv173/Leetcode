#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        dp = [[0 for j in range(sum+1)] for i in range(N+1)]
        
        for i in range(N+1):
            for j in range(sum+1):
                if j > 0 and i == 0:
                    dp[i][sum] = False
                elif j == 0:
                    dp[i][j] = True
                elif arr[i-1] <= j:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[N][sum]   

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends