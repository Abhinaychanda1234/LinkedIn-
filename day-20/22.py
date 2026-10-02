class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, open_count, close_count):
            # A complete valid combination
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we haven't used all n opening brackets
            if open_count < n:
                backtrack(
                    current + "(",
                    open_count + 1,
                    close_count
                )

            # Add ')' only when it won't make the string invalid
            if close_count < open_count:
                backtrack(
                    current + ")",
                    open_count,
                    close_count + 1
                )

        backtrack("", 0, 0)

        return result