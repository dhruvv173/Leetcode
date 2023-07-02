#User function Template for python3
from heapq import heappop, heappush, heapify
class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        # Your code goes here
        res = 0
        def kSmallest(arr,k):
            maxheap = []
            heapify(maxheap)
            for i in arr:
                heappush(maxheap, -1 * i)
                if len(maxheap) > k:
                    heappop(maxheap)
            return maxheap[0] * -1
        
        first = kSmallest(A, K1)
        second = kSmallest(A, K2)
        for i in A:
            if i > first and i < second:
                res += i
            
        return res
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        sz = [int(x) for x in input().strip().split()]
        k1, k2 = sz[0], sz[1]
        ob=Solution()
        print( ob.sumBetweenTwoKth(a, n, k1, k2) )

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends