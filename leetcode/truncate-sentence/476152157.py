# title: truncate-sentence
# detail: https://leetcode.com/submissions/detail/476152157/
# datetime: Sun Apr  4 10:31:11 2021
# runtime: 28 ms
# memory: 14.3 MB

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])