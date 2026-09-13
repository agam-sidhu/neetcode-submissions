class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1, 0]]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc>= cols or grid[nr][nc] != 1:
                        continue
                    fresh-=1
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    
            time +=1
        return time if fresh ==0 else -1
                    
        