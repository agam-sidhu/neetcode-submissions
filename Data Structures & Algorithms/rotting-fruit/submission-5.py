class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        freshFruit = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    freshFruit +=1
        while len(queue)>0 and freshFruit >0:
            for i in range(len(queue)):
                directions = [[0,1], [1,0],[-1,0], [0,-1]]
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if (nr >= rows or nr < 0 or nc < 0 or nc >= cols or grid[nr][nc] != 1):
                        continue
                    
                    grid[nr][nc] = 2
                    freshFruit-=1
                    queue.append((nr,nc))
            time +=1
        return -1 if freshFruit > 0 else time
        