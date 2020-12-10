# title: smallest-string-with-a-given-numeric-value
# detail: https://leetcode.com/submissions/detail/422817122/
# datetime: Sun Nov 22 11:35:43 2020
# runtime: 752 ms
# memory: 15.4 MB

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if n == k:
            return 'a' * n
        s = ['a'] * n
        k -= n
        for i in range(n - 1, -1, -1):
            s[i] = chr(ord('a') + min(k, 25))
            k -= min(k, 25)
            if k <= 0:
                break
        return ''.join(s)