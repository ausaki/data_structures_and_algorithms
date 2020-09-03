# title: can-convert-string-in-k-moves
# detail: https://leetcode.com/submissions/detail/379399227/
# datetime: Tue Aug 11 23:09:41 2020
# runtime: 628 ms
# memory: 15.2 MB

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
            moves = max(moves, sh + 26 * shifts[sh])
            shifts[sh] += 1
        return moves <= k
        