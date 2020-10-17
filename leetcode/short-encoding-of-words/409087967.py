# title: short-encoding-of-words
# detail: https://leetcode.com/submissions/detail/409087967/
# datetime: Thu Oct 15 23:32:57 2020
# runtime: 104 ms
# memory: 14.8 MB

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = collections.Counter(words)
        min_len = len(min(words, key=len))
        suffix = set()
        for w in words:
            for i in range(1, len(w) - min_len + 1):
                suffix.add(w[i:])
        return sum(len(w) + 1 for w in words if w not in suffix)
