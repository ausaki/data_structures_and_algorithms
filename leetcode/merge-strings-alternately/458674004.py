# title: merge-strings-alternately
# detail: https://leetcode.com/submissions/detail/458674004/
# datetime: Sun Feb 21 12:53:15 2021
# runtime: 28 ms
# memory: 14.1 MB

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n, m = len(word1), len(word2)
        for i in range(min(n, m)):
            res.append(word1[i])
            res.append(word2[i])
        return ''.join(res) + word1[min(n, m):] + word2[min(n, m):]