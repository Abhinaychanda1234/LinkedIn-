class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            # Pattern is finished
            if j == len(p):
                return i == len(s)

            # Does current character match?
            first_match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == ".")
            )

            # Handle '*'
            if j + 1 < len(p) and p[j + 1] == "*":
                dp[(i, j)] = (
                    dfs(i, j + 2) or
                    (first_match and dfs(i + 1, j))
                )
                return dp[(i, j)]

            # Normal character / '.'
            dp[(i, j)] = (
                first_match and dfs(i + 1, j + 1)
            )

            return dp[(i, j)]

        return dfs(0, 0)