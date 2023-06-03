#User function Template for python3

class Solution:
    def fill(self, n,m,mat):
        """
        Do not return anything, modify board in-place instead.
        """
        vis = [[0] * m for _ in range(n)]
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]

        # Loop through the columns of the first row
        for j in range(m):
            if not vis[0][j] and mat[0][j] == 'O':
                self.dfs(0, j, vis, mat, delrow, delcol)

            # Check the bottom row for 'O' cells
            if not vis[n-1][j] and mat[n-1][j] == 'O':
                self.dfs(n-1, j, vis, mat, delrow, delcol)

        # Loop through the rows of the matrix
        for i in range(n):
            # Check the leftmost column for 'O' cells
            if not vis[i][0] and mat[i][0] == 'O':
                self.dfs(i, 0, vis, mat, delrow, delcol)

            # Check the rightmost column for 'O' cells
            if not vis[i][m-1] and mat[i][m-1] == 'O':
                self.dfs(i, m-1, vis, mat, delrow, delcol)
        
        # Loop through the entire matrix
        for i in range(n):
            for j in range(m):
                # Convert unvisited 'O' cells to 'X'
                if not vis[i][j] and mat[i][j] == 'O':
                    mat[i][j] = 'X'

        return mat


    def dfs(self, row, col, vis, mat, delrow, delcol):
        vis[row][col] = 1
        n, m = len(mat), len(mat[0])
        for i in range(4):
            nrow = row + delrow[i]
            ncol = col + delcol[i]

            # Perform DFS on adjacent 'O' cells
            if (
                nrow >= 0
                and nrow < n
                and ncol >= 0
                and ncol < m
                and not vis[nrow][ncol]
                and mat[nrow][ncol] == 'O'
            ):
                self.dfs(nrow, ncol, vis, mat, delrow, delcol)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends