#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        adjLs = [[] for _ in range(V)]
        
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 and i != j:
                    adjLs[i].append(j)
                    adjLs[j].append(i)
                    
        vis = [0] * V
        count = 0
        for i in range(V):
            if not vis[i]:
                count += 1
                self.dfs(i, adjLs, vis)
                
        return count
        
    def dfs(self, node, adjLs, vis):
        vis[node] = 1
        for neighbor in adjLs[node]:
            if not vis[neighbor]:
                self.dfs(neighbor, adjLs, vis)
 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends