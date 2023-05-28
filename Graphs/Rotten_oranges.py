class Solution:
    def orangesRotting(self, grid):
        ROWS = len(grid)
        COLS = len(grid[0])

        q = []
        vis = [[0] * COLS for _ in range(ROWS)]
        cntFresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append(((i, j), 0))
                    vis[i][j] = 2
                else:
                    vis[i][j] = 0
                if grid[i][j] == 1:
                    cntFresh += 1

        tm = 0
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        cnt = 0

        while q:
            r, c = q[0][0]
            t = q[0][1]
            tm = max(tm, t)
            q.pop(0)

            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                if (
                    nrow >= 0
                    and nrow < ROWS
                    and ncol >= 0
                    and ncol < COLS
                    and vis[nrow][ncol] == 0
                    and grid[nrow][ncol] == 1
                ):
                    q.append(((nrow, ncol), t + 1))
                    vis[nrow][ncol] = 2
                    cnt += 1
        if cnt != cntFresh:
            return -1

        return tm