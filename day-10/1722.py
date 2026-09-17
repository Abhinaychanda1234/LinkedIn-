from typing import List
from collections import Counter


class Solution:
    def minimumHammingDistance(
        self,
        source: List[int],
        target: List[int],
        allowedSwaps: List[List[int]]
    ) -> int:

        n = len(source)

        # DSU / Union-Find
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return

            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pa] > rank[pb]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa] += 1

        # Connect all indices that can be swapped
        for a, b in allowedSwaps:
            union(a, b)

        # Store source values for each component
        groups = {}

        for i in range(n):
            root = find(i)

            if root not in groups:
                groups[root] = []

            groups[root].append(i)

        answer = 0

        # Compare source and target inside each component
        for indices in groups.values():

            freq = Counter()

            for i in indices:
                freq[source[i]] += 1
                freq[target[i]] -= 1

            # Values that cannot be matched contribute to Hamming distance
            for count in freq.values():
                if count > 0:
                    answer += count

        return answer