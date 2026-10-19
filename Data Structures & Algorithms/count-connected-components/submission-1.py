class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for a , b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
            
        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        num_comp = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                num_comp+=1
        return num_comp

        