# title: first-unique-character-in-a-string
# detail: https://leetcode.com/submissions/detail/415932040/
# datetime: Mon Nov  2 18:19:22 2020
# runtime: 180 ms
# memory: 14.2 MB

class Solution:
    def firstUniqChar(self, s: str) -> int:
        pos = {'*': [len(s) + 1, -1]}
        for i, c in enumerate(s):
            pos.setdefault(c, [0, i])[0] += 1
        p = min(pos.values())
        return p[1] if p[0] == 1 else -1