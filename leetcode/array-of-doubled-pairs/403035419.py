# title: array-of-doubled-pairs
# detail: https://leetcode.com/submissions/detail/403035419/
# datetime: Thu Oct  1 16:11:27 2020
# runtime: 536 ms
# memory: 16.5 MB

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        cnt = collections.Counter(A)
        for k in sorted(cnt.keys()):
            if cnt[k] == 0:
                continue
            if k < 0:
                a = cnt[k]
                if k % 2:
                    continue
                b = cnt.get(k // 2, 0)
                cnt[k] -= min(a, b)
                cnt[k // 2] -= min(a, b)
            elif k > 0:
                a = cnt[k]
                b = cnt.get(2 * k, 0)
                cnt[k] -= min(a, b)
                cnt[2 * k] -= min(a, b)
        z = cnt.get(0, 0)
        for k, v in cnt.items():
            if v == 0:
                continue
            if z >= v:
                z -= v
            else:
                return False
        return z % 2 == 0
            