# title: smallest-string-with-a-given-numeric-value
# detail: https://leetcode.com/submissions/detail/422795448/
# datetime: Sun Nov 22 10:45:27 2020
# runtime: 276 ms
# memory: 15.5 MB

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if n == k:
            return 'a' * n
        s = ['a'] * n
        k -= n
        for i in range(n - 1, -1, -1):
            if k >= 25:
                s[i] = 'z'
                k -= 25
            else:
                s[i] = chr(ord('a') + k)
                break
        return ''.join(s)