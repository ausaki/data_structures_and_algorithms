# title: permutation-sequence
# detail: https://leetcode.com/submissions/detail/415914143/
# datetime: Mon Nov  2 16:45:41 2020
# runtime: 56 ms
# memory: 13.9 MB

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def count(n, m):
            digits = list(map(int, str(m)))
            cnt = 0
            used = [False] * (n + 1)
            for i in range(n):
                k = sum(1 for j in range(1, min(n + 1, digits[i])) if not used[j])
                cnt += math.factorial(n - i - 1) * k
                if digits[i] == 0 or digits[i] > n or used[digits[i]]:
                    break
                used[digits[i]] = True
            else:
                cnt += 1
            return cnt
        
        l = sum(i * (10 ** (n - i)) for i in range(1, n + 1))
        r = sum(i * (10 ** (i - 1)) for i in range(1, n + 1))
        while l <= r:
            m = (l + r) // 2
            cnt = count(n, m)    
            # print(l, r, m, cnt)
            if cnt < k:
                l = m + 1
            else:
                r = m - 1
        return str(l)
        