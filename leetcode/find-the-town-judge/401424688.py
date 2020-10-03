# title: find-the-town-judge
# detail: https://leetcode.com/submissions/detail/401424688/
# datetime: Sun Sep 27 23:47:07 2020
# runtime: 764 ms
# memory: 18.4 MB

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust or N == 1:
            return 1 if N == 1 else -1
        cnt = collections.Counter()
        s = set()
        for a, b in trust:
            cnt[b] += 1
            s.add(a)
        i, k = cnt.most_common(1)[0]
        if k == N - 1 and i not in s:
            return i
        return -1 