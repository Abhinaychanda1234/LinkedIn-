class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)

        # best[i] = minimum length of a target-sum subarray
        # completely inside arr[0:i]
        best = [float('inf')] * (n + 1)

        left = 0
        curr_sum = 0
        answer = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            # Shrink window if sum is too large
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # We found a subarray [left, right]
            if curr_sum == target:
                length = right - left + 1

                # best[left] contains the shortest target-sum
                # subarray ending before 'left'
                if best[left] != float('inf'):
                    answer = min(answer, length + best[left])

                # Store this subarray as the best one
                # ending before future positions
                best[right + 1] = min(best[right + 1], length)

            # Carry forward the best previous subarray
            best[right + 1] = min(best[right + 1], best[right])

        return -1 if answer == float('inf') else answer