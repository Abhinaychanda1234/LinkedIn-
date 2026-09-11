from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = [0] * 10

        # Count how many copies of each digit we have
        for digit in digits:
            count[digit] += 1

        result = 0

        # Choose hundreds digit
        for a in range(1, 10):
            if count[a] == 0:
                continue

            count[a] -= 1

            # Choose tens digit
            for b in range(10):
                if count[b] == 0:
                    continue

                count[b] -= 1

                # Choose units digit (must be even)
                for c in range(0, 10, 2):
                    if count[c] > 0:
                        result += 1

                count[b] += 1

            count[a] += 1

        return result