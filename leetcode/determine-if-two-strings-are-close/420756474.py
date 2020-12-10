# title: determine-if-two-strings-are-close
# detail: https://leetcode.com/submissions/detail/420756474/
# datetime: Mon Nov 16 12:46:52 2020
# runtime: 124 ms
# memory: 14.8 MB

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        m, n = len(word1), len(word2)
        if m != n:
            return False
        w1, w2 = collections.Counter(word1), collections.Counter(word2)
        if len(w1) != len(w2) or sorted(w1) != sorted(w2):
            return False
        return sorted(w1.values()) == sorted(w2.values())