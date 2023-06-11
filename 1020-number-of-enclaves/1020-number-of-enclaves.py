class Solution:
    def numEnclaves(self, mat: List[List[int]]) -> int:
        n,m = len(mat), len(mat[0])
        vis = [[0] * m for _ in range(n)]
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]
        count = 0

        for j in range(m):
            if not vis[0][j] and mat[0][j] == 1:
                self.dfs(0, j, vis, mat, delrow, delcol)
            if not vis[n-1][j] and mat[n-1][j] == 1:
                self.dfs(n-1, j, vis, mat, delrow, delcol)

        for i in range(n):
            if not vis[i][0] and mat[i][0] == 1:
                self.dfs(i, 0, vis, mat, delrow, delcol)
            if not vis[i][m-1] and mat[i][m-1] == 1:
                self.dfs(i, m-1, vis, mat, delrow, delcol)

        for i in range(n):
            for j in range(m):
                if not vis[i][j] and mat[i][j] == 1:
                    count += 1

        return count 

    def dfs(self, row, col, vis, mat, delrow, delcol):
        vis[row][col] = 1
        n, m = len(mat), len(mat[0])
        for i in range(4):
            nrow = row + delrow[i]
            ncol = col + delcol[i]

            if (
                nrow >= 0
                and nrow < n
                and ncol >= 0
                and ncol < m
                and not vis[nrow][ncol]
                and mat[nrow][ncol] == 1
            ):
                self.dfs(nrow, ncol, vis, mat, delrow, delcol)