#User function Template for python3
from heapq import heappop, heappush, heapify
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        # code here
        minHeap = []
        cost = 0
        heapify(minHeap)
        
        for i in arr:
            heappush(minHeap, i)
        
        while len(minHeap) >= 2:
            first = heappop(minHeap)
            second = heappop(minHeap)       #get the top two elements from the heap
            cost += first + second          #add them to the cost 
            heappush(minHeap, first+second) #again add the new rope ie (first+second) to the heap again
        return cost

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict
# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minCost(a,n))
# } Driver Code Ends