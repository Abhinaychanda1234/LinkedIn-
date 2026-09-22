from typing import List


class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)

        # Each node:
        # [prod, cnt[0], cnt[1], ..., cnt[k-1]]
        #
        # prod = product of the whole segment modulo k
        # cnt[r] = number of non-empty prefixes with product % k == r

        size = 1
        while size < n:
            size <<= 1

        tree = [[0] * (k + 1) for _ in range(2 * size)]

        def make_node(value):
            value %= k

            node = [0] * (k + 1)
            node[0] = value
            node[value + 1] = 1
            return node

        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left

            res = [0] * (k + 1)

            # Product of the complete segment
            res[0] = (left[0] * right[0]) % k

            # Prefixes completely inside left
            for r in range(k):
                res[r + 1] += left[r + 1]

            # Prefixes that contain all of left
            # and then some prefix of right.
            for r in range(k):
                count = right[r + 1]

                new_r = (left[0] * r) % k
                res[new_r + 1] += count

            return res

        # Build leaves
        for i in range(n):
            tree[size + i] = make_node(nums[i])

        # Build tree
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[i << 1], tree[i << 1 | 1])

        def update(pos, value):
            idx = size + pos
            tree[idx] = make_node(value)

            idx >>= 1

            while idx:
                tree[idx] = merge(tree[idx << 1], tree[idx << 1 | 1])
                idx >>= 1

        def query(l, r):
            """
            Returns the segment information for [l, r).
            """

            left_res = None
            right_res = None

            l += size
            r += size

            while l < r:
                if l & 1:
                    left_res = merge(left_res, tree[l])
                    l += 1

                if r & 1:
                    r -= 1
                    right_res = merge(tree[r], right_res)

                l >>= 1
                r >>= 1

            return merge(left_res, right_res)

        ans = []

        for index, value, start, x in queries:

            # Persistent update
            update(index, value)

            # We need all non-empty prefixes of nums[start:]
            node = query(start, n)

            # cnt[x]
            ans.append(node[x + 1])

        return ans