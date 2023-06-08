from collections import deque
#Intuition: Brute Force BFS
class Solution:
    def check(self, start, V, adj, color):
        q = deque()
        q.append(start)
        color[start] = 0
        while q:
            node = q.popleft()
            
            for it in adj[node]:
                if color[it] == -1:
                    color[it] = 1 - color[node]
                    q.append(it)
                elif color[it] == color[node]:
                    return False
        return True
    
    def isBipartite(self, V, adj):
        color = [-1] * V
        
        for i in range(V):
            if color[i] == -1:
                if not self.check(i, V, adj, color):
                    return False
        return True


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