# title: uncommon-words-from-two-sentences
# detail: https://leetcode.com/submissions/detail/406049061/
# datetime: Thu Oct  8 15:04:44 2020
# runtime: 32 ms
# memory: 14 MB

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        return [k for k, v in collections.Counter(A.split() + B.split()).items() if v == 1]
        