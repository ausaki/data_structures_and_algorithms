# title: count-unique-characters-of-all-substrings-of-a-given-string
# detail: https://leetcode.com/submissions/detail/408992841/
# datetime: Thu Oct 15 16:35:10 2020
# runtime: 80 ms
# memory: 14.4 MB

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        idx = collections.defaultdict(lambda: [-1, -1])
        result = 0
        for i, c in enumerate(s):
            j, k = idx[c]
            result = (result + (k - j) * (i - k)) % MOD
            idx[c][:] = k, i
        for j, k in idx.values():
            result = (result + (k - j) * (len(s) - k)) % MOD
        return result