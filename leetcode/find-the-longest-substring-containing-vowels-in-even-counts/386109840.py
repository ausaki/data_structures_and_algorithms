# title: find-the-longest-substring-containing-vowels-in-even-counts
# detail: https://leetcode.com/submissions/detail/386109840/
# datetime: Tue Aug 25 18:19:03 2020
# runtime: 636 ms
# memory: 19.4 MB

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        m = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        dp = {0: -1}
        prefix = 0
        l = 0
        result = 0
        for i, c in enumerate(s):
            prefix ^= m.get(c, 0)
            result = max(result, i - dp.setdefault(prefix, i))
        return result