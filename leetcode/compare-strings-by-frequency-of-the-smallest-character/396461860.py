# title: compare-strings-by-frequency-of-the-smallest-character
# detail: https://leetcode.com/submissions/detail/396461860/
# datetime: Wed Sep 16 14:28:35 2020
# runtime: 136 ms
# memory: 14.4 MB

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        freqs = sorted(w.count(min(w)) for w in words)
        return (len(freqs) - bisect.bisect(freqs, w.count(min(w))) for w in queries)
