Problem link - https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1


class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here
        res = 0
        maxi = 0
        i,j = 0,0
        while j < N:
            res = res + Arr[j]
            if j - i + 1 < K:  #to get to the size of sliding window K
                j +=1 
            elif j - i + 1 == K:
                maxi = max(res, maxi)
                res = res - Arr[i]
                i += 1
                j += 1
        return maxi