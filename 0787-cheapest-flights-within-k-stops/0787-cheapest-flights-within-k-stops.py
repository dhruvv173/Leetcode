class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for it in flights:
            adj[it[0]].append((it[1], it[2]))
        q = deque()
        q.append((0, src, 0))     #(stops, node, dist)
        dist = [float('inf')] * n

        while q:
            stops, node, cost = q.popleft()
            if stops > k:
                continue
            for iter in adj[node]:
                adjNode, edW = iter[0], iter[1]

                if cost + edW < dist[adjNode] and stops <= k:
                    dist[adjNode] = cost + edW
                    q.append((stops+1, adjNode, cost + edW))

        return -1 if dist[dst] == float("inf") else dist[dst]