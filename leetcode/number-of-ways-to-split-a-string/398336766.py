# title: number-of-ways-to-split-a-string
# detail: https://leetcode.com/submissions/detail/398336766/
# datetime: Sun Sep 20 22:57:51 2020
# runtime: 104 ms
# memory: 14.5 MB

class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        t = s.count('1')
        if t % 3:
            return 0
        if t == 0:
            return ((n - 2) * (n - 1) // 2) % MOD
        a = 0
        j, k = 0, 0
        for i, c in enumerate(s):
            if c == '1':
                a += 1
                if a == t // 3:
                    j = i
                if a == t // 3 + 1:
                    j = i - j
                if a == t // 3 * 2:
                    k = i
                if a == t // 3 * 2 + 1:
                    k = i - k
                    break
        return (j * k) % MOD 
        