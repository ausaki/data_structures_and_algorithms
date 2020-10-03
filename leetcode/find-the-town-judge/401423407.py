# title: find-the-town-judge
# detail: https://leetcode.com/submissions/detail/401423407/
# datetime: Sun Sep 27 23:42:16 2020
# runtime: 764 ms
# memory: 18.6 MB

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        cnt = collections.Counter()
        s = set()
        for a, b in trust:
            cnt[b] += 1
            s.add(a)
        m = cnt.most_common(2)
        if not m :
            if N == 1:
                return 1
            return -1
        if m[0][1] == N - 1 and (len(m) == 1 or m[1][1] < N - 1) and m[0][0] not in s:
            return m[0][0]
        return -1 