# title: check-if-a-string-contains-all-binary-codes-of-size-k
# detail: https://leetcode.com/submissions/detail/381694807/
# datetime: Sun Aug 16 19:38:35 2020
# runtime: 384 ms
# memory: 22.5 MB

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if k >= n:
            return False
        b = 0
        for i in range(k):
            b = (b << 1) | (1 if s[i] == '1' else 0)
        mask = (1 << k) - 1
        seen = [0] * (mask + 1)
        seen[b] = 1
        cnt = 1
        for i in range(i + 1, n):
            b = mask & ((b << 1) | (1 if s[i] == '1' else 0))
            if seen[b] == 0:
                seen[b] = 1
                cnt += 1
        return cnt == mask + 1
            