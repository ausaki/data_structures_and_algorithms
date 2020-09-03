# title: minimum-number-of-steps-to-make-two-strings-anagram
# detail: https://leetcode.com/submissions/detail/387389342/
# datetime: Fri Aug 28 11:04:50 2020
# runtime: 320 ms
# memory: 14.4 MB

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - 97] -= 1
            cnt[ord(t[i]) - 97] += 1
        return sum(filter(lambda i: i > 0, cnt))
