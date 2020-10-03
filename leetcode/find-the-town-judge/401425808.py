# title: find-the-town-judge
# detail: https://leetcode.com/submissions/detail/401425808/
# datetime: Sun Sep 27 23:51:11 2020
# runtime: 780 ms
# memory: 18.6 MB

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust or N == 1:
            return 1 if N == 1 else -1
        cnt = collections.Counter()
        for a, b in trust:
            cnt[b] += 1
            cnt[a] -= 1
        i, k = cnt.most_common(1)[0]
        return i if k == N - 1 else -1
