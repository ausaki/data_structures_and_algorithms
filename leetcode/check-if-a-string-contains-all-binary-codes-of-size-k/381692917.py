# title: check-if-a-string-contains-all-binary-codes-of-size-k
# detail: https://leetcode.com/submissions/detail/381692917/
# datetime: Sun Aug 16 19:30:43 2020
# runtime: 396 ms
# memory: 23.2 MB

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if k >= n:
            return False
        b = 0
        for i in range(k):
            b = (b << 1) | (1 if s[i] == '1' else 0)
        mask = (1 << k) - 1
        seen = {b}
        for i in range(i + 1, n):
            b = mask & ((b << 1) | (1 if s[i] == '1' else 0))
            seen.add(b)
        return len(seen) == mask + 1
            