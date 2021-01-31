# title: palindrome-partitioning-iv
# detail: https://leetcode.com/submissions/detail/449984925/
# datetime: Sun Jan 31 12:23:52 2021
# runtime: 1944 ms
# memory: 14.4 MB

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
            a, b = False, False
            c = (l - 1) // 2
            m = l
            if m == 0:
                return False
            if (m % 2 and d1[c] - 1 == m // 2) or (m % 2 == 0 and d2[c + 1] == m // 2):
                a = True
            c = (r + n) // 2
            m = n - r - 1
            if m == 0:
                return False
            if (m % 2 and d1[c] - 1 == m // 2) or (m % 2 == 0 and d2[c + 1] == m // 2):
                b = True
            return a and b
            
        for i in range(n):
            l = d1[i] - 1
            l, r = i - d1[i] + 1, i + d1[i] - 1
            while l <= r:
                if check(l, r):
                    return True
                l += 1
                r -= 1
            l, r = i - d2[i], i + d2[i] - 1
            while l < r:
                if check(l, r):
                    return True
                l += 1
                r -= 1
        return False