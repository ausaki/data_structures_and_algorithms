# title: merge-strings-alternately
# detail: https://leetcode.com/submissions/detail/458603435/
# datetime: Sun Feb 21 10:33:16 2021
# runtime: 28 ms
# memory: 14.1 MB

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join((a if a else '') + (b if b else '') for a, b in itertools.zip_longest(word1, word2))