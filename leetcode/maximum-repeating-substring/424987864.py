# title: maximum-repeating-substring
# detail: https://leetcode.com/submissions/detail/424987864/
# datetime: Sat Nov 28 22:41:26 2020
# runtime: 36 ms
# memory: 14.2 MB

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        m, n = len(sequence), len(word)
        k = 1
        s = ''
        ans = 0
        for k in range(1, m // n + 1):
            s += word
            if s not in sequence:
                break
            ans = k
        return ans