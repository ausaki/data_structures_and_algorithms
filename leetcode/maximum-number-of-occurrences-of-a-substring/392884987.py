# title: maximum-number-of-occurrences-of-a-substring
# detail: https://leetcode.com/submissions/detail/392884987/
# datetime: Wed Sep  9 01:11:39 2020
# runtime: 96 ms
# memory: 15.9 MB

class Solution:
    def maxFreq(self, s: str, maxLetters: int, k: int, maxSize: int) -> int:
        count = collections.Counter(s[i:i + k] for i in range(len(s) - k + 1))
        return max([count[w] for w in count if len(set(w)) <= maxLetters] + [0])
