class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:

        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Try creating the smallest valid interval
        # for every character
        for c in range(26):

            if last[c] == -1:
                continue

            l = first[c]
            r = last[c]

            i = l
            valid = True

            while i <= r:
                x = ord(s[i]) - ord('a')

                # This character appeared before l,
                # so we cannot create a valid substring
                # starting at l.
                if first[x] < l:
                    valid = False
                    break

                # We must include all occurrences of x
                r = max(r, last[x])

                i += 1

            if valid:
                intervals.append((l, r))

        # Greedy: choose intervals with earliest ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for l, r in intervals:

            if l > prev_end:
                result.append(s[l:r + 1])
                prev_end = r

        return result