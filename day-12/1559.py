class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, parent_r, parent_c):
            visited[r][c] = True

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Out of bounds
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Different character
                if grid[nr][nc] != grid[r][c]:
                    continue

                # This is the cell we came from.
                if nr == parent_r and nc == parent_c:
                    continue

                # Already visited and not parent -> cycle
                if visited[nr][nc]:
                    return True

                # Continue DFS
                if dfs(nr, nc, r, c):
                    return True

            return False

        for r in range(m):
            for c in range(n):
                if not visited[r][c]:
                    if dfs(r, c, -1, -1):
                        return True

        return False