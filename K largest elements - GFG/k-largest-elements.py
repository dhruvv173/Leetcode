#User function Template for python3
from heapq import heapify, heappop, heappush

class Solution:
    def kLargest(self, li, n, k):
        minHeap = []
        heapify(minHeap)
        
        for i in li:
            heappush(minHeap, i)
            if len(minHeap) > k:
                heappop(minHeap)
        
        result = []
        for _ in range(k):
            result.append(heappop(minHeap))
        
        return result[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    li = [int(x) for x in input().strip().split()]
    n=li[0]
    k=li[1]
    li = [int(x) for x in input().strip().split()]
    ob=Solution()
    k_largest_list = ob.kLargest(li,n,k)
    
    for element in k_largest_list:
        print(element, end = ' ')
    print('')
# } Driver Code Ends