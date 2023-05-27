class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, node, adj, vis, dfs):
        vis[node] = 1
        dfs.append(node)
        # traverse all its neighbors
        for it in adj[node]:
            # if the neighbor is not visited
            if not vis[it]:
                self.dfs(it, adj, vis, dfs)

    def dfsOfGraph(self, V, adj):
        vis = [0] * V
        start = 0
        # create a list to store dfs
        dfs = []
        # call dfs for starting node
        self.dfs(start, adj, vis, dfs)
        return dfs

#Problem link
# https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1