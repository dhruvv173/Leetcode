#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        maxi = 100000000
        dist = [maxi] * V
        dist[S] = 0
        
        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] != maxi and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
          # Check for negative weight cycles.
        for u, v, w in edges:
            if dist[u] != maxi and dist[u] + w < dist[v]:
                return [-1]
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
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends