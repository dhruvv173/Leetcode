#User function Template for python3
class Solution:
    #TC- V+E
    #SC- 2n cus using 2 arrays vis and pathVis
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        vis = [0] * V
        pathVis = [0] * V
        for i in range(V):
            if not vis[i]:
                if self.dfs(i, adj, vis, pathVis):
                    return True
        return False
        
    def dfs(self, node, adj, vis, pathVis):
        vis[node] = 1
        pathVis[node] = 1
        #traverse the adjacent nodes
        for it in adj[node]:
            #when the node is not visited
            if not vis[it]:
                if self.dfs(it, adj, vis, pathVis):
                    return True
        
            # if the node is visited
            # but also path visited
            elif pathVis[it]:
                return True
        pathVis[node] = 0
        return False
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends