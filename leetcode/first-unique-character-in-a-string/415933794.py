# title: first-unique-character-in-a-string
# detail: https://leetcode.com/submissions/detail/415933794/
# datetime: Mon Nov  2 18:29:35 2020
# runtime: 36 ms
# memory: 14.3 MB

class Solution:
    def firstUniqChar(self, s: str) -> int:
        k = len(s)
        for c in string.ascii_letters:
            i = s.find(c)
            if -1 != i == s.rfind(c):
                k = min(k, i)
        return k if k < len(s) else -1