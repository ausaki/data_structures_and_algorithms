# title: lexicographically-smallest-string-after-applying-operations
# detail: https://leetcode.com/submissions/detail/410102501/
# datetime: Sun Oct 18 12:23:59 2020
# runtime: 168 ms
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
        def make_rotations(s):
            rotations = set()
            while s not in rotations:
                rotations.add(s)
                s = s[-b:] + s[:-b]
            return rotations
        rotations = set()
        for r in rems:
            ss =''.join(str((int(s[i]) + r) % 10) if i % 2 else s[i] for i in range(n))
            rotations.add(ss)
        if b % 2 == 1:
            evens = set()
            for ro in rotations:
                for r in rems:
                    ss =''.join(str((int(s[i]) + r) % 10) if i % 2 == 0 else ro[i] for i in range(n))
                    evens.add(ss)
            rotations |= evens
        result = s
        for ro in rotations:
            result = min(result, min(make_rotations(ro)))
        return result