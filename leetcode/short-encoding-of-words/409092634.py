# title: short-encoding-of-words
# detail: https://leetcode.com/submissions/detail/409092634/
# datetime: Thu Oct 15 23:48:21 2020
# runtime: 100 ms
# memory: 14.5 MB

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words2 = set(words)
        min_len = len(min(words2, key=len))
        for w in words:
            for i in range(1, len(w) - min_len + 1):
                words2.discard(w[i:])
        return sum(len(w) + 1 for w in words2)
