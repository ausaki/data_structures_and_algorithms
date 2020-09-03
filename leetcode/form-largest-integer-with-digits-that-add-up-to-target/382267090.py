# title: form-largest-integer-with-digits-that-add-up-to-target
# detail: https://leetcode.com/submissions/detail/382267090/
# datetime: Tue Aug 18 00:05:20 2020
# runtime: 308 ms
# memory: 178.8 MB

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        @lru_cache(None)
        def dp(i, m):
            if m == 0:
                return True, ''
            if i < 0:
                return False, ''
            a = ''
            if m >= cost[i]:
                f, t = dp(i, m - cost[i])
                if f:
                    a = str(i + 1) + t
            f, b = dp(i - 1, m)
            c = ''
            if len(a) == len(b):
                c = max(a, b)
            elif len(a) > len(b):
                c = a
            else:
                c = b
            f =  (c != '')
            # print(i, m, c)
            return f, (c if f else '')
        
        f, s = dp(8, target)
        if f:
            return s
        return '0'
        