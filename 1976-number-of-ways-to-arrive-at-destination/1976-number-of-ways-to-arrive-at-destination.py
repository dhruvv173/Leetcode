class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for it in roads:
            adj[it[0]].append((it[1], it[2]))
            adj[it[1]].append((it[0], it[2]))
        minHeap = []
        heapify(minHeap)
        MOD = 10 ** 9 + 7
        dist, ways = [float('inf')] * n, [0] * n
        dist[0] = 0
        ways[0] = 1
        heappush(minHeap, (0,0))

        while minHeap:
            dis, node = heappop(minHeap)

            for adjNode, edW in adj[node]:
                if dis + edW < dist[adjNode]:
                    dist[adjNode] = dis + edW
                    heappush(minHeap, (dis + edW, adjNode))
                    ways[adjNode] = ways[node]
                elif dis+ edW == dist[adjNode]:
                    ways[adjNode] = (ways[adjNode] + ways[node]) % MOD

        return ways[n-1] % MOD