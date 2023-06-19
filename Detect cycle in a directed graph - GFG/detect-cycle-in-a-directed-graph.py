#User function Template for python3
from collections import deque
class Solution:
    def isCyclic(self,V, adj):
        #Kahns algorithm
        # Code here
        q = deque()
        indegree = [0] * V
        for i in range(V):
            for it in adj[i]:
                indegree[it] += 1
        for i in range(V):
            if not indegree[i]:
                q.append(i)
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for it in adj[node]:
                indegree[it] -= 1
                if not indegree[it]:
                    q.append(it)
                    
        return count != V
    
    
    
    # DFS
    #TC- V+E
    #SC- 2n cus using 2 arrays vis and pathVis
    #Function to detect cycle in a directed graph.
    # def isCyclic(self, V, adj):
    #     # code here
    #     vis = [0] * V
    #     pathVis = [0] * V
    #     for i in range(V):
    #         if not vis[i]:
    #             if self.dfs(i, adj, vis, pathVis):
    #                 return True
    #     return False
        
    # def dfs(self, node, adj, vis, pathVis):
    #     vis[node] = 1
    #     pathVis[node] = 1
    #     #traverse the adjacent nodes
    #     for it in adj[node]:
    #         #when the node is not visited
    #         if not vis[it]:
    #             if self.dfs(it, adj, vis, pathVis):
    #                 return True
        
    #         # if the node is visited
    #         # but also path visited
    #         elif pathVis[it]:
    #             return True
    #     pathVis[node] = 0
    #     return False
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