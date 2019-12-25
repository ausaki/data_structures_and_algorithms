# title: unique-substrings-in-wraparound-string
# detail: https://leetcode.com/submissions/detail/286313288/
# datetime: Mon Dec 16 13:41:46 2019
# runtime: 76 ms
# memory: 12.7 MB

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        p += 'X'
        N = len(p)
        i = 0
        j = 1
        res = 0
        mapping = collections.Counter()
        while j < N:
            if ord(p[j]) - ord('a') == (ord(p[j - 1]) - ord('a') + 1) % 26:
                j += 1
            else:
                if j - i > mapping[p[i]]:
                    for k in range(i, j):
                        if j - k > mapping[p[k]]:
                            mapping[p[k]] = j - k
                        else:
                            break
                i = j
                j = i + 1
        return sum(mapping.values())