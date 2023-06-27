#User function Template for python3
from heapq import heapify, heappop, heappush
class Solution:
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        # code here
        minHeap = []
        heapify(minHeap)
        res = []
        for i in a:
            heappush(minHeap, i)
            if len(minHeap) > k:
                res.append(heappop(minHeap))
                
        while minHeap:
            res.append(heappop(minHeap))
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(*ob.nearlySorted(a,n,k))

# } Driver Code Ends