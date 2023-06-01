#GFG
from collections import deque
class Solution:
    # Function to find the distance of the nearest 1 in the grid for each cell.
    def nearest(self, grid):
        n, m = len(grid), len(grid[0])
        vis = [[0] * m for _ in range(n)]
        dist = [[0] * m for _ in range(n)]
        q = deque()

        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
                    vis[i][j] = 1
                else:
                    vis[i][j] = 0

        while q:
            row, col, steps = q.popleft()
            dist[row][col] = steps

            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]

                if (
                    nrow >= 0
                    and nrow < n
                    and ncol >= 0
                    and ncol < m
                    and vis[nrow][ncol] == 0
                ):
                    vis[nrow][ncol] = 1
                    q.append((nrow, ncol, steps + 1))

        return dist


#Leetcode
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        queue = deque()
        visited = [[0] * m for _ in range(n)]
        distance = [[0] * m for _ in range(n)]

        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited[i][j] = 1
                else:
                    visited[i][j] = 0
        while queue:
            row, col, steps = queue.popleft()
            distance[row][col] = steps
            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]
                if (
                    nrow >= 0 
                    and nrow < n 
                    and ncol >= 0 
                    and ncol < m 
                    and visited[nrow][ncol] == 0
                    ):
                    queue.append((nrow, ncol, steps + 1))
                    visited[nrow][ncol] = 1
        return distance
