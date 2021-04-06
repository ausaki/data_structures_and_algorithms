# title: sentence-similarity-iii
# detail: https://leetcode.com/submissions/detail/475920942/
# datetime: Sat Apr  3 22:45:12 2021
# runtime: 28 ms
# memory: 14.2 MB

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # if sentence1.startswith(sentence2) or sentence1.endswith(sentence2):
        #     return True
        # if sentence2.startswith(sentence1) or sentence2.endswith(sentence1):
        #     return True
        a = sentence1.split()
        b = sentence2.split()
        i = j = 0
        n, m = len(a), len(b)
        while i < n and j < m:
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                break
        ii, jj = n - 1, m - 1
        while ii >= i and jj >= j:
            if a[ii] == b[jj]:
                ii -= 1
                jj -= 1
            else:
                break
        return ii < i or jj < j