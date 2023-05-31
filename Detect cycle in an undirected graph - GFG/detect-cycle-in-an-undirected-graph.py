from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
    #Cycle detection usig BFS
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis = [0] * V
		for i in range(V):
		    if not vis[i]:
		        if self.detect(i, adj, vis):
		            return True
		return False
    
    def detect(self, src, adj, vis):
        vis[src] = 1
        queue = deque([(src, -1)])
        while queue:
            node = queue[0][0]
            parent = queue[0][1]
            queue.popleft()
            
            for adjacentNode in adj[node]:
                if not vis[adjacentNode]:
                    vis[adjacentNode] = 1
                    queue.append((adjacentNode, node))
                elif parent != adjacentNode:
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