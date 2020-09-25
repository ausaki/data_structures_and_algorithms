# title: smallest-subsequence-of-distinct-characters
# detail: https://leetcode.com/submissions/detail/397885678/
# datetime: Sat Sep 19 23:29:17 2020
# runtime: 60 ms
# memory: 14 MB

class Solution:
    def smallestSubsequence(self, text: str) -> str:
        pos = collections.defaultdict(collections.deque)
        for i, c in enumerate(text):
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
            