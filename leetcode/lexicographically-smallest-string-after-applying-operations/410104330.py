# title: lexicographically-smallest-string-after-applying-operations
# detail: https://leetcode.com/submissions/detail/410104330/
# datetime: Sun Oct 18 12:28:55 2020
# runtime: 172 ms
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
        all_opts = set()
        for r in rems:
            ss =''.join(str((int(s[i]) + r) % 10) if i % 2 else s[i] for i in range(n))
            all_opts.add(ss)
        if b % 2 == 1:
            evens = set()
            for opt in all_opts:
                for r in rems:
                    ss =''.join(str((int(s[i]) + r) % 10) if i % 2 == 0 else opt[i] for i in range(n))
                    evens.add(ss)
            all_opts |= evens
        result = s
        for opt in all_opts:
            result = min(result, min_rotation(opt))
        return result