# title: unique-substrings-in-wraparound-string
# detail: https://leetcode.com/submissions/detail/286313717/
# datetime: Mon Dec 16 13:43:45 2019
# runtime: 92 ms
# memory: 12.8 MB

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        res = {i: 1 for i in p}
        l = 1
        for i, j in zip(p, p[1:]):
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], l)
        return sum(res.values())