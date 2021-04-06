# title: sentence-similarity-iii
# detail: https://leetcode.com/submissions/detail/475960606/
# datetime: Sun Apr  4 00:04:53 2021
# runtime: 40 ms
# memory: 14.4 MB

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a = sentence1.split()
        b = sentence2.split()
        i = j = 0
        n, m = len(a), len(b)
        while i < n and j < m and a[i] == b[j]:
            i += 1
            j += 1
        ii, jj = n - 1, m - 1
        while ii >= i and jj >= j and a[ii] == b[jj]:
            ii -= 1
            jj -= 1
        return ii < i or jj < j