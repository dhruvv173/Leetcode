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