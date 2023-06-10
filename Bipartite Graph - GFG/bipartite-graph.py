from collections import deque
class Solution:
    # def check(self, start, V, adj, color):
    #Intuition: Brute Force BFS
    #     q = deque()
    #     q.append(start)
    #     color[start] = 0
    #     while q:
    #         node = q.popleft()
            
    #         for it in adj[node]:
    #             if color[it] == -1:
    #                 color[it] = 1 - color[node]
    #                 q.append(it)
    #             elif color[it] == color[node]:
    #                 return False
    #     return True
    
    # def isBipartite(self, V, adj):
    #     color = [-1] * V
        
    #     for i in range(V):
    #         if color[i] == -1:
    #             if not self.check(i, V, adj, color):
    #                 return False
    #     return True


    #DFS
    def isBipartite(self, V, adj):
        color = [-1] * V  # Initialize color array as unvisited nodes
        for i in range(V):  # Iterate through each node
            if color[i] == -1:  # If node is unvisited
                color[i] = 1  # Assign color 1
                if not self.dfs(i, adj, color):  # Call DFS on node and adjacent nodes
                    return False  # Return False if graph is not bipartite
        return True  # Return True if graph is bipartite
    
    def dfs(self, node, adj, color):
        for it in adj[node]:  # Iterate through adjacent nodes
            if color[it] == -1:  # If adjacent node is unvisited
                color[it] = 1 - color[node]  # Assign opposite color of current node
                if not self.dfs(it, adj, color):  # Call DFS on adjacent node
                    return False  # Return False if graph is not bipartite
            elif color[it] == color[node]:  # If adjacent node has same color as current node
                return False  # Return False if graph is not bipartite
        return True  # Return True if graph is bipartite

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends