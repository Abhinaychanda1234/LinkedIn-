from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        answer = n

        for i in range(n):
            if words[i] == target:
                distance = abs(i - startIndex)

                # Circular distance
                distance = min(distance, n - distance)

                answer = min(answer, distance)

        return -1 if answer == n else answer