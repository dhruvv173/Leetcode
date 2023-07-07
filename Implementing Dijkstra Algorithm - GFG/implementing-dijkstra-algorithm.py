from heapq import heappop, heappush, heapify

class Solution:
    def dijkstra(self, V, adj, S):
        minHeap = []
        heapify(minHeap)
        dist = [float('inf')] * V
        
        dist[S] = 0
        heappush(minHeap, (0, S))
        
        while minHeap:
            dis, node = minHeap[0]
            heappop(minHeap)
            
            for it in adj[node]:
                v, w = it[0], it[1]
                if dis + w < dist[v]:
                    dist[v] = dis + w
                    heappush(minHeap, (dis + w, v))
                    
        return dist

            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends