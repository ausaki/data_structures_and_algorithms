# title: unique-substrings-in-wraparound-string
# detail: https://leetcode.com/submissions/detail/286315227/
# datetime: Mon Dec 16 13:51:07 2019
# runtime: 64 ms
# memory: 12.8 MB

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        p += 'X'
        N = len(p)
        i = 0
        j = 1
        res = 0
        mapping = collections.Counter()
        while j < N:
            if (ord(p[j]) - ord(p[j - 1])) % 26 == 1:
                j += 1
            else:
                for k in range(i, j):
                    if j - k > mapping[p[k]]:
                        mapping[p[k]] = j - k
                    else:
                        break
                i = j
                j = i + 1
        return sum(mapping.values())