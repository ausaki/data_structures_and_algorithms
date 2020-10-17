# title: binary-trees-with-factors
# detail: https://leetcode.com/submissions/detail/409118322/
# datetime: Fri Oct 16 01:08:56 2020
# runtime: 156 ms
# memory: 14.3 MB

class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        result = 0
        A.sort()
        cnt = {a: 1 for a in A}
        for i, a in enumerate(A):
            t = int(math.sqrt(a))
            for j in range(i):
                if A[j] > t:
                    break
                q, r = divmod(a, A[j])
                if r == 0 and q in cnt:
                    s = cnt[A[j]] * cnt[q]
                    if A[j] != q:
                        s *= 2
                    cnt[a] = (cnt[a] + s) % MOD
            result = (result + cnt[a]) % MOD
        return result