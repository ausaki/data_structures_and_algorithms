# title: backspace-string-compare
# detail: https://leetcode.com/submissions/detail/408231864/
# datetime: Tue Oct 13 21:35:09 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def g(s):
            cnt = 0
            for c in reversed(s):
                if c == '#':
                    cnt += 1
                elif cnt > 0:
                    cnt -= 1
                else:
                    yield c
        
        return all(a == b for a, b in itertools.zip_longest(g(S), g(T)))