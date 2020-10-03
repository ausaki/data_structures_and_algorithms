# title: find-the-town-judge
# detail: https://leetcode.com/submissions/detail/401426729/
# datetime: Sun Sep 27 23:54:41 2020
# runtime: 720 ms
# memory: 18.6 MB

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust or N == 1:
            return 1 if N == 1 else -1
        cnt = [0] * N
        for a, b in trust:
            a, b = a - 1, b - 1
            cnt[b] += 1
            cnt[a] -= 1
        try:
            return cnt.index(N - 1) + 1
        except:
            return -1
