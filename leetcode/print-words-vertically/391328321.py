# title: print-words-vertically
# detail: https://leetcode.com/submissions/detail/391328321/
# datetime: Sat Sep  5 21:54:11 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def printVertically(self, s: str) -> List[str]:
        return [''.join(s).rstrip() for s in itertools.zip_longest(*s.split(), fillvalue=' ')]