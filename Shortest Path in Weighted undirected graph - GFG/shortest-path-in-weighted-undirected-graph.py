import heapq
class Solution:
    def shortestPath(self, n, m, edges):
        adj = [[] for _ in range(n+1)]
        minHeap = []
        dist = [float('inf')] * (n+1)
    
        for i in range(m):
            adj[edges[i][0]].append((edges[i][1], edges[i][2]))
            adj[edges[i][1]].append((edges[i][0], edges[i][2]))
    
        dist[1] = 0
        heapq.heappush(minHeap, (0, 1))
        parent = [-1] * (n+1)
    
        for i in range(1, n+1):
            parent[i] = i
    
        while minHeap:
            weight, node = heapq.heappop(minHeap)
    
            for it in adj[node]:
                adjNode, edW = it
    
                if dist[adjNode] > weight + edW:
                    dist[adjNode] = weight + edW
                    heapq.heappush(minHeap, (weight + edW, adjNode))
                    parent[adjNode] = node
    
        if dist[n] == float('inf'):
            return [-1]
    
        ans = []
        curr_node = n
        while parent[curr_node] != curr_node:
            ans.append(curr_node)
            curr_node = parent[curr_node]
    
        ans.append(1)
        ans.reverse()
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends