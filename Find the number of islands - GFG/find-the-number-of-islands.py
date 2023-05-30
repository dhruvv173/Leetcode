#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
from collections import deque
class Solution:
    def numIslands(self, grid):
        n, m = len(grid), len(grid[0])
        count = 0
        vis = [[0] * m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                if not vis[row][col] and grid[row][col] == 1:
                    self.bfs(row, col, vis, grid)
                    count += 1
        return count

    def bfs(self, row, col, vis, grid):
        vis[row][col] = 1
        queue = deque([(row, col)])
        n, m = len(grid), len(grid[0])

        while queue:
            row, col = queue.popleft()
            for del_row in [-1, 0, 1]:
                for del_col in [-1, 0, 1]:
                    nrow = row + del_row
                    ncol = col + del_col
                    if (
                        nrow >= 0
                        and nrow < n
                        and ncol >= 0
                        and ncol < m
                        and grid[nrow][ncol] == 1
                        and not vis[nrow][ncol]
                    ):
                        vis[nrow][ncol] = 1
                        queue.append((nrow, ncol))



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends