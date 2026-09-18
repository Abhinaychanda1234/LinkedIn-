from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        result = []

        for query in queries:

            for word in dictionary:

                differences = 0

                for i in range(len(query)):
                    if query[i] != word[i]:
                        differences += 1

                    # More than 2 edits is already invalid
                    if differences > 2:
                        break

                if differences <= 2:
                    result.append(query)
                    break

        return result