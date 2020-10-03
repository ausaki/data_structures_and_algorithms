# title: verifying-an-alien-dictionary
# detail: https://leetcode.com/submissions/detail/403029771/
# datetime: Thu Oct  1 15:50:49 2020
# runtime: 36 ms
# memory: 14.1 MB

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx = {c: i for i, c in enumerate(order )}
        for i in range(len(words) - 1):
            if list(map(idx.__getitem__, words[i])) > list(map(idx.__getitem__, words[i + 1])):
                return False
        return True