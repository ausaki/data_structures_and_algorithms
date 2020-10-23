# title: lexicographically-smallest-string-after-applying-operations
# detail: https://leetcode.com/submissions/detail/410105162/
# datetime: Sun Oct 18 12:31:12 2020
# runtime: 140 ms
# memory: 14.1 MB

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        rems = set()
        r = a
        while r not in rems:
            rems.add(r)
            r = (r + a) % 10
        rems.add(0)
        def min_rotation(s):
            rotations = set()
            min_ = s
            while s not in rotations:
                rotations.add(s)
                min_ = min(min_, s)
                s = s[-b:] + s[:-b]
            return min_
        result = s
        all_opts = set()
        for r in rems:
            ss =''.join(str((int(s[i]) + r) % 10) if i % 2 else s[i] for i in range(n))
            if ss not in all_opts:
                all_opts.add(ss)
                result = min(result, min_rotation(ss))
        if b % 2 == 1:
            for opt in all_opts:
                for r in rems:
                    ss =''.join(str((int(s[i]) + r) % 10) if i % 2 == 0 else opt[i] for i in range(n))
                    result = min(result, min_rotation(ss))
        return result