class Solution:
    def rotatedDigits(self, n: int) -> int:
        good = 0

        for num in range(1, n + 1):
            s = str(num)

            # Digits that cannot be rotated
            if any(d in "347" for d in s):
                continue

            # At least one digit must change
            if any(d in "2569" for d in s):
                good += 1

        return good