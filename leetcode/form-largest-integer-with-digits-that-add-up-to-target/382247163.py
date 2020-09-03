# title: form-largest-integer-with-digits-that-add-up-to-target
# detail: https://leetcode.com/submissions/detail/382247163/
# datetime: Mon Aug 17 23:13:42 2020
# runtime: 460 ms
# memory: 24 MB

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        
        def compare(d1, d2):
            n = len(d1)
            m = len(d2)
            i = n - 1
            j = m - 1
            while i >= 0 and j >= 0:
                a = d1[i][0] - d2[j][0]
                if a > 0:
                    return True
                if a < 0:
                    return False
                a = d1[i][1] - d2[j][1]
                if a > 0:
                    return True
                elif a < 0:
                    return False
                i -= 1
                j -= 1
            return i >= 0

        C = {}
        for i, c in enumerate(cost):
            C[c] = i + 1
        cost = sorted(C.items())
        # print(cost)
        n = len(cost)
        result = []
        
        @lru_cache(None)
        def paint(i, m):
            if i >= n:
                return 0, []
            c, j = cost[i]
            q, r = divmod(m, c)
            if r == 0:
                # print(j, q)
                return q, [(j, q)]
            if q == 0:
                return 0, []
            max_l = 0
            max_digit = 0
            result = None
            for k in range(q + 1):
                l, digits = paint(i + 1, r)
                r += c
                if l == 0:
                    continue
                digits = list(digits)
                l += q - k
                # if i == 0 and k <= 2:
                #     print(l, max_l, digits, result)
                if l < max_l:
                    continue
                if q - k:
                    bisect.insort(digits, (j, q - k))
                if l > max_l:
                    max_l = l
                    result = digits
                    continue
                # if i == 0 and k <= 2:
                #     print(digits, result)
                if compare(digits, result):
                    result = digits
            return max_l, result
        
        l, digits = paint(0, target)
        # print(l, digits)
        if not l:
            return '0'
        return ''.join(str(i) * j for i, j in reversed(digits))