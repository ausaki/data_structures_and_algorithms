# title: array-of-doubled-pairs
# detail: https://leetcode.com/submissions/detail/403038637/
# datetime: Thu Oct  1 16:24:12 2020
# runtime: 536 ms
# memory: 16.5 MB

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        cnt = collections.Counter(A)
        for k in sorted(cnt, key=abs):
            a = cnt[k]
            if cnt[k] == 0:
                continue
            b = cnt.get(2 * k, 0)
            if b < a:
                return False
            cnt[2 * k] -= a
            
        return True
            