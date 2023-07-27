import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        visited = [False] * n
        pq = [(0, points[0][0], points[0][1], 0)]
        while pq:
            dist, x1, y1, idx = heapq.heappop(pq)
            if visited[idx]:
                continue
            visited[idx] = True
            res += dist
            for i in range(n):
                if not visited[i]:
                    x2, y2 = points[i]
                    heapq.heappush(pq, (abs(x1 - x2) + abs(y1 - y2), x2, y2, i))
            
        return res
