class Solution:
    def eventualSafeNodes(self, adj: List[List[int]]) -> List[int]:
        V = len(adj)
        vis = [0] * V
        pathVis = [0] * V
        safeNodes = []
        check = [0] * V
        for i in range(V):
            if not vis[i]:
                self.dfs(i, adj, vis, pathVis, check)
        # for i in range(V):
        #     if check[i]:
        #         safeNodes.append(i)
        # return safeNodes
        return [i for i in range(V) if check[i]] #can also do this to save space


    def dfs(self, node, adj, vis, pathVis, check):
        vis[node] = 1
        pathVis[node] = 1
        #traverse the adjacent nodes
        for it in adj[node]:
            #when the node is not visited
            if not vis[it]:
                if self.dfs(it, adj, vis, pathVis, check):
                    check[node] = 0
                    return True
        
            # if the node is visited
            # but also path visited
            elif pathVis[it]:
                check[node] = 0
                return True
        check[node] = 1
        pathVis[node] = 0
        return False