from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        ans = 0

        while i < len(nums1) and j < len(nums2):
            if i > j:
                j = i

            if j < len(nums2) and nums1[i] <= nums2[j]:
                # Valid pair
                ans = max(ans, j - i)
                j += 1
            else:
                # nums1[i] is too large, move i
                i += 1

        return ans