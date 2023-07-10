class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0,0,1)])
        visit = set((0,0))
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0],
                  [1, 1], [-1, -1], [1, -1], [-1, 1]]
        while q:
            r, c, length = q.popleft()
            
            # Check if the current cell is out of bounds or a blocked cell
            if r < 0 or c < 0 or r >= N or c >= N or grid[r][c] != 0:
                continue
            
            if r == N - 1 and c == N - 1:
                return length
            
            for dr, dc in direct:
                new_r, new_c = r + dr, c + dc
                if (new_r, new_c) not in visit:
                    q.append((new_r, new_c, length + 1))
                    visit.add((new_r, new_c))
                    
        return -1