from typing import List


class Solution:

    def minMirrorPairDistance(self, nums: List[int]) -> int:

        last = {}
        ans = float('inf')

        for j, x in enumerate(nums):

            # If reverse(nums[i]) == x,
            # then nums[i] is the value we need.
            if x in last:
                ans = min(ans, j - last[x])

            # Store reverse(x) for future indices
            rev = int(str(x)[::-1])
            last[rev] = j

        return -1 if ans == float('inf') else ans