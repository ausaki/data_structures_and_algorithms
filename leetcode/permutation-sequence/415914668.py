# title: permutation-sequence
# detail: https://leetcode.com/submissions/detail/415914668/
# datetime: Mon Nov  2 16:48:11 2020
# runtime: 52 ms
# memory: 14.1 MB

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
                if i == n - 1:
                    cnt += 1
            return cnt
        
        l = sum(i * (10 ** (n - i)) for i in range(1, n + 1))
        r = sum(i * (10 ** (i - 1)) for i in range(1, n + 1))
        while l <= r:
            m = (l + r) // 2
            cnt = count(n, m)    
            if cnt < k:
                l = m + 1
            else:
                r = m - 1
        return str(l)
        