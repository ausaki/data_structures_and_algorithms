# title: long-pressed-name
# detail: https://leetcode.com/submissions/detail/403977544/
# datetime: Sun Oct  4 00:23:21 2020
# runtime: 40 ms
# memory: 14 MB

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m, n = len(name), len(typed)
        i, j = 0, 0
        for i, c in enumerate(name):
            while j < n and typed[j] != c and j and typed[j] == typed[j - 1]:
                j += 1
            if j >= n or typed[j] != c:
                return False
            j += 1
        for i in range(j, n):
            if typed[i] != typed[j - 1]:
                return False
        return True