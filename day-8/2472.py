class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # dp[i] = maximum number of valid palindromes
        # using the first i characters
        dp = [0] * (n + 1)

        # pal[l][r] = True if s[l:r+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if length == 1:
                    pal[l][r] = True
                elif length == 2:
                    pal[l][r] = s[l] == s[r]
                else:
                    pal[l][r] = s[l] == s[r] and pal[l + 1][r - 1]

        for i in range(1, n + 1):
            # Option 1: don't use a palindrome ending at i-1
            dp[i] = dp[i - 1]

            # Option 2: choose a palindrome ending at i-1
            for start in range(i - k + 1):
                if pal[start][i - 1]:
                    dp[i] = max(dp[i], dp[start] + 1)

        return dp[n]