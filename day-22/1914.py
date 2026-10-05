from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):
            elements = []

            top = layer
            bottom = m - layer - 1
            left = layer
            right = n - layer - 1

            # Top row: left -> right
            for j in range(left, right + 1):
                elements.append(grid[top][j])

            # Right column: top+1 -> bottom
            for i in range(top + 1, bottom + 1):
                elements.append(grid[i][right])

            # Bottom row: right-1 -> left
            for j in range(right - 1, left - 1, -1):
                elements.append(grid[bottom][j])

            # Left column: bottom-1 -> top+1
            for i in range(bottom - 1, top, -1):
                elements.append(grid[i][left])

            # Counter-clockwise rotation = left rotation
            shift = k % len(elements)
            elements = elements[shift:] + elements[:shift]

            index = 0

            # Put back: Top row
            for j in range(left, right + 1):
                grid[top][j] = elements[index]
                index += 1

            # Right column
            for i in range(top + 1, bottom + 1):
                grid[i][right] = elements[index]
                index += 1

            # Bottom row
            for j in range(right - 1, left - 1, -1):
                grid[bottom][j] = elements[index]
                index += 1

            # Left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = elements[index]
                index += 1

        return grid