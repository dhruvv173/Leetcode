from typing import List
class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        vis = [0] * V
        for i in range(V):
            if vis[i] == 0:
                if self.dfs(i, -1, vis, adj) == True:
                    return True
        return False

    def dfs(self, node, parent, vis, adj):
        vis[node] = 1
        for adjacentNode in adj[node]:
            if not vis[adjacentNode]:
                if self.dfs(adjacentNode, node, vis, adj) == True:
                    return True
            elif vis[adjacentNode] and adjacentNode != parent:
                return True
        return False



#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends