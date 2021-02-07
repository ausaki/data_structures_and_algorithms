# title: minimum-length-of-string-after-deleting-similar-ends
# detail: https://leetcode.com/submissions/detail/452750269/
# datetime: Sat Feb  6 22:50:14 2021
# runtime: 152 ms
# memory: 14.9 MB

class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                break
            c = s[l]
            while l <= r and s[l] == c:
                l += 1
            while r >= l and s[r] == c:
                r -= 1
        return r - l + 1