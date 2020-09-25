# title: compare-strings-by-frequency-of-the-smallest-character
# detail: https://leetcode.com/submissions/detail/396460615/
# datetime: Wed Sep 16 14:25:33 2020
# runtime: 112 ms
# memory: 14.3 MB

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        freqs = sorted(w.count(min(w)) for w in words)
        result = []
        for w in queries:
            cnt = w.count(min(w))
            i = bisect.bisect(freqs, cnt)
            result.append(len(freqs) - i)
        return result