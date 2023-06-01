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


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends