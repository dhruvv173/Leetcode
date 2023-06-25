#User function Template for python3
from typing import List

class Solution:
    def topoSort(self, node, adj, vis, st):
        # This is the function to implement Topological sort.
        vis[node] = 1
        for it in adj[node]:
            v = it[0]
            if not vis[v]:
                self.topoSort(v, adj, vis, st)
        st.append(node)

    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for i in range(m):
            u = edges[i][0]
            v = edges[i][1]
            wt = edges[i][2]
            adj[u].append((v, wt))
        # A visited array is created with initially
        # all the nodes marked as unvisited (0).
        vis = [0] * n
        # Now, we perform topo sort using DFS technique
        # and store the result in the stack st.
        st = []
        for i in range(n):
            if not vis[i]:
                self.topoSort(i, adj, vis, st)
                
        dist = [float('inf')] * n
        dist[0] = 0
        while st:
            node = st.pop()
            for it in adj[node]:
                v, wt = it[0], it[1]
                if dist[node] + wt < dist[v]:
                    dist[v] = dist[node] + wt
        
        # Replace infinity with -1 for unreachable nodes
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
        
        return dist


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends