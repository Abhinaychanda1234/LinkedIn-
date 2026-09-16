from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        if colors[0] != colors[-1]:
            return n - 1

        left = 1
        while colors[left] == colors[0]:
            left += 1

        right = n - 2
        while colors[right] == colors[-1]:
            right -= 1

        return max(n - 1 - left, right)