use normal BFS, no need for Dijkstra as the weights on edges are not given assume unit weights. Quadratic TC and SC ie O(N^2)
​
```
#implementation using a visited array (no diff in TC & SC)
class Solution:
def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
N = len(grid)
q = deque([(0, 0, 1)])
visited = [[0] * N for _ in range(N)]
direct = [[0, 1], [1, 0], [0, -1], [-1, 0],
[1, 1], [-1, -1], [1, -1], [-1, 1]]
while q:
r, c, length = q.popleft()
​
# Check if the current cell is out of bounds or a blocked cell
if r < 0 or c < 0 or r >= N or c >= N or grid[r][c] != 0 or visited[r][c] != 0:
continue
​
if r == N - 1 and c == N - 1:
return length
​
visited[r][c] = 1
​
for dr, dc in direct:
new_r, new_c = r + dr, c + dc
if 0 <= new_r < N and 0 <= new_c < N and visited[new_r][new_c] == 0:
q.append((new_r, new_c, length + 1))
visited[new_r][new_c] = 1
​
return -1
​
```