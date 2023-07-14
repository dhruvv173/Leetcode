#User function Template for python3

from typing import List
from collections import deque
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        if start == end:
            return 0
        q = deque()
        q.append((start, 0))
        dist = [float("inf")] * 100000
        dist[start] = 0

        while q:
            node, steps = q.popleft()

            for it in arr:
                num = (it * node) % 100000

                if steps + 1 < dist[num]:
                    dist[num] = steps + 1
                    q.append((num, steps + 1))

                    if num == end:
                        return steps + 1

        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends