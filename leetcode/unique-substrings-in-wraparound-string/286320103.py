# title: unique-substrings-in-wraparound-string
# detail: https://leetcode.com/submissions/detail/286320103/
# datetime: Mon Dec 16 14:13:18 2019
# runtime: 88 ms
# memory: 12.8 MB

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        N = len(p)
        p += 'X'
        i = 0
        j = 0
        counter = collections.Counter()
        while j < N:
            if j - i + 1 > counter[p[j]]:
                counter[p[j]] = j - i + 1
            if (ord(p[j + 1]) - ord(p[j])) % 26 != 1:
                i = j + 1
            j += 1
        return sum(counter.values())