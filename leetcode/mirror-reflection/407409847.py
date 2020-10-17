# title: mirror-reflection
# detail: https://leetcode.com/submissions/detail/407409847/
# datetime: Mon Oct 12 00:57:48 2020
# runtime: 32 ms
# memory: 13.9 MB

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        a, b, c, d = -1, -1, -1, -1
        if q < p / 2:
            i, r = divmod(p, q)
            if r == 0:
                if i % 2:
                    return 1
                return 2
            a, b = r, p / q * r
            c = 0
            d = -1 if i % 2 else 1
        else:
            a, b = p, q
            c = 1
            d = -1
        # print(a, b, c, d)
        while True:
            if abs(b - p) <= 1e-3:
                if c == 0:
                    return 2 if d == -1 else 1
                if c == 1:
                    return 1 if d == -1 else 0
                if c == 2:
                    return 0 if d == -1 else -1
                if c == 3:
                    return -1 if d == -1 else 2
            a, b = p - b, a / b * (p - b)
            c = (c + d) % 4
            # print(a, b, c)
            while b - p >= 0.1:
                a, b = (b - p) / b * a, b - p
                # print('--', a, b, c)
                d = -d
        return -1