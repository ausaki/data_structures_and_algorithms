# title: count-unhappy-friends
# detail: https://leetcode.com/submissions/detail/398674632/
# datetime: Mon Sep 21 16:30:41 2020
# runtime: 436 ms
# memory: 27.4 MB

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        r = [0] * n
        for i, j in pairs:
            r[i] = j
            r[j] = i
        pre = []
        for p in preferences:
            pp = [0] * n
            for i, j in enumerate(p):
                pp[j] = i
            pre.append(pp)
        result = 0
        for i in range(n):
            j = r[i]
            for k in range(pre[i][j]):
                f = preferences[i][k]
                if pre[f][i] < pre[f][r[f]]:
                    result += 1
                    break
        return result