# title: can-convert-string-in-k-moves
# detail: https://leetcode.com/submissions/detail/379400355/
# datetime: Tue Aug 11 23:12:30 2020
# runtime: 700 ms
# memory: 15 MB

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        m = len(t)
        if n != m: return False
        shifts = {}
        moves = 0
        for i in range(n):
            if t[i] == s[i]: continue
            sh = (ord(t[i]) - ord(s[i]) + 26) % 26
            if sh not in shifts:
                shifts[sh] = 0
            shifts[sh] += 1
            moves = max(moves, sh + 26 * (shifts[sh] - 1))
            if moves > k:
                return False
        return True
        