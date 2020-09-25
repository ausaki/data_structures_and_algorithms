# title: smallest-subsequence-of-distinct-characters
# detail: https://leetcode.com/submissions/detail/397883142/
# datetime: Sat Sep 19 23:23:40 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def smallestSubsequence(self, text: str) -> str:
        pos = collections.defaultdict(collections.deque)
        for i, c in enumerate(text):
            pos[c].append(i)
        result = []
        keys = sorted(pos.keys())
        while pos:
            for c in keys:
                i = pos[c][0]
                for cc in keys:
                    if cc != c and pos[cc][-1] < i:
                        break
                else:
                    result.append(c)
                    pos.pop(c)
                    keys.remove(c)
                    for c in keys:
                        l = pos[c]
                        while l and l[0] < i:
                            l.popleft()
                    break
        return ''.join(result)
            