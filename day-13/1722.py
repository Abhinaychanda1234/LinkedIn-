class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        directions = [
            (-1, 0),  # Up
            (0, 1),   # Right
            (1, 0),   # Down
            (0, -1)   # Left
        ]

        streets = {
            1: {1, 3},  # Right, Left
            2: {0, 2},  # Up, Down
            3: {3, 2},  # Left, Down
            4: {1, 2},  # Right, Down
            5: {3, 0},  # Left, Up
            6: {1, 0}   # Right, Up
        }

        visited = set()

        def dfs(r, c):
            # Destination reached
            if r == m - 1 and c == n - 1:
                return True

            visited.add((r, c))

            street = grid[r][c]

            for d in streets[street]:
                dr, dc = directions[d]

                nr = r + dr
                nc = c + dc

                # Check boundaries
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Don't visit again
                if (nr, nc) in visited:
                    continue

                # Check if neighboring street connects back
                opposite = (d + 2) % 4

                if opposite not in streets[grid[nr][nc]]:
                    continue

                if dfs(nr, nc):
                    return True

            return False

        return dfs(0, 0)