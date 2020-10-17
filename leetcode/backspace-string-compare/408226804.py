# title: backspace-string-compare
# detail: https://leetcode.com/submissions/detail/408226804/
# datetime: Tue Oct 13 21:14:46 2020
# runtime: 28 ms
# memory: 14.1 MB

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        s, t = 0, 0
        while i >= 0 or j >= 0:
            if i >= 0 and S[i] == '#':
                s += 1
                i -= 1
                continue
            if s > 0:
                s -= 1
                i = max(-1, i - 1)
                continue
            if j >= 0 and T[j] == '#':
                t += 1
                j -= 1
                continue
            if t > 0:
                t -= 1
                j = max(-1, j - 1)
                continue
            if i < 0 or j < 0 or S[i] != T[j]:
                return False
            i -= 1
            j -= 1
        return True