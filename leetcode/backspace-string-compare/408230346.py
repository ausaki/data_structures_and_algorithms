# title: backspace-string-compare
# detail: https://leetcode.com/submissions/detail/408230346/
# datetime: Tue Oct 13 21:28:50 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        s, t = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0 and (s > 0 or S[i] == '#'):
                s += (1 if S[i] == '#' else -1)
                i -= 1
            while j >= 0 and (t > 0 or T[j] == '#'):
                t += (1 if T[j] == '#' else -1)
                j -= 1
            if i < 0 and j < 0:
                break
            if i < 0 or j < 0 or S[i] != T[j]:
                return False
            i -= 1
            j -= 1
        return True