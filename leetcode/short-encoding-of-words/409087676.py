# title: short-encoding-of-words
# detail: https://leetcode.com/submissions/detail/409087676/
# datetime: Thu Oct 15 23:32:03 2020
# runtime: 100 ms
# memory: 14.9 MB

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = collections.Counter(words)
        min_len = len(min(words, key=len))
        suffix = set()
        for w in words:
            for i in range(1, len(w) - min_len + 1):
                suffix.add(w[i:])
        result = 0
        for w in words:
            if w in suffix:
                continue
            result += len(w) + 1
        return result