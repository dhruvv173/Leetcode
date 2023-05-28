class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        adjLs = [[] for _ in range(V)]

        for i in range(V):
            for j in range(V):
                if isConnected[i][j] ==  1 and i != j:
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