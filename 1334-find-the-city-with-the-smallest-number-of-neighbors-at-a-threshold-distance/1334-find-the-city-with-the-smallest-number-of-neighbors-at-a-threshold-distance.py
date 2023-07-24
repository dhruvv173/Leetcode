class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for i in range(n):
            dist[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] == float('inf') or dist[k][j] == float('inf'):
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        cntCity = n
        cityNo = -1
        for city in range(n):
            cnt = 0
            for adjCity in range(n):
                if dist[city][adjCity] <= distanceThreshold:
                    cnt += 1

            if cnt <= cntCity:
                cntCity = cnt
                cityNo = city
        return cityNo