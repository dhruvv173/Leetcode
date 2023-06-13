class Solution:
    
    #Function to return list containing vertices in Topological order.
    #SC - O(n) + O(n) -> stack + vis array
    #TC - V + E for directed graph 
    def topoSort(self, V, adj):
        # Code here
        vis = [0] * V
        stack = []
        for i in range(V):
            if not vis[i]:
                self.dfs(i, vis, stack, adj)
                
        res = []
        while stack:
            res.append(stack[-1])
            stack.pop()
        return res
        
    def dfs(self, node, vis, stack, adj):
        vis[node] = 1
        for it in adj[node]:
            if not vis[it]:
                self.dfs(it, vis, stack, adj)
        stack.append(node)


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends