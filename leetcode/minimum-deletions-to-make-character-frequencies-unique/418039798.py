# title: minimum-deletions-to-make-character-frequencies-unique
# detail: https://leetcode.com/submissions/detail/418039798/
# datetime: Sun Nov  8 17:00:19 2020
# runtime: 112 ms
# memory: 14.6 MB

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = collections.Counter(s)
        freqs = sorted(cnt.values())
        d = 0
        last = freqs[-1]
        for i in range(len(freqs) - 2, -1, -1):
            if freqs[i] >= last:
                last = max(last - 1, 0)
                d += freqs[i] - last
            else:
                last = freqs[i]                
        return d
        