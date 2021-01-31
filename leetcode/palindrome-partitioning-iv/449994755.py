# title: palindrome-partitioning-iv
# detail: https://leetcode.com/submissions/detail/449994755/
# datetime: Sun Jan 31 12:50:50 2021
# runtime: 6656 ms
# memory: 14.5 MB

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        d1 = [0] * n
        d2 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            k -= 1
            if i + k > r:
                l, r = i - k, i + k
        l, r = 0, -1
        for i in range(n):
            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
            while 0 <= i - k - 1 and i + k < n and s[i - k - 1] == s[i + k]:
                k += 1
            d2[i] = k
            k -= 1
            if i + k > r:
                l, r = i - k - 1, i + k
                
        def check(l, r):
            m = r - l + 1
            if m == 0:
                return False
            c = (l + r) // 2
            return (m % 2 and d1[c] - 1 >= m // 2) or (m % 2 == 0 and d2[c + 1] >= m // 2)
            
        for l in range(n - 1):
            for r in range(l, n):
                if check(0, l -1) and check(l, r) and check(r + 1, n - 1):
                    return True
        return False