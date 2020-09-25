# title: remove-duplicate-letters
# detail: https://leetcode.com/submissions/detail/397887049/
# datetime: Sat Sep 19 23:32:24 2020
# runtime: 36 ms
# memory: 14.4 MB

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        pos = collections.defaultdict(collections.deque)
        for i, c in enumerate(s):
            pos[c].append(i)
        result = []
        keys = sorted(pos.keys())
        while keys:
            last = min(pos[c][-1] for c in keys)
            for c in keys:
                i = pos[c][0]
                if i > last:
                    continue
                result.append(c)
                keys.remove(c)
                for c in keys:
                    l = pos[c]
                    while l and l[0] < i:
                        l.popleft()
                break
        return ''.join(result)