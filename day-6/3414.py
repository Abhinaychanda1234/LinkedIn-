from typing import List
from bisect import bisect_right


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Store:
        # [left, right, weight, original_index]
        arr = []

        for i, interval in enumerate(intervals):
            l, r, w = interval
            arr.append((l, r, w, i))

        # Sort by starting position
        arr.sort()

        starts = [x[0] for x in arr]

        # Find the first interval that does NOT overlap
        #
        # Current interval ends at r.
        # Next interval must have left > r.
        next_idx = [0] * n

        for i in range(n):
            next_idx[i] = bisect_right(starts, arr[i][1])

        # dp[k][i]
        #
        # = best result when we can select at most k intervals
        #   from interval i onwards.
        #
        # Each state contains:
        # (score, tuple_of_original_indices)
        dp = [[None] * (n + 1) for _ in range(5)]

        # Base case:
        # If we are allowed to select 0 intervals,
        # answer is always score 0 and empty list.
        for i in range(n + 1):
            dp[0][i] = (0, ())

        # Base case:
        # If there are no intervals left,
        # answer is score 0 and empty list for any k.
        for k in range(1, 5):
            dp[k][n] = (0, ())

        def better(a, b):
            """
            Choose the better result.

            1. Higher score wins.
            2. If scores are equal, lexicographically smaller
               index array wins.
            """
            if a[0] > b[0]:
                return a

            if a[0] < b[0]:
                return b

            if a[1] < b[1]:
                return a

            return b

        # Fill DP from right to left
        for k in range(1, 5):

            for i in range(n - 1, -1, -1):

                # Option 1: Skip current interval
                skip = dp[k][i + 1]

                # Option 2: Take current interval
                j = next_idx[i]

                future = dp[k - 1][j]

                current_index = arr[i][3]
                current_weight = arr[i][2]

                # Add current index and keep indices sorted
                selected_indices = tuple(
                    sorted((current_index,) + future[1])
                )

                take = (
                    current_weight + future[0],
                    selected_indices
                )

                # Pick the better option
                dp[k][i] = better(skip, take)

        return list(dp[4][0][1])