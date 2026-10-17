class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        visited = set()
        maxArea = 0
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            area = 0
            while queue:
                (r,c) = queue.popleft()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                area+=1
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, bfs(r,c))       
        return maxArea
