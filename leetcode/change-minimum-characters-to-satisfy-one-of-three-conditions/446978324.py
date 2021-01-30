# title: change-minimum-characters-to-satisfy-one-of-three-conditions
# detail: https://leetcode.com/submissions/detail/446978324/
# datetime: Sun Jan 24 10:56:05 2021
# runtime: 112 ms
# memory: 15 MB

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        a = collections.Counter(a)
        b = collections.Counter(b)
        
        def make_less(a, b):
            res = math.inf
            n = 0
            for c in sorted(a, reverse=True):
                if c == 'z':
                    n += a[c]
                    continue
                cnt = n
                for k, v in b.items():
                    if k <= c:
                        cnt += v
                res = min(res, cnt)
                n += a[c]
            return res
        
        res = min(make_less(a, b), make_less(b, a))
        res = min(res, sum(a.values()) - a.most_common()[0][1] + sum(b.values()) - b.most_common()[0][1])
        return res