class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def isValid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        result = []
        queue = [s]
        visited = {s}

        found = False

        while queue:

            for _ in range(len(queue)):
                current = queue.pop(0)

                # If valid, this is the minimum-removal level
                if isValid(current):
                    result.append(current)
                    found = True

                # Don't generate deeper levels after finding answers
                if found:
                    continue

                # Remove one parenthesis
                for i in range(len(current)):
                    if current[i] not in "()":
                        continue

                    next_string = current[:i] + current[i + 1:]

                    if next_string not in visited:
                        visited.add(next_string)
                        queue.append(next_string)

            if found:
                break

        return result