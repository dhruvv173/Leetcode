#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, row, col, vis, grid, vec, start_row, start_col):
        # Mark the cell as visited
        vis[row][col] = 1
        
        # Calculate the relative coordinates
        vec.append((row - start_row, col - start_col))
        
        n = len(grid)
        m = len(grid[0])
        
        # Delta row and delta column
        delrow = [-1, 0, 1, 0]
        delcol = [0, -1, 0, 1]
        
        # Traverse all 4 neighbors
        for i in range(4):
            next_row = row + delrow[i]
            next_col = col + delcol[i]
            
            # Check for valid unvisited land neighbor coordinates
            if (
                next_row >= 0 
                and next_row < n 
                and next_col >= 0 
                and next_col < m 
                and not vis[next_row][next_col] 
                and grid[next_row][next_col] == 1
                ):
                self.dfs(next_row, next_col, vis, grid, vec, start_row, start_col)
    
    def countDistinctIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        vis = [[0] * m for _ in range(n)]
        st = set()
        
        # Traverse the grid
        for i in range(n):
            for j in range(m):
                # If not visited and is a land cell
                if not vis[i][j] and grid[i][j] == 1:
                    vec = []
                    self.dfs(i, j, vis, grid, vec, i, j)
                    
                    # Store in set
                    st.add(tuple(vec))
        
        return len(st)



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
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends