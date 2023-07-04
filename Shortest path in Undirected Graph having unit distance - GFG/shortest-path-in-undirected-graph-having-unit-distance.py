#User function Template for python3
from collections import deque
class Solution:
    def shortestPath(self, edges, N, m, src):
        # code here
        # Create an adjacency list of size N for storing the undirected graph.
        adj = [[] for _ in range(N)]
        for it in edges:
            adj[it[0]].append(it[1])
            adj[it[1]].append(it[0])

        dist = [float('inf')] * N

        dist[src] = 0
        q = deque([src])
        while q:
            node = q.popleft()
            for it in adj[node]:
                if dist[node] + 1 < dist[it]:
                    dist[it] = 1 + dist[node]
                    q.append(it)

        # Updated shortest distances are stored in the resultant list 'ans'.
        # Unreachable nodes are marked as -1.
        # ans = [-1] * N
        for i in range(N):
            if dist[i] == float('inf'):
                dist[i] = -1

        return dist

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends