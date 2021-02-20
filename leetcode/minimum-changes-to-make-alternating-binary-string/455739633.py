# title: minimum-changes-to-make-alternating-binary-string
# detail: https://leetcode.com/submissions/detail/455739633/
# datetime: Sun Feb 14 10:34:41 2021
# runtime: 64 ms
# memory: 14.4 MB

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        prev = s[0]
        m = 0
        for i in range(1, n):
            if s[i] != prev:
                prev = s[i]
            else:
                m += 1
                prev = '0' if prev == '1' else '1'
        prev = '0' if s[0] == '1' else '1'
        k = 1
        for i in range(1, n):
            if s[i] != prev:
                prev = s[i]
            else:
                k += 1
                prev = '0' if prev == '1' else '1'
        return min(m, k)
        