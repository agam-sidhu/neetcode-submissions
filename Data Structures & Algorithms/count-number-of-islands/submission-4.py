class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                directions = [[1,0], [0,1], [-1,0], [0, -1]]
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if (nr in range(rows)) and nc in range(cols) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands

                        
                
            
            
        